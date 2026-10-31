# SAFE-CARE™ Change Control

*Re-testing scaled to the type of change, around a fixed safety core*

*SAFE-CARE Framework · authored by Yassen Eltayeb, Conefia · Version 1.3.0 · October 2026*

**Practical example:** Re-test scope follows what a change can reach. For instance, a vendor updates the model snapshot behind the same product name. Nothing in the team's code changed, yet every behavior of the agent may have, so a model change re-runs every suite. By contrast, a one-line edit to a tool permission re-runs the tool suite and the safety core.

## The rule

Change control scales re-testing to the type of change, around a critical safety core that is re-run unchanged. Four rules set the scope of each re-test:

1. **Classify every change by type.** Use the change log and `templates/change_control_map.yaml`.
2. **Re-run the suites the map marks for that type.** Suites marked "if" are re-run when a written impact analysis says the change can reach them.
3. **Always re-run the critical safety core, unchanged**, on every change that could alter generated output, safety controls, routing, context handling or actions. Compare the result with the **original** baseline, so drift cannot accumulate across releases.
4. **Re-test periodically even when nothing was declared.** Periodic re-tests catch drift in a third-party model or retrieval source, infrastructure changes, and shifts in how people use the agent.

## The map

In practice, the map tells a team which suites to re-run for each type of change. Its columns are suites of the scenario library: the critical safety core, escalation and refusal, clinical knowledge and citation, personalization and memory, tools and actions, communication and scope, and timing and trajectory. Only the safety core column is marked "run" in every row, including the periodic re-test.

| Change type | Safety core | Escalation | Knowledge | Memory | Tools | Scope | Timing |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model version or snapshot | run | run | run | run | run | run | run |
| System prompt or instructions | run | run | if | if | if | run | if |
| Retrieval corpus or sources | run | if | run | if | | if | |
| Guardrail or filter rules | run | run | if | | | if | if |
| Session or cross-session memory | run | if | | run | if | | if |
| Tool definitions or permissions | run | if | | if | run | | if |
| Orchestration or routing logic | run | run | | | if | | run |
| No declared change (periodic) | run | if | if | if | if | if | if |

A blank cell means no re-run of that suite.

## Changes to the evaluation system

**A change to the judge, however, is a change to the evaluation itself.** That covers a new judge model, a new judge prompt and a rubric edit. Because the new scores come from a different instrument, bridge-test before comparing them with an old baseline:

1. Re-score a frozen set of earlier outputs with the new judge.
2. Compare the new scores with the old ones.
3. Re-qualify the judge if they differ beyond the noise floor (see `docs/10`).

## Production identity

Every rule above assumes that production runs the configuration that passed the gate. The lifecycle's Operate stage therefore requires confirming it, although the method for that check is outside the scope of this release.

## Evidence to keep

Finally, the change record lets a reviewer trace each release decision back to its tests. For every change, record:

- the change type;
- the suites re-run, and the impact analysis for each "if";
- the safety-core result against the original baseline;
- the bridge-test result, when the judge changed;
- the release decision and its sign-offs.

## References

[FDA PCCP] U.S. Food and Drug Administration. Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions. Final guidance, December 2024.

[FDA-2026-N-7874-0091] Eltayeb Y. Measurement-system qualification for generative AI medical-device benchmarks. Public comment FDA-2026-N-7874-0091, regulations.gov, 2026.

---

## Publication and citation

- **Author:** Yassen Eltayeb.
- **Version:** 1.3.0 · October 2026.
- **License:** CC BY 4.0 for documents; Apache-2.0 for code and reusable machine-readable templates.
- **How to cite:** Eltayeb, Y. (2026). *SAFE-CARE: A framework for designing, evaluating and releasing patient-facing healthcare AI agents*. Conefia LLC. DOI: https://doi.org/10.5281/zenodo.21330841.
- **Copyright:** © 2026 Yassen Eltayeb.

> Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.
