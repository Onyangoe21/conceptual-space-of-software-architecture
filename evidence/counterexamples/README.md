# Counterexamples

This directory is empty. That is not a good sign, and it is the most honest thing on the
repository's front page.

A theory whose counterexample folder stays empty is either very good or not being read
adversarially. Early on, the second explanation is much more likely than the first. So this
directory is the one the maintainer most wants filled, and a counterexample that survives review
and forces a revision is a rung two contribution under
[the credit ladder](../../docs/STANDARDS.md#the-credit-ladder-in-full).

## What a counterexample targets

The paper makes several claims that a single well documented case can damage. In rough order of
how much damage a successful case would do:

1. **A coordinate that is really a potential, or the reverse.** The sharpest version: an
   intentional, force justified migration *toward* a larger cyclic core of mutually dependent
   files. The paper classifies dependency graph health as a one way potential, something systems
   slide into and must spend effort to climb out of, on the grounds that nobody chooses it. One
   documented case of a competent team choosing it, for reasons they articulated, would move it
   into the coordinates and change how the dynamics section has to be written.
2. **A generator the basis cannot express.** The paper claims a fixed superset of generators
   with a time varying attention weighting: framing changes which dimensions are salient but
   does not manufacture new ones. A recurring decision dimension that architects actually use,
   and that genuinely resists expression in the basis, would falsify the fixed superset claim.
   Note the word recurring. One idiosyncratic decision is not a generator.
3. **A failed prediction.** Each of the six has a protocol in
   [`predictions/`](../../predictions/) stating what would falsify it. Data collected under one
   of those protocols, coming out the wrong way, is the cleanest counterexample the project can
   receive, because the falsification condition was written down before the data existed.
4. **A congruence claim that does not hold.** Prediction 2 says the congruence terms will beat
   single graph metrics at predicting maintenance outcomes. A matched sample where propagation
   cost alone beats them would count.
5. **Graphs that will not separate.** The paper's central empirical finding is that the logical
   cut and the physical cut are independent choices. A domain where they are genuinely not
   independent, for a stated structural reason rather than by habit, would cut deep.

## The bar

Exactly the same as for supporting evidence. Not higher, which would make the theory
unfalsifiable in practice while advertising falsifiability in principle. Not lower, which would
let a single anecdote overturn accumulated convergence.

That means primary sources, archived links, load bearing passages quoted, and forces in the
engineers' own words. A counterexample that rests on an analyst's reconstruction of why a team
did something is the same weak evidence as supporting evidence resting on the same thing.

Read [the bar](../../docs/STANDARDS.md#the-bar) and
[the file format](../../docs/STANDARDS.md#evidence-file-format) before you write. Use
[the counterexample issue template](../../../../issues/new?template=counterexample.yml).

## How it will be handled

The maintainer will write the three tests out against your evidence in the thread, in public,
and will say what would change the verdict. This procedure exists specifically for
counterexamples, because the maintainer has an obvious interest in the theory surviving and that
interest needs a check. See [GOVERNANCE.md](../../GOVERNANCE.md#resolving-disputes-about-whether-evidence-meets-the-bar).

If a counterexample is rejected, the file may still be committed here with `status: rejected`
and the reasoning attached, and the contributor is still credited. The ladder rewards work that
was done, not conclusions that happened to be right.

## The strongest form

The most useful counterexample does two things at once: it shows the failure, and it says what
the theory would have to change to accommodate it. A case that forces a claim to be narrowed is
worth more than a case that only says no, because a narrowed claim is still a claim and the
paper can carry it forward.
