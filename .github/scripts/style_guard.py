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

"""Mechanical checks on the paper's voice contract.

Three checks, described in CONTRIBUTING.md section 4:

1. ERROR  No em dashes, and no en dashes adjacent to a letter, in the paper body.
          The bibliography block and LaTeX comments are exempt, since page ranges and
          multi author date ranges legitimately need en dashes.
2. ERROR  Every \\cite key has a matching \\bibitem, and every \\bibitem is cited.
3. WARN   Sentences longer than a word threshold, printed as a nudge toward the register.
          Never fails the build. The paper has a few long sentences on purpose.

Run it locally before you push:

    python3 .github/scripts/style_guard.py paper/conceptual-space-arxiv.tex

Exit code 0 if there are no errors, 1 if there are. Warnings do not affect the exit code
unless you pass --strict.

No third party dependencies, on purpose. Any Python 3.8 or later will run it.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_SENTENCE_LIMIT = 60

# Environments whose contents are not prose. Skipped for the sentence length check, since a
# table with no full stops in it reads to a naive splitter as one enormous sentence.
NON_PROSE_ENVIRONMENTS = {
    "thebibliography",
    "tabular",
    "tabularx",
    "longtable",
    "array",
    "verbatim",
    "lstlisting",
    "equation",
    "equation*",
    "align",
    "align*",
    "displaymath",
    "center",
    "table",
    "figure",
    "tabbing",
}

BEGIN_RE = re.compile(r"\\begin\{([^}]*)\}")
END_RE = re.compile(r"\\end\{([^}]*)\}")
CITE_RE = re.compile(r"\\cite[tpalyear]*\*?(?:\[[^\]]*\])*\{([^}]*)\}")
BIBITEM_RE = re.compile(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}")

# Three or more hyphens is an em dash in TeX. Two hyphens is an en dash, which is fine between
# digits, as in a page range, and not fine touching a letter.
EM_DASH_RE = re.compile(r"-{3,}")
UNICODE_DASH_RE = re.compile(r"[\u2013\u2014\u2015]")
EN_DASH_RE = re.compile(r"(?<!-)--(?!-)")

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")


@dataclass
class Line:
    """One physical line, with the flags the checks need."""

    number: int
    raw: str
    code: str  # comment stripped
    in_bibliography: bool = False
    in_prose: bool = True


@dataclass
class Report:
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)

    def error(self, line_number: int, message: str, excerpt: str = "") -> None:
        self.errors.append((line_number, message, excerpt))

    def warn(self, line_number: int, message: str, excerpt: str = "") -> None:
        self.warnings.append((line_number, message, excerpt))


def strip_comment(raw: str) -> str:
    """Remove a LaTeX comment, respecting the escaped percent sign."""
    out = []
    escaped = False
    for char in raw:
        if escaped:
            out.append(char)
            escaped = False
            continue
        if char == "\\":
            out.append(char)
            escaped = True
            continue
        if char == "%":
            break
        out.append(char)
    return "".join(out)


def parse(text: str) -> list:
    """Annotate every line with whether it is bibliography and whether it is prose."""
    lines = []
    in_bibliography = False
    in_document = False
    environment_stack = []

    for index, raw in enumerate(text.splitlines(), start=1):
        code = strip_comment(raw)

        begins = BEGIN_RE.findall(code)
        ends = END_RE.findall(code)

        # A line carrying \begin{thebibliography} is itself part of the bibliography block, and
        # so is the line carrying \end{thebibliography}.
        starts_bibliography = "thebibliography" in begins
        ends_bibliography = "thebibliography" in ends
        if starts_bibliography:
            in_bibliography = True

        if "document" in begins:
            in_document = True

        non_prose_before = bool(environment_stack)
        for name in begins:
            if name in NON_PROSE_ENVIRONMENTS:
                environment_stack.append(name)
        for name in ends:
            if name in NON_PROSE_ENVIRONMENTS and environment_stack:
                environment_stack.pop()
        non_prose_after = bool(environment_stack)

        line = Line(
            number=index,
            raw=raw,
            code=code,
            in_bibliography=in_bibliography,
            in_prose=in_document
            and not in_bibliography
            and not non_prose_before
            and not non_prose_after
            and "document" not in begins,
        )
        lines.append(line)

        if ends_bibliography:
            in_bibliography = False

    return lines


def excerpt_around(text: str, start: int, end: int, width: int = 34) -> str:
    left = max(0, start - width)
    right = min(len(text), end + width)
    prefix = "..." if left > 0 else ""
    suffix = "..." if right < len(text) else ""
    return f"{prefix}{text[left:right].strip()}{suffix}"


def check_dashes(lines: list, report: Report) -> None:
    """No em dashes, and no letter adjacent en dashes, in the paper body."""
    for line in lines:
        if line.in_bibliography:
            continue
        code = line.code

        for match in EM_DASH_RE.finditer(code):
            report.error(
                line.number,
                "em dash. Use a comma, a colon, a full stop, or restructure the sentence.",
                excerpt_around(code, match.start(), match.end()),
            )

        for match in UNICODE_DASH_RE.finditer(code):
            report.error(
                line.number,
                f"unicode dash {match.group()!r}. Prose uses no em or en dashes.",
                excerpt_around(code, match.start(), match.end()),
            )

        for match in EN_DASH_RE.finditer(code):
            before = code[match.start() - 1] if match.start() > 0 else ""
            after = code[match.end()] if match.end() < len(code) else ""
            if before.isalpha() or after.isalpha():
                report.error(
                    line.number,
                    "letter adjacent en dash. A number range is fine, a word range is not.",
                    excerpt_around(code, match.start(), match.end()),
                )


def check_citations(lines: list, report: Report) -> None:
    """Every cite key has a bibitem, and every bibitem is cited."""
    cited = {}
    defined = {}

    for line in lines:
        for match in CITE_RE.finditer(line.code):
            for key in match.group(1).split(","):
                key = key.strip()
                if key:
                    cited.setdefault(key, line.number)
        for match in BIBITEM_RE.finditer(line.code):
            key = match.group(1).strip()
            if not key:
                continue
            if key in defined:
                report.error(
                    line.number,
                    f"duplicate bibitem key {key!r}, first defined on line {defined[key]}.",
                )
            else:
                defined[key] = line.number

    for key, line_number in sorted(cited.items(), key=lambda item: item[1]):
        if key not in defined:
            report.error(line_number, f"cite key {key!r} has no matching bibitem.")

    for key, line_number in sorted(defined.items(), key=lambda item: item[1]):
        if key not in cited:
            report.error(line_number, f"bibitem {key!r} is never cited.")


def prose_text(lines: list) -> list:
    """Return prose lines with LaTeX markup reduced to something sentence shaped."""
    kept = []
    for line in lines:
        if not line.in_prose:
            continue
        text = line.code

        # Drop constructs whose contents are not words.
        text = re.sub(r"\\(?:cite[tpalyear]*|ref|eqref|label|input|include)\*?"
                      r"(?:\[[^\]]*\])*\{[^}]*\}", " ", text)
        text = re.sub(r"\$[^$]*\$", " ", text)
        text = re.sub(r"\\[a-zA-Z@]+\*?(?:\[[^\]]*\])*", " ", text)
        text = re.sub(r"\\.", " ", text)
        text = text.replace("{", " ").replace("}", " ").replace("&", " ")
        text = re.sub(r"[ \t]+", " ", text).strip()

        if text:
            kept.append((line.number, text))
    return kept


def check_sentence_length(lines: list, report: Report, limit: int) -> None:
    """Warn on very long sentences. Never an error."""
    chunks = prose_text(lines)
    if not chunks:
        return

    # Join into paragraphs so that sentences spanning line breaks are measured whole. A blank
    # line in the source, which is a paragraph break in LaTeX, also breaks a sentence here.
    paragraphs = []
    current: list = []
    previous_number = None
    for number, text in chunks:
        if previous_number is not None and number != previous_number + 1:
            if current:
                paragraphs.append(current)
            current = []
        current.append((number, text))
        previous_number = number
    if current:
        paragraphs.append(current)

    for paragraph in paragraphs:
        start_line = paragraph[0][0]
        joined = " ".join(text for _, text in paragraph)
        for sentence in SENTENCE_SPLIT_RE.split(joined):
            sentence = sentence.strip()
            if not sentence:
                continue
            words = sentence.split()
            if len(words) > limit:
                report.warn(
                    start_line,
                    f"sentence of {len(words)} words, over the {limit} word nudge threshold.",
                    sentence,
                )


def render(report: Report, path: Path, limit: int) -> None:
    if report.warnings:
        print(f"Long sentences in {path} (warnings, these do not fail the build):\n")
        for line_number, message, excerpt in report.warnings:
            print(f"  {path}:{line_number}: {message}")
            if excerpt:
                wrapped = excerpt if len(excerpt) <= 400 else excerpt[:400] + "..."
                print(f"      {wrapped}\n")
        print(
            "  These are a nudge, not a rule. The voice contract asks for short declarative\n"
            "  sentences. Where a long one is doing real work, keep it.\n"
        )

    if report.errors:
        print(f"Errors in {path}:\n")
        for line_number, message, excerpt in report.errors:
            print(f"  {path}:{line_number}: {message}")
            if excerpt:
                print(f"      {excerpt}")
        print()
        print(
            f"{len(report.errors)} error(s). See CONTRIBUTING.md section 4 for the voice\n"
            "contract and why these are enforced mechanically."
        )
    else:
        counts = f"{len(report.warnings)} long sentence warning(s)"
        print(f"Style guard passed on {path}. No errors, {counts}.")
        print(f"Sentence length threshold: {limit} words.")


def main(argv: list) -> int:
    parser = argparse.ArgumentParser(
        description="Check the paper against the mechanical parts of the voice contract."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="LaTeX files to check")
    parser.add_argument(
        "--max-sentence-words",
        type=int,
        default=DEFAULT_SENTENCE_LIMIT,
        help=f"word count above which a sentence is reported (default {DEFAULT_SENTENCE_LIMIT})",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat long sentence warnings as errors",
    )
    args = parser.parse_args(argv)

    failed = False
    for path in args.paths:
        if not path.is_file():
            print(f"error: {path} is not a file")
            failed = True
            continue

        lines = parse(path.read_text(encoding="utf-8"))
        report = Report()
        check_dashes(lines, report)
        check_citations(lines, report)
        check_sentence_length(lines, report, args.max_sentence_words)
        render(report, path, args.max_sentence_words)

        if report.errors or (args.strict and report.warnings):
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
