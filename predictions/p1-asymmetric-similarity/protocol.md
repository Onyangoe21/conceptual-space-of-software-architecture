# Prediction 1: asymmetric similarity

**Status:** stub. The design below states the shape of a test. It needs a sharper specification
of the stimulus set and the statistical treatment before anyone should collect data. Sharpening
it is a contribution.

## The prediction in plain language

Ask an architect how similar system A is to system B, and then ask how similar B is to A. If
architectural similarity behaved like distance on a map, the two answers would match. The paper
predicts they will not, and predicts the direction of the mismatch.

The reason is that distance in this space is not a comparison of shapes. It is the cost of
re deciding: how much work it would take to move a real system from where it is to where the
other one is. That cost is asymmetric by nature. Splitting one deployable into several and
merging several back into one are not the same job at the same price. Adding a dependency edge
is cheap and removing it is dear. So the prediction is that the asymmetry in human judgment will
line up with re decision cost, specifically with how many dependents a decision has accrued and
how early it was bound, rather than with any count of surface features the two systems share.

This matters beyond the psychology. Similarity judgments that violate metric axioms have been
known since Tversky's work in 1977, and they are usually treated as an embarrassment for
geometric theories of concepts. The paper's move is to make the asymmetry a prediction instead
of a problem. If the asymmetry is there and points the way re decision cost points, the metric
was right to be asymmetric.

## The formal statement, from the paper

Architects' pairwise judgments of system similarity and migration difficulty will be
systematically asymmetric, with the asymmetry oriented by re decision cost, meaning dependents
accrued and binding time, and not by surface feature counts.

## What would confirm it

- Paired similarity judgments over architecture descriptions where the mean of judgments in one
  direction differs reliably from the mean in the other, on a substantial fraction of pairs.
- The sign and size of that difference predicted by an independently computed re decision cost
  estimate, better than by a surface feature overlap measure computed on the same descriptions.
- The effect surviving with the presentation order counterbalanced, so the asymmetry is not an
  artifact of which system was named first.
- Migration difficulty judgments, asked directly, correlating with the similarity asymmetry.
  These are the same quantity under the theory, and if they come apart, the theory is wrong
  about what the metric measures.

## What would falsify it

- Symmetric judgments within noise, across a stimulus set with a wide spread of computed
  re decision costs.
- Reliable asymmetry that is *not* oriented by re decision cost, for instance asymmetry
  explained entirely by which system is better known to the respondent, or by which is more
  prototypical of a named style. Prototypicality is a live alternative explanation and the
  design has to separate it, since Tversky's own account is a prototypicality account.
- Asymmetry predicted better by surface feature counts than by re decision cost.

## Design sketch

**Respondents.** Practicing architects and senior engineers. The judgment being tested is expert
judgment, and the paper is explicit that expert categorization is part exemplar and part causal
theory. Novices are a different population and would test a different claim.

**Stimuli.** Pairs of architecture descriptions, held to a fixed length and format so that
description verbosity does not become the hidden variable. The stimulus set is the hard part of
this design and is currently unspecified. It needs pairs that vary widely in computed re
decision cost while holding surface feature overlap roughly constant, and that requires
computing both quantities over a candidate pool first.

**Task.** For each ordered pair, a similarity rating, and separately, an estimate of migration
difficulty in that direction. Order counterbalanced across respondents.

**Independent variables, computed not asked.** Dependents accrued and binding time for the
decisions that differ between the two systems, per the commitment calculus. Surface feature
overlap as the competing predictor.

## Open design questions

These are the reasons this is a stub. Any of them is worth an issue.

- How to construct architecture descriptions that are comparable without being artificial. Real
  systems carry reputation, which contaminates the judgment. Synthetic systems remove the
  expertise that makes the respondents worth asking.
- Whether to use real systems the respondent knows, which is more valid and less controlled, or
  descriptions of unfamiliar systems, which is the reverse.
- Sample size. No power analysis has been done, and the effect size is unknown.
- Whether migration difficulty and similarity should be asked of the same respondents, risking
  one anchoring the other, or of separate groups, costing sample size.
- Human subjects review. Any run involving human respondents needs whatever approval the
  runner's institution requires, and the protocol should say so before anyone starts.

## Cheaper partial versions

The full study needs respondents. Two smaller things do not:

- **Compute the predictor first.** Build the re decision cost estimate over a candidate stimulus
  pool and show that it varies enough to be worth asking about. This is an estimator
  contribution and needs no human subjects at all.
- **Mine the judgments that already exist.** Migration difficulty estimates appear in public
  engineering writing, in both directions, on axes the paper names. A corpus of those would not
  be a controlled experiment, but it would establish whether the asymmetry is even visible in
  the wild before anyone designs a study around it.

## Results

None yet. See [`results/`](results/).
