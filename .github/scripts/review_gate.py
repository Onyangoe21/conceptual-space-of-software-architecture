#!/usr/bin/env python3
"""Count approvals on proposals and pull requests, and label them accordingly.

The point is that contributing should not require anyone to remember a process. A reviewer clicks
a thumbs up, or approves a pull request, or writes /approve, and the thread labels itself.

What counts as one approval from one person:

  * a thumbs up reaction on the issue or pull request body
  * an approving review, for pull requests
  * a comment containing /approve on a line of its own

The author's own approval never counts, and neither do bots.

What this touches:

  * pull requests, always
  * issues labeled `proposal`

Everything else is left alone, so that the maintainer's own backlog of task issues does not get
decorated with review labels it has no use for.

Labels applied:

  needs-reviews        below threshold
  ready-to-integrate   threshold met
  maintainer-decision  below threshold and older than the patience window

Run it locally against the live repository without changing anything:

    GITHUB_TOKEN=$(gh auth token) python3 .github/scripts/review_gate.py --dry-run

No third party dependencies, on purpose.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://api.github.com"

# Approvals needed, by contribution type label. A citation fix does not need a committee. A
# proposal to restructure a section does. Checked in this order, first match wins.
THRESHOLDS = [
    ("erratum", 0),
    ("proposal", 2),
    ("counterexample", 2),
    ("convergence", 1),
    ("evidence", 1),
    ("estimator", 1),
]
DEFAULT_THRESHOLD = 1

PATIENCE_DAYS = 14

LABEL_NEEDS = "needs-reviews"
LABEL_READY = "ready-to-integrate"
LABEL_STALLED = "maintainer-decision"
MANAGED_LABELS = {LABEL_NEEDS, LABEL_READY, LABEL_STALLED}

# Marker so the "this is ready" comment is posted once rather than on every scheduled run.
COMMENT_MARKER = "<!-- review-gate: ready -->"

APPROVE_COMMAND = re.compile(r"^\s*/approve\s*$", re.MULTILINE)


class Client:
    def __init__(self, token: str, repo: str, dry_run: bool = False):
        self.token = token
        self.repo = repo
        self.dry_run = dry_run

    def _request(self, method: str, path: str, body=None):
        url = path if path.startswith("http") else f"{API}{path}"
        data = json.dumps(body).encode() if body is not None else None
        request = urllib.request.Request(url, data=data, method=method)
        request.add_header("Authorization", f"Bearer {self.token}")
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("X-GitHub-Api-Version", "2022-11-28")
        if data is not None:
            request.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(request) as response:
            payload = response.read()
            link = response.headers.get("Link", "")
        parsed = json.loads(payload) if payload else None
        return parsed, link

    def get_all(self, path: str) -> list:
        """GET a paginated collection, following Link headers."""
        results: list = []
        url = f"{API}{path}"
        separator = "&" if "?" in url else "?"
        url = f"{url}{separator}per_page=100"
        while url:
            page, link = self._request("GET", url)
            if isinstance(page, list):
                results.extend(page)
            else:
                results.append(page)
            url = ""
            for part in link.split(","):
                if 'rel="next"' in part:
                    url = part.split(";")[0].strip().strip("<>")
        return results

    def get(self, path: str):
        return self._request("GET", path)[0]

    def post(self, path: str, body) -> None:
        if self.dry_run:
            print(f"      [dry run] POST {path} {json.dumps(body)}")
            return
        self._request("POST", path, body)

    def delete(self, path: str) -> None:
        if self.dry_run:
            print(f"      [dry run] DELETE {path}")
            return
        try:
            self._request("DELETE", path)
        except urllib.error.HTTPError as error:
            if error.code != 404:
                raise


def is_bot(user: dict) -> bool:
    return not user or user.get("type") == "Bot" or user.get("login", "").endswith("[bot]")


def threshold_for(labels: set) -> int:
    for name, count in THRESHOLDS:
        if name in labels:
            return count
    return DEFAULT_THRESHOLD


def collect_approvers(client: Client, item: dict) -> set:
    """Distinct people, other than the author, who have signalled approval."""
    number = item["number"]
    author = (item.get("user") or {}).get("login", "")
    approvers = set()

    for reaction in client.get_all(f"/repos/{client.repo}/issues/{number}/reactions"):
        user = reaction.get("user") or {}
        if reaction.get("content") == "+1" and not is_bot(user):
            login = user.get("login", "")
            if login and login != author:
                approvers.add(login)

    for comment in client.get_all(f"/repos/{client.repo}/issues/{number}/comments"):
        user = comment.get("user") or {}
        login = user.get("login", "")
        if is_bot(user) or not login or login == author:
            continue
        if APPROVE_COMMAND.search(comment.get("body") or ""):
            approvers.add(login)

    if item.get("pull_request"):
        # Latest review state per person, so a dismissed or superseded approval stops counting.
        latest = {}
        for review in client.get_all(f"/repos/{client.repo}/pulls/{number}/reviews"):
            user = review.get("user") or {}
            login = user.get("login", "")
            if is_bot(user) or not login or login == author:
                continue
            if review.get("state") == "COMMENTED":
                continue
            latest[login] = review.get("state")
        approvers.update(login for login, state in latest.items() if state == "APPROVED")

    return approvers


def reconcile_labels(client: Client, number: int, current: set, wanted: set) -> None:
    for label in sorted(wanted - current):
        print(f"      + {label}")
        client.post(f"/repos/{client.repo}/issues/{number}/labels", {"labels": [label]})
    for label in sorted((current & MANAGED_LABELS) - wanted):
        print(f"      - {label}")
        client.delete(f"/repos/{client.repo}/issues/{number}/labels/{label}")


def already_announced(client: Client, number: int) -> bool:
    for comment in client.get_all(f"/repos/{client.repo}/issues/{number}/comments"):
        if COMMENT_MARKER in (comment.get("body") or ""):
            return True
    return False


def announce(client: Client, number: int, approvers: set, required: int) -> None:
    names = ", ".join(f"@{login}" for login in sorted(approvers))
    body = (
        f"{COMMENT_MARKER}\n"
        f"**Threshold met.** {len(approvers)} of {required} approvals: {names}.\n\n"
        "Labeled `ready-to-integrate`. The maintainer still writes the three tests out against "
        "this in the thread before it lands, because approvals establish that other people find "
        "it credible and do not by themselves establish that it belongs in the paper.\n\n"
        "If you approved this without reading the primary sources, say so now rather than later."
    )
    client.post(f"/repos/{client.repo}/issues/{number}/comments", {"body": body})


def process(client: Client, item: dict) -> None:
    number = item["number"]
    labels = {label["name"] for label in item.get("labels", [])}
    is_pull = bool(item.get("pull_request"))

    if not is_pull and "proposal" not in labels:
        return

    required = threshold_for(labels)
    kind = "PR" if is_pull else "issue"
    title = (item.get("title") or "")[:58]

    if required == 0:
        print(f"  {kind} #{number}: {title}\n      no approvals required")
        reconcile_labels(client, number, labels, set())
        return

    approvers = collect_approvers(client, item)
    met = len(approvers) >= required

    created = datetime.strptime(item["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc
    )
    stalled = not met and datetime.now(timezone.utc) - created > timedelta(days=PATIENCE_DAYS)

    wanted = {LABEL_READY} if met else {LABEL_NEEDS}
    if stalled:
        wanted.add(LABEL_STALLED)

    state = "ready" if met else ("stalled" if stalled else "waiting")
    print(f"  {kind} #{number}: {title}\n      {len(approvers)}/{required} approvals, {state}")

    reconcile_labels(client, number, labels, wanted)

    if met and not already_announced(client, number):
        if client.dry_run:
            print("      [dry run] would post the threshold comment")
        else:
            announce(client, number, approvers, required)


def main(argv: list) -> int:
    parser = argparse.ArgumentParser(description="Count approvals and label threads.")
    parser.add_argument(
        "--repo",
        default=os.environ.get("GITHUB_REPOSITORY", ""),
        help="owner/name, defaults to $GITHUB_REPOSITORY",
    )
    parser.add_argument("--number", type=int, help="only this issue or pull request")
    parser.add_argument("--dry-run", action="store_true", help="report without writing anything")
    args = parser.parse_args(argv)

    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("error: GITHUB_TOKEN is not set. Locally, try GITHUB_TOKEN=$(gh auth token).")
        return 1
    if not args.repo:
        print("error: no repository. Pass --repo owner/name.")
        return 1

    client = Client(token, args.repo, dry_run=args.dry_run)
    print(f"Review gate on {args.repo}{' (dry run)' if args.dry_run else ''}")

    if args.number:
        items = [client.get(f"/repos/{args.repo}/issues/{args.number}")]
    else:
        items = client.get_all(f"/repos/{args.repo}/issues?state=open")

    considered = 0
    for item in items:
        if not item:
            continue
        labels = {label["name"] for label in item.get("labels", [])}
        if item.get("pull_request") or "proposal" in labels:
            considered += 1
        process(client, item)

    print(f"Done. {considered} thread(s) under the gate, {len(items)} open in total.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
