---
estimates: Propagation cost, the density of the transitive closure of the dependency graph. Equivalently Lakos's average cumulative component dependency normalized by system size.
axis: Axis 10, reachability density
rung: bare-repo
inputs: A Python repository checkout. No history, no traces, no human input.
outputs: JSON with a metadata block and two estimates, plus optional per file visibility as CSV.
language: python
status: working
submitted-by: Edwin O Onyango (@Onyangoe21)
---

The paper's flagship convergence says that propagation cost and average cumulative component
dependency are the same mathematical object, reached independently from a change cost argument
and from a build cost argument. That claim is currently an argument. This estimator computes the
object, which turns one piece of it into a demonstration.

## What it computes and how

Build the directed graph whose vertices are source files and whose edges are import
relationships. Take the transitive closure. Propagation cost is the density of that closure:

```
propagation_cost = |{(i, j) : j is reachable from i}| / n^2
```

MacCormack, Rusnak and Baldwin define this as the density of the visibility matrix, where the
visibility matrix is the sum of all powers of the adjacency matrix starting at the zeroth. They
read it as the expected fraction of the system affected by a change to a randomly chosen element.
Lakos, a decade earlier, sums over components the number of components needed to compile and
test each one in isolation, and calls it cumulative component dependency. Divided by n it is the
same number. The full argument for the independence of those two derivations is in
[`evidence/convergences/propagation-cost-and-cumulative-component-dependency.md`](../../evidence/convergences/propagation-cost-and-cumulative-component-dependency.md).

The closure is computed by depth first search from every vertex, with the reachable set held as a
Python integer used as a bitset.

### Choices the sources leave open

These are where reimplementations diverge, so each one is named with its reason.

**The diagonal is set.** Every file is counted as reaching itself, because the visibility matrix
begins at the zeroth power of the adjacency matrix, which is the identity. A system of n isolated
files therefore scores 1/n rather than 0. This follows MacCormack directly. It also means the
measure has a size dependent floor, which matters when comparing systems, and is discussed under
limits below.

**Granularity is the file.** Not the function, class, package, or directory. MacCormack works at
the source file level and Lakos at the level of the C++ component, meaning a header and
implementation pair. The file is the closest available analogue in Python.

**Only intra-repository edges count.** An import of the standard library or of a third party
package is not an edge. Propagation cost asks how much of *this* system a change reaches, and a
dependency on something outside the system does not propagate within it.

**Cycles are not special cased.** Every member of a cycle reaches every other member, which falls
out of the closure without any extra rule. This is also the answer Lakos's reading gives, since a
dependency cycle must be compiled as a unit. The evidence file names cycle treatment as the most
technically plausible objection to the convergence, so it is worth stating that both readings
agree here rather than leaving it implied.

**Import roots are resolved permissively.** A file at `src/pkg/mod.py` is registered under
`src.pkg.mod`, `pkg.mod`, and `mod`, because which of those is importable depends on a build
configuration this estimator cannot see. The alternative, guessing a single root, silently drops
real edges in any repository using a `src/` layout. The cost of the permissive choice is that a
repository containing two files with the same basename in different unrelated trees can attract
an edge that a real interpreter would not resolve.

**Tests are included by default.** Test files import production code heavily and are imported by
almost nothing, which raises the node count and the edge count while lowering the closure
density. Passing `--no-tests` drops them. Neither choice is obviously right, so both are
available and the setting is recorded in the output.

## What it does not handle

**Python only.** The measure is language neutral. This implementation is not.

**Static imports only.** Anything reached through `importlib`, `__import__`, a plugin registry, a
string based entry point, or a dependency injection container is invisible. In a codebase built
around dynamic dispatch, the graph will be sparser than the real one and the estimate will read
low.

**Conditional imports count unconditionally.** An import inside a `try` block, an `if
TYPE_CHECKING` guard, or a platform branch produces an edge, even where the real system would
take only one path.

**Namespace packages and shadowing.** Resolution is name based, not interpreter based. It does not
consult `sys.path`, editable installs, or namespace package machinery. Where an in-repository
module shares a name with an installed package, the in-repository file wins, which is usually but
not always what a real import would do.

**Comparison across systems of very different size is unsound.** This is the limit most likely to
produce a wrong conclusion. The diagonal alone contributes 1/n, so small systems have an inflated
floor, and a 22 file library will score far above a 10,000 file application with genuinely worse
coupling. The measure is meaningful for comparing a system against itself over time, or against
systems of comparable size. It is not a leaderboard.

**These numbers are not comparable to the published ones.** MacCormack's figures for Mozilla and
Linux come from a C and C++ extraction over includes and calls. Reproducing them would need that
extractor, not this one. Extraction quality is known to move these results as much as algorithm
choice does.

## How to run it

No third party dependencies. Python 3.10 or newer, for `int.bit_count`.

```bash
git clone --depth 1 https://github.com/psf/requests.git /tmp/requests
python3 propagation_cost.py /tmp/requests --no-tests
```

Write the report to a file and also emit per file visibility:

```bash
python3 propagation_cost.py /tmp/requests --no-tests \
  --out requests.json --per-file requests-per-file.csv
```

`--exclude NAME` skips an additional directory and is repeatable. The defaults already skip
`.git`, `__pycache__`, `node_modules`, `build`, `dist`, and the usual virtual environment
directory names.

## Worked output

Checked in under [`example-output/`](example-output/), so the numbers can be read without
running anything. Both were measured with `--no-tests`.

`psf/requests` at commit `8068356`: propagation cost `0.5165` over 22 files and 81 edges.

`pallets/flask` at commit `d318b68`: propagation cost `0.5812` over 35 files and 138 edges.

Flask scores higher than requests despite having a lower density of direct edges, `0.1127`
against `0.1674`. That is the measure doing the thing it exists to do. Direct coupling counts
edges, and the closure counts consequences. A system can have few direct dependencies arranged so
that changes still reach everywhere, and counting edges will not tell you that.

Both numbers are high in absolute terms because both systems are small, per the size limit above.

## Validation

The 32 checks in `test_propagation_cost.py` pin the closure arithmetic against cases computed by
hand: a three chain at 6/9, a diamond at 9/16, a two cycle at 1, two isolated files at 2/4, and a
single file at 1. They also pin import resolution, which is where an implementation like this
actually goes wrong: relative imports at several depths, `from package.module import name`,
aliased imports, self imports, files that fail to parse, and imports that leave the repository.

```bash
python3 test_propagation_cost.py
```

No network access, no third party packages.

**What is not validated.** This has not been checked against an independent implementation of the
same measure, and it has not reproduced a published figure for a named system. Doing either would
be a real contribution. The most valuable version would be a second implementation over the same
extraction that agrees, since the convergence claim is about the measure rather than about any
one program that computes it.
