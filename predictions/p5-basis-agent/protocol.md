# Prediction 5: an agent with the basis beats an agent with the observables

**Status:** specified well enough to run. This is the most developed protocol in the directory,
because it is the prediction that can be tested today with ordinary equipment, and because it is
where the paper's practical claim either pays out or does not.

## The prediction in plain language

A coding agent today sees a codebase through its observables. The file tree. A symbol and
reference graph. Some form of text or embedding search. And often a hand written prose file in
which the team has tried to write down what actually matters about the system.

That last file is the tell. Teams maintain those files by hand because they know the important
things are not in the file tree. What they are writing down, laboriously and staleley, are the
latent variables: which modules are supposed to depend on which, what this part is really for,
where the load bearing boundaries are, what not to touch.

The paper's claim is that most of what those files contain can be computed instead of typed, and
that an agent given the computed version will do better work. Specifically: give one agent the
estimated basis, meaning the intended module map, the allowed dependency relation, the
propagation structure, the hotspots, the element roles, the concern vectors, and the recent
decision trajectory. Give another agent the file tree, the symbol graph, and embeddings. Hold
the token budget equal, so the comparison is about what the tokens say rather than how many
there are. The basis agent should win.

And it should win by the most on the tasks where the naive representation fails hardest: changes
whose blast radius crosses module boundaries. On a change contained inside one file, knowing the
propagation structure buys you nothing. On a change that will ripple, it is the whole game.

## The formal statement, from the paper

On repository level change tasks, an agent whose context is the estimated basis, meaning the
intended map, the allowed dependency relation, propagation structure, hotspots, roles, concern
vectors, and the recent decision trajectory, will outperform an agent with the file tree, symbol
graph, and embeddings at equal token budget. The margin will be largest on tasks whose blast
radius crosses module boundaries.

## Why equal token budget is the load bearing control

Without it the experiment is worthless, and it is worth being explicit about why.

Any additional context improves an agent's performance up to a point, simply by being more
information. If the basis arm is allowed more tokens than the observables arm, a win tells you
that more context helps, which nobody doubts and which the paper does not claim. The claim is
about the *content* of the representation: that a given number of tokens spent on estimated
latent variables buys more than the same number spent on the file tree and retrieved snippets.

So the budget is the experiment. Everything else in this design is in service of making the
budget comparison honest.

## Design

### Arms

**Arm O, the observables agent.** Context is built from the file tree, a symbol and reference
graph, and lexical plus embedding retrieval over the repository. This is the composite of what
current agents actually do, and it should be implemented as the strongest reasonable version of
that rather than a weakened one. If a real agent scaffold is used off the shelf for this arm,
name it and pin its version.

**Arm B, the basis agent.** Context is built from the estimated basis:

1. The intended module map, from the reflexion loop or from a declared map where the project has
   one.
2. The allowed dependency relation, meaning which modules may depend on which.
3. Propagation structure: the transitive closure summary, the core, and element roles.
4. Hotspots from history: churn, co change, and modularity violations, meaning units that change
   together without a structural dependency between them.
5. Concern vectors over units.
6. The recent decision trajectory, meaning the last several decisions on the typed decision
   graph.

Arm B also needs a retrieval mechanism, since it must still find the code it is going to edit.
The difference between the arms is what fills the *context budget*, not whether the agent can
read files at all. Both arms get the same file reading tools. This is the single most important
implementation detail and getting it wrong invalidates the run.

**Arm C, control, recommended but optional.** Observables plus a hand written prose context file
where the project has one. This is the honest comparator, because it is what a well run project
actually has today, and beating a bare observables agent while losing to one with a good hand
written file would be an important and publishable result.

### Holding the budget equal

- Fix a context token budget per task, identical across arms. State it. A few settings are
  better than one, since the ordering could reverse with budget.
- Count tokens with the same tokenizer for all arms, and count everything that enters the
  context: system prompt, representation, retrieved code, and tool output.
- Where an arm cannot fill the budget, record the shortfall rather than padding.
- Cap total tool calls and total generated tokens identically. An agent that gets more turns can
  compensate for a worse representation by exploring more, which would confound the result.
- Use the same model, the same temperature, and the same decoding settings for both arms, and
  state them. Run every task multiple times per arm, since single samples at nonzero temperature
  will not separate anything.

### Tasks

Repository level change tasks, meaning tasks that require modifying real code in a real project
and that have a mechanical correctness check.

**Sourcing.** Historical commits or merged pull requests that fix an issue or add a feature,
with the tests that accompanied them. The agent sees the task description and the repository at
the parent commit, and must produce a change that passes the tests. Existing benchmark suites
built this way are usable, and using one makes the result comparable to other work, at the cost
of contamination risk discussed below.

