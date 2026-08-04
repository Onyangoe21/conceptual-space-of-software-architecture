# Estimators

The computability program: working code that computes a basis variable from a repository, its
history, or its traces.

## Why this directory exists

The paper's third test is whether a machine can check a variable. A latent variable that is well
defined but unestimable in principle can still constrain theory, but it cannot enter the working
basis, because the working basis is meant to be what an agent estimates on opening a repository.
So the paper tags every variable with what it needs, and it claims that roughly nine of the
seventeen basis entries are estimable from a bare repository, four more fall out of git history,
and only the intent carriers need a person.

That claim is currently an argument. Every estimator that runs turns a piece of it into a
demonstration, which is a considerably stronger thing to have. An estimator is also the only
contribution type here that produces something immediately useful outside the paper, since the
same code that validates a computability claim is the code an agent would need to actually hold
an architecture.

Estimators are licensed [MIT](../LICENSE-CODE), separately from the paper text.

## The evidence ladder

Every estimator declares its rung. This is the paper's own classification and it is what the
estimator is testing.

| Rung | Input | Examples of what it can reach |
| --- | --- | --- |
| **Bare repository** | Source, build files, no history | Code cut and its alternatives under several recovery objectives, reachability density, decoupling level, core size, element roles, cycles, levelization, dependency orientation, boundary interaction types from interface signatures, binding times, declared visibility, concern vectors from identifiers and comments, dominant decomposition choice |
| **Plus git history** | The above, plus commits | Churn and hotspots, logical coupling, modularity violations, interface instability, ownership and organization to code congruence, drift dating |
| **Plus runtime traces** | The above, plus execution data | The realized interaction graph as against the potential one, hot paths, dynamic feature location |
| **Plus human intent** | The above, plus a bounded human input | The intended module map, the allowed dependency relation, fitness priorities, rationale for tolerated divergences |

The fourth rung is not a defeat. The reflexion model protocol is the proven pattern: the machine
drafts, the human corrects, the machine enforces from then on. One engineer reflexion modeled a
1.2 million line codebase in about a month that way. An estimator that produces a good draft map
for a human to correct is squarely in scope and is arguably the most valuable kind, because it
is where the human cost actually sits.

## What is most wanted

Roughly in order of value to the paper.

1. **Modularity violations**, meaning units that change together in history without a structural
   dependency between them. The paper calls this the highest value single derived signal, and it
   needs both the code graph and the history, which makes it a real integration rather than a
   metric wrapper.
2. **Organization to code congruence.** Git authorship crossed with dependency structure. This
   feeds Prediction 2 directly and there is no good open implementation.
3. **The recovery disagreement profile.** Four recovery objectives run over one extraction, with
   pairwise partition agreement. This is Prediction 4's part one, computable today, and it is
   the single contribution that would most cheaply tell the project whether that prediction is
   worth pursuing.
4. **Reachability density and decoupling level**, on one extraction so the two projections are
   comparable. Existing implementations are scattered and hard to compare.
5. **Logical to physical congruence.** Module structure crossed with build and deploy manifests.
6. **A decision graph extractor** over issues and pull requests, feeding Prediction 6 and
   Prediction 5's basis arm.
7. **Element roles and core classification** on the visibility fan in and fan out plane.

An estimator does not have to be novel research. A careful, documented, runnable implementation
of a measure that already exists in a paper is exactly what is wanted, because the papers
usually do not ship code and the measures usually do not survive reimplementation unchanged.

## What a submission needs

One directory per estimator, named for what it computes:
`estimators/modularity-violations/`, `estimators/propagation-cost/`.

Language is your choice. Do not add a shared framework or a plugin system to this directory;
independent tools that run are worth more than an architecture for tools that might.

Required in every estimator directory:

**1. A `README.md` with a front matter block:**

```yaml
---
estimates: Which basis variable or variables this computes.
axis: The axis name or number from the paper.
rung: bare-repo | plus-history | plus-traces | plus-human
inputs: What it needs, concretely.
outputs: What it produces, and in what format.
language: python
status: working | prototype
submitted-by: Your Name (@your-handle)
---
```

Then prose covering:

- **What it computes and how**, with the definition it implements and the source of that
  definition. Where you had to make a choice the source leaves open, say which choice and why.
  These choices are where reimplementations diverge, and documenting them is most of the value.
- **What it does not handle.** Languages, build systems, repository shapes, and scales where it
  will be wrong or will not run.
- **How to run it**, with a real command line and a real repository as the example.
- **A worked output** on a public repository, checked in, so a reader can see what the numbers
  look like without running anything.
- **Validation**, at whatever level you managed. Agreement with published numbers for a known
  system is the strongest. Agreement with a hand computation on a small case is fine. No
  validation at all is acceptable if you say so plainly and mark `status: prototype`.

**2. Runnable code**, with pinned dependencies. A `requirements.txt` with versions, a lockfile,
or a container definition. An estimator that ran once on your machine in 2026 is not a
demonstration of computability.

**3. At least one test**, even a small one, that runs without network access.

**4. Output as machine readable data**, JSON or CSV, not only a printed table. Estimators should
compose, since the interesting variables are the ones that cross graphs, and those need two
estimators' outputs side by side.

## The output contract

Loose on purpose, because the variables have genuinely different shapes: some are scalars, some
are partitions, some are matrices, some are per unit fields. Two requirements only:

1. **Emit JSON or CSV to a specified path or to standard output.**
2. **Include a metadata block** with the repository identifier, the commit hash analyzed, the
   estimator name and version, the run timestamp, and the parameter values used.

The metadata block is the part that matters. A number without the commit it came from cannot be
checked by anyone, including you in six months. Extraction quality is known to change these
results as much as algorithm choice does, so a result that does not record its extraction
settings is not reproducible even in principle.

## Review

Estimators are held to a lighter bar than evidence, per
[GOVERNANCE.md](../GOVERNANCE.md#scope-of-this-document). An estimator needs to run, to state
what it computes and on what evidence, and to be MIT licensed. It does not need to change the
paper to be worth merging.

An estimator that *does* ground a computability claim in the paper, by demonstrating that a
variable tagged estimable really is, is a rung two contribution with a named credit line in
CRediT software role language. See
[the credit ladder](../CONTRIBUTING.md#5-the-credit-ladder).

If your estimator finds that a variable the paper tags as bare repository estimable actually
requires history, or intent, that is a **counterexample to the computability test** and it is
more valuable than a working estimator. File it in
[`evidence/counterexamples/`](../evidence/counterexamples/) with the code attached as evidence.

## Getting started

Use [the estimator issue template](../../../issues/new?template=estimator.yml) to claim a variable
before you build, so two people do not implement the same thing in the same month.
