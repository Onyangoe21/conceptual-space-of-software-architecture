---
claim: >-
  Propagation cost and average cumulative component dependency are the same mathematical object,
  the density of the transitive closure of the dependency graph, derived independently from a
  change cost argument and from a build cost argument by authors who did not cite each other.
type: convergence
axis: Axis 10, reachability density
sources:
  - title: >-
      Exploring the Structure of Complex Software Designs: An Empirical Study of Open Source and
      Proprietary Code
    author: MacCormack, A., Rusnak, J., Baldwin, C.Y.
    year: 2006
    venue: Management Science 52(7):1015-1030
    url: https://doi.org/10.1287/mnsc.1060.0552
    primary: true
  - title: Large-Scale C++ Software Design
    author: Lakos, J.
    year: 1996
    venue: Addison-Wesley
    primary: true
  - title: "Decoupling Level: A New Metric for Architectural Maintenance Complexity"
    author: Mo, R., Cai, Y., Kazman, R., Xiao, L., Feng, Q.
    year: 2016
    venue: Proceedings of ICSE 2016
    url: https://doi.org/10.1145/2884781.2884825
    primary: true
status: integrated
submitted-by: Edwin O Onyango (@Onyangoe21)
reference-example: true
---

> **This is a reference example.** It documents a convergence already argued in the paper, and
> it is committed so that contributors have a real file to copy rather than a template to
> interpret. It is not an open contribution slot.

## The two derivations

MacCormack, Rusnak and Baldwin define propagation cost as the density of the transitive closure
of the dependency matrix: the expected fraction of the system affected by a change to a randomly
chosen element. The motivating question is change cost. If I touch one file, how much of this
system do I now have to think about?

Lakos, a decade earlier, defines cumulative component dependency as the sum over components of
the number of components needed to compile and test that component in isolation. Averaged and
normalized by system size, ACD/N is the same quantity. The motivating question is build cost. If
I change one component, how long is the incremental build, and how much must be relinked?

Same matrix, same transitive closure, same normalization by system size. Two entirely different
costs, arrived at from two entirely different professional concerns.

## Independence

The claim is not that the two formulas resemble each other. Resemblance is cheap. The claim is
that there is no path between the derivations, and that is what makes the agreement evidence.

- **No mutual citation.** Neither work cites the other. Lakos predates the 2006 paper by a
  decade, and the 2006 paper's related work is drawn from the design structure matrix and
  modularity literatures.
- **No shared ancestor carrying the measure.** The DSM tradition, from Steward through Baldwin
  and Clark, supplies the dependency matrix but not transitive closure density as a design
  measure. Lakos derives the closure from C++ link semantics, specifically what must be present
  for a translation unit to build, with no reference to any partitioning or modularity theory.
- **Different literatures and audiences.** Lakos is a practitioner's book on C++ physical
  design, published by a trade press, addressed to engineers whose builds had become
  intolerable. MacCormack, Rusnak and Baldwin publish in a management science venue, motivated
  by the economics of modularity and the comparison of open source against proprietary design
  structure.
- **Disjoint vocabulary.** One says propagation, visibility, and change. The other says
  levelization, physical dependency, insulation, and compile time. Neither uses the other's
  words for the object they share.

## What it does for the paper

This is the paper's flagship convergence, and it is doing specific work rather than decorating
the argument.

It is the reason reachability density enters the basis as a first class variable rather than as
one metric among the hundreds catalogued in the software measurement literature. A quantity that
two unconnected traditions were both forced to invent, approaching from opposite ends of the
software lifecycle, is more plausibly a feature of the territory than of either map. That is the
convergence test in its cleanest instance, and the paper uses it as the worked demonstration of
what the test is asking for.

It also carries a geometric consequence that shapes the rest of the construction. Lakos's
formulation makes the nonlocality of edge cost visible in a way the density formulation hides. A
single added edge can double the transitive closure, because it can merge two previously
independent regions of the graph. Edge cost is therefore not additive and not local, and the
space is not Euclidean in the edge basis. The paper's refusal of a Euclidean metric starts here,
before the argument from Tversky ever arrives.

Finally, the refinement matters. Decoupling level discounts dependence that is legitimate,
meaning dependence on design rules that are supposed to be depended upon, and it can rank
systems in the opposite order to raw propagation cost. The two are different projections of the
same underlying order structure, and the basis needs both. A convergence establishing that a
dimension is real does not establish that one projection of it is sufficient.

## Standing caveat

The decoupling level validations to date come largely from one research group. The paper flags
this as a replication gap rather than smoothing over it. The convergence between MacCormack and
Lakos is unaffected by that gap, since it concerns the base quantity rather than the refinement,
but a contributor looking for high value work could do worse than an independent replication of
the decoupling level results on a fresh corpus.

## What would undercut this

Any of the following would turn this from a convergence into an inheritance, and the paper would
have to say so:

- A citation path between the two literatures before 2006, in either direction.
- An earlier common source that already states transitive closure density as a design measure,
  which both traditions could have absorbed without attribution.
- Evidence that Lakos's ACD and the 2006 propagation cost are not in fact the same object under
  normalization, for instance because of a difference in how each treats cycles or transitively
  redundant edges. This is the most technically plausible objection and the paper would welcome
  someone checking it carefully against both primary texts.
