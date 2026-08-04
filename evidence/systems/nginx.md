---
claim: >-
  nginx occupies the compile time end of the binding axis and the event driven end of the
  concurrency axis, and its architects justify both by the same force, predictable resource use
  under high connection counts, which makes it a clean single system datum for the claim that
  binding time and concurrency model are separable coordinates rather than a single style
  package.
type: system
axis: Axis 12, binding time; boundary interaction type, synchronicity; and the variation table
sources:
  - title: nginx
    author: Alexeev, A.
    year: 2012
    venue: The Architecture of Open Source Applications, volume II
    url: https://aosabook.org/en/v2/nginx.html
    archive: https://web.archive.org/web/20240101000000/https://aosabook.org/en/v2/nginx.html
    primary: true
  - title: Eclipse
    author: Moir, K.
    year: 2011
    venue: The Architecture of Open Source Applications, volume I
    url: https://aosabook.org/en/v1/eclipse.html
    primary: true
    role: the opposing pole on the binding axis
status: integrated
submitted-by: Edwin O Onyango (@Onyangoe21)
reference-example: true
---

> **This is a reference example.** It surveys a system already used in the paper, and it is
> committed so that contributors have a real file to copy. It is not an open contribution slot.

## Position on the variation table

| Column | Value | Where the architects say so |
| --- | --- | --- |
| Process model | Master process plus a small fixed set of single threaded worker processes, typically one per core | Architecture overview, process model section |
| Concurrency model | Event driven, non blocking, one worker multiplexing many connections through a state machine | Explicitly contrasted with process per connection and thread per connection |
| Extension mechanism | Modules compiled into the binary, selected at build configuration time | Module compilation is a build step, not a runtime load |
| Topology | Pipeline of phase handlers per request, with a small set of well defined phases | Request processing phases |
| State management | Per connection state held explicitly in the worker's state machine rather than implicitly on a stack | The stated reason the event model is viable at high connection counts |
| Isolation boundary | Process boundary between master and workers, with privilege separation at that line | Master retains privileged operations, workers drop privileges |
| Binding time | Compile time for module selection; run time only for configuration values | The paper's compile time pole |
| Synchrony | Asynchronous throughout the connection handling path | Non blocking is the design premise, not an optimization |

## Why this system is worth a file

Two reasons, and the second is the one that earns it a place in the paper.

**It anchors a pole.** Compile time module binding is unfashionable, and a reader who has only
seen plugin architectures with runtime loading may take late binding for a strictly dominant
choice. nginx is a widely deployed, long lived, actively maintained counterweight, and its
maintainers chose early binding deliberately rather than inheriting it. The opposing pole is
occupied just as clearly by extension systems that install and activate bundles into a running
process. Both are competent. The forces differ.

**It separates two columns that style talk fuses.** In the informal vocabulary, event driven
and compiled tend to travel together as a single package, roughly the high performance C server
style. They are separable, and treating them as one obscures which force is doing what. There
are event driven systems with runtime plugin loading, and there are thread per connection
systems compiled as a single static binary. In nginx the two choices happen to share a
justification, predictable and bounded resource consumption per connection, but sharing a
justification is not the same as being one decision. The paper's variation table exists to make
exactly this kind of accidental bundling visible, by showing the columns taking values
independently across respected systems.

## Applying the tests

**Two way traffic.** Contributes the compile time pole on the binding axis, against the runtime
install pole from the extension system literature. Convergence of Apache and nginx toward each
other's concurrency mechanisms over time, from opposite starting points, is separate evidence on
the concurrency column and is worth its own file from someone who knows both codebases well
enough to date the changes.

**Computability.** Every row in the table above except the stated forces is estimable from a
bare repository plus build configuration. Module binding time is visible in the build system.
The process model is visible in the source. This system is a reasonable target for an early
estimator, since the ground truth is unusually unambiguous.

**Convergence.** Not applicable to a system survey.

## Gaps in this file

Honest about what is missing, so the next contributor knows where to push:

- The architects' reasoning is drawn from a secondary architecture chapter rather than from
  design discussion in the project's own development records. A contributor who can point to
  primary discussion of the module binding decision would strengthen this materially.
- The dynamic module mechanism added later is not covered here. It complicates the compile time
  characterization in an interesting way, and covering it accurately requires someone who has
  followed that work. This is a real gap and a good first contribution.
- No dates. The table describes the system as characterized in the source rather than as of a
  stated commit. A system file that pins its claims to a version or a date is more useful, and
  future files should do so.
