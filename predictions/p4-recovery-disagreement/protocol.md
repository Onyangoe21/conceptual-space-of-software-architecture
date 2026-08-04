# Prediction 4: recovery disagreement is lawful

**Status:** stub, but the first half is fully computable today and needs no human subjects. The
second half needs maintainers to answer a survey.

## The prediction in plain language

Architecture recovery algorithms try to infer a system's module structure from its code. Several
exist, and each optimizes a different idea of what a module is. One looks for dense dependency
clusters. One looks for recurring structural idioms. One looks for coherent concerns in the
identifiers and comments. One looks for information theoretic equivalence.

Measured against decompositions that the systems' own engineers certified as correct, all of
them score poorly, and they disagree with each other roughly as much as they disagree with the
truth. On the usual view, that architecture is one partition waiting to be found, this is an
embarrassment for the field.

On this paper's view it is a measurement. The algorithms disagree because each is capturing a
different real dimension, and any single partition is a lossy projection of a multi dimensional
state. If that is right, the disagreement is not noise. It is a fingerprint, reproducible for a
given system, and it should carry information about where that system sits in the space.

The prediction adds a testable consequence. Because the disagreement profile and the
conformance rules a team will accept are both functions of the same underlying position, the
profile should predict the rules. A system whose structure is dominated by dependency density
should have maintainers who accept dependency shaped rules, and a system whose structure is
dominated by concern coherence should have maintainers who accept concern shaped ones.

## The formal statement, from the paper

The disagreement profile among recovery objectives, meaning density, idiom, concern, and
information, on a given system is reproducible and predicts which conformance rules its
maintainers will accept, because both are functions of the same latent position.

## What would confirm it

**Part one, reproducibility.** The disagreement profile for a system is stable across
reasonable perturbations: different but valid dependency extractions, minor version changes,
and algorithm parameter settings within their normal ranges. Stable means the pattern of which
objectives agree with which stays put, not that the numbers are identical.

**Part two, informativeness.** The profile varies meaningfully across systems and clusters in a
way that corresponds to other basis coordinates computed independently. If every system has the
same profile, the profile carries no information, and part one can pass while part two fails.

**Part three, prediction.** Maintainers of systems whose profile leans one way accept
conformance rules of the corresponding shape at a higher rate than maintainers of systems whose
profile leans another way.

## What would falsify it

- The profile moving substantially under extraction changes that a reasonable analyst would
  consider equivalent. This is the most likely failure, since extraction quality is known to
  change recovery results as much as algorithm choice does, and it may well swamp the signal.
  Finding that out is worth doing regardless.
- The profile being effectively constant across systems, making the disagreement generic rather
  than a fingerprint.
- No relationship between profile and accepted conformance rules, which would leave the
  disagreement real but uninformative about anything a maintainer cares about.

## Design

**Part one and two are pure computation.** Take a corpus of systems. Run four recovery
objectives, one per family: dependency density, structural idiom, concern coherence, and
information theoretic. Compute pairwise agreement between the resulting partitions using a
standard partition comparison measure, giving each system a profile vector. Then:

- Perturb the extraction and recompute, to test stability. Vary the dependency extractor, the
  handling of generated code, and the treatment of test code.
- Compare profiles across systems, and correlate the profile with independently computed basis
  coordinates: core size, propagation cost, ownership concentration, and the dominant
  decomposition choice.

All of this runs on public repositories with no human involvement. It is a good target for an
estimator contribution, and the profile computation would be a reusable component.

**Part three needs maintainers.** Present each system's maintainers with candidate conformance
rules of each shape, phrased concretely for their system, and ask which they would enforce.
Concretely phrased matters. A generic question about whether modularity is good produces
agreement from everyone and measures nothing. A specific proposed rule for their actual codebase
produces a real answer.

## Open design questions

- Which four algorithms, specifically, and which implementations. Availability and
  maintainedness of the implementations may decide this, and the choice should be recorded
  rather than treated as obvious.
- Which partition comparison measure. Different measures weight cluster size differently, and
  the choice could produce the result on its own. Reporting more than one is the safe path.
- Corpus size and selection. Selecting systems that are easy to extract biases toward one kind
  of system, and that bias runs in the same direction as the prediction.
- How to reach maintainers, and how to phrase rules without leading the answer.

## Cheapest useful contribution

Run part one on ten systems and publish the profiles. That alone establishes whether there is
anything here, requires no coordination with anyone, and would immediately tell the paper
whether this prediction is worth the rest of the design.

## Results

None yet. See [`results/`](results/).
