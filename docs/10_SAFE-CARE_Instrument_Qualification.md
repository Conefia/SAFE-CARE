# SAFE-CARE™ Instrument Qualification

*Checking that an evaluation can detect the change it is used to judge*

*SAFE-CARE Framework · authored by Yassen Eltayeb, Conefia · Version 1.3.0 · October 2026*

**Practical example:** One run can block a release on a drop that may be noise. For instance, a team edits its system prompt and reruns the benchmark once. The high-risk pass rate moves from 95.5% to 94.5%, and the release is blocked. Run the unchanged agent five times, however, and the same pass rate moves between 93% and 97% on its own. The drop sits inside that spread.

## Why qualify the instrument

To help teams that read a release gate, and reviewers who check one, tell noise from a real change, this document treats an evaluation of a generative agent as a measuring instrument with at least three sources of variability:

- **The agent varies between runs.** The same input does not always produce the same output, even at fixed settings.
- **The judge varies.** An automated judge, or a human rater, does not always score the same output the same way.
- **The reference varies.** The clinicians who define the correct answer do not fully agree with each other.

As a result, a gate read without measuring these sources can block a good change or pass a bad one. Qualification is the evidence, produced before any gate is read, that the instrument is precise enough for the decision.

## The qualification record

That evidence lives in the qualification record, where each row names one check, what to do and the evidence to keep.

| Component | What to do | Evidence to keep |
| --- | --- | --- |
| Reference standard | Fix the correct answer for each scenario in advance and independently of the judge that will score against it. | Who set it, how, and when; the scenario file hash |
| Observation window | For multi-turn scenarios, declare the turn by which action is required and define the scoring window relative to it. | `required_action_turn` and `observation_window_turns` in each scenario |
| Judge calibration | Compare the judge with qualified clinicians, dimension by dimension, with a chance-corrected statistic. Raw agreement alone can be near 100% while kappa is unstable. | Agreement per dimension, with intervals |
| Clinician band | Measure how far clinicians disagree with each other on the same conversations. | Between-clinician agreement per dimension |
| Judged-turn coverage | Report the share of turns, and of safety interventions, that some judge actually scored. | Coverage per dimension and per tier |
| Positive control | Run a scenario built to fail each hard-fail gate and confirm the gate blocks it. | The control scenario and its result, per rubric version |
| Disagreement rule | Write down, before any result is seen, how rater or judge disagreement is resolved. | The rule, dated |
| Provenance | Record agent, judge, corpus and prompt versions and the configuration hash with every score. | One row per scored run |
| Null comparison | Run the unchanged configuration K times and measure its noise floor (below). | Noise floor and smallest detectable difference |

**A proposed acceptance rule for judges.** Based on the clinician band, accept a judge on a dimension when its disagreement with clinicians is no larger than the disagreement among the clinicians themselves on the same conversations. For example, a judge that passes on citations and fails on escalation is used for citations only.

## The null comparison

The null comparison measures how far the score of an unchanged agent moves on its own, so a team knows which gains to trust.

1. Fix the configuration: agent version, prompt, retrieval sources, tools, decoding settings and judge.
2. Run the full scenario set K times (K of at least 5), judging each run afresh.
3. For each scenario, split its K runs at random into two pretend versions, A and B.
4. Compute the comparison statistic you would use between two real versions, for example the difference in pass rate.
5. Repeat the split many times. The spread of those differences is the **noise floor**.

In practice, the noise floor is the range of differences a team should expect between two identical versions. That floor covers generation and judge variability on this scenario set. However, it leaves out uncertainty in the reference answers and in which scenarios were drawn, so characterize those two separately.

**Reading the result:**

- A measured improvement inside the noise floor is not claimed as an improvement.
- By contrast, a decline is judged against a margin fixed in advance (see `docs/07`). The noise floor sets how many runs that test needs, and the margin decides it.
- The smallest detectable difference, reported for 1, 2, 3, 5 and 10 runs per version, tells a team how many runs a gate needs.

To measure that floor, run the comparison with `tools/repeat_run_floor.py`, and record the result in `templates/instrument_qualification.yaml`.

## Gates read against bounds

At a release gate, a pass means a one-sided lower bound on the pass rate clears its threshold, and three rules govern that bound:

