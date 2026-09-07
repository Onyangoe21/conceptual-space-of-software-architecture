# How the Sources Were Read

The companion to [*What Computation Costs*](../paper/what-computation-costs.pdf). The paper
cites about a hundred sources and moves on. This directory holds the account of how each one
was read: where in the paper it is used, what it was taken to support, how it was interpreted,
where that interpretation could be wrong, and, where the paper leaned on a formal result without
explaining it, the result built up from scratch.

## The files

| File | What it is |
| --- | --- |
| [`sources.json`](sources.json) | The single source of truth. One object per cited work. Edit this and nothing else. |
| [`build_supplement.py`](build_supplement.py) | Renders the JSON to LaTeX. CI fails if the `.tex` is out of date with the JSON. |
| [`how-the-sources-were-read.tex`](how-the-sources-were-read.tex) | Generated. Do not edit by hand. |
| [`how-the-sources-were-read.pdf`](how-the-sources-were-read.pdf) | The compiled companion. |

The same JSON is rendered as a page at
[curiousedwin.com/publications/what-computation-costs](https://curiousedwin.com/publications/what-computation-costs),
where every entry can be opened, the source followed, and an objection filed against that entry
alone. The page fetches this file from `main`, so the site and the repository cannot drift.

## The fields

```json
{
  "key": "gray1987",
  "authors": "Gray, J., Putzolu, G. R.",
  "year": "1987",
  "title": "...",
  "venue": "...",
  "url": "https://doi.org/...",
  "open": "https://... (a free copy, when one exists)",
  "kind": "proved | measured | agreed | disputed, with a qualifier if needed",
  "used_in": ["Section titles of the paper where the source is cited"],
  "supports": "What the paper takes the source to establish.",
  "how_read": "How the source was interpreted, and what in the paper is the paper's own gloss.",
  "could_be_wrong": "Where the interpretation is weakest, stated by the authors of the paper.",
  "explainer": "Optional. The formal result explained from scratch."
}
```

`key` must match a `\bibitem` in the paper, and every `\bibitem` must have an entry here. That
correspondence is checked when the paper is built.

## Objecting to a reading

The `could_be_wrong` field is the authors' own statement of where each reading is weakest. If
you can do better, do. Either open an [erratum issue](../../../issues/new/choose) naming the key,
or file the objection on the web page, or edit `sources.json` and open a pull request. An
objection that survives changes the entry and, where it matters, the paper, with credit under
the [credit ladder](../docs/STANDARDS.md#the-credit-ladder-in-full).

## Regenerating

```bash
python3 supplement/build_supplement.py supplement/sources.json supplement/how-the-sources-were-read.tex
cd supplement && pdflatex how-the-sources-were-read.tex && pdflatex how-the-sources-were-read.tex
```
