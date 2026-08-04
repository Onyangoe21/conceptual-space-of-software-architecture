# Launch plan

These are the maintainer's notes on how this repository gets opened to the world. They are
public, which is unusual for a launch plan, and deliberate. A project that asks contributors to
write their reasoning out in the open cannot keep its own process private and expect to be taken
seriously. If the sequencing below is wrong, someone reading it can say so.

The plan has four phases. The ordering constraint that shapes all of them: attention arrives
once. A person who visits after the announcement, finds nothing they can act on, and leaves,
does not come back a month later to check whether it improved.

---

## Phase 0: before any announcement

**Goal:** a visitor who arrives cold can find something to do within ten minutes.

Complete before anything is shared with anyone:

- [x] Repository structure complete, every directory has a README that explains itself
- [x] Paper source and compiled PDF committed
- [x] `CONTRIBUTING.md` with the bar, the schema, the voice contract, and the credit ladder
      written out in full
- [x] `GOVERNANCE.md` with the decision procedure and the release process
- [x] Code of conduct with a real contact address
- [x] Both licenses in place: CC BY 4.0 for the text, MIT for code
- [x] `CITATION.cff` valid
- [x] Three example evidence files committed, one per shape, marked as reference examples so
      nobody mistakes them for open slots
- [x] Six prediction folders, each with a protocol stating its own falsification condition, with
      Prediction 5 specified tightly enough to actually run
- [x] Five issue templates, each collecting the evidence schema fields, each auto labeling
- [x] Pull request template with the three tests and the credit line
- [x] Both CI workflows green on the committed paper
- [x] All labels created
- [ ] arXiv identifier filled in everywhere it is currently a placeholder
- [ ] Five to ten issues pre filed by the maintainer as `good-first-contribution`

**On the pre filed issues.** This is the part that decides whether the launch works, and it is
the part most easily skipped in the rush to announce.

An empty repository wastes the attention it attracts. A visitor arrives with roughly ten minutes
of goodwill and a vague willingness to help. If the only thing on offer is a general invitation
to contribute evidence, they have to first understand the theory well enough to know what
evidence would count, then find some, then decide whether it is good enough. Almost nobody
crosses all three gaps in one sitting.

A specific issue collapses all three. "Survey this named system on the variation table, here are
the eight columns, here is a filled in example, here is one primary source to start from" is a
task someone can finish in an evening, and finishing it teaches them the theory better than
reading the paper would have.

So the pre filed issues must be specific. Each one names a target, says why it matters to the
paper, points at the example to copy, and where possible names one source to start from. Good
categories, five to ten total:

- A named system nobody has surveyed, chosen because it likely sits in an unusual combination of
  cells on the variation table.
- A migration the maintainer knows exists but has not documented, especially one that ran
  against the fashion of its moment.
- A suspected convergence, stated as a hypothesis, with both candidate sources named and the
  independence check left as the work.
- A citation in the paper that rests on secondary quotation and should be verified against the
  primary table.
- An estimator for a specific variable, with the definition and the source of the definition
  named.
- Part one of Prediction 4, which is pure computation and needs no coordination with anyone.

Each should be honestly achievable in an evening or a weekend. An issue labeled as a good first
contribution that actually takes three weeks is worse than no issue at all, because the person
who tries it will not come back.

---

## Phase 1: soft launch

**Goal:** find the friction before an audience does.

Share the repository quietly with five to ten people whose judgment the author trusts.
Practitioners who have lived through the migrations, researchers in adjacent areas, and at least
two people expected to disagree with the thesis. The last group is the most useful and the
easiest to leave out.

Ask each for exactly one thing: file one contribution, or review one. Not "take a look and let
me know what you think," which produces polite encouragement and no data. A single concrete act
surfaces the friction that reading never does.

What to watch for, in priority order:

1. **Where they stop.** The step where someone abandons the process is the step to fix. If three
   of eight stall at the same place, that place is the launch blocker.
2. **What they ask that the documentation should have answered.** Every such question is a
   documentation defect, and the fix goes in before the public announcement rather than into a
   backlog.
3. **Whether the schema fits their evidence.** The ten minute claim is testable and this is the
   test. If filling in the front matter takes them forty minutes, the schema is wrong.
