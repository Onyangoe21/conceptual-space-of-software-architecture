# Standards

The details behind [CONTRIBUTING.md](../CONTRIBUTING.md). Nobody needs to read this before
contributing. It is here so that when a judgment gets made, you can check it against something
written down rather than against a mood.

- [The bar: the paper's three tests](#the-bar)
- [Sources](#sources)
- [Evidence file format](#evidence-file-format)
- [Voice contract for paper text](#voice-contract-for-paper-text)
- [The credit ladder in full](#the-credit-ladder-in-full)
- [Review thresholds](#review-thresholds)
- [Commit messages](#commit-messages)

---

## The bar

Every substantive contribution is judged by the paper's own three tests. They are stated here in
plain language, because you should be able to apply them to your own work before you file, and
because they will be applied to it in public, in writing, in the thread.

### Test one: independent derivation, the convergence test

*Does the evidence show the same variable being reached from an unconnected starting point?*

A quantity earns its place as a real dimension, rather than as an artifact of one author's
formalism, when people solving different problems from different premises keep arriving at it.
When you claim a convergence, the burden is to show the independence, not the similarity. Say
what you checked: that neither source cites the other, that neither cites a common ancestor
already carrying the idea, that the vocabularies differ, that the motivating problems differ.
Similarity of formulas is the easy half. Absence of a path between them is the half that carries
the evidence.

### Test two: real systems moving under articulated forces, the two way traffic test

*Does the evidence show competent teams at opposite poles, and systems moving in both
directions?*

The paper's sharpest distinction is between a coordinate and a potential. A coordinate is a
genuine degree of freedom: competent designers sit at either pole depending on the forces they
face, and real systems move both ways over time. A potential is a slope nobody descends on
purpose. A catalog cannot tell these apart. The empirical record can, and only if it includes the
forces.

So evidence must carry the *why*, in the engineers' own words, not in your reconstruction. "They
moved to a coarser deployment boundary" is not evidence. "They moved to a coarser deployment
boundary and named the operational cost that drove it, and here is where they said so" is
evidence. Migration evidence without stated forces is the commonest reason a contribution comes
back labeled `needs-sources`.

### Test three: can a machine check it, the computability test

*Could a program compute this from a repository, its history, or its traces?*

A variable that is well defined but unestimable in principle can constrain theory, but it cannot
enter the working basis, because the working basis is what an agent estimates on opening a
repository. Say what your variable needs on the evidence ladder: bare repository, plus git
history, plus runtime traces, or plus human intent. If it needs human intent, say what the human
supplies and how bounded that input is. One engineer reflexion modeled a 1.2 million line
codebase in about a month by iterating a hypothesized module map against computed divergences.
Human intent is an input, not an excuse.

### Counterexamples are judged by the same tests in reverse

A counterexample to an axis must show that the axis is *not* independently derived, or that
traffic on it is *not* two way, or that the variable is *not* estimable as claimed. A
counterexample to a prediction must show the predicted relationship failing on data where the
prediction says it should hold, with the same standards of sourcing and articulated forces that
supporting evidence carries.

The bar is the same in both directions. Not higher for counterexamples, which would make the
theory unfalsifiable in practice while advertising falsifiability in principle. Not lower, which
would let anecdote overturn accumulated convergence. The rhetorically strongest counterexample is
one that also says what the theory would have to change to accommodate it.

---

## Sources

Primary wherever they exist. The engineers' own account, the post mortem the team wrote, the peer
reviewed paper, the mailing list thread where the argument actually happened, the commit, the
design document. Not a blog post summarizing any of those, and not a conference talk recap.

Two practical rules:

1. **Archive every link.** Engineering blogs get deleted, reorganized, and quietly rewritten.
   Include an archive link with a capture date alongside the live link for every web source.
2. **Quote the load bearing sentence.** If a source is doing real work in your argument, quote
   the passage rather than citing the document as a whole. This makes review fast, and it catches
   the failure mode where a source is cited for a claim it does not quite make.

Where a source sits behind an access restriction, say so plainly and mark what you reconstructed
from secondary quotation. The paper already carries one such caveat, about the enumerated value
sets in several classical dimension tables. A marked gap can be reviewed and worked around. An
unmarked one gets found later by somebody else, usually after the claim has been cited.

---

## Evidence file format

Every file in `evidence/` is markdown with a YAML front matter block, then free prose. The schema
is deliberately small. If the front matter takes you more than ten minutes, the schema has failed
and that is worth an issue.

```yaml
---
claim: One sentence. What this file establishes, stated so it could be true or false.
type: convergence | migration | system | counterexample
axis: Which axis, congruence term, or prediction this touches.
sources:
  - title: Title of the source
    author: Who wrote it
    year: 2019
    url: https://example.org/primary-source
    archive: https://web.archive.org/web/20240101000000/https://example.org/primary-source
    primary: true
status: proposed
submitted-by: Your Name (@your-handle)
---
```

| Field | Required | Notes |
| --- | --- | --- |
| `claim` | yes | One sentence, falsifiable in shape. Not a topic label. |
| `type` | yes | Must match the directory the file sits in. |
| `axis` | yes | Axis name, congruence term, or prediction number. Free text is fine when the target has no crisp name yet. |
| `sources` | yes | At least one. Each needs `title`, `url`, and `primary`. Add `archive` for anything on the web. |
| `status` | yes | `proposed` when you file. The maintainer moves it. |
| `submitted-by` | yes | The name that goes in the acknowledgments. Write it as you want to read it. |

**On the `claim` field.** The commonest weak submission has a claim like "notes on the Istio
control plane consolidation." That is a topic. The claim is the thing you are asserting: "the
consolidation of four control plane deployables into one is documented two way traffic on the
granularity axis, at the coarse end, justified by measured operational cost." A reviewer should
be able to disagree with your claim by reading only that sentence.

**Status lifecycle.** You file as `proposed`. It moves to `accepted` when it clears the bar,
`integrated` when the change lands in the paper text, or `rejected` with written reasoning in the
thread. Rejected files may stay in the repository when they are instructive, because a well
documented near miss saves the next contributor an evening.

**File naming.** Lowercase, hyphenated, descriptive, unnumbered.

Three reference examples are committed, one per shape, in
[`evidence/convergences/`](../evidence/convergences/),
[`evidence/migrations/`](../evidence/migrations/), and
[`evidence/systems/`](../evidence/systems/). Copying one and editing it is the intended path.

---

## Voice contract for paper text

Applies only to prose proposed for `paper/*.tex`. Evidence files, issues, pull requests, and
discussion posts are exempt. Write those the way you write.

The paper has a specific register, and it is load bearing rather than decorative. The argument
asks the reader to follow a chain of reasoning across sixty years of literature, and the prose is
built to make that possible.

**Short declarative sentences.** State one thing, then the next. The paper's hardest ideas are
carried by its plainest sentences. A sentence past forty words with three subordinate clauses is
usually two sentences that have not been separated yet.

**No em dashes and no en dashes anywhere in prose.** Use a comma, a colon, a full stop, or
restructure. CI enforces this and will fail your pull request. The bibliography block is exempt,
since page ranges legitimately need en dashes, and so are LaTeX comments.

**Plain language before formal names.** Every technical concept is introduced in ordinary words
before it is given its formal name, never the reverse. The paper says a cut is nothing exotic, it
is a partition of a graph's vertices into blocks, a decision about where the lines get drawn, and
only then uses the word freely. A reader meeting an idea for the first time should never have to
look something up to continue.

**A contemplative pace at section openings.** Sections orient the reader before they argue. "We
want to begin somewhere that almost feels too obvious to mention." "Theory proposes; the deployed
world disposes." "A list of variables is not yet a space." The opening earns attention rather
than assuming it.

**Honesty markers stay.** The paper repeatedly flags the limits of its own evidence: a
replication gap, a sourcing caveat, a hypothesis that is not a theorem. Carry the same habit. If
your evidence is thinner than your sentence implies, change the sentence.

Run the mechanical checks yourself before pushing:

```bash
python3 .github/scripts/style_guard.py paper/conceptual-space-arxiv.tex
```

CI rejects dashes, checks that every `\cite` key has a matching `\bibitem` and the reverse, and
prints a warning for sentences over sixty words without failing on them. Everything else in this
section is editorial and reviewed in the pull request.

If you would rather not write LaTeX, do not. Submit the evidence and the maintainer writes the
paper text. That is the default path and it earns the same rung on the credit ladder as drafting
the text yourself.

---

## The credit ladder in full

### Rung one: acknowledgment

**Earned by** any merged erratum or evidence file.

Your name appears in the Acknowledgments of the next arXiv version and in
[`CONTRIBUTORS.md`](../CONTRIBUTORS.md) with a link to what you contributed. The name used is the
one you gave, so write it exactly as you want it to appear, including diacritics.

This rung is automatic. A one line citation fix earns it. There is no threshold of significance
to clear.

### Rung two: named credit line

**Earned by** contributions that materially change the paper's content. A new convergence
integrated into the basis. A counterexample that forces a revision. An estimator that converts a
computability claim from an argument into a demonstration. Evidence that changes what a table is
entitled to say.

You get a named credit line in the acknowledgments describing specifically what you contributed,
in [CRediT](https://credit.niso.org/) role language. For example: "Investigation and data
curation for the extended migration corpus." Roles are named because "we thank the following
people" flattens a one line fix and three weeks of work into the same sentence, and that is not
accurate.

The maintainer proposes the role language in the thread and you can correct it before merge. If
you think your contribution belongs on this rung and it was placed on rung one, say so in the
thread. Either the placement changes or the reasoning for it gets written out.

### Rung three: co-authorship on future versions

**Earned by** sustained, substantial intellectual contribution across multiple revisions.
Shaping the argument rather than adding to it. Contributing a section. Reframing a tier. Running
a prediction protocol to a result that changes the conclusions. Carrying a research lane over
months.

Decided by the maintainer, discussed openly in an issue labeled `governance`, with the reasoning
written out. Never promised in advance and never negotiated as a condition of contributing. If
you are on a trajectory toward it, you will be told plainly rather than left to infer it.

**Authorship on existing arXiv versions never changes retroactively.** A posted, cited version is
a fixed historical object. If your work ships in v3, you are credited in v3 and everything after
it, and v1 and v2 stay as they are.

### What is not on the ladder

An issue that turns out to be wrong carries no cost, because nothing in this project tracks a hit
rate. A counterexample the theory survives is still a contribution, credited at rung one, and the
file may stay in the repository as `rejected` with the reasoning attached. The ladder rewards work
that was done, not conclusions that happened to be right.

---

## Review thresholds

Proposals and pull requests pass when enough people other than the author have said yes. The
count is automated: a thumbs up reaction on the issue or pull request body, an approving review,
or a comment containing `/approve` on its own line, all count as one approval per person.

| What you filed | Approvals needed |
| --- | --- |
| Erratum, meaning a citation or factual fix | 0. It gets merged when it is right. |
| Evidence, convergence, estimator | 1 |
| Counterexample | 2 |
| Proposal to rewrite or restructure a section | 2 |

When the threshold is met, the automation labels the thread `ready-to-integrate` and says so in a
comment. The maintainer still does the integration, and still writes out the three tests, because
approvals establish that other people find the evidence credible and do not establish that it
belongs in the paper.

**The bootstrap exception.** This project is new and may not have two available reviewers for a
while. If a proposal sits for fourteen days without reaching its threshold, the automation labels
it `maintainer-decision` and the maintainer decides alone, in writing, in the thread. A review
requirement that silently blocks everything is worse than no review requirement, and pretending
otherwise would just mean nothing ever moves.

**Approving is a real act.** If you approve something, you are saying you checked it, not that
you like the idea. Approvals from people who did not read the sources are worse than no approvals,
because they launder a claim into the paper. Saying "I read the primary source and it says what
the file says it says" in a comment is worth more than a reaction.

---

## Commit messages

Conventional commits, so the changelog can be assembled semi automatically.

```
evidence(convergence): add Simon and Alexander cut criteria convergence
evidence(migration): add PostgreSQL process to thread deliberation
paper: integrate binding time fifth convergence into Axis 12
fix(citation): correct Lakos 1996 page range
estimators: add propagation cost reference implementation
docs: clarify archive link requirement
```

## Licensing your contribution

By opening a pull request you agree to license prose and evidence under
[CC BY 4.0](../LICENSE) and code under [Apache 2.0](../LICENSE-CODE). There is no separate
contributor license agreement to sign, and there will not be one. Apache 2.0 section 5 already
does the work a CLA usually does: a contribution you submit for inclusion is under the same terms
as the license itself, unless you say otherwise in writing in the pull request.

That means the patent grant in section 3 runs in both directions. You grant it for what your
contribution necessarily infringes, and every other contributor has granted it to you for theirs.
Both grants are scoped to the code, and terminate for a party who brings a patent suit alleging
that the code infringes. If you are contributing on behalf of an employer, check that you have the
authority to grant this, which is the same check any Apache project asks for.

Add the standard header to every source file you contribute:

```
Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

Keep your own copyright line. Contributing does not assign it to anyone, here or elsewhere.

[PATENTS.md](../PATENTS.md) states the whole position in one place, including what the paper's
CC BY 4.0 license does not grant.
