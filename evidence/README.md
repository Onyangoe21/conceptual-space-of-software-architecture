# Evidence

This directory is the paper's empirical base, opened up.

The paper's method is cumulative convergent evidence. It does not argue that its variables are
real by defining them carefully. It argues that they are real because independent lines of work
keep arriving at them, because real systems move along them in both directions under forces
their engineers wrote down, and because a machine can compute most of them. That kind of
argument has an unusual property: it gets stronger one data point at a time, and each data point
is small enough for one person to contribute in an evening.

That is what lives here. Four kinds of data point, one file each.

| Directory | What goes in it | Which test it feeds |
| --- | --- | --- |
| [`convergences/`](convergences/) | Two or more bodies of work that independently derive the same variable | The convergence test |
| [`migrations/`](migrations/) | A documented migration along a named axis, with the forces stated | The two way traffic test |
| [`systems/`](systems/) | One surveyed system placed on the variation table | The two way traffic test, and prototype structure |
| [`counterexamples/`](counterexamples/) | A documented case that cuts against an axis, a congruence claim, or a prediction | All three, applied in reverse |

Evidence files are exempt from the paper's voice contract. Write them the way you write. Only
`paper/*.tex` carries the register requirements, and the maintainer does that translation.

## The file format

YAML front matter, then free prose. The schema is small on purpose: if the front matter takes
you more than ten minutes to fill in, something is wrong with the schema and you should open an
issue about it.

```yaml
---
claim: One sentence. What this file establishes, stated so it could be true or false.
type: convergence | migration | system | counterexample
axis: Which axis, congruence term, or prediction this touches.
sources:
  - title: Title of the source
    author: Who wrote it
    year: 2019
    url: https://example.org/primary-source
    archive: https://web.archive.org/web/20240101000000/https://example.org/primary-source
    primary: true
status: proposed
submitted-by: Your Name (@your-handle)
---
```

Full field reference, including what makes a good `claim` and who sets `status`, is in
[docs/STANDARDS.md](../docs/STANDARDS.md#evidence-file-format). The bar every file is
judged against is in [the same document](../docs/STANDARDS.md#the-bar).

**File naming.** Lowercase, hyphens, descriptive, unnumbered.
`propagation-cost-and-cumulative-component-dependency.md`.

**Status lifecycle.** You file as `proposed`. The maintainer moves it to `accepted` when it
clears the bar, `integrated` when the corresponding change lands in the paper text, or
`rejected` with written reasoning in the thread. Rejected files may stay in the repository when
they are instructive, because a well documented near miss saves the next contributor a wasted
evening.

## What the prose should do

Four things, in whatever order suits the material.

1. **State the evidence.** What the sources say, with the load bearing passages quoted rather
   than summarized.
2. **Apply the three tests to it yourself.** Independence for a convergence. Articulated forces
   and traffic direction for a migration. Evidence ladder position for anything touching
   computability. Doing this yourself is not a formality. It is usually where you discover that
   your convergence has a shared ancestor, or that your migration's stated forces are your
   reconstruction rather than the engineers' words.
3. **Say what it changes.** Which sentence in the paper is now differently supported. Being
   wrong about this is fine. Not attempting it leaves the maintainer guessing at your argument.
4. **Say what would undercut it.** The strongest evidence files name their own weakest joint.

## A worked example, in full

Below is a complete convergence file, reproducing an argument the paper already makes. It is
committed at
[`convergences/propagation-cost-and-cumulative-component-dependency.md`](convergences/propagation-cost-and-cumulative-component-dependency.md)
and marked `status: integrated`, since it is already in the paper. Copy it and edit.

Two more committed reference examples show the other shapes:
[`migrations/istio-control-plane-consolidation.md`](migrations/istio-control-plane-consolidation.md)
for a migration, and [`systems/nginx.md`](systems/nginx.md) for a system survey. All three are
marked as reference examples in their front matter so nobody mistakes them for open
contributions.

````markdown
---
claim: >-
  Propagation cost and average cumulative component dependency are the same mathematical
  object, the density of the transitive closure of the dependency graph, derived independently
  from a change cost argument and from a build cost argument by authors who did not cite each
  other.
type: convergence
axis: Axis 10, reachability density
sources:
  - title: >-
      Exploring the Structure of Complex Software Designs: An Empirical Study of Open Source
      and Proprietary Code
    author: MacCormack, A., Rusnak, J., Baldwin, C.Y.
    year: 2006
    venue: Management Science 52(7):1015-1030
    primary: true
  - title: Large-Scale C++ Software Design
    author: Lakos, J.
    year: 1996
    venue: Addison-Wesley
    primary: true
status: integrated
submitted-by: Edwin O Onyango (@Onyangoe21)
---

## The two derivations

MacCormack, Rusnak and Baldwin define propagation cost as the density of the transitive closure
of the dependency matrix: the expected fraction of the system affected by a change to a randomly
chosen element. The motivating question is change cost. If I touch one file, how much of this
system must I now think about?

Lakos, a decade earlier, defines average cumulative component dependency as the mean over
components of the number of components that must be compiled and linked to test that component
in isolation. Normalized by system size, ACD/N is the same quantity. The motivating question is
build cost. If I change one component, how long is the incremental build?

Same matrix, same closure, same normalization. Two different costs.

## Independence

The claim is not that the formulas resemble each other. It is that there is no path between the
derivations.

- Lakos is a practitioner's book on C++ physical design, published by a trade press, aimed at
  build engineers. It does not cite the modularity or design structure matrix literature.
- MacCormack, Rusnak and Baldwin work in the design structure matrix and modularity tradition,
  descending from Steward and from Baldwin and Clark's options theory. Their motivating
  literature is organizational and economic.
- Neither cites the other. They share no common ancestor that already contains the measure: the
  DSM tradition supplies the matrix but not the transitive closure density, and Lakos derives
  the closure from link semantics rather than from any partitioning theory.
- The vocabularies do not overlap. One says propagation, visibility, and change. The other says
  levelization, physical dependency, and compile time.

## Why it matters to the paper

This is the paper's flagship convergence, and it does specific work. It is the reason
reachability density enters the basis as a first class variable rather than as one metric among
the hundreds in the measurement literature. A quantity that two unconnected traditions were both
forced to invent, from opposite ends of the software lifecycle, is more plausibly a property of
the territory than of either map.

It also carries the geometric caveat that shapes the space. Lakos's derivation makes the
nonlocality visible in a way the density formulation hides: a single added edge can double the
transitive closure. Edge cost is therefore nonlocal, and the space is not Euclidean in the edge
basis.

## What would undercut this

Evidence of a citation path between the two literatures before 2006, or an earlier common source
that already states transitive closure density as a design measure. If either turns up, this
stops being a convergence and becomes an inheritance, and the paper should say so.
````

## Before you file

- Sources primary, links archived, load bearing passages quoted.
- `claim` is a sentence someone could disagree with, not a topic label.
- The three tests applied in the prose, including the one your evidence handles worst.
- One contribution per file, one file per pull request.

Then open the matching issue template, or go straight to a pull request if you have the file
ready.
