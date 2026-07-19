# SAFE-CARE™ Framework One-Pager

*A practical operating model for patient-facing healthcare AI agents*

*SAFE-CARE Framework — authored by Yassen Eltayeb, Conefia · Version 1.1 · July 2026*

Start with the failure: a patient says, “I have heavy bleeding and feel dizzy.” The agent’s first job is not to sound helpful—it is to recognize risk, avoid reassurance, and route the user to prompt care. SAFE-CARE turns that principle into an end-to-end operating model.

## The SAFE-CARE operating model

| Principle | Practical requirement |
| --- | --- |
| S — Scope | Define intended use, prohibited actions, claims, users, and escalation boundary. |
| A — Anchor | Ground health claims in approved evidence and make support traceable. |
| F — Fence | Layer input, output, retrieval, tool, memory, and monitoring guardrails. |
| E — Evaluate | Use simulations, ablations, AI judges, human calibration, and regression tests. |
| C — Contextualize | Personalize from confirmed, time-stamped, correctable health context. |
| A — Act | Use permissioned tools with confirmation, audit logs, and rollback. |
| R — Route | Escalate urgent, uncertain, severe, or regulated cases to humans. |
| E — Evidence | Maintain a safety case, registries, release report, and production monitoring. |

Architecture: User → input safety → evidence/context → orchestrator → governed tools → output safety → response/citations → monitoring and human review.

## Who benefits

| Stakeholder | Value |
| --- | --- |
| Patients | Clear education, appropriate personalization, citations, and safe escalation. |
| Clinicians and operations | Lower repetitive follow-up burden while high-risk cases stay human-owned. |
| Product and engineering teams | A repeatable build-test-release pattern instead of one-off prompt work. |
| Healthcare organizations & the field | A shareable safety baseline that raises the bar for patient-facing AI. |

## In one line

Healthcare AI safety is not a prompt. It is an operating system: scope, evidence, guardrails, tools, memory, evaluation, escalation, and governance.

## Companion documents

Published alongside this one-pager in the SAFE-CARE public release repository (github.com/Conefia/SAFE-CARE · DOI 10.5281/zenodo.21330841):

- **Menopause-support companion design case study** — the first applied case study of SAFE-CARE, based on the author's prior applied work and presented in anonymized form (docs/03_SAFE-CARE_Menopause-Support_Companion_Case_Study).
- **Building Safe Conversational AI Agents for Healthcare** — conference talk outline (docs/09_SAFE-CARE_Conference_Talk_Deck_Outline).

Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.
---

## Publication and citation

- **Author:** Yassen Eltayeb — Conefia.
- **Version:** v1.1 · July 2026.
- **License:** CC BY 4.0 for documents; Apache-2.0 for code and reusable machine-readable templates.
- **How to cite:** Eltayeb, Y. (2026). *SAFE-CARE: A Framework for Designing and Evaluating Safe Healthcare AI Agents*. Conefia. DOI: https://doi.org/10.5281/zenodo.21330841.
- **Trademark:** SAFE-CARE™ is a trademark of Yassen Eltayeb / Conefia.
- **Copyright:** © 2026 Yassen Eltayeb / Conefia.

> Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.

