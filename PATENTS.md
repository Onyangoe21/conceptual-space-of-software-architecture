# Patent policy

This document says plainly what this repository grants and what it does not. It exists because
the answer is genuinely different for the code than for the paper, and because a reader who has
to guess will guess wrong in one direction or the other.

**This document adds nothing and takes nothing away.** It describes
[LICENSE-CODE](LICENSE-CODE) and [LICENSE](LICENSE). It imposes no condition that those files do
not already impose. Where anything here reads as conflicting with either license file, the
license file governs and this document is wrong.

## The two licenses cover different things

| | License | Copyright | Patents |
| --- | --- | --- | --- |
| Code, meaning `estimators/` and `.github/scripts/` | [Apache 2.0](LICENSE-CODE) | Granted | Granted, bounded, see below |
| Paper text and everything in `evidence/` and `predictions/` | [CC BY 4.0](LICENSE) | Granted | Not granted, see below |

## What the code grants

Section 3 of Apache 2.0 grants you a patent license from every contributor, including the
maintainer. It is perpetual, worldwide, royalty free, and irrevocable except as stated below.

Its scope is fixed by the license text and it is narrower than people often assume. It reaches
only those claims that are **necessarily infringed by that contributor's contribution alone, or
by the combination of that contribution with the work it was submitted to**. So merging an
estimator that computes propagation cost grants you what you need to run and build on that
estimator. It does not sweep in unrelated claims that the same contributor happens to own, and
it does not operate as a grant across anyone's whole portfolio. That is the license doing its
job, not a reservation being smuggled in.

The grant runs in every direction. You get it from the maintainer and from every other
contributor. They get it from you for what you contribute. This is why the project has no
contributor license agreement and will not add one. Section 5 already places your contribution
under the same terms unless you say otherwise in writing in the pull request.

**Defensive termination.** Section 3 ends your patent license under Apache 2.0 if you begin
patent litigation alleging that the work, or a contribution in it, infringes a patent. It ends
only your patent license, only for you, and only from that date. Your copyright license is
untouched, and so is everyone else's patent license. Nothing about this is unusual. It is the
standard Apache term and it is one of the reasons the project uses Apache 2.0 rather than a
permissive license that is silent on patents.

## What the paper does not grant

CC BY 4.0 grants copyright permissions. It does not grant patent rights, and it says so in its
own words at section 2(b)(2):

> Patent and trademark rights are not licensed under this Public License.

So you may copy, redistribute, adapt, and build on the paper text, with attribution, under CC BY
4.0. Reading a variable's definition in the paper, or citing it, or reimplementing it in your own
work, is a matter between you and whatever patent rights exist independently of this repository.
The paper describes ideas. It does not license them.

This is not a trap laid for readers. It is the ordinary state of every academic paper ever
published, stated out loud because this repository ships code next to the paper and the two
carry different terms.

## No implied license beyond the express grants

The maintainer may hold, or may apply for, patents on work related to this research. Publishing
this repository is not an offer of a license to anything beyond what
[LICENSE-CODE](LICENSE-CODE) and [LICENSE](LICENSE) expressly grant, and no license beyond those
should be inferred from the act of publication, from the paper's contents, from a discussion in
an issue or pull request, or from a contribution being merged.

Stating this is the point of using Apache 2.0 here. An express grant of a defined scope is
clearer for everyone than silence that each party interprets in its own favor. You know what you
have, which is a real and irrevocable license to the code and everything it necessarily needs.
The project knows what it gave.

## If you need more than this

Email [edwin.o.onyango.jr@gmail.com](mailto:edwin.o.onyango.jr@gmail.com) and say what you want
to do. A licensing question is not an imposition and will get a straight answer within a week,
the same as everything else here. Asking is cheaper for you than assuming, and it is cheaper for
the project than a dispute.

Nothing in this document is legal advice, and the maintainer is not your lawyer. If your use is
close enough to the line that this document matters to you, it is close enough to be worth asking
your own counsel.
