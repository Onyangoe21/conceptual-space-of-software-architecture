# Changelog

Every content change to the paper, version by version, in human readable form.

This file is not a git log. A git log records that a file changed. This records what a reader
would now take away differently, and who is responsible for the difference. Formatting changes,
typo fixes that do not touch meaning, and repository infrastructure are out of scope and stay in
the commit history.

Each released version names every contributor whose work shipped in it, per
[GOVERNANCE.md](../GOVERNANCE.md#release-process). Entries are written before the arXiv upload,
not after.

Change categories used below:

- **Corrected** for errata: citations, attributions, facts.
- **Added** for new evidence integrated into the text: convergences, systems, migrations,
  estimator results.
- **Narrowed** for claims weakened or bounded in response to a counterexample or a review.
- **Restructured** for reorganization that changes how the argument reads.
- **Removed** for claims withdrawn.

---

## Unreleased

Changes merged into `main` and awaiting the next arXiv version. Until v1 is posted, anything
listed here ships inside v1 rather than in a revision after it.

### Restructured

- **Flat structure.** No table of contents and no Parts; eighteen short numbered sections
  in the order of the argument, from the machine to the predictions.
- **A standing referee.** `docs/REFEREE.md` rebuilds the world the paper stands on from
  Turing upward and records, step by step, what the paper answers, what it must answer,
  and what nobody has answered. Applied to this draft it produced the corrections below.

### Corrected

- A computer is defined as matter whose state changes correspond, for every input, to
  Turing's operations under an assigned interpretation; the substrate is not the computer.
- The unbounded tape is idealisation 1, priced per byte; distance is idealisation 2; the
  bills are said to set floors under the idealisations rather than to price each one.
- On a finite machine halting is decidable at an unpayable price, so the walls stand as
  prices; a new substrate moves prices, not walls.
- The three kinds of knowledge are derived from how fast reality answers (theorems where
  the object holds still, lookups where a fact holds still without a reason, rules where
  prices move), and the mechanisation episodes and the five-minute rule are presented as
  the same fact.
- Learned models are programs with fixed meaning; analogue computation is set aside.
- "Walls are theorems", not "theorems are walls"; idealisation 5 checked with 6, not with
  1 to 4; the census stated as the largest gap in evidence and the missing running example
  as the largest gap in explanation.

### Removed

- **The opening disclaimer and the Related Work section.** The paper now begins with
  Turing in 1936; the contributions are carried by the abstract and the Method subsection;
  the positioning against prior work stays inline where each source is used. Restatements,
  pre-empted objections (Landauer, Prime Video) and asides that no step of the argument
  used (Conway as cost law, Moore's law, the erosion of assignments) are cut. Six sources
  leave the reference list with them. About 10,500 words of body and 24 pages.

### Restructured

- **Condensed to claim-first prose and given the four anchors readers look for.** Every
  section now states its claim first and explains after; duplicated explanation, ornamental
  transitions and the folklore endnote are removed; the bibliography drops its annotations
  (the companion carries them). Added: a numbered list of the paper's eight claims in the
  opening section; a Method subsection at the end of section 4; a Related Work section that
  gathers the inline positioning; a Threats to Validity section. The body falls from about
  14,000 to about 11,000 words and the paper from 33 to about 26 pages with every table,
  hypothesis and prediction kept.
- **Consistency fixes found in review.** One line, not two, for where formal knowledge
  stops (cost models stop after idealisation 5, theorems after 6); the four bills mapped
  onto the five physical idealisations; idealisation 5 treated as a premise with measured
  overheads throughout; the criterion for sorting theorems stated; halt used in one sense;
  Prediction 5 restated as a halt cost; the automation ladder aligned with its table; the
  abstract's count of verdicts corrected; Gödel credited for general recursive functions.

### Corrected

- **Term: *deletion* is now *idealisation*.** The eight removed costs are named with the
  word physics and philosophy of science use for a real quantity deliberately set to zero
  (McMullin 1985 added); *deletion* collided with the everyday meaning of removing code.
  Glossary defines the term and the phrase "to pay under an idealisation".
- **Turing's choice machines acknowledged.** Section 1 quotes Turing setting the choice
  machine aside and says the model removes choice twice: the operator's, and the sheet
  writer's.
- **Halt attributed to the modern statement.** Turing's machines printed for ever; the
  idealisation is that the job is fixed when the machine starts, whichever statement is used.
- **Code claim narrowed to fixed meaning.** Randomness, concurrency and model calls are
  meaning fixed as "any of these"; the defect is meaning left unfixed by accident.
- **Lloyd's ratio scoped.** The 10^10 figure is for a kilogram in a litre near the physical
  rate limit; a machine near that limit must be parallel; real machines went parallel by
  choice. "No machine of ordinary density can be serial" withdrawn.
- **FLP and CAP restated precisely** (termination, not agreement; consistency against
  availability during a partition).
- **Simon 1969/1996 and Gunter, Gunter, Jackson and Zave 2000 cited** as the ancestors of
  the interpreter framing and the three tiers; the paper says what it inherits and adds.
- **Simon 1962 attribution corrected** (interrupted assembly, not bounded builders).

### Added

- **A preface addressed to three kinds of reader** (theorist, practitioner, requirements
  engineer) saying where each will find the thing they will want to check.
- **Section "Four Accounts a Reader Might Prefer"**: conventions all the way down; applied
  computer science; social standing and taste; the machine does not matter. Each imagined as
  true and met with the observation in the paper that decides against it.

### Restructured

- ***What Computation Costs* rebuilt on one backbone.** The paper now runs as a single
  story: Turing's machine as the exact description of a computer; code as the deterministic
  layer for telling it what to do; the engineer as an interpreter standing between a person
  who wants something and the machine; the *software intention* (a term the paper coins) as
  what the interpreter produces, shaped by what the machine cannot do (walls) and what it
  charges (the eight removed costs); the principles of the field reconstructed from those
  costs; and a closing invitation to find a principle that does not fit. A new section on
  what the machine cannot do at any price (undecidability, Rice, FLP, CAP) precedes the bills.
  Five sources added: Brooks 1987, Zave and Jackson 1997, Rice 1953, Fischer, Lynch and
  Paterson 1985, Gilbert and Lynch 2002. The companion is regenerated to match.

### Added

- **A second paper, *What Computation Costs*.** Puts the eight costs Turing's machine set to
  zero back one at a time, prices the five that physics can price, shows that the field's
  theorems and cost models stop at the boundary between those five and the other three,
  derives every engineering decision from the eight, asks of four famous rules what each is
  answerable to, writes the cost of a decision as four terms, and draws the consequence for
  verification when the cost of writing code collapses. Source at
  `paper/what-computation-costs.tex`.
- **A companion, *How the Sources Were Read*.** One entry per source the second paper cites,
  recording where it is used, what it was taken to support, how it was read, and where the
  reading could be wrong. Generated from `supplement/sources.json`, which is also what the
  web page renders.
- **CI now builds and style-guards all three documents**, and fails if the companion's
  `.tex` is out of date with its JSON.

---

## v1, not yet posted

Drafted August 2026. This will become the initial arXiv posting, and it is the baseline for
everything above. Until it is posted there is no frozen snapshot, only the current state of
`main`, so anything merged before the posting ships inside v1 rather than after it.

The paper as drafted: the four graph decomposition of the architectural object, the four tier
basis of seventeen entries, the three triangulating tests, six reduction tests against the
field's standing vocabulary, an empirical base of eighteen surveyed systems and five industrial
migrations, an assessment of what a machine can measure against what coding agents currently
represent, four undischarged limits, and six falsifiable predictions.

Authors: Edwin O Onyango, Walter Wagunde.

No external contributions yet. Any that land before the posting are named here and in the
acknowledgments before v1 goes up.
