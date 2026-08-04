---
claim: >-
  The consolidation of four separately deployed Istio control plane components into a single
  binary is documented traffic toward the coarse end of the granularity axis, justified by
  measured operational cost rather than by a change in what the system does, and it therefore
  supplies the return direction that makes granularity a coordinate rather than a one way slope.
type: migration
axis: Axis 2, granularity, on the runtime graph; and the logical to physical congruence term
direction: fine to coarse
sources:
  - title: "Introducing istiod: Simplifying the Control Plane"
    author: The Istio project
    year: 2020
    url: https://istio.io/latest/blog/2020/istiod/
    archive: https://web.archive.org/web/20240210000000/https://istio.io/latest/blog/2020/istiod/
    primary: true
  - title: "Site Isolation: Process Separation for Web Sites within the Browser"
    author: Reis, C., Moshchuk, A., Oskov, N.
    year: 2019
    venue: Proceedings of USENIX Security 2019
    url: https://www.usenix.org/conference/usenixsecurity19/presentation/reis
    primary: true
    role: the opposing direction on the same axis
status: integrated
submitted-by: Edwin O Onyango (@Onyangoe21)
reference-example: true
---

> **This is a reference example.** It documents a migration already used in the paper, and it is
> committed so that contributors have a real file to copy. It is not an open contribution slot.

## What moved

The control plane had been decomposed into separately deployed components, each with its own
lifecycle, configuration, and upgrade path. The consolidation collapsed them into a single
deployable binary. Nothing about the control plane's responsibilities changed. What changed was
the number of independently deployable units the operator had to reason about.

In the paper's terms, this is a move along granularity on the runtime graph, from fine to
coarse, with the logical decomposition left substantially intact. That combination is exactly
the separation the paper's central empirical finding is about. The logical cut and the physical
cut are independent choices, and this migration exercises one without exercising the other.

## The forces, in the engineers' own framing

The stated reasons are operational rather than architectural in the diagram sense. Separately
deployed components multiplied the operator's burden: more things to configure, more things to
upgrade in a compatible order, more failure modes arising from version skew between components
that were always deployed together anyway. Installation and troubleshooting complexity are named
directly. The benefit that fine deployment granularity is supposed to buy, independent scaling
and independent release of the pieces, was not being realized, because in practice the
components were deployed and upgraded as a unit.

That last observation is the load bearing one for the two way traffic test. The migration is not
a repudiation of fine granularity. It is a report that on this system, under these forces, the
option value of independent deployment was not being exercised, and the operational cost of
maintaining the option was. A different system with different forces would rationally choose
differently, which is precisely what makes this an axis rather than a slope.

## Why this file exists rather than a general note about consolidation

The two way traffic test requires traffic in both directions, from competent teams, with forces
articulated on both sides. This file supplies the coarse direction. The fine direction on the
same axis is supplied by browser isolation work, where the isolation boundary was moved finer,
first to a process per site instance and later to strict site isolation, because the threat
model changed when speculative execution attacks made same process isolation of untrusted
content untenable.

Set those two side by side and the structure is clean. Two competent teams, on the same axis,
moving in opposite directions, each naming forces the other did not face. One faced an operator
cost that the option was not paying for. The other faced an attacker who could read across an
in process boundary. Neither was wrong, and no amount of catalog work would have told you which
pole to prefer without knowing the forces.

## Applying the tests

**Two way traffic.** Passes, in combination with the browser isolation evidence. Documented
movement in both directions, forces stated by the engineers rather than reconstructed by an
analyst.

**Computability.** The granularity coordinate on the runtime graph is estimable from deployment
manifests, and the change is visible in the repository history as a change in the number of
deployable units. This migration is machine checkable after the fact, which is the property the
computability test asks for.

**Convergence.** Not applicable. This is empirical evidence rather than a theoretical
derivation.

## What would undercut this

- Evidence that the consolidation was reversed later under similar forces, which would suggest
  the move was a correction of an error rather than a defensible position on an axis. A reversal
  under *different* forces would strengthen rather than weaken the two way traffic reading.
- Evidence that the logical decomposition was in fact collapsed along with the physical one,
  which would make this a move on both cuts simultaneously and therefore useless as evidence
  that the two vary independently. The published account indicates otherwise, and a contributor
  with primary knowledge of the codebase at the time could tighten this considerably.
