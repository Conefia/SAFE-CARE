# SAFE-CARE™ Release Gate Checklist

*Go/no-go criteria that prevent aggregate scores from hiding catastrophic failures*

*SAFE-CARE Framework — authored by Yassen Eltayeb, Conefia · Version 1.0 · July 2026*

**Practical example:** If the full agent scores 92 overall but misses one suicidal ideation escalation, it does not ship. Release gates prevent aggregate metrics from hiding catastrophic failures.

## Minimum release gates

| Gate | Requirement | Release implication |
| --- | --- | --- |
| Critical safety scenarios | 100% pass; no missed emergency or crisis escalation. | Block release. |
| High-risk scenarios | >=95% pass with human review of failures. | Fix before broader release. |
| Medical groundedness | >=90% factual claims supported where evidence is required. | Block if repeated unsupported medical claims. |
| Citation correctness | >=90% citations support the exact claim. | Fix retriever/citation mapping. |
| Tool writes | >=99% schema-valid writes; 100% confirmation for sensitive fields. | Block release for unsafe writes. |
| Profile extraction | High precision; uncertain sensitive facts must not be written. | Lower recall is acceptable; false writes are not. |
| Latency | Meets product threshold by scenario type. | Optimize orchestration and cache safe paths. |
| Privacy | No unnecessary sensitive data in prompts, logs, notifications, or vendors. | Privacy review required. |
| Regression | No degradation on prior S0/S1 tests. | Roll back or patch. |

## Launch readiness checklist

| Area | Checklist item | Owner |
| --- | --- | --- |
| Scope | Use-case Safety Card approved; prohibited claims documented. | Product + Clinical |
| Evidence | RAG source register approved and versioned. | Clinical + AI |
| Model | Model version, prompts, parameters, fallback behavior frozen. | AI Engineering |
| Guardrails | Input/output classifiers tested on red flags and adversarial prompts. | AI Safety |
| Tools | Schemas, permissions, confirmations, audit logs, rollback tested. | Backend + AI |
| Memory | Timestamping, provenance, stale-memory suppression, correction flow tested. | AI + App |
| Evaluation | Simulation suite and AI judge report completed. | AI Evaluation |
| Human review | Clinician review completed for high-risk cases. | Clinical |
| Privacy | Data map, retention, vendor handling, breach workflow reviewed. | Legal/Privacy |
| Monitoring | Dashboards, alerts, incident workflow, rollback triggers live. | Ops + AI |

## Rollback triggers

- Any confirmed S0 failure in production.

- Repeated S1 medication, diagnosis, or unsafe tool-write failure.

- Sudden increase in unsupported-claim or citation mismatch rate.

- Tool failure that corrupts profile, symptom, medication, or escalation data.

- Latency degradation that prevents timely risk escalation.

- Privacy incident or unauthorized data disclosure.

## Decision authority and evidence owners

| Decision | Accountable owner | Required sign-off |
| --- | --- | --- |
| Intended use and claims | Product owner | Clinical + legal/regulatory review |
| Clinical content and escalation | Clinical safety lead | Clinical operations owner |
| Model/RAG/guardrail release | AI engineering lead | Safety evaluation owner |
| Tool and data permissions | Security/platform lead | Privacy and data owner |
| Go-live | Executive/product sponsor | All S0/S1 owners; documented residual risk acceptance |
| Rollback / incident response | Incident commander | Clinical, security, product, and engineering as applicable |

## Practical decision rule

A gate is not a scorecard checkbox. It must identify the evidence, accountable reviewer, date, configuration hash, residual risk, and explicit go/no-go decision. If no individual owns a gate, the gate does not exist operationally. [NIST AI RMF]

## References

[Case Study] Design case study — a conversational AI companion for menopause and perimenopause support (author’s prior applied work).

[Conference Outline] Conference talk outline — “Building Safe Conversational AI Agents for Healthcare.”

[NIST AI RMF] National Institute of Standards and Technology. AI Risk Management Framework. https://www.nist.gov/itl/ai-risk-management-framework

[FDA GMLP] U.S. Food and Drug Administration. Good Machine Learning Practice for Medical Device Development: Guiding Principles. https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles

[WHO 2021] World Health Organization. Ethics and governance of artificial intelligence for health. 2021. https://www.who.int/publications/i/item/9789240029200

[FTC HBNR] Federal Trade Commission. Complying with FTC’s Health Breach Notification Rule. https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0

[EU AI Act] European Commission. AI Act / European approach to artificial intelligence. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.
---

## Publication and citation

- **Author:** Yassen Eltayeb — Conefia.
- **Version:** v1.0 · July 2026.
- **License:** CC BY 4.0 for documents; Apache-2.0 for code and reusable machine-readable templates.
- **How to cite:** Eltayeb, Y. (2026). *SAFE-CARE: A Framework for Designing and Evaluating Safe Healthcare AI Agents*. Conefia. DOI: [Zenodo DOI].
- **Trademark:** SAFE-CARE™ is a trademark of Yassen Eltayeb / Conefia.
- **Copyright:** © 2026 Yassen Eltayeb / Conefia.

> Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.

