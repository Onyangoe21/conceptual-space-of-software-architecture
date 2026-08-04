# Governance

This is a small project with one maintainer and an unusual property: the artifact being governed
is a paper with a fixed author line, not a codebase with a rotating committer list. That makes
the governance question sharper than usual. Someone has to decide what enters the paper, and
that person's judgment is not neutral. The response is not to pretend otherwise. It is to make
every decision in public with the reasoning written out, so that the judgment can be inspected
and argued with.

## Maintainer

**Edwin O Onyango**, [@Onyangoe21](https://github.com/Onyangoe21), edwin.o.onyango.jr@gmail.com

The maintainer decides what enters the paper. There is no committee, no voting, and no pretense
of consensus process. What there is instead is an obligation to explain.

## How decisions are made

Every decision about what enters the paper is made in public, in the issue or pull request
thread where the contribution lives, with the reasoning written out.

That last clause is the whole of it. A decision announced without reasoning cannot be
challenged, and a decision that cannot be challenged is not accountable to anything. So the
maintainer writes out why, at whatever length the decision needs. A citation fix needs a
sentence. A contested counterexample may need several paragraphs.

Nothing that affects the paper's content is decided in private channels. If a conversation about
a contribution starts somewhere else, by email or in person or in a talk after a conference, the
substance of it gets written back into the public thread before any decision follows from it.

### Resolving disputes about whether evidence meets the bar

When it is unclear whether a contribution clears the bar, and when a contributor disagrees with
a rejection, the resolution procedure is to write out the paper's three tests against that
specific evidence, explicitly, in the thread. Not to assert a conclusion. To show the work.

The maintainer writes, in order:

1. **The convergence test.** Does this show the same variable derived from an independent
   starting point? Where is the independence established, and where is it assumed? If the two
   sources share a lineage, say where the shared ancestor sits.
2. **The two way traffic test.** Does this show real systems moving under forces the engineers
   articulated? Are the forces in the sources, or are they the contributor's reconstruction? Is
   there traffic in the other direction, and if not, does that make this a potential rather than
   a coordinate?
3. **The computability test.** Could a machine check this? What does it need on the evidence
   ladder? If it needs human intent, how bounded is that input?

Then a conclusion, and then what would change it. That last part is required. A rejection that
does not say what additional evidence would flip it is a dead end rather than a decision, and it
tells the next contributor nothing.

This procedure applies symmetrically to counterexamples. A counterexample the maintainer would
prefer to reject is exactly the case where the written reasoning matters most, because the
maintainer has an obvious interest in the theory surviving. Writing the three tests out in full,
in public, is the check against that interest. Readers are invited to hold the maintainer to it,
and pointing out that a rejection skipped a test is a legitimate and welcome intervention.

### When the maintainer is wrong

A decision can be revisited. Reopen the issue, or open a new one referencing the old thread,
with the new argument or the new evidence. There is no appeal body, because there is nobody to
appeal to. There is only the written record, which is public and permanent, and the fact that a
maintainer who repeatedly rejects good evidence on bad reasoning will have done so in a form
anyone can read.

### Governance questions

Anything about how the project is run rather than what the paper says goes in an issue labeled
`governance`. This includes the credit ladder's application to a specific contribution, rung
three discussions, changes to the bar, changes to the contribution schema, and changes to this
document. Governance issues are open for comment before a decision.

## Release process

The paper revs to arXiv as v2, v3, and so on, when accumulated merged changes justify a new
version.

**Cadence.** Roughly quarterly, and never more than once a month. The upper bound is a
discipline rather than a policy detail. Each arXiv version is a citable object that somebody may
build on, and versions that churn faster than the literature can absorb make the citation record
worse rather than better. If merged changes accumulate faster than that, they wait in `main`,
where they are public and readable, until the next window.

**What justifies a release.** A judgment call, made in public in a `governance` issue before the
release is prepared. The rough shape of it: a release is justified when the merged changes would
alter what a careful reader takes away. A new convergence integrated into a tier. A counterexample
that forced a claim to be narrowed. Enough new systems or migrations that a table's conclusion is
differently supported. A batch of errata alone can justify a release if any of them affect a
claim rather than only a citation.

**What a release consists of.** Each release produces, in this order:

1. A `governance` issue announcing the intent to release, listing every merged change that will
   ship in it, open for comment for at least one week. This is where a contributor can say that
   their credit line is wrong, or that a change misrepresents their evidence, while it is still
   cheap to fix.
2. An updated `paper/CHANGELOG.md` entry for the version, naming **every contributor** whose work
   ships in it, with what they contributed. The changelog is the permanent public record of who
   built what, and it is written before the arXiv upload rather than after.
3. Updated acknowledgments in `paper/conceptual-space-arxiv.tex`, carrying rung one names and
   rung two named credit lines in CRediT style role language, per
   [CONTRIBUTING.md](CONTRIBUTING.md).
4. A compiled PDF committed to `paper/conceptual-space.pdf`. The PDF is committed only on
   release, so that the file in `main` always corresponds to a posted version rather than to an
   intermediate state. Between releases, read the CI artifact from any pull request.
5. The arXiv upload, producing the new version number.
6. A git tag matching the arXiv version exactly: `v2`, `v3`, and so on, on the release commit,
   with the arXiv identifier in the tag message. A reader who has a citation to a specific arXiv
   version can then check out the exact source that produced it.
7. A GitHub release attached to the tag, with the changelog entry as its body.
8. A post in the Announcements discussion category.

**Contributor credit is not optional and not batched away.** Every contributor whose work ships
in a version is named in that version's changelog entry and in that version's acknowledgments.
If a change is small enough that the maintainer is tempted to skip the credit, the change was
still large enough to merge, and those are the same threshold.

## Operating rhythm

- **Weekly.** The maintainer triages new issues and pull requests. Labels applied, obvious
  errata merged, contributions that need more sources marked `needs-sources` with a note saying
  which specific claim needs which specific kind of source.
- **First response within one week**, for everything. A first response may be a question rather
  than a decision. If a week has passed in silence, bumping the thread is the correct thing to
  do.
- **Monthly.** A post in Discussions summarizing what was merged, what is open, and what the
  project most needs next. Written whether or not the month was busy, because a quiet month is
  itself information for anyone deciding whether to invest an evening here.
- **Quarterly, roughly.** An arXiv revision, per the release process above.

## Scope of this document

This document governs the paper and its evidence base. Estimator code under `estimators/` is
held to a lighter standard: it needs to run, to state what it computes and on what evidence, and
to be licensed MIT. It does not need to change the paper to be worth merging.

Changes to this document are made through a `governance` issue, open for comment, decided by the
maintainer in writing, like everything else.
