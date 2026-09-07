# The Referee

A standing document, kept apart from the paper, and applied to every draft. It builds the world the paper stands on one step at a time, from Turing upward, and at each step asks the question a hostile, competent reader would ask. For each question it records one of three things: the paper answers it, with the evidence named; the paper must answer it and does not yet; or nobody has answered it and the paper must say so. The purpose is not defence. It is to make the claims stand on the strongest base that can be built, so that the paper can be minimal without being thin.

The question the paper exists to answer is fixed: can most of what software engineers know be given a name and a shape, so that the work of deciding, and now of verifying, becomes navigable? Every step below is judged by whether it makes that answer stronger, weaker, or better bounded.

## Step 1. If Turing is right, what exactly do we have?

Turing's 1936 analysis says: whatever a person computes by rule can be computed by an automatic machine with a tape, a head, a finite state and a sheet. If that is right, then anything we call "a computer" is a physical object built so that a class of its state changes corresponds, under an interpretation we assign, to those operations. That is what the paper should mean by a computer, and it is a definition that reaches back before electronics: gears in Pascal's calculator, beads on an abacus, relays, tubes, transistors. The substrate changes; the correspondence is the computer.

Questions the referee asks.

Is Turing right? The claim is the Church-Turing thesis, and it is held by a failed search for exceptions: every definition of effective computation proposed before or since computes the same class. The paper says this and holds its own enumerations to the same standard. Answered.

Is the thesis about what is computable, or about what is computable cheaply? Only the first. The extended thesis, that every reasonable machine can simulate every other with at most polynomial overhead, is the one quantum computation challenges. The paper's walls are computability walls (undecidability, Rice) and physical floors (latency, energy), and neither is touched by a machine that changes prices. But the paper does not say this, and a theorist will ask. Must answer, in one sentence: the paper's walls are the ones no change of substrate moves; a new substrate changes the price list, which is exactly what the paper is built to absorb.

Is a real computer a Turing machine? No: it has finite memory, so formally it is a finite-state machine, and the unbounded tape is itself an idealisation. The paper lists the tape as uniform (idealisation 1) but not as unbounded. The referee's verdict: unboundedness is a cost, the price of a byte, and belongs under idealisation 1, which already prices it; the paper should say so in one clause so that nobody thinks the eight missed the most famous idealisation of all. Must answer.

Does all code build on it? Every program that runs on a physical computer is a sheet for a machine that is, up to its price list, the machine Turing described. That includes learned models: a neural network is a program with fixed meaning executed on the same hardware, and its "output varies" only in the sense the paper already handles (meaning fixed as "any of these"). The one honest exception is analogue and physical computation that does not pass through symbols at all, which the paper can set aside as Turing did the choice machine. Answered, with the caveat to be stated.

## Step 2. From one exact machine to many real machines

If every real machine is Turing's machine with a price list, then the differences between a CPU, a GPU, a phone, a data centre and a fleet of them are differences in price under the same eight idealisations: how far a byte is, how many heads there are, how often the tape fails, who else can read it. This is the single most useful sentence the referee produced: software engineering for any particular machine is interpretation under that machine's price list, and what is fundamental to all of them is the list of things that have a price. The paper implies this and should say it, because it is what makes the rows table and the bills an account of every machine rather than of a typical one.

Questions.

Is the list of eight complete? Held as a failed search, refutable by a ninth. The paper says so. The referee adds the test that a theorist will apply: take each element of Turing's definition (tape, head, motion, state, sheet, input, run) and ask what a real machine pays; the eight fall out and nothing is left over. The paper's opening of the idealisations section does this. Answered.

Why is the sorting into physical, boundary and world the right one? Because it is the sorting reality's feedback imposes (Step 4). Answered by the censuses, which are checkable.

## Step 3. How a field of knowledge forms around a tool

A tool is adopted, people learn to operate it, they offload work into it, and knowledge accumulates around it. The referee asks what determines the shape of that knowledge, because the paper's claim (three kinds, with rules in the middle) is a claim about shape.

