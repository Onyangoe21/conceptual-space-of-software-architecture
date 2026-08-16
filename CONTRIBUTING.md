# Contributing

**If you have something, tell me. Do not study the process first.**

This paper argues that architecture has a small set of underlying variables, and its evidence is
cumulative: it gets stronger with every independent data point and weaker with every documented
case that cuts against it. So the useful thing you can do is add a data point or take one away.
Everything below is just plumbing for that.

## Three ways in, easiest first

**1. Email me.** [edwin.o.onyango.jr@gmail.com](mailto:edwin.o.onyango.jr@gmail.com). Tell me what
you want to change, add, or tear down, in whatever form it is currently in. A paragraph is fine. I
answer within a week. If it turns out to be worth doing, I will help you shape it, or I will write
it up and credit you. This is the preferred path and it is not a lesser one.

**2. Open a proposal issue.** [Use the proposal template](../../issues/new?template=proposal.yml)
if you would rather work in public or you already know what you want to say. Put your suggested
wording directly in the issue. You do not need a fork, a branch, or LaTeX.

**3. Edit a file in the browser.** Any markdown file in this repository has a pencil icon on
GitHub. Click it, edit, describe what you changed. GitHub makes the fork and the pull request for
you. This is the whole workflow for adding an evidence file.

Prefer talking to guessing. If you are not sure whether something counts, ask, and the answer will
be a sentence rather than a rejection.

## How something passes

Approvals are counted automatically. A thumbs up on the issue or pull request, an approving
review, or a comment with `/approve` on its own line each count as one approval from that person.

| What you filed | Approvals needed |
| --- | --- |
| Citation or factual fix | 0, it just gets merged |
| Evidence, convergence, estimator | 1 |
| Counterexample | 2 |
| Proposal to rewrite or restructure a section | 2 |

When the count is reached, the thread is labeled `ready-to-integrate` automatically. If a proposal
sits fourteen days without reaching its threshold, it gets labeled `maintainer-decision` and I
decide alone, in writing, in the thread. A review requirement that silently blocks everything is
worse than none.

I do the integration into the paper unless you want to write the LaTeX yourself.

## What is worth contributing

| | Where it goes |
| --- | --- |
| **A system you know well**, placed on the survey columns | [`evidence/systems/`](evidence/systems/) |
| **A migration you lived through**, especially one that ran against the fashion of its moment | [`evidence/migrations/`](evidence/migrations/) |
| **Two theories saying the same thing** without citing each other | [`evidence/convergences/`](evidence/convergences/) |
| **A case where the paper is wrong.** The most valuable kind. | [`evidence/counterexamples/`](evidence/counterexamples/) |
| **Code that computes one of the variables** from a repository | [`estimators/`](estimators/) |
| **A citation or fact that is wrong** | [Erratum issue](../../issues/new?template=erratum.yml) |
| **A section you think should be restructured or torn down** | [Proposal issue](../../issues/new?template=proposal.yml) |

Not sure which? Browse the
[**good first contribution**](../../issues?q=is%3Aissue+is%3Aopen+label%3Agood-first-contribution)
issues. They are specific, pre scoped, and finishable in an evening: a named system nobody has
surveyed, a suspected convergence nobody has documented, a citation that needs verifying against
its primary source.

## The bar, in three questions

Applied to your contribution in public, in writing, in the thread. Applied to counterexamples the
same way and no more harshly.

1. **Is it independently derived?** For a convergence, show that the two sources have no path
   between them, not just that they resemble each other.
2. **Did real systems move, and did the engineers say why?** Forces in their words, not your
   reconstruction. This is the commonest thing sent back.
3. **Could a machine check it?** Say what it needs: a bare repository, plus git history, plus
   traces, or plus a human.

Sources primary wherever they exist, archived, with the load bearing sentence quoted. Full detail
in [docs/STANDARDS.md](docs/STANDARDS.md).

## Credit

Merged work puts your name in the next arXiv version's acknowledgments and in
[CONTRIBUTORS.md](CONTRIBUTORS.md). Work that materially changes the paper gets a named credit
line describing what you did. Sustained contribution across revisions can lead to co-authorship
on future versions, decided openly and never promised in advance. Authorship on already posted
versions never changes retroactively.
[Full ladder](docs/STANDARDS.md#the-credit-ladder-in-full).

## If you are writing paper text

Only `paper/*.tex` carries the voice contract: short declarative sentences, no em or en dashes,
plain words before formal names. CI enforces the dashes. Run it yourself:

```bash
python3 .github/scripts/style_guard.py paper/conceptual-space-arxiv.tex
```

Details in [docs/STANDARDS.md](docs/STANDARDS.md#voice-contract-for-paper-text). Evidence files and
issues are exempt. Write those however you write.

---

Questions that are not contributions belong in [Discussions](../../discussions). Contributions are
licensed [CC BY 4.0](LICENSE), code [Apache 2.0](LICENSE-CODE), with no contributor license
agreement to sign. What that does and does not grant: [PATENTS.md](PATENTS.md). How decisions get
made: [GOVERNANCE.md](GOVERNANCE.md).