**Stratification is mandatory, not optional.** The prediction is specifically about the margin
being largest where blast radius crosses module boundaries, so tasks must be labeled and
analyzed by blast radius:

- **Local:** the reference change touches one file.
- **Intra module:** several files, one module.
- **Cross module:** files in two or more modules.
- **Boundary altering:** the change alters an interface, a dependency edge, or a module
  boundary.

Label from the reference change, using a module map fixed in advance of the run, and commit the
labels before results are collected. A minimum of roughly twenty tasks per stratum is a starting
point, though anyone who does a real power analysis should replace that number and say so.

**The stratified analysis is the primary result.** If Arm B wins overall but the margin does not
grow with blast radius, the prediction is only half confirmed, and the protocol should say so
rather than reporting the aggregate and stopping.

### Measures

**Primary.** Resolution rate, meaning the fraction of tasks where the produced change passes the
project's tests, per stratum.

**Secondary, and worth as much for understanding what happened.**

- Regression rate: tests that passed before the change and fail after. This is where a bad
  representation should hurt most, since an agent that cannot see propagation structure breaks
  things it did not know it was touching.
- Files touched compared with the reference change, and specifically the count of files touched
  that the reference did not. Unnecessary edits are the signature of an agent searching blindly.
- Boundary violations introduced, checked against the allowed dependency relation. Arm B has
  this relation in context and Arm O does not, so this measure is close to a manipulation check.
- Tokens consumed against the cap, since an arm that uses half its budget is telling you
  something.

**Manipulation check.** Verify that Arm B's basis estimates are actually correct for the
repositories used. An agent given a wrong module map is not testing the prediction. Where the
map is estimated rather than declared, spot check it against the maintainers' own understanding
and report the accuracy. A run where the basis estimate was bad and Arm B lost says nothing
about the theory, and a run that does not check cannot distinguish that case from a real
negative.

### Contamination

Historical tasks from public repositories may be in the model's training data, which inflates
both arms and can inflate them unequally if one arm's representation cues recall more strongly.
Mitigations, in order of strength:

1. Use repositories or commits postdating the model's training cutoff, and state the cutoff.
2. Report results separately for pre cutoff and post cutoff tasks.
3. At minimum, state the risk explicitly and do not claim a small margin as decisive without
   addressing it.

## What would confirm it

- Arm B beating Arm O on resolution rate at equal token budget, on held out tasks, with a margin
  larger than the run to run variance from repeated sampling.
- The margin increasing monotonically, or close to it, across the blast radius strata from local
  to boundary altering.
- Arm B introducing fewer regressions and fewer boundary violations.
- The pattern holding at more than one budget setting and on more than one model family. A
  result that appears at one budget on one model is a finding about that configuration.

## What would falsify it

- No difference at equal budget. This is the outcome that would matter most, because the paper's
  practical thesis, that agents should represent the basis rather than the observables, rests on
  this prediction more than on any other.
- Arm B winning overall but with no gradient across blast radius strata, which falsifies the
  specific mechanism even while the aggregate looks favorable. The paper claims to know *why*
  the basis helps, and a flat gradient says it does not.
- Arm O matching Arm B once Arm O is given the same total budget through more retrieval, which
  would mean the basis is a compression convenience rather than a different kind of information.
- Arm C, observables plus a good hand written prose file, matching Arm B. That would not
  falsify the claim that latents matter, since the prose file is full of latents. It would
  falsify the claim that computing them beats writing them down, which is the practical half of
  the argument.

## Reporting

Results go in [`results/`](results/) with:

- Models, versions, decoding settings, and training cutoffs.
- The exact token budgets and the tokenizer used.
- Task list with blast radius labels, committed before results were collected.
- Per stratum results with dispersion across repeated runs, not just means.
- The manipulation check on basis estimate quality.
- Code to reproduce, under [`estimators/`](../../estimators/) or linked, Apache 2.0 licensed.
- Deviations from this protocol, listed.

Negative results are published. See [the directory README](../README.md).

## Smaller versions worth running

The full design is a real project. These are not, and each would be genuinely useful:

- **One repository, one model, three strata, twenty tasks.** A pilot that establishes whether
  the effect is visible at all. Clearly marked as a pilot.
- **The manipulation check alone.** How accurately can the basis be estimated on ten real
  repositories, checked against their maintainers? This is a standalone contribution and it
  gates the whole experiment.
- **Ablations within Arm B.** Which basis components carry the effect? If the allowed dependency
  relation does all the work and concern vectors do none, that is a finding the paper should
  absorb, and it is cheaper to test than the main comparison.

## Results

None yet. See [`results/`](results/).
