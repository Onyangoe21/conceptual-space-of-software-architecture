# Prediction 2: the congruence terms dominate

**Status:** stub. The measurement is well defined and the corpus is not. Naming and assembling a
corpus is the contribution this protocol most needs.

## The prediction in plain language

Most structural metrics look at one graph. They measure the code's dependency structure, and
nothing else, and then try to predict how painful the system will be to maintain.

The paper's claim is that the more powerful predictors are not properties of any one graph. They
are properties of *pairs* of graphs, specifically whether the boundaries drawn on one graph line
up with the boundaries drawn on another. Two of these matter most. Whether the way the code is
divided matches the way the teams are divided, which is Conway alignment. And whether the way
the code is divided matches the way it is deployed, which is the logical to physical congruence
that three of the paper's five migration post mortems name as their root error.

The prediction is that these alignment terms will beat any single graph metric, including
propagation cost, at predicting maintenance outcomes.

There is already strong evidence for the first half of this. Organizational metrics predicted
failure prone binaries in a large commercial system better than any code metric did. The
prediction extends that result in two directions: from defects to delivery velocity, and from
the organization to code congruence alone to the logical to physical congruence as well.

## The formal statement, from the paper

In matched samples, the organization to code congruence and the logical to physical congruence
will predict maintenance outcomes better than any single graph structural metric, including
propagation cost, extending the existing organizational structure result from defects to
velocity.

## What would confirm it

- On a corpus of systems with comparable outcome data, a model using congruence terms
  outperforming a model using the best single graph metric, on held out data, by a margin that
  survives the usual corrections for the congruence model having more inputs.
- The result holding for at least two distinct outcome measures, one defect flavored and one
  velocity flavored. The extension from defects to velocity is the new part of the claim and
  needs to be tested as such rather than assumed.
- The result holding when the congruence terms are computed at more than one granularity, since
  a congruence statistic that only works at one arbitrary scale is a measurement artifact.

## What would falsify it

- Propagation cost, or any other single graph metric, matching or beating the congruence terms
  on held out data across the corpus.
- The congruence terms predicting defects but carrying no signal for velocity, which would
  confine the existing result rather than extend it and would require the paper to narrow the
  prediction.
- The congruence terms working only where team boundaries were drawn from module boundaries by
  construction, which would make the correlation a definition rather than a finding. This is the
  most likely quiet failure mode and the design has to control for it.

## Measurement

**Organization to code congruence.** Git authorship crossed with dependency structure. For each
module boundary, how concentrated is ownership, and how much of the cross boundary dependency
traffic corresponds to cross team communication. Ownership concentration at a boundary is the
form with the most existing validation behind it.

**Logical to physical congruence.** Module structure crossed with build and deploy manifests.
Do the units that are deployed together correspond to the units that are modularized together,
and where they diverge, in which direction.

**Single graph comparators.** Propagation cost, decoupling level, and a standard coupling or
cohesion metric, all computed on the same extraction. Extraction quality changes results as much
as algorithm choice, so all metrics in the comparison must come from one extraction pipeline or
the comparison is meaningless.

**Outcomes.** Defect density per module, change lead time, and change failure rate, where the
corpus supports them. Population scale work on delivery performance gives the velocity side its
operational definitions.

## The corpus problem

This is why the protocol is a stub. The measurement is specified well enough to implement. The
corpus is not, and it is genuinely hard, because the prediction needs three things together:

1. Dependency structure, which needs the code.
2. Team structure, which needs authorship history and ideally something about actual
   communication.
3. Maintenance outcomes, which need issue tracking or deployment records.

Open source supplies the first two abundantly and the third unevenly. Commercial systems supply
all three and cannot usually be published. Note that the mirroring between organization and code
is known to weaken in open source, which is a substantive complication rather than an
inconvenience: an open source corpus may test the prediction on the population where the effect
is weakest.

Contributions that would move this forward, in order of value:

- A named, assemblable corpus with all three data types, with the licensing worked out.
- An estimator for either congruence term that runs on a public repository, which is a
  standalone contribution under [`estimators/`](../../estimators/) whether or not this study
  ever runs.
- A pilot on five systems establishing that the outcome data is comparable enough across
  projects to pool. If it is not, this prediction needs a within project design instead, and
  finding that out early is worth a lot.

## Results

None yet. See [`results/`](results/).
