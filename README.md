# The Conceptual Space of Software Architecture

**The latent variables that generate architectural decisions.**

[![Build paper](https://github.com/Onyangoe21/conceptual-space-of-software-architecture/actions/workflows/build-paper.yml/badge.svg)](https://github.com/Onyangoe21/conceptual-space-of-software-architecture/actions/workflows/build-paper.yml)
[![Style guard](https://github.com/Onyangoe21/conceptual-space-of-software-architecture/actions/workflows/style-guard.yml/badge.svg)](https://github.com/Onyangoe21/conceptual-space-of-software-architecture/actions/workflows/style-guard.yml)
[![Paper: CC BY 4.0](https://img.shields.io/badge/paper-CC%20BY%204.0-blue)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue)](LICENSE-CODE)

Ask two engineers to draw the architecture of the system they share and you will get two
different diagrams. Ask the same two engineers which proposed change is dangerous, which module
is load bearing, and which shortcut will be regretted, and they will largely agree. Whatever
architecture is, it is not the diagrams. It is the thing that lets two people who have never
compared diagrams make the same predictions.

This paper argues that the thing has a small number of moving parts. Not a catalog of styles and
patterns, but a short list of underlying quantities, such that every architectural decision, in
any system, is a move along one of them. The claim is that architecture is not a structure. It
is a set of decisions laid over four graphs: what the problem requires, what the code depends
on, what the runtime talks to, and who talks to whom in the organization. The variables that
position those decisions fall into four groups. Where the boundaries fall and whether the
boundaries on different graphs line up. Which orders sit over those boundaries, meaning who may
know about whom and whose decisions bind whose. What each decision costs to make and to unmake,
meaning how volatile it is, when it takes force, what reversing it would cost, and how far it
reaches. And finally the quality goals that orient the whole thing, held deliberately separate
from the coordinates, plus the drift that pulls a system downhill when nobody is pushing.

The evidence for those variables is that the field keeps rediscovering them. The measure now
called propagation cost was derived twice, once from a change cost argument and once from a
build cost argument, by authors who did not cite each other. Binding time appears independently
in five separate frameworks. The dominance order was discovered four times. One agreement
between two theories is a coincidence. A pattern of them is a signal that the variables are in
the territory rather than in the map. The paper collects those convergences, checks them against
eighteen surveyed systems and five industrial migrations, asks of every variable whether a
machine could estimate it, and closes with six falsifiable predictions.

## Read it

- **arXiv version (citable snapshot):** [ARXIV-LINK]
- **Latest compiled PDF from this repository:** [`paper/conceptual-space.pdf`](paper/conceptual-space.pdf)
- **LaTeX source, single file:** [`paper/conceptual-space-arxiv.tex`](paper/conceptual-space-arxiv.tex)
- **What has changed since arXiv v1:** [`paper/CHANGELOG.md`](paper/CHANGELOG.md)

Every pull request that touches the paper builds a PDF as a CI artifact, so you can read the
result of a proposed change without installing LaTeX.

## This paper is open

Most papers are finished when they are posted. This one is not, and the reason is structural
rather than sentimental.

The paper's central method is cumulative convergent evidence. A variable earns its place in the
basis when independent lines of work, starting from different premises and sharing no
vocabulary, keep arriving at it. That kind of argument does not get stronger by being rewritten.
It gets stronger by accumulating independent data points. One more documented convergence, one
more migration that moved in the unfashionable direction, one more surveyed system, one more
counterexample that the theory has to survive or bend to. Each of those is a small, bounded
piece of work, and each of them changes what the paper is entitled to claim.

So the model is this. The arXiv version is a snapshot, frozen and citable. This repository is
where the paper grows. Contributions that are merged here ship in the next arXiv version, with
credit. See [CONTRIBUTING.md](CONTRIBUTING.md) for the three ways in, [docs/STANDARDS.md](docs/STANDARDS.md)
for the bar, the file format, and the credit ladder in full, and [GOVERNANCE.md](GOVERNANCE.md)
for who decides what and how release timing works.

## How to contribute in ten minutes

**The shortest path is to email me at
[edwin.o.onyango.jr@gmail.com](mailto:edwin.o.onyango.jr@gmail.com)** and say what you want to
change, add, or tear down. Any form. A paragraph is fine. I answer within a week and I will help
shape it, or write it up and credit you. Everything below is for people who would rather work in
public.

You do not need to read all twenty six pages to add something useful. Pick whichever of these
matches what you already know.

1. **You know a system well.** Fill in one row of the survey. Copy
   [`evidence/systems/`](evidence/systems/) and describe how that system answers the recurring
   questions: process model, concurrency model, extension mechanism, topology, state management,
   isolation boundary, binding time, synchrony. Cite the engineers' own account of why.
2. **You lived through a migration.** File it in [`evidence/migrations/`](evidence/migrations/).
   The most valuable migrations are the ones that ran against the fashion of their moment,
   because the theory needs traffic in both directions to call an axis a real degree of freedom.
3. **You have noticed two theories saying the same thing.** File it in
   [`evidence/convergences/`](evidence/convergences/). Two bodies of work that derive the same
   quantity without citing each other is the paper's strongest evidence type.
4. **You think the paper is wrong.** File it in
   [`evidence/counterexamples/`](evidence/counterexamples/). This is the most valuable
   contribution type. See the FAQ below.
5. **You would rather write code.** Implement a basis variable as an estimator over a real
   repository. See [`estimators/README.md`](estimators/README.md).
6. **You spotted an error.** Open an erratum issue. Wrong citation, wrong year, wrong
   attribution of an idea, a claim the cited source does not actually support.
7. **You think a section should be restructured or taken apart.** Open a
   [proposal issue](../../issues/new?template=proposal.yml). Put your suggested wording straight
   into the issue. No fork and no LaTeX required.

Approvals are counted automatically. A thumbs up, an approving review, or a comment with
`/approve` on its own line each count as one approval from that person. Errata need none,
evidence needs one, counterexamples and proposals need two. Details in
[CONTRIBUTING.md](CONTRIBUTING.md).

Every one of these has an issue template with the fields already laid out. Start at
[**Issues, new issue**](../../issues/new/choose), or browse the
[**good first contribution**](../../issues?q=is%3Aissue+is%3Aopen+label%3Agood-first-contribution)
issues, which are specific and pre scoped: a named system nobody has surveyed yet, a suspected
convergence nobody has documented, a citation that needs strengthening.

Evidence files are markdown with a short front matter block. Filling one in honestly takes about
ten minutes if you already know the material.

## How you get credit

Three rungs, stated in full in [docs/STANDARDS.md](docs/STANDARDS.md#the-credit-ladder-in-full).

| Rung | What earns it | What you get |
| --- | --- | --- |
| One | Any merged erratum or evidence file | Your name in the Acknowledgments of the next arXiv version, and in [CONTRIBUTORS.md](CONTRIBUTORS.md) |
| Two | Work that materially changes the paper's content | A named credit line in the Acknowledgments describing what you contributed, in CRediT style role language |
| Three | Sustained, substantial intellectual contribution across multiple revisions | Possible co-authorship on future versions, decided openly in a governance issue, never promised in advance |

Authorship on already posted arXiv versions never changes retroactively. Rung three is a real
possibility and not a marketing device, which is exactly why it is not offered up front.

## Frequently asked

**Can I disagree with the paper?**
Yes, and this is the single most useful thing you can do. File a counterexample. The paper makes
falsifiable claims on purpose: that certain axes carry traffic in both directions, that others
carry it in only one, that congruence between graphs predicts outcomes better than single graph
metrics, that the basis is a fixed superset which framing re weights rather than extends. A
documented case that cuts against any of those forces a revision, and a theory that cannot be
cut against was not saying anything. Counterexamples are held to the same evidentiary bar as
supporting evidence, no higher and no lower.

**Do I need to know LaTeX?**
No. Evidence files are plain markdown. The maintainer does the integration into the paper text.
If you would rather draft the LaTeX yourself, you are welcome to, and the pull request template
has a box for saying so.

**Do I need academic credentials?**
No. A large share of the paper's empirical base is practitioner writing: post mortems,
architecture notes, mailing list threads where the engineers argued out their reasoning in
public. If you have shipped and maintained systems, you have seen data the literature has not
written down.

**What counts as a source?**
Primary sources wherever they exist. The engineers' own account, the post mortem, the paper, the
mailing list thread, the commit. Not a blog summarizing one of those. Archive your links, since
engineering blogs disappear.

**Is this affiliated with anyone?**
No. This is independent research, maintained by the author. Systems and migrations named in the
paper are named as evidence, from their public engineering accounts, and nothing here is
endorsed by or produced on behalf of any organization.

**How fast will you respond?**
Within one week for a first response. See [GOVERNANCE.md](GOVERNANCE.md) for the operating
rhythm and the release cadence.

## Repository layout

| Path | What lives there |
| --- | --- |
| [`paper/`](paper/) | The single source LaTeX file, the compiled PDF, and the content changelog |
| [`evidence/`](evidence/) | Convergences, migrations, surveyed systems, counterexamples |
| [`predictions/`](predictions/) | One folder per falsifiable prediction, each with a test protocol and results |
| [`estimators/`](estimators/) | Working code that computes a basis variable from a repository, its history, or traces |
| [`docs/`](docs/) | Maintainer notes, including the launch plan |

## Citing

Use [CITATION.cff](CITATION.cff), or cite the arXiv version directly. If you are citing a claim
that entered the paper through a contribution made here, cite the arXiv version that contains
it, and the contributor is credited in that version's acknowledgments.

## License

The paper text and all evidence files are licensed
[CC BY 4.0](LICENSE). Estimator code is licensed [MIT](LICENSE-CODE). By contributing you agree
to license your contribution under the corresponding license.

## Code of conduct

This project follows the [Contributor Covenant 2.1](CODE_OF_CONDUCT.md). The short version:
argue with the evidence, not the person.
