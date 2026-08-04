# What this contributes

<!-- One or two sentences. If this closes an issue, write "Closes #123". -->

## Contribution type

<!-- Check exactly one. One contribution per pull request, so that each can be accepted or
     rejected on its own evidence. -->

- [ ] **Erratum**, a factual or citation error in the paper
- [ ] **Convergence**, two or more bodies of work that independently derive the same variable
- [ ] **Migration or system evidence**, extending the empirical base
- [ ] **Counterexample**, a documented case that cuts against an axis, a congruence claim, or a
      prediction
- [ ] **Estimator**, code that computes a basis variable
- [ ] **Prediction protocol or results**
- [ ] **Repository infrastructure or documentation**, not a claim about the paper

## Evidence schema

<!-- Skip this section for infrastructure and documentation changes. -->

- [ ] The file has front matter with `claim`, `type`, `axis`, `sources`, `status`, and
      `submitted-by`
- [ ] `claim` is one sentence that someone could disagree with, not a topic label
- [ ] `status` is `proposed`. The maintainer moves it from there.
- [ ] `type` matches the directory the file is in
- [ ] The file name is lowercase, hyphenated, descriptive, and unnumbered

## Sources

- [ ] Sources are primary wherever they exist: the engineers' own account, the post mortem, the
      paper, the thread, the commit. Not a blog summarizing one of those.
- [ ] Every web link has an archive link alongside it, with a capture date
- [ ] The load bearing passages are quoted, not just cited
- [ ] Where a source sits behind an access restriction, that is stated, and anything
      reconstructed from secondary quotation is marked as such

## The three tests

<!-- Answer for substantive contributions. "Not applicable" is a legitimate answer for some
     contribution types. Answering these yourself is not a formality: it is usually where you
     find out that your convergence has a shared ancestor, or that your migration's forces are
     your reconstruction rather than the engineers' words. -->

**Convergence, independent derivation.** What did you check to establish that the derivations are
independent, rather than one inheriting from the other?

**Two way traffic, real systems under articulated forces.** Where are the forces stated, and by
whom? Is there documented movement in the other direction?

**Computability, can a machine check it.** What does this need on the evidence ladder: bare
repository, plus git history, plus runtime traces, or plus human intent?

## Paper text

<!-- Only if this pull request changes paper/*.tex. Delete this section otherwise. -->

- [ ] No em dashes and no en dashes in prose, outside the bibliography block and comments
- [ ] Short declarative sentences, and no sentence flagged by the style guard that I have not
      deliberately kept
- [ ] Every technical concept introduced in plain words before its formal name
- [ ] Section openings orient the reader before they argue
- [ ] I ran `python3 .github/scripts/style_guard.py paper/conceptual-space-arxiv.tex` locally and
      it passed
- [ ] Any new `\cite` key has a matching `\bibitem`

<!-- If you would rather not write LaTeX, do not. Submit the evidence file and say so below. The
     maintainer writes the paper text, and this is the default path, not a lesser contribution. -->

- [ ] I would like the maintainer to write the paper text for this
- [ ] I have drafted the paper text myself and accept editing for register

## Estimator

<!-- Only if this pull request adds code. Delete this section otherwise. -->

- [ ] `README.md` with the front matter block: `estimates`, `axis`, `rung`, `inputs`, `outputs`,
      `language`, `status`, `submitted-by`
- [ ] Runnable, with pinned dependencies
- [ ] At least one test that runs without network access
- [ ] Output is JSON or CSV and includes the metadata block: repository, commit hash, estimator
      version, timestamp, parameters
- [ ] A worked output on a public repository is checked in
- [ ] Licensed MIT, matching `LICENSE-CODE`

## Credit

**Name as it should appear:**

<!-- Exactly as you want it in the acknowledgments of the next arXiv version and in
     CONTRIBUTORS.md, including any diacritics. Write "no credit" if you would rather not be
     named. This is the name that gets used, so write it the way you want to read it. -->

**Handle, or affiliation you want listed:**

<!-- Optional. -->

- [ ] I understand that merged contributions are credited at rung one automatically, that rung
      two named credit lines are proposed by the maintainer in this thread and can be corrected
      before merge, and that authorship on already posted arXiv versions never changes
      retroactively
- [ ] I license this contribution under CC BY 4.0 for prose and evidence, and MIT for code

## Anything the reviewer should know

<!-- Where you are unsure. What you could not verify. Which part of this you expect to be
     argued with. Naming your own weakest joint is a strength, not a concession. -->
