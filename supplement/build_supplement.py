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

"""Generate the companion document "How the Sources Were Read" from sources.json.

The JSON file is the single source of truth. This script renders it to LaTeX; the web page
under curiousedwin.com renders the same file. Edit the JSON, never the .tex.

    python3 supplement/build_supplement.py supplement/sources.json supplement/how-the-sources-were-read.tex
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

SPECIAL = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}


def esc(text: str) -> str:
    return "".join(SPECIAL.get(c, c) for c in text)


PREAMBLE = r"""\documentclass[11pt,oneside]{article}
\pdfoutput=1
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[a4paper,margin=1.05in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{microtype}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{setspace}
\usepackage[hidelinks,breaklinks]{hyperref}
\usepackage{parskip}
\usepackage{enumitem}
\definecolor{accent}{RGB}{40,72,120}
\hypersetup{colorlinks=true,linkcolor=accent,citecolor=accent,urlcolor=accent}
\titleformat{\section}{\large\bfseries\color{accent}}{\thesection}{0.6em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection}{0.6em}{}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape How the Sources Were Read}
\fancyhead[R]{\small\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\setstretch{1.04}
\setlength{\parskip}{0.4em}
\newcommand{\field}[1]{\par\noindent\textbf{\color{accent}#1.}\ }
\title{\vspace{-1.2cm}\textbf{\color{accent}How the Sources Were Read}\\[0.3cm]
\large Companion to \emph{What Computation Costs}}
\author{Edwin O Onyango \and Walter O Wagunde}
\date{September 2026}
\begin{document}
\maketitle
\thispagestyle{empty}

\section*{What this is}
\emph{What Computation Costs} rests on about a hundred sources. The paper cites them and moves
on. This document is the account of how each was read: where in the paper it is used, what it
was taken to support, how it was interpreted, and where that interpretation could be wrong.
Where the paper needed a formal result explained from scratch and the explanation was not part
of the argument, the explanation is here, under the source it belongs to.

The document exists so that a reader who doubts a claim can go straight to the reading behind
it, and so that the reading can be objected to. Every entry here is also published as a page at
\url{https://curiousedwin.com/publications/what-computation-costs/sources}, where each
interpretation can be opened, the source followed, and an objection filed against that entry
alone. Objections that survive change the paper, with credit, under the process described in
the repository.

The file this document is generated from, \texttt{supplement/sources.json}, is the single source
of truth. The web page and this PDF are two renderings of it.

\section*{Where each source is used}
"""


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    src = json.loads(Path(argv[0]).read_text())
    src.sort(key=lambda s: s["key"])

    by_section: dict[str, list[str]] = defaultdict(list)
    for s in src:
        for sec in s.get("used_in", []):
            by_section[sec].append(s["key"])

    out = [PREAMBLE]
    out.append(r"\begin{description}[leftmargin=1.2em,itemsep=1pt]")
    for sec, keys in by_section.items():
        refs = ", ".join(r"\hyperlink{src:%s}{%s}" % (k, esc(k)) for k in keys)
        out.append(r"\item[%s] %s" % (esc(sec), refs))
    out.append(r"\end{description}")
    out.append(r"\section*{The sources, one by one}")
    out.append(r"\addcontentsline{toc}{section}{The sources, one by one}")

    for s in src:
        out.append(r"\hypertarget{src:%s}{}" % s["key"])
        out.append(r"\subsection*{%s (%s). %s}" % (esc(s["authors"]), esc(s["year"]), esc(s["title"])))
        out.append(r"\noindent\small\emph{%s}. Key \texttt{%s}. Standing: %s." % (esc(s["venue"]), esc(s["key"]), esc(s["kind"])))
        out.append(r"\par\noindent\small Source: \url{%s}" % s["url"])
        if s.get("open"):
            out.append(r"\par\noindent\small Open copy: \url{%s}" % s["open"])
        out.append(r"\normalsize")
        out.append(r"\field{Used in} %s." % esc("; ".join(s.get("used_in", []))))
        out.append(r"\field{Taken to support} %s" % esc(s["supports"]))
        out.append(r"\field{How it was read} %s" % esc(s["how_read"]))
        out.append(r"\field{Where the reading could be wrong} %s" % esc(s["could_be_wrong"]))
        if s.get("explainer"):
            out.append(r"\field{The result, from scratch} %s" % esc(s["explainer"]))
        out.append("")

    out.append(r"\end{document}")
    Path(argv[1]).write_text("\n".join(out) + "\n")
    print(f"wrote {argv[1]} with {len(src)} sources")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
