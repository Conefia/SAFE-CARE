# SAFE-CARE™ Conference Talk Deck Outline

*Building Safe Conversational AI Agents for Healthcare*

*SAFE-CARE Framework — authored by Yassen Eltayeb, Conefia · Version 1.0 · July 2026*

Talk promise: Attendees should leave with one idea they can repeat: healthcare AI safety is not a prompt; it is an operating system.

## Audience and talk goal

Audience: healthcare founders, product leaders, clinicians, digital health operators, AI engineers, and innovation teams.

Goal: establish founder-led credibility by showing a practical, reusable framework for building safe healthcare AI agents, grounded in the companion as a real applied case study. [Case Study]

## Deck outline

| Slide | Title | Content / visual idea | Speaker takeaway |
| --- | --- | --- | --- |
| 1 | Cold open: the dangerous “good answer” | Tell the heavy bleeding + dizziness example. Show that a fluent answer can be unsafe if it misses escalation. | A safe healthcare agent must optimize for risk before helpfulness. |
| 2 | The care gap between visits | Patients need support, education, and guidance outside visits; clinics face staff capacity and follow-up burden. [Conference Outline] | This is why healthcare needs agents. |
| 3 | Where agents create value | Education, care navigation, adherence, follow-up, chronic disease support, menopause support, engagement. | Agents are operational infrastructure, not just chat. |
| 4 | Why many agents fail | Hallucinations, unsafe advice, missing escalation, lack of personalization, overreliance. [Conference Outline] | These failures are predictable and testable. |
| 5 | The shift: chatbot -> governed agent system | Show the model/evidence/safety/tools/memory/evaluation/governance stack. | Do not ship a chatbot. Ship a system. |
| 6 | Introduce SAFE-CARE | Scope, Anchor, Fence, Evaluate, Contextualize, Act, Route, Evidence. | A memorable framework for safe healthcare agents. |
| 7 | Scope: define what the agent will not do | Example: the companion educates and personalizes but does not prescribe HRT or diagnose with certainty. | Safety starts with claims. |
| 8 | Anchor: approved evidence and citations | RAG + clinician-approved library + citation support checks. | Credibility requires traceability. |
| 9 | Fence: guardrails at every layer | Input, output, retrieval, tool, memory, monitoring guardrails. | One safety prompt is not enough. |
| 10 | Evaluate: simulation before release | Show scenario schema and A0–A4 ablation ladder. | You cannot improve what you do not measure. |
| 11 | Contextualize: safe personalization | Use profile, active symptoms, triggers, stage, memory — but label known vs inferred vs predicted. | Personalization creates value and risk. |
| 12 | Act: governed tools | Read profile, read symptoms, update profile, log symptom, schedule reminder; confirmations and audit logs. | Agents that act need contracts. |
| 13 | Route: risk to humans | Severe symptoms, crisis, medication danger, contraindication uncertainty. | The safest agent knows when to stop. |
| 14 | Evidence: governance dossier | Safety cards, model cards, prompt registry, tool registry, evaluation report, incident response. | Trust requires artifacts. |
| 15 | The companion case study | Menopause companion: RAG, citations, progressive profiling, stage prediction, app tools, time-series memory. | A practical example of SAFE-CARE in action. |
| 16 | The evaluation ladder | A0 baseline, A1 RAG, A2 guardrails, A3 personalization, A4 full agentic companion. | Ablations turn design choices into evidence. |
| 17 | Release gates | S0 critical must pass 100%; aggregate scores cannot hide catastrophic failures. | Good enough is not safe enough for critical scenarios. |
| 18 | What founders should publish | Framework, risk taxonomy, case study, templates, scenario schema, rubric, release gates. | Open-sourcing process builds credibility. |
| 19 | Closing line | Healthcare AI safety is not a prompt. It is an operating system. | Repeatable takeaway. |
| 20 | Q&A | Invite discussion around use cases, risk levels, and evaluation design. | Move from demo culture to safety culture. |

## Suggested visual system

- Use a red/yellow/green risk color system: red = stop/escalate, yellow = clarify, green = educate/engage.

- Use one repeated diagram: User -> Safety -> Evidence -> Agent -> Tools -> Safety -> Response -> Monitoring.

- Lead every technical concept with a user story before showing architecture.

- Show A0–A4 as a staircase to make technical choices tangible.

- Close with a checklist slide that audience members can copy into their own agent projects.

## Conference abstract

Healthcare organizations need scalable support between visits, but generic AI agents can hallucinate, provide unsafe advice, miss escalation, lack personalization, or encourage overreliance. In this talk, Yassen Eltayeb introduces SAFE-CARE, a practical framework for building safe healthcare AI agents. Drawing from the the companion menopause companion case study, the talk explains how to combine clinician-approved RAG, safety guardrails, progressive profiling, app-integrated tools, time-series memory, simulation-based evaluation, AI judges, clinician review, release gates, and production monitoring into a credible end-to-end agent design process.

## Live demonstration storyboard

| Beat | What the audience sees | Teaching point |
| --- | --- | --- |
| 1. Generic answer | A fluent baseline answers a severe-symptom message as ordinary education | Fluency is not safety |
| 2. Grounded answer | RAG adds evidence and citations but still may miss escalation | Grounding solves only one failure class |
| 3. Guarded answer | Safety layer detects red flags and routes to urgent care | Escalation must override normal conversation |
| 4. Personalized answer | Agent uses confirmed symptoms/history and asks one missing question | Personalization should reduce burden without inventing facts |
| 5. Governed action | Agent proposes a profile update and waits for confirmation | Acting safely requires permissions, auditability, and rollback |
| 6. Evaluation view | The same scenario runs through A0–A4 with score and trace differences | Claims become measurable engineering evidence |

## Audience takeaway card

Before connecting a model to a patient conversation, answer five questions: What is it allowed to do? What evidence supports its claims? What makes it stop or escalate? How will we test the risky cases? Who owns failures after launch?

## References

[Case Study] Design case study — a conversational AI companion for menopause and perimenopause support (author’s prior applied work).

[Conference Outline] Conference talk outline — “Building Safe Conversational AI Agents for Healthcare.”

[WHO 2021] World Health Organization. Ethics and governance of artificial intelligence for health. 2021. https://www.who.int/publications/i/item/9789240029200

[WHO 2025] World Health Organization. Ethics and governance of artificial intelligence for health: guidance on large multi-modal models. 2025. https://www.who.int/publications/i/item/9789240084759

[RAG] Lewis et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. 2020. https://arxiv.org/abs/2005.11401

[LLM-as-Judge] Zheng et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. 2023. https://arxiv.org/abs/2306.05685

[HealthBench] Arora et al. HealthBench: Evaluating Large Language Models Towards Improved Human Health. 2025. https://arxiv.org/abs/2505.08775

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

