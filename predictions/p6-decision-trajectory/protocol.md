# Prediction 6: decision trajectory signal

**Status:** stub. Runnable once a decision corpus exists, and building that corpus is the
contribution this needs most.

## The prediction in plain language

If you want a model to predict or draft the next architectural decision on a project, what
should you show it?

The best result currently available says: show it the last three to five decisions from the same
project. A flat recency window beats the alternatives that were tried.

The paper's reading is that this finding is right and undersells itself. Recency works because
the signal is in the path, not because recency is the right way to describe the path. Decisions
are not a list. They form a graph with typed edges, where one decision constrains another,
forbids another, enables another, subsumes, comprises, conflicts with, overrides, or stands as
an alternative to another. Each decision carries a state, from tentative through decided and
approved, with challenged and rejected and obsolesced as demotions, and a restriction force
saying how strongly it prunes what remains possible.

A recency window is a degenerate projection of that graph: take the nodes, drop the edges, drop
the states, drop the restriction force, and order by time. The prediction is that keeping the
structure beats throwing it away.

## The formal statement, from the paper

Conditioning next decision prediction on the typed decision graph, its states, edges, and
restriction force, will beat the flat recency window, because the window is a degenerate
projection of the graph.

## What would confirm it

- On a held out set of decisions, a model conditioned on the graph structured context
  outperforming the same model conditioned on a recency window of the same token size, with
  quality judged by whatever measure the corpus supports.
- The margin being larger for decisions with many graph neighbors that fall outside the recency
  window. This is the mechanism, and it should be visible directly. A decision whose relevant
  ancestors are recent is one where the two conditionings nearly coincide, and no difference
  should be expected there.
- An ablation showing which structural components carry the effect: edges alone, states alone,
  restriction force alone. If edges do all the work, the paper should say edges rather than
  claiming the whole calculus.

## What would falsify it

- Graph conditioning matching or losing to the recency window at equal token budget. Equal token
  budget matters here for the same reason as in Prediction 5: structured context that is simply
  longer would win for an uninteresting reason.
- The advantage appearing only when the graph is hand curated, and vanishing when the graph is
  mined automatically. That would leave the theory intact and the practical claim empty, since
  nobody is going to hand curate a decision graph at scale. It would need to be reported plainly
  as such.
- The advantage disappearing on projects that keep decision records poorly, which is most of
  them. Generalization to the untidy case is the real test.

## The corpus problem

The decision store the commitment calculus wants is the one thing the historical record never
had, and the paper explains why: rationale capture failed for human economic reasons rather than
representational ones. The capturer was not the beneficiary. Formalization demanded structure
before the designer had any. Capture intruded on the design mid flight. The value was deferred
and diffuse.

Two facts make a corpus possible anyway.

**Most real decisions live in issues, pull requests, and chat.** They were recorded, just not as
decision records. Mining them is a recovery problem rather than a collection problem, and there
is prior work on extracting design decisions from issue tracking systems to build on.

**Decision record adoption in the open is real but shallow.** A substantial number of
repositories have adopted architecture decision records, and a large share abandon the practice
after fewer than five records. That is bad for the projects and useful here, because it means
there is a public corpus of genuine early stage decision sequences, and the abandonment pattern
itself is data about restriction force and perceived value.

**Building the corpus is the contribution.** Concretely, what is needed:

1. A set of projects with recoverable decision sequences, from decision records where they
   exist, from issues and pull requests where they do not.
2. Typed edges between decisions, extracted or annotated. This is the hard part, and the
   annotation guide is itself worth writing before anyone annotates.
3. States and, where recoverable, restriction force.
4. A held out split by project rather than by decision, so the evaluation measures
   generalization to a new project rather than interpolation within one.

## Open design questions

- How to evaluate a predicted decision. Exact match is wrong, since many phrasings of the same
  decision are correct. Human judgment is expensive. A ranking task over candidate next
  decisions, including the real one, may be the practical compromise, and its weaknesses should
  be stated.
- Whether to mine edges with a model, which risks the extractor and the predictor sharing a bias
  and inflating the result, or to annotate by hand, which caps the corpus size.
- How to handle projects where the decision record is a partial and idealized reconstruction of
  what happened, which is most of them.

## Relationship to the rest of the repository

This prediction is the one that most directly needs an estimator. A decision graph extractor
that runs over a repository's issues and pull requests would serve this test, would populate the
commitment calculus for Prediction 5's Arm B, and would be a useful artifact on its own even if
neither prediction ever gets run. See [`estimators/README.md`](../../estimators/README.md).

## Results

None yet. See [`results/`](results/).