4. **Whether the bar reads as achievable or as gatekeeping.** The three tests are demanding on
   purpose, and there is a real risk they read as a wall rather than as a standard. If capable
   people conclude their evidence would not qualify, the framing needs work, not the bar.
5. **Whether the credit ladder is believed.** Rung three in particular. If it reads as an empty
   promise, it is worse than not offering it.

Fix the friction. Then, if the fixes were substantial, do a second small round rather than
assuming they worked.

Exit criterion: at least two contributions filed by people other than the maintainer, and the
friction they hit fixed.

---

## Phase 2: public announcement

**Goal:** the arXiv link and the repository arrive together, framed so the openness reads as a
consequence of the method rather than a marketing device.

**Timing.** The announcement post and the arXiv link go out together. Not the paper first and
the repository later, which trains people to treat the paper as finished. Not the repository
first, which asks people to invest in something they cannot yet cite.

**Framing.** One paragraph, roughly this shape:

> We wrote a paper arguing that software architecture has a small set of discoverable latent
> variables, and that the field has been rediscovering them independently for sixty years
> without noticing. The evidence is cumulative: the argument gets stronger with every
> independent data point, and weaker with every documented case that cuts against it. That is an
> unusual property for a paper to have, and it seemed dishonest to publish it as a finished
> object. So the paper is open. Contributions of evidence, counterexamples, and estimators are
> welcome, and they ship in the next version with credit.

What the framing must avoid:

- Claiming a finished result. The paper is a synthesis with six untested predictions and four
  undischarged limits, and saying so plainly is both accurate and more interesting than the
  alternative.
- Treating openness as generosity. It is a consequence of the method. A convergent evidence
  argument that refuses outside evidence is not much of an argument.
- Asking for stars, follows, or attention. Ask for one specific act.

**Call to action, one sentence.** Pick a good first contribution issue, or file a counterexample.

Naming the counterexample path in the call to action is deliberate. It signals that
disagreement is wanted rather than tolerated, and disagreement is the contribution the project
most needs and is least likely to receive by default.

**Being ready for the first week.** The announcement should not go out before a week in which
the maintainer can respond within a day. First contributors who wait five days for a reply do
not file a second contribution, and the first week sets the project's reputation for
responsiveness more than the following six months do.

---

## Phase 3: operating rhythm

The rhythm is specified in [GOVERNANCE.md](../GOVERNANCE.md#operating-rhythm) and repeated here
because a launch plan that ends at the announcement is the reason most open research projects
are archived within a year.

- **Weekly.** Triage new issues and pull requests. Label them. Merge obvious errata. Mark
  anything short on sources as `needs-sources`, and say which specific claim needs which
  specific kind of source rather than leaving a bare label.
- **First response within one week**, without exception. A first response can be a question. It
  cannot be silence.
- **Monthly.** A post in Discussions summarizing what was merged, what is open, and what the
  project most needs next. Written in quiet months too. A quiet month is information for anyone
  deciding whether to invest an evening here, and hiding it only wastes their time later.
- **Quarterly, roughly.** An arXiv revision, with the full release process: the announcement
  issue open for a week, the changelog naming every contributor whose work shipped, updated
  acknowledgments, a committed PDF, a git tag matching the arXiv version, and a release.

### The failure modes to watch for

Named here so they can be recognized early rather than diagnosed in a postmortem.

**Silence after the launch spike.** Attention arrives once and decays fast. The recovery is the
pre filed issue queue, kept stocked. If the good first contribution issues are exhausted and not
replenished, the repository becomes read only in practice while still looking open.

**The bar applied unevenly.** The temptation is to accept weak evidence that supports the thesis
and demand rigor of evidence that cuts against it. The written three test procedure exists as
the check, and it only works if it is applied to the comfortable cases too. If the maintainer
notices having skipped the written reasoning on an easy acceptance, that is the early warning.

**Credit drifting.** Rung two contributions quietly acknowledged at rung one, because writing
the CRediT line is more work than adding a name to a list. This is the failure that ends
projects, and it is invisible to the maintainer and glaring to the contributor.

**The paper freezing anyway.** Evidence accumulating in `evidence/` while `paper/` stays
untouched, because integration is harder than merging. The changelog's Unreleased section is the
instrument: if it is long and old, integration has stopped and the living paper model has
quietly become an archive with a suggestions box.
