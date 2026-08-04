# Predictions

The paper closes with six falsifiable predictions. This directory is where they get tested.

A prediction in a paper is a promise that the theory could be wrong in a specified way. That
promise is only worth something if somebody eventually collects the data, and papers that close
with predictions rarely come back to them. This directory exists so that coming back is the
default rather than an act of unusual conscience.

## The six

| Folder | Prediction, in one line | Testable today? |
| --- | --- | --- |
| [`p1-asymmetric-similarity/`](p1-asymmetric-similarity/) | Architects' similarity judgments are asymmetric, oriented by re decision cost | Needs human subjects |
| [`p2-congruence-dominates/`](p2-congruence-dominates/) | Congruence terms predict maintenance outcomes better than any single graph metric | Needs a matched corpus |
| [`p3-two-way-one-way-partition/`](p3-two-way-one-way-partition/) | New migrations keep moving both ways on coordinates and one way on potentials | Ongoing, cheap, incremental |
| [`p4-recovery-disagreement/`](p4-recovery-disagreement/) | Recovery objective disagreement is reproducible and predicts accepted conformance rules | Fully computable, partly today |
| [`p5-basis-agent/`](p5-basis-agent/) | An agent with the basis beats an agent with the observables at equal token budget | **Yes, today** |
| [`p6-decision-trajectory/`](p6-decision-trajectory/) | The typed decision graph beats a flat recency window for next decision prediction | Yes, with a mined corpus |

Prediction 5 has the most developed protocol, because it is the one that can be run now with
ordinary equipment and because it is where the theory pays out or does not. Prediction 3 is the
cheapest to contribute to, since every migration file in
[`evidence/migrations/`](../evidence/migrations/) is a data point in it.

## How prediction testing works here

**A protocol is written before the data.** Each folder has a `protocol.md` stating the
prediction in plain language, what data would confirm it, and what data would falsify it. The
falsification condition is written down first, in public, with a timestamp in the git history.
This is the whole point. A prediction whose falsification condition is decided after the results
are in is not a prediction.

**Protocols can be improved, and improving one is a contribution.** Several of these are stubs
that state the shape of a test without specifying it tightly enough to run. Sharpening a
protocol, adding the statistical treatment, naming a corpus, specifying the controls, is real
work and is credited as such. Open an issue against the prediction folder.

**Amending a protocol after data collection has started requires a public note.** Add an
amendment section to the protocol saying what changed, when, and why, with the original text
left in place. Amendments are not forbidden and are sometimes necessary. Silent amendments are
forbidden.

**Results go in `results/`.** One folder or file per run, with:

- Who ran it and when.
- The protocol version, as a commit hash.
- The data, or a link to it and an archive, or a precise statement of why it cannot be shared.
- The analysis, in a form someone else can rerun.
- The conclusion, stated against the confirmation and falsification conditions the protocol
  wrote down.
- Deviations from the protocol, listed explicitly.

**Negative results are published here.** A run that comes out against the prediction is a
counterexample under [the credit ladder](../CONTRIBUTING.md#5-the-credit-ladder), and a
counterexample that forces a revision is rung two. There is no version of this project in which
burying an inconvenient result is acceptable, and the fact that the maintainer would obviously
prefer confirming results is exactly why the protocols and the reasoning are public.

**Partial runs count.** A pilot on three systems that establishes the measurement is feasible is
worth committing, clearly marked as a pilot. Most of these protocols will be run at a scale
smaller than the ideal, and a small honest run beats a large imagined one.

## If you want to run one

1. Read the protocol and open an issue saying you intend to run it. This prevents duplicated
   effort and lets the maintainer flag problems with the design before you spend the time.
2. If the protocol is underspecified for what you need, sharpen it in a pull request first, and
   get that merged before collecting data. This keeps the falsification condition ahead of the
   evidence.
3. Run it. Deviate where you must, and record every deviation.
4. Submit results as a pull request into that prediction's `results/`.

Preregistration in the formal sense is not required. Writing down what would count as failure,
before you look, is.
