# Prediction 3: the two way and one way partition is stable

**Status:** running continuously. This is the one prediction that is already being tested, by
every migration file merged into [`evidence/migrations/`](../../evidence/migrations/). It needs
no special study, only accumulation.

## The prediction in plain language

The paper sorts architectural differences into two kinds.

Some are real choices. Competent teams sit at either pole, for reasons they can state, and over
the years real systems move in both directions. How fine the isolation boundaries are. How
centralized the coordination is. When decisions get bound. Which concurrency model. How state is
represented. These are the coordinates.

Others are not choices at all. Nobody sets out to build a large tangle of mutually dependent
files. Nobody chooses to scatter one concern across forty places. Systems slide into these, and
climbing back out costs effort nobody enjoys spending. These are the potentials, and they are a
slope rather than an axis.

The prediction is that this sorting holds up as new evidence arrives. New migrations will keep
moving in both directions on the coordinates and in only one intentional direction on the
potentials.

This is the prediction with the sharpest single falsifier in the paper, and it is stated
explicitly in the text: an intentional, force justified migration toward a larger cyclic core
would count against the theory.

## The formal statement, from the paper

New industrial migrations will continue to move bidirectionally on the coordinate axes,
granularity, centralization, binding, concurrency model, and state representation, and
unidirectionally on the potentials, cyclic core, scattering, and hub overload. An intentional,
force justified migration toward a larger cyclic core would count against the theory.

## What would confirm it

- New migration files, filed after this protocol was committed, landing on both poles of each
  coordinate axis, each with forces stated by the engineers involved.
- Movement away from the potentials being deliberate and effortful in every documented case, and
  movement toward them being incidental, unremarked, or regretted.
- The classification holding for axes the paper did not originally examine. A newly identified
  axis that shows two way traffic on first contact is stronger evidence than another data point
  on granularity, because it was not selected to fit.

## What would falsify it

**The sharp falsifier.** One documented case of a competent team deliberately increasing the
cyclic core of mutually dependent components, with articulated forces, defended as the right
call rather than accepted as a cost. The paper says plainly that this would count against the
theory. It must therefore be looked for honestly, and looking for it is a specifically valuable
contribution.

**The soft falsifiers.**

- A coordinate axis that turns out to carry traffic in only one direction across a large
  accumulation of cases, which would demote it to a potential and change the dynamics section.
- A potential that a team articulated forces for descending, on purpose, in a way that
  generalizes.
- Scattering deliberately increased, and defended, on grounds other than temporary expedience.

Note what does not falsify it: a team sliding into a cyclic core through neglect and then
rationalizing it afterward. The prediction is about intentional, force justified movement, and
the distinction is doing real work rather than protecting the claim. The test is whether the
forces were weighed before the move or assembled after it, and evidence has to speak to that.

## How to contribute to this prediction

File migration evidence. That is the whole protocol. Each file in
[`evidence/migrations/`](../../evidence/migrations/) is a data point in this test, and no
separate study is needed.

The evidence most worth chasing, in order:

1. **Any intentional move toward a cyclic core.** The sharp falsifier. Look in monorepo
   consolidations, in deliberate coupling of components that were split too early, and in cases
   where a team removed an abstraction layer and accepted the resulting cycles.
2. **Counter fashion migrations on the coordinates.** Movement against the prevailing wisdom of
   its moment, which is worth several with the grain, because only counter fashion traffic
   distinguishes a genuine degree of freedom from a slow industry consensus.
3. **Migrations on the less examined coordinates.** State representation and centralization have
   thinner evidence in the paper than granularity does.
4. **Abandoned and reversed migrations.** Badly undersupplied in the public record, because
   nobody writes up the ones that did not work.

## Standing tally

To be maintained as evidence accumulates, so the state of the test is visible without reading
every file.

| Axis | Classified as | Documented direction A | Documented direction B |
| --- | --- | --- | --- |
| Isolation granularity | coordinate | finer, browser site isolation | coarser, control plane consolidation |
| Logical to physical congruence | coordinate | decoupled | coupled more tightly |
| Concurrency model | coordinate | converging from event driven | converging from process per request |
| Centralization | coordinate | broker removed | coordination re centralized |
| Binding time | coordinate | compile time | runtime install |
| State representation | coordinate | snapshots | deltas and log as truth |
| Cyclic core | potential | out, deliberate and effortful | none documented |
| Scattering | potential | out, deliberate | none documented |
| Hub overload | potential | out, deliberate | none documented |

The three empty cells in the bottom right are the prediction. Filling any of them, with real
evidence, would be a significant contribution.

## Results

Ongoing. Individual data points live in
[`evidence/migrations/`](../../evidence/migrations/). Periodic assessments of the tally go in
[`results/`](results/).