The answer the referee arrives at, and the paper should state without dressing it up: knowledge accumulates where reality answers, and its form is set by how fast and how exactly reality answers. A program is an object that holds still, so questions about programs get exact answers and become theorems. A price is a quantity that moves, so questions about prices get answers that are true for a while and become rules whose conditions are the prices at the time. What people want is a quantity nobody can measure, so questions about it get no formal answer at all. That is the three kinds, derived rather than asserted, and it is why the censuses find theorems under the program (idealisation 6) and the tape (4), cost models under the physical five, and nothing under 7 and 8.

Question the paper must answer: is there evidence the field's knowledge actually formed this way, rather than the sorting being imposed after the fact? Evidence the paper already holds: every episode in which generation became mechanical began with somebody writing down what had to be preserved (the C abstract machine, serial equivalence, relational algebra), which is reality being made to hold still; the five-minute rule was recomputed each time its prices moved, which is reality answering slowly; and architecture has never been mechanised because its input is a forecast. The paper should present these three as the same fact seen three times. Must connect, not add.

## Step 4. The reality feedback loop, and whether the paper subscribes to it

Nature gives feedback continuously; whoever experiments most is rewarded most. Applied to a paper, this means the paper's own claims must be placed where reality can answer them. The referee checks each claim. The eight idealisations: refutable by a ninth. The grammar: refutable by an uncodable decision, with a procedure to find one. The test: refutable by a rule with no answer, with an invitation to find one. The formula and its collapse: hypotheses with observables. The residue: a prediction with a direction. The paper subscribes. What it does not do is show the loop running on itself: the census is designed and not run. The referee's verdict is that this is the largest single weakness and must be stated as such, not softened, until the census is run.

## Step 5. What software engineering irreducibly boils down to

Assemble the steps. A computer is an executor of fixed-meaning descriptions. Every real one is the same executor with a price list. Software engineering is the work of producing descriptions for a party that cannot speak in descriptions, under that price list. The knowledge of the field forms where reality answers. What is left when all of that is granted?

Two things, and the paper should say both plainly. First, a few walls, which are theorems and do not move. Second, everything else is a choice among alternatives that pay differently, and a choice has coordinates: the operation, the row, and the set of idealisations under which the alternatives differ. That is the hard claim: every decision in software engineering has that shape, and every rule is the cheaper side of an inequality between two costs in that space. It is hard because it is refutable, and the referee's job is to keep it refutable rather than let it become a vocabulary.

Objections the referee anticipates, with the paper's answer or its admission.

"This is just 'engineering is trade-offs'." No: trade-offs between what? The paper names the complete list of what, and a list is refutable where a slogan is not.

"The coordinates are not measurable." Row and operation are named on sight; the idealisation set is the coordinate nobody records, and the paper says so and gives the procedure for recording it.

"Rules are social, not economic." Partly true, and the paper keeps the part: uptake is a category of the test, and standing decides which rules a person holds between price crossings. What standing cannot do is decide where the crossings are, and the inversions show practice following prices against habit.

"Where is the running example?" Not in the paper. The referee records this as the largest gap in explanation rather than in argument, and it needs a real system with real numbers.

"What about the first tier, what people want?" Out of scope by construction, because no cost model reaches it, and the paper says exactly where the line is (idealisations 7 and 8).

## Step 6. Turing machines of a certain affordance

The reader's phrase, and the referee's reading of it. Each real machine affords a subset of the operations at each row at a price, and forbids nothing except the walls. To engineer software for a given machine is to know its price list; to engineer software in general is to know the list of things that have a price. The paper's rows table is that list laid across levels, and the bills are its physical floor. What the paper should add is the one sentence that makes the generality explicit: a new machine is a new price list, not a new list. That sentence is what lets a reader who works on GPUs, phones or fleets recognise their own machine in the paper.

## Standing verdicts to carry into every draft

Say what a computer is in one sentence that reaches back before electronics. Say that the unbounded tape is priced under idealisation 1. Say that a new substrate changes prices and not walls. Derive the three kinds from how reality answers, do not assert them. Present the three episodes of mechanisation as the same fact. State the unrun census as the largest weakness. Keep every claim in a form reality can refuse. Add nothing that does not serve the question the paper exists to answer.
