# SAFE-CARE™ Framework: Executive Overview

*A practical operating model for patient-facing healthcare AI agents*

*SAFE-CARE Framework · authored by Yassen Eltayeb, Conefia · Version 1.2.0 · July 2026*

SAFE-CARE turns one order of priorities into an end-to-end operating model: recognize risk first, and sound helpful second. For example, when a patient says, “I have heavy bleeding and feel dizzy,” the agent must recognize risk, avoid reassurance, and route the user to prompt care.

## The SAFE-CARE operating model

To do so, eight principles set practical requirements:

| Principle | Practical requirement |
| --- | --- |
| S: Scope | Define intended use, prohibited actions, claims, users, and escalation boundary. |
| A: Anchor | Ground health claims in approved evidence and make support traceable. |
| F: Fence | Layer input, output, retrieval, tool, memory, and monitoring guardrails. |
| E: Evaluate | Use simulations, ablations, AI judges, human calibration, and regression tests. |
| C: Contextualize | Personalize from confirmed, time-stamped, correctable health context. |
| A: Act | Use permissioned tools with confirmation, audit logs, and rollback. |
| R: Route | Escalate urgent, uncertain, severe, or regulated cases to humans. |
| E: Evidence | Maintain a safety case, registries, release report, and production monitoring. |

In practice, the architecture is one chain: User → input safety → evidence/context → orchestrator → governed tools → output safety → response/citations → monitoring and human review.

## Who benefits

On top of that, each stakeholder benefits differently:

| Stakeholder | Value |
| --- | --- |
| Patients | Clear education, appropriate personalization, citations, and safe escalation. |
| Clinicians and operations | Lower repetitive follow-up burden while high-risk cases stay human-owned. |
| Product and engineering teams | A repeatable build-test-release pattern that replaces one-off prompt work. |
| Healthcare organizations and the field | A shareable safety baseline that raises the bar for patient-facing AI. |

## In one line

Healthcare AI safety is an operating system built around the model: scope, evidence, guardrails, tools, memory, evaluation, escalation, and governance.

## Companion documents

These companion documents sit alongside this overview in the SAFE-CARE public release repository (github.com/Conefia/SAFE-CARE · DOI 10.5281/zenodo.21330841):

- **Menopause-support companion design case study**: the first applied case study of SAFE-CARE, based on the author's prior applied work and presented in anonymized form (docs/03_SAFE-CARE_Menopause-Support_Companion_Case_Study).
- **Building Safe Conversational AI Agents for Healthcare**: the conference talk outline (docs/09_SAFE-CARE_Conference_Talk_Deck_Outline).

---

## Publication and citation

- **Author:** Yassen Eltayeb.
- **Publisher:** Conefia LLC.
- **Version:** 1.2.0 · July 2026.
- **License:** CC BY 4.0 for documents; Apache-2.0 for code and reusable machine-readable templates.
- **How to cite:** Eltayeb, Y. (2026). *SAFE-CARE: A framework for designing, evaluating and releasing safe patient-facing healthcare AI agents*. Conefia LLC. DOI: https://doi.org/10.5281/zenodo.21330841.
- **Trademark:** SAFE-CARE is a claimed unregistered trademark of Yassen Eltayeb, used by Conefia LLC under license in connection with its healthcare-AI framework and related services.
- **Copyright:** © 2026 Yassen Eltayeb.

> Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.

