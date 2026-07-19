# SAFE-CARE™ Agent Ablation Evaluation Template

*A/B testing technical design choices instead of relying on safety claims*

*SAFE-CARE Framework — authored by Yassen Eltayeb, Conefia · Version 1.2.0 · July 2026*

**Practical example:** Instead of claiming “guardrails make the agent safer,” build A1 without guardrails and A2 with guardrails, then run the same severe-bleeding, HRT, and overreliance scenarios through both. The delta becomes evidence.

## Capability ladder

| Agent | Name | Capabilities | Primary comparison | Expected performance lift |
| --- | --- | --- | --- | --- |
| A0 | Unguided baseline | Base model only | Baseline | Fluency only; weak accuracy, safety, personalization. |
| A1 | Grounded education | A0 + approved RAG + citations + disclaimer | A1 vs A0 | Medical groundedness, citation credibility. |
| A2 | Safety-governed grounded | A1 + input/output guardrails + escalation | A2 vs A1 | Safety, red-flag routing, no-prescription behavior. |
| A3 | Personalized intake | A2 + progressive profiling + read tools + summaries + time-series context | A3 vs A2 | Personalization, UX, continuity, data completeness. |
| A4 | Full agentic companion | A3 + prediction + write tools + profile/symptom/stage sync | A4 vs A3 | Closed-loop personalization and profile consistency. |

## Evaluation matrix

| Dimension | A0 expectation | A1 expectation | A2 expectation | A3 expectation | A4 expectation |
| --- | --- | --- | --- | --- | --- |
| Medical accuracy | Low–medium | High | High | High | Highest |
| Safety | Low | Medium | High | High | Highest |
| Personalization | Low | Low | Low–medium | High | Highest |
| Citation quality | None | High | High | High | High |
| Tool correctness | N/A | N/A | N/A | Read tools | Read/write tools |
| Latency | Fastest | Medium | Medium | Slower | Slowest / most complex |

## Experimental protocol

1. Freeze model versions, prompts, RAG snapshot, tool schemas, and guardrail versions before each run.

1. Run the same scenario set through A0–A4 with randomized order and blinded agent identity for the AI judge.

1. Capture full traces: prompts, retrievals, citations, guardrail decisions, tool calls, latency, and final responses.

1. Score with an AI judge using a fixed rubric; calibrate a subset with clinician/human review.

1. Report absolute scores and deltas: A0→A1, A1→A2, A2→A3, A3→A4, A0→A4.

1. Treat S0/S1 failures as qualitative findings even if aggregate score is high.

## Minimum credible experiment

- Use at least 100 scenario runs per major risk/capability bucket, or report why a smaller exploratory set is appropriate.

- Run repeated stochastic trials when the model temperature or tool routing is non-deterministic.

- Blind the judge to agent identity and randomize comparison order to reduce preference and position bias.

- Calibrate at least a stratified subset with clinicians or qualified domain reviewers; report agreement and disagreement patterns.

- Report confidence intervals and failure counts, not only average scores.

- Treat every S0/S1 failure as a separate release-blocking finding regardless of aggregate score.

## Interpretation rules

| Observed change | Interpretation |
| --- | --- |
| Accuracy rises; safety falls | Do not call the configuration better overall; inspect overconfident or action-oriented answers. |
| Personalization rises; wrong-profile use rises | Context retrieval is working, but provenance/recency controls are insufficient. |
| Safety rises; UX falls sharply | Guardrails may be over-triggering; refine routing without weakening critical gates. |
| Full agent score rises; latency becomes unacceptable | Optimize orchestration, cache safe evidence paths, or reduce nonessential tool calls. |
| No material delta after adding a capability | The capability may be ineffective, incorrectly implemented, or not stressed by the dataset. |

## Companion documents

Also published in the SAFE-CARE public release repository (github.com/Conefia/SAFE-CARE · DOI 10.5281/zenodo.21330841):

- **Menopause-support companion design case study** — the first applied case study of SAFE-CARE (docs/03_SAFE-CARE_Menopause-Support_Companion_Case_Study).
- **Building Safe Conversational AI Agents for Healthcare** — conference talk outline (docs/09_SAFE-CARE_Conference_Talk_Deck_Outline).

## References

[LLM-as-Judge] Zheng et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. 2023. https://arxiv.org/abs/2306.05685

[HealthBench] Arora et al. HealthBench: Evaluating Large Language Models Towards Improved Human Health. 2025. https://arxiv.org/abs/2505.08775

[AI Hospital] Fan et al. AI Hospital: Benchmarking Large Language Models in a Multi-agent Medical Interaction Simulator. 2024. https://arxiv.org/abs/2402.09742

[AgentClinic] Schmidgall et al. AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments. 2024. https://arxiv.org/abs/2405.07960

Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.
---

## Publication and citation

- **Author:** Yassen Eltayeb.
- **Version:** 1.2.0 · July 2026.
- **License:** CC BY 4.0 for documents; Apache-2.0 for code and reusable machine-readable templates.
- **How to cite:** Eltayeb, Y. (2026). *SAFE-CARE: A Framework for Designing and Evaluating Safe Healthcare AI Agents*. Conefia. DOI: https://doi.org/10.5281/zenodo.21330841.
- **Trademark:** SAFE-CARE™ is a claimed unregistered trademark used by Conefia LLC in connection with its healthcare-AI framework and related services.
- **Copyright:** © 2026 Yassen Eltayeb.

> Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.

