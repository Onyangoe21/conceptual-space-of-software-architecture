#!/usr/bin/env python3
#
# Copyright 2026 Edwin O Onyango
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for the review gate's counting rules.

The rules that matter are about who does not count: the author, bots, and people whose approval
was later dismissed. Those cases are hard to exercise against a live repository with one account,
so they are pinned here instead.

    python3 .github/scripts/test_review_gate.py

No network, no third party dependencies.
"""

from __future__ import annotations

import sys

import review_gate as gate


class StubClient:
    """Stands in for the API. Serves fixture data keyed by URL suffix."""

    repo = "owner/name"
    dry_run = True

    def __init__(self, reactions=(), comments=(), reviews=()):
        self.reactions = list(reactions)
        self.comments = list(comments)
        self.reviews = list(reviews)

    def get_all(self, path: str) -> list:
        if path.endswith("/reactions"):
            return self.reactions
        if path.endswith("/comments"):
            return self.comments
        if path.endswith("/reviews"):
            return self.reviews
        raise AssertionError(f"unexpected path {path}")


def user(login: str, kind: str = "User") -> dict:
    return {"login": login, "type": kind}


def issue(number: int = 1, author: str = "author", pull: bool = False) -> dict:
    item = {"number": number, "user": user(author), "created_at": "2026-01-01T00:00:00Z"}
    if pull:
        item["pull_request"] = {"url": "..."}
    return item


FAILURES = []


def check(name: str, actual, expected) -> None:
    if actual == expected:
        print(f"  pass  {name}")
    else:
        FAILURES.append(name)
        print(f"  FAIL  {name}\n          expected {expected!r}\n          got      {actual!r}")


def main() -> int:
    print("Thresholds by label:")
    check("erratum needs nobody", gate.threshold_for({"erratum"}), 0)
    check("proposal needs two", gate.threshold_for({"proposal"}), 2)
    check("counterexample needs two", gate.threshold_for({"counterexample"}), 2)
    check("evidence needs one", gate.threshold_for({"evidence"}), 1)
    check("estimator needs one", gate.threshold_for({"estimator"}), 1)
    check("unlabelled falls back to one", gate.threshold_for(set()), 1)
    check(
        "erratum wins over proposal when both present",
        gate.threshold_for({"proposal", "erratum"}),
        0,
    )

    print("\nWho counts as an approver:")

    client = StubClient(reactions=[{"content": "+1", "user": user("reviewer")}])
    check("a thumbs up from someone else", gate.collect_approvers(client, issue()), {"reviewer"})

    client = StubClient(reactions=[{"content": "+1", "user": user("author")}])
    check("the author's own thumbs up", gate.collect_approvers(client, issue()), set())

    client = StubClient(reactions=[{"content": "heart", "user": user("reviewer")}])
    check("a reaction that is not a thumbs up", gate.collect_approvers(client, issue()), set())

    client = StubClient(reactions=[{"content": "+1", "user": user("robot", "Bot")}])
    check("a bot's thumbs up", gate.collect_approvers(client, issue()), set())

    client = StubClient(comments=[{"body": "/approve", "user": user("reviewer")}])
    check("an /approve comment", gate.collect_approvers(client, issue()), {"reviewer"})

    client = StubClient(
        comments=[{"body": "looks good, I would /approve this later", "user": user("reviewer")}]
    )
    check(
        "/approve mentioned inside a sentence does not count",
        gate.collect_approvers(client, issue()),
        set(),
    )

    client = StubClient(
        comments=[{"body": "I read the sources.\n/approve\nGood file.", "user": user("reviewer")}]
    )
    check(
        "/approve on its own line inside a longer comment",
        gate.collect_approvers(client, issue()),
        {"reviewer"},
    )

    client = StubClient(
        reactions=[{"content": "+1", "user": user("reviewer")}],
        comments=[{"body": "/approve", "user": user("reviewer")}],
    )
    check(
        "one person approving twice counts once",
        gate.collect_approvers(client, issue()),
        {"reviewer"},
    )

    print("\nPull request reviews:")

    client = StubClient(reviews=[{"state": "APPROVED", "user": user("reviewer")}])
    check(
        "an approving review",
        gate.collect_approvers(client, issue(pull=True)),
        {"reviewer"},
    )

    client = StubClient(reviews=[{"state": "APPROVED", "user": user("reviewer")}])
    check(
        "reviews are ignored on plain issues",
        gate.collect_approvers(client, issue(pull=False)),
        set(),
    )

    client = StubClient(
        reviews=[
            {"state": "APPROVED", "user": user("reviewer")},
            {"state": "CHANGES_REQUESTED", "user": user("reviewer")},
        ]
    )
    check(
        "an approval later replaced by changes requested stops counting",
        gate.collect_approvers(client, issue(pull=True)),
        set(),
    )

    client = StubClient(
        reviews=[
            {"state": "CHANGES_REQUESTED", "user": user("reviewer")},
            {"state": "APPROVED", "user": user("reviewer")},
        ]
    )
    check(
        "changes requested then approved does count",
        gate.collect_approvers(client, issue(pull=True)),
        {"reviewer"},
    )

    client = StubClient(
        reviews=[
            {"state": "APPROVED", "user": user("reviewer")},
            {"state": "COMMENTED", "user": user("reviewer")},
        ]
    )
    check(
        "a later plain comment does not dismiss an approval",
        gate.collect_approvers(client, issue(pull=True)),
        {"reviewer"},
    )

    client = StubClient(
        reactions=[{"content": "+1", "user": user("alice")}],
        comments=[{"body": "/approve", "user": user("bob")}],
        reviews=[{"state": "APPROVED", "user": user("carol")}],
    )
    check(
        "three different people through three different routes",
        gate.collect_approvers(client, issue(pull=True)),
        {"alice", "bob", "carol"},
    )

    print()
    if FAILURES:
        print(f"{len(FAILURES)} failure(s): {', '.join(FAILURES)}")
        return 1
    print("All review gate counting rules hold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