- **The unit is the scenario.** With repeat runs, average each scenario's result over its K runs first, then form the bound across scenarios. A scenario-clustered bootstrap does this, and the tool caps its bound at the Wilson bound on the number of scenarios, because a bootstrap of a perfect or near-perfect library collapses to 100%.
- **For a single run, use the one-sided Wilson lower bound.**
- **Library size limits the strongest claim.** With every scenario passing, a one-sided 95% Wilson bound reaches 90% only with at least 25 scenarios, 95% with 52, and 99% with 268.

For this reason, size the library before the first run for the strongest claim the gate has to support; on a smaller library, no result can clear it.

## What the first SAFE-CARE Bench run found

The first published SAFE-CARE Bench run (A0 to A2, nine headline scenarios, three repeats, then re-scored) shows why each row of the record exists. All figures are in the [Bench results](https://github.com/Conefia/SAFE-CARE-Bench/tree/main/results).

- **Null comparison.** 16.3% of 270 in-scope cells changed across three runs at temperature zero; a second scoring of identical transcripts changed 5.9%. The two figures come from different designs and cannot be compared directly, so this run cannot split the movement between the agent and the judge.
- **Ablation read against noise.** Adding one guardrail flag lowered scored medical accuracy in 6 of 9 scenarios, while the 95% interval of the single-turn safety gain included zero. This is an exploratory, uncorrected comparison.
- **Observation window.** Multi-turn escalation scored turn 1 of a two-turn scenario; the guarded agent corrected itself in turn 2, so the correction went unscored.
- **Judged-turn coverage.** 33 of 75 in-scope turns per tier were scored by no judge, and 12 of 36 enforced safety actions were read by no safety or escalation judge.
- **Positive control.** The rubric declared no hard-fail entry, so the hard-fail column read zero by construction.
- **Judge calibration.** Single-turn escalation agreed with its own repeat on 97.5% of rows, with kappa 0.654 and an interval from -0.017 to 1.000.
- **Reference standard.** One blinded family physician agreed with the declared escalation label on 7 of 12 scenarios; the disagreements traced mainly to a label that merged clinical need with agent handoff.

Although the Bench run is M1 evidence (one generation model, judges from the same family, no measured judge-clinician agreement), a team can run the same checks on its own first run before it trusts its gate.

## When to re-qualify

Because these checks hold only for the instrument they were run on, re-qualify whenever a part of it changes:

- **Any change to the judge model, judge prompt or rubric.** Re-score a frozen set of earlier outputs (a bridge test) before comparing new scores with an old baseline.
- **A change to the scenario library or the reference answers.**
- **At least once per release cycle**, on the safety core.

By contrast, for changes to the agent, SAFE-CARE Change Control maps each type to the suites a team re-runs.

## References

[FDA-2026-N-7874-0091] Eltayeb Y. Measurement-system qualification for generative AI medical-device benchmarks. Public comment FDA-2026-N-7874-0091, regulations.gov, 2026.

[Wilson 1927] Wilson EB. Probable inference, the law of succession, and statistical inference. J Am Stat Assoc. 1927;22(158):209–212.

[LLM-as-Judge] Zheng et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. 2023. https://arxiv.org/abs/2306.05685

[SAFE-CARE Bench results] Eltayeb Y, Abdelkarim M, Hafez M. SAFE-CARE Bench results: run_2026-09-01, run_2026-09-08 and clinician Label Set A. Conefia LLC; 22 October 2026. https://github.com/Conefia/SAFE-CARE-Bench/tree/main/results

[Feinstein 1990] Feinstein AR, Cicchetti DV. High agreement but low kappa: I. The problems of two paradoxes. J Clin Epidemiol. 1990;43(6):543–549.

[CLSI EP05-A3] Clinical and Laboratory Standards Institute. Evaluation of precision of quantitative measurement procedures; approved guideline, 3rd ed. 2014.

[CARE-Bench] Hua Y, Na H, Ayubcha C. CARE-Bench: Benchmarking patient-facing LLM triage. arXiv:2608.03731, 2026.

---

## Publication and citation

- **Author:** Yassen Eltayeb.
- **Version:** 1.3.0 · October 2026.
- **License:** CC BY 4.0 for documents; Apache-2.0 for code and reusable machine-readable templates.
- **How to cite:** Eltayeb, Y. (2026). *SAFE-CARE: A framework for designing, evaluating and releasing patient-facing healthcare AI agents*. Conefia LLC. DOI: https://doi.org/10.5281/zenodo.21330841.
- **Copyright:** © 2026 Yassen Eltayeb.

> Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.
