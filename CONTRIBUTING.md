# Contributing

This paper is an argument from accumulated evidence, which means it is the kind of argument that
gets stronger when other people add to it. This document explains what counts as an addition,
how good it has to be, what format it takes, and what you get for it.

Read the section that matches what you want to do. You do not need the whole document.

- [What we accept](#1-what-we-accept)
- [The bar](#2-the-bar)
- [Evidence file format](#3-evidence-file-format)
- [Voice contract for paper text](#4-voice-contract-for-paper-text)
- [The credit ladder](#5-the-credit-ladder)
- [Workflow](#6-workflow)

---

## 1. What we accept

Five kinds of contribution. Each one has an issue template that collects the right fields, and a
directory where the merged artifact lives.

### (a) Errata

**Issue template:** [Erratum](../../issues/new?template=erratum.yml) · **Lands in:**
`paper/conceptual-space-arxiv.tex` and a line in `paper/CHANGELOG.md`

Factual and citation errors. A wrong year, a misattributed idea, a page or volume number that
does not resolve, a quotation that the source does not contain, a claim attributed to a paper
that the paper does not make. This last one matters most. A synthesis of sixty years of
literature is exactly the kind of document where a citation can drift away from what its source
actually says, and the correction is cheap only if someone catches it.

Small errata are merged quickly and with thanks. They do not need to be dressed up as anything
larger.

### (b) New convergences

**Issue template:** [Convergence](../../issues/new?template=convergence.yml) · **Lands in:**
`evidence/convergences/`

Two or more bodies of work that independently derive the same variable. This is the paper's
strongest evidence type, because it is the whole basis of the method. The flagship example is
already in the paper: propagation cost and average cumulative component dependency are the same
mathematical object, the density of the transitive closure of the dependency graph, reached once
from a change cost argument and once from a build cost argument, by authors who did not cite
each other.

What makes a convergence count is independence. Two authors in the same research lineage, citing
each other or a common ancestor, arriving at the same measure is not convergence. It is
inheritance. The value of the evidence comes precisely from the absence of a path between them.
Convergences from outside software engineering are especially welcome and especially
under collected: hardware design, systems biology, organizational theory, control theory, and
economics all partition graphs under boundedness pressure and may have derived these variables
in their own vocabularies.

### (c) Migration and system evidence

**Issue template:** [Evidence](../../issues/new?template=evidence.yml) · **Lands in:**
`evidence/migrations/` or `evidence/systems/`

This extends the paper's empirical base, which currently rests on eighteen surveyed systems and
five industrial migrations. Both are small numbers for the weight they carry.

**Migrations** are the two way traffic test's raw material. A migration file documents a system
that moved along a named axis, in a named direction, under forces its engineers articulated.
Migrations that run against the prevailing fashion of their moment are worth several that run
with it, because the theory's claim is that these axes are genuine degrees of freedom rather
than a march toward one correct answer, and only counter fashion traffic can distinguish those
two.

**Systems** extend the variation table. A system file places one system on the recurring
columns: process model, concurrency model, extension mechanism, topology, state management,
isolation boundary, binding time, synchrony. The point of the table is to show that these
columns vary with substantial independence across respected systems, so the systems most worth
adding are the ones you expect to sit in an unusual combination of cells.

Unsuccessful and abandoned migrations are in scope, and are undersupplied in the public record
because nobody writes them up. If you can describe one accurately, from primary knowledge, do.

### (d) Counterexamples

**Issue template:** [Counterexample](../../issues/new?template=counterexample.yml) · **Lands
in:** `evidence/counterexamples/`

A documented case that cuts against an axis, a congruence claim, or a prediction. Some of the
paper's claims are shaped so that a single well documented case does real damage, and those are
the ones worth attacking first:

- An intentional, force justified migration **toward** a larger cyclic core would count against
  the classification of dependency graph health as a one way potential rather than a coordinate.
- A recurring decision dimension that architects use and that genuinely resists expression in
  the basis would count against the fixed superset claim, which holds that framing re weights
  the basis but does not manufacture new generators.
- A matched sample in which a single graph structural metric predicts maintenance outcomes
  better than the congruence terms would count against Prediction 2.
- A system where the four graphs cannot be separated, or where the logical and physical cuts are
  genuinely not independent choices, would cut at the paper's central empirical finding.

Counterexamples are held to exactly the same evidentiary bar as supporting evidence. Not higher,
which would make the theory unfalsifiable in practice while claiming falsifiability in
principle, and not lower, which would let anecdote overturn accumulated convergence. A
counterexample that survives review and forces a revision to the paper is a rung two
contribution.

### (e) Estimators

**Issue template:** [Estimator](../../issues/new?template=estimator.yml) · **Lands in:**
`estimators/`

Working code that computes a basis variable from a repository, its history, or its runtime
traces. The paper claims that roughly three quarters of the basis is machine estimable today,
and it tags each variable with what it needs: a bare repository, plus git history, plus runtime
traces, or plus human intent. That claim is currently an argument. Every estimator that runs
converts a piece of it into a demonstration, which is a considerably stronger thing.

See [`estimators/README.md`](estimators/README.md) for the interface, the output contract, and
what a submission needs to include.

---

## 2. The bar

Every substantive contribution is judged by the paper's own three tests. They are stated here in
plain language, because you should be able to apply them to your own contribution before you
file it, and because the maintainer will apply them in public, in writing, in the thread.

### Test one: independent derivation, the convergence test

*Does the evidence show the same variable being reached from an unconnected starting point?*

A quantity earns its place as a real dimension rather than an artifact of one author's formalism
when people solving different problems, from different premises, keep arriving at it. When you
claim a convergence, the burden is to show the independence, not just the similarity. Say
explicitly what you checked: that neither cites the other, that neither cites a common ancestor
that already contains the idea, that the vocabularies differ, that the motivating problems
differ. Similarity of formulas is the easy half. Absence of a path between them is the half that
carries the evidence.

### Test two: real systems moving under articulated forces, the two way traffic test

*Does the evidence show competent teams at opposite poles, and systems moving in both
directions?*

The paper's sharpest distinction is between a coordinate and a potential. A coordinate is a
genuine degree of freedom: competent designers sit at either pole depending on the forces they
face, and real systems move both ways over time. A potential is a slope nobody descends on
purpose: systems slide down it and must spend effort to climb out. A catalog cannot tell these
apart. The empirical record can, and only if the record includes the forces.

So evidence must carry the *why*, in the engineers' own words, not the analyst's reconstruction.
"They moved to a coarser deployment boundary" is not evidence. "They moved to a coarser
deployment boundary and named the specific operational cost that drove it, and here is where
they said so" is evidence. Migration evidence without stated forces is the most common reason a
contribution comes back with the `needs-sources` label.

### Test three: can a machine check it, the computability test

*Could a program compute this from a repository, its history, or its traces?*

A variable that is well defined but unestimable in principle can constrain theory, but it cannot
enter the working basis, because the working basis is meant to be something an agent estimates
on opening a repository. When you propose a variable or a refinement, say what evidence it needs
on the ladder: bare repository, plus git history, plus runtime traces, or plus human intent. If
it needs human intent, say what the human has to supply and how bounded that input is. The
reflexion model result matters here as a proof of scale: one engineer reflexion modeled a 1.2
million line codebase in about a month by iterating a hypothesized module map against computed
divergences. Human intent is an input, not an excuse.

### Counterexamples are judged by the same tests in reverse

A counterexample to an axis must show that the axis is *not* independently derived, or that
traffic on it is *not* two way, or that the variable is *not* estimable in the way claimed. A
counterexample to a prediction must show the predicted relationship failing on data where the
prediction says it should hold, with the same standards of primary sourcing and articulated
forces that supporting evidence carries. The rhetorically strongest counterexample is one where
you can also say what the theory would have to change to accommodate it.

### Sources

Primary wherever possible. The engineers' own account, the post mortem written by the team, the
peer reviewed paper, the mailing list thread where the argument actually happened, the commit,
the design document. Not a blog post summarizing any of those, not a conference talk recap, not
a secondary retelling that has already lost the reasoning.

Two practical rules:

1. **Archive every link.** Engineering blogs are deleted, reorganized, and rewritten. Include an
   archive link alongside the live link for every web source. Use the Wayback Machine or an
   equivalent, and include the capture date.
2. **Quote the load bearing sentence.** If a source is doing real work in your argument, quote
   the specific passage rather than citing the document as a whole. This makes review fast, and
   it catches the failure mode where a source is cited for a claim it does not quite make.

Where a source sits behind an access restriction, say so plainly and mark what you reconstructed
from secondary quotation. The paper already carries one such caveat about the enumerated value
sets in several classical dimension tables, and this kind of honesty costs nothing and buys the
reader's trust.

---

## 3. Evidence file format

Every file in `evidence/` is markdown with a YAML front matter block, then free prose. The
schema is deliberately small. If it takes you more than ten minutes to fill in the front matter,
the schema has failed and you should open an issue about it.

```markdown
---
claim: One sentence. What this file establishes, stated so it could be true or false.
type: convergence | migration | system | counterexample
axis: Which axis, congruence term, or prediction this touches.
sources:
  - title: Title of the source
    author: Who wrote it
    year: 2019
    url: https://example.org/the-primary-source
    archive: https://web.archive.org/web/20240101000000/https://example.org/the-primary-source
    primary: true
status: proposed
submitted-by: Your Name (@your-github-handle)
---

Free prose below. Explain the evidence, apply the three tests to it, and say what you think it
changes about the paper.
```

### Field reference

| Field | Required | Notes |
| --- | --- | --- |
| `claim` | yes | One sentence, falsifiable in shape. Not a topic label. See below. |
| `type` | yes | One of `convergence`, `migration`, `system`, `counterexample`. Must match the directory. |
| `axis` | yes | The axis name, congruence term, or prediction number. Free text is fine if the target does not have a crisp name yet. |
| `sources` | yes | At least one. Each entry needs `title`, `url`, and `primary`. Add `archive` for anything on the web, and `author` and `year` where they exist. |
| `status` | yes | `proposed` when you file it. The maintainer moves it. |
| `submitted-by` | yes | Name as you want it credited, plus handle. This is the name that goes in the acknowledgments. |

**Status values and who sets them.** You always file as `proposed`. The maintainer moves the file
to `accepted` when it passes the bar, to `integrated` when the corresponding change lands in the
paper text, and to `rejected` with written reasoning in the thread when it does not pass. A
rejected file may stay in the repository if it is instructive, since a well documented near miss
tells the next contributor something useful.

**On the `claim` field.** The most common weak submission has a claim like "notes on the Istio
control plane consolidation." That is a topic. The claim should be the thing you are asserting:
"the consolidation of four control plane deployables into one is documented two way traffic on
the granularity axis, at the coarse end, justified by measured operational cost." A reviewer
should be able to disagree with your claim by reading only that sentence.

**File naming.** Lowercase, hyphen separated, descriptive:
`propagation-cost-and-cumulative-component-dependency.md`,
`istio-control-plane-consolidation.md`. Do not number files.

Worked examples, written in full, are in
[`evidence/README.md`](evidence/README.md) and in the three example files already committed
under `evidence/convergences/`, `evidence/migrations/`, and `evidence/systems/`. Copying one of
those and editing it is the intended path.

---

## 4. Voice contract for paper text

This section applies only to prose proposed for `paper/*.tex`. Evidence files, issues, pull
request descriptions, and discussion posts are exempt. Write those however you write. Only the
paper itself carries the contract.

The paper has a specific register, and it is load bearing rather than decorative. The argument
asks the reader to slow down and follow a chain of reasoning across sixty years of literature.
The prose is built to make that possible.

**Short declarative sentences.** State one thing, then the next thing. The paper's hardest ideas
are carried by its plainest sentences. Where a sentence has grown past forty words or acquired
three subordinate clauses, it is usually two sentences that have not been separated yet.

**No em dashes and no en dashes anywhere in prose.** Use a comma, a colon, a full stop, or
restructure. This is enforced mechanically by CI, which will fail your pull request. The
bibliography block is exempt, since page ranges and multi author date ranges legitimately need
en dashes, and so are LaTeX comments.

**Plain language before formal names.** Every technical concept is introduced in ordinary words
before it is given its formal name, and never the other way around. The paper says that a cut is
nothing exotic, it is a partition of a graph's vertices into blocks, a decision about where the
lines get drawn, and only then uses the word freely. It explains that conceptual spaces are a
picture of how minds hold concepts, where qualities become dimensions and concepts become
regions and similarity becomes nearness, before it leans on the framework. A reader meeting an
idea for the first time should never have to look something up to continue.

**A contemplative pace at section openings.** Sections open by orienting the reader before they
argue. "We want to begin somewhere that almost feels too obvious to mention, because it is
usually in those places that the most important assumptions sit unnoticed." "Theory proposes;
the deployed world disposes." "A list of variables is not yet a space." The opening earns the
reader's attention rather than assuming it.

**Honesty markers stay.** The paper repeatedly flags the limits of its own evidence: a
replication gap, a sourcing caveat, a claim that is a hypothesis rather than a theorem. When you
propose text, carry the same habit. If your evidence is thinner than the sentence implies,
change the sentence.

**What CI checks and what the maintainer checks.** CI rejects em dashes and letter adjacent en
dashes mechanically, checks that every `\cite` key has a matching `\bibitem` and the reverse,
and prints a warning for any sentence over sixty words without failing on it. Everything else in
this section is editorial and reviewed by the maintainer in the pull request. You can run the
checker yourself before you push:

```bash
python3 .github/scripts/style_guard.py paper/conceptual-space-arxiv.tex
```

If you would rather not write LaTeX at all, do not. Submit the evidence file and the maintainer
writes the paper text. This is the default path and it is not a lesser contribution.

---

## 5. The credit ladder

Three rungs. They are written out here so that nobody has to guess, and so that the maintainer
can be held to them.

### Rung one: acknowledgment

**Earned by:** any merged erratum or evidence file.

Your name appears in the Acknowledgments section of the next arXiv version, and in
[`CONTRIBUTORS.md`](CONTRIBUTORS.md) in this repository with a link to what you contributed. The
name used is the one you put in `submitted-by` and in the pull request template's credit line,
so write it exactly as you want it to appear, including any diacritics.

This rung is automatic. A one line citation fix earns it. There is no threshold of significance
to clear.

### Rung two: named credit line

**Earned by:** contributions that materially change the paper's content. A new convergence that
gets integrated into the basis. A counterexample that forces a revision. An estimator that
converts a computability claim from an argument into a demonstration. A system or migration that
changes what a table or a finding is entitled to say.

You get a named credit line in the acknowledgments describing specifically what you contributed,
using [CRediT](https://credit.niso.org/) role language. For example: "Investigation and data
curation for the extended migration corpus" or "Software: reference implementation of the
propagation cost estimator" or "Formal analysis: identification of the convergence between X and
Y." Roles are named because "we thank the following people" flattens a one line fix and three
weeks of work into the same sentence, and that is not accurate.

The maintainer proposes the role language in the pull request thread and you can correct it
before merge. If you think your contribution belongs on this rung and it has been placed on rung
one, say so in the thread. That is a reasonable thing to raise and it will be answered in
writing.

### Rung three: co-authorship on future versions

**Earned by:** sustained, substantial intellectual contribution across multiple revisions.

This means shaping the argument rather than adding to it. Contributing a section. Reframing a
tier. Running a prediction protocol to a real result that changes the paper's conclusions.
Carrying a research lane over months.

How it is decided: by the maintainer, discussed openly in a governance issue, with the reasoning
written out. Never promised in advance and never negotiated as a condition of contributing. If
you are on a trajectory toward it, you will be told that plainly in the thread rather than left
to infer it.

Stated plainly, so there is no ambiguity: **authorship on the existing arXiv versions never
changes retroactively.** Rung three affects future versions only. A version that has been posted
and cited is a fixed historical object, and rewriting its author list would break the citation
record. If your contribution ships in v3, you are credited in v3 and every version after it, and
v1 and v2 stay exactly as they are.

### What is not on the ladder

Opening an issue that turns out to be wrong costs you nothing and is not held against you.
Filing a counterexample that the theory survives is still a contribution, and if the file is
well made it stays in the repository as `rejected` with the reasoning attached, credited at rung
one. The ladder rewards work that was done, not conclusions that happened to be right.

---

## 6. Workflow

1. **Check for an existing issue.** Someone may already be working on the same system,
   convergence, or migration. If there is an open issue, comment on it rather than starting a
   parallel effort.
2. **Open an issue first for anything substantive.** Use the template that matches. Errata and
   typo fixes can skip straight to a pull request. Everything else benefits from a short
   conversation before you spend an evening on it, mostly so the maintainer can tell you early
   if the evidence will not clear the bar.
3. **Fork and branch.** Branch names like `convergence/simon-and-alexander`,
   `migration/postgres-threading`, `erratum/lakos-year`.
4. **One contribution per pull request.** One convergence, one migration, one system, one
   counterexample, one estimator. This is not bureaucratic neatness. Each contribution is
   accepted or rejected on its own evidence, and a pull request containing three of them cannot
   be half merged.
5. **Fill in the pull request template**, including the credit line stating your name as it
   should appear.
6. **Expect a first response within one week.** If a week passes with silence, comment on the
   thread to bump it. That is not rude and it is not a nuisance.
7. **Expect the three tests applied in writing.** Whether the answer is acceptance or rejection,
   the reasoning is written out in the thread so you can argue with it. See
   [GOVERNANCE.md](GOVERNANCE.md).
8. **Integration.** Once evidence is accepted, the maintainer writes the paper text unless you
   said in the pull request that you want to draft the LaTeX. If you do want to, you take on the
   voice contract in section 4, and the maintainer will still edit for register before merge.

### Commit messages

Conventional commits, so the changelog can be assembled semi automatically:

```
evidence(convergence): add Simon and Alexander cut criteria convergence
evidence(migration): add PostgreSQL process to thread deliberation
paper: integrate binding time fifth convergence into Axis 12
fix(citation): correct Lakos 1996 page range
estimators: add propagation cost reference implementation
docs: clarify archive link requirement in CONTRIBUTING
```

### Licensing your contribution

By opening a pull request you agree to license prose and evidence under
[CC BY 4.0](LICENSE) and code under [MIT](LICENSE-CODE), matching the repository. There is no
separate contributor license agreement to sign.

---

## Questions

Anything that is not a specific contribution belongs in
[Discussions](../../discussions) rather than an issue. Questions about the theory, arguments
about whether something is a coordinate or a potential, and half formed ideas that are not
evidence yet are all welcome there.
