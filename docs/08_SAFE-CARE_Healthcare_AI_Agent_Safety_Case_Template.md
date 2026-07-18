# SAFE-CARE™ Healthcare AI Agent Safety Case Template

*A structured, evidence-backed argument that an agent is safe enough for its intended use*

*SAFE-CARE Framework — authored by Yassen Eltayeb, Conefia · Version 1.1 · July 2026*

**Practical example:** A safety case is the document you want in your hand when a hospital buyer asks: “How do you know this agent will not give unsafe advice?” It connects claims, risks, controls, evidence, and open issues.

## Safety case structure

| Section | What to write |
| --- | --- |
| 1. Intended use | Who uses the agent, for what tasks, in what setting, with what limitations? |
| 2. Safety claims | What must be true for the agent to be considered safe enough? |
| 3. Hazard analysis | What can go wrong? Use the risk taxonomy. |
| 4. Controls | Which guardrails, tool constraints, memory policies, and escalation rules mitigate each risk? |
| 5. Evidence | Which tests, simulations, judge scores, clinician reviews, and production metrics support each claim? |
| 6. Human oversight | When and how humans review, intervene, and approve releases. |
| 7. Residual risk | What risks remain and why they are acceptable for intended use. |
| 8. Monitoring plan | How production signals detect drift, incidents, and regressions. |
| 9. Incident response | How severe failures are triaged, fixed, reported, and converted into regression tests. |
| 10. Signoff | Product, AI, clinical, privacy/legal, and operations approval. |

## Safety claim examples

| Claim | Evidence required |
| --- | --- |
| The agent does not provide prescription-like guidance. | Medication scenario suite, output guardrail logs, clinician review of failures. |
| The agent escalates red flags reliably. | 100% pass on critical scenarios; production escalation monitoring. |
| The agent grounds medical claims in approved evidence. | RAG trace audit, citation judge score, clinician spot-check. |
| The agent writes sensitive health profile fields only after confirmation. | Tool-call logs, schema validation, confirmation UI screenshots. |
| The agent uses memory without stale or invented facts. | Time-series tests, contradiction scenarios, user correction logs. |

## Risk-control-evidence matrix

| Risk | Control | Evidence | Owner |
| --- | --- | --- | --- |
| Missed red flag | Input classifier + output escalation check | Critical scenario suite pass rate | AI Safety |
| Unsafe medication advice | No-prescription prompt + output guardrail | HRT/medication scenario review | Clinical + AI |
| False citation | Citation support judge | Citation QA report | AI Evaluation |
| Bad profile write | Confirmation + schema validation | Tool trace audit | Backend + AI |
| Privacy leakage | Data minimization + retention policy | Privacy review + log audit | Privacy/Legal |

## Residual risk acceptance

| Residual risk | Why it remains | Compensating control | Owner | Acceptance / expiry |
| --- | --- | --- | --- | --- |
| Example: occasional false-positive escalation | Sensitivity prioritized for a high-risk symptom class | Human review; user-friendly wording; monitor escalation rate | Clinical safety lead | Accepted for pilot; review after 30 days |
| [Risk] | [Rationale] | [Control] | [Owner] | [Decision/date] |

## Safety claim pattern

Write every claim as: “For [intended use and population], configuration [version] is acceptably safe with respect to [specific hazard] because [controls] achieved [measured evidence], subject to [limitations and monitoring].” This prevents vague claims such as “the agent is safe.”

### Required review questions

- What evidence would falsify this safety claim?

- Which user group or context is not represented in the evidence?

- What happens when retrieval, tools, or escalation services are unavailable?

- Who can stop the system, and how quickly?

- When does the safety case expire or require re-approval?

## References

[Case Study] Eltayeb, Y. (2026). Menopause-support companion design case study. In SAFE-CARE public release repository, v1.0. Conefia. GitHub/Zenodo. https://doi.org/10.5281/zenodo.21330842

[Conference Outline] Eltayeb, Y. (2026). Building Safe Conversational AI Agents for Healthcare: Conference talk outline. In SAFE-CARE public release repository, v1.0. Conefia. GitHub/Zenodo. https://doi.org/10.5281/zenodo.21330842

[WHO 2021] World Health Organization. Ethics and governance of artificial intelligence for health. 2021. https://www.who.int/publications/i/item/9789240029200

[WHO 2025] World Health Organization. Ethics and governance of artificial intelligence for health: guidance on large multi-modal models. 2025. https://www.who.int/publications/i/item/9789240084759

[NIST AI RMF] National Institute of Standards and Technology. AI Risk Management Framework. https://www.nist.gov/itl/ai-risk-management-framework

[NIST AI 600-1] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1). U.S. Department of Commerce, July 2024. https://doi.org/10.6028/NIST.AI.600-1

[FDA GMLP] U.S. Food and Drug Administration. Good Machine Learning Practice for Medical Device Development: Guiding Principles. https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles

[FTC HBNR] Federal Trade Commission. Complying with FTC’s Health Breach Notification Rule. https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0

Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.
---

## Publication and citation

- **Author:** Yassen Eltayeb — Conefia.
- **Version:** v1.1 · July 2026.
- **License:** CC BY 4.0 for documents; Apache-2.0 for code and reusable machine-readable templates.
- **How to cite:** Eltayeb, Y. (2026). *SAFE-CARE: A Framework for Designing and Evaluating Safe Healthcare AI Agents*. Conefia. DOI: https://doi.org/10.5281/zenodo.21330159.
- **Trademark:** SAFE-CARE™ is a trademark of Yassen Eltayeb / Conefia.
- **Copyright:** © 2026 Yassen Eltayeb / Conefia.

> Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.

