<p align="center">
  <img src="assets/social-preview.png" alt="SAFE-CARE: a framework for designing and evaluating safe healthcare AI agents" width="820">
</p>

<h1 align="center">SAFE-CARE&#8482;</h1>

<p align="center">
  <b>A practical, end-to-end framework for designing, evaluating, releasing, and monitoring healthcare AI agents.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Docs-CC--BY--4.0-DEFF00?style=flat-square&labelColor=2B2B2B" alt="Docs license CC BY 4.0">
  <img src="https://img.shields.io/badge/Code-Apache--2.0-DEFF00?style=flat-square&labelColor=2B2B2B" alt="Code license Apache 2.0">
  <img src="https://img.shields.io/badge/version-1.3.0-2B2B2B?style=flat-square" alt="Version 1.3.0">
  <a href="https://doi.org/10.5281/zenodo.21330841"><img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21330841-2B2B2B?style=flat-square" alt="DOI"></a>
  <img src="https://img.shields.io/badge/Cite-CITATION.cff-2B2B2B?style=flat-square" alt="Cite this">
  <img src="https://img.shields.io/badge/PRs-welcome-2B2B2B?style=flat-square" alt="PRs welcome">
</p>

> **Healthcare AI safety is an operating system built around the model:** scope, evidence, guardrails, tools, memory, evaluation, escalation, and governance.

SAFE-CARE turns the principles of **WHO**, the **NIST AI Risk Management Framework**, and **FDA software-as-a-medical-device** guidance into an engineering method you can build, test, and audit. It is written for healthcare organizations, clinicians, founders, product and engineering teams, safety reviewers, and researchers who need more than a generic "be safe" instruction.

---

## Why SAFE-CARE

Healthcare agents fail fluently, and nobody can test a "be safe" instruction. That is, an agent can sound **fluent while being wrong, unsafe, overconfident, poorly personalized, or unauditable**. For this reason, SAFE-CARE makes safety an *architectural property*, with explicit controls, evaluations, and release gates, so a team can show with evidence how its agent behaves.

### Same input, two behaviors

In practice, a safe agent must first **detect risk, avoid reassurance, escalate appropriately, and record enough evidence to explain why it acted.** For example, when a patient says *"I have heavy bleeding and feel dizzy,"* a fluent chatbot may answer the menopause question and miss the red flag, as the figure below shows.

![Same input, two behaviors: a generic chatbot answers fluently and misses the red flag; a SAFE-CARE agent detects the red flag, avoids reassurance, escalates, and logs evidence](assets/failure-response.png)

## Start here

With that failure in mind, find your task below and open what it names.

| If you want to… | Go to |
|---|---|
| Understand the whole method | [`docs/SAFE-CARE_Framework.md`](docs/SAFE-CARE_Framework.md) · [white paper v2.0 PDF](release_assets/pdf/SAFE-CARE_Framework_White_Paper.pdf) |
| Share an executive overview | [`docs/01_SAFE-CARE_One_Pager.md`](docs/01_SAFE-CARE_One_Pager.md) |
| Map your failure modes | [`docs/02_..._Risk_Taxonomy.md`](docs/02_SAFE-CARE_Healthcare_AI_Agent_Risk_Taxonomy.md) |
| Evaluate an agent | [ablation](docs/04_SAFE-CARE_Agent_Ablation_Evaluation_Template.md) · [scenarios](docs/05_SAFE-CARE_Scenario_Simulation_Schema.md) · [AI-judge rubric](docs/06_SAFE-CARE_AI_Judge_Rubric_for_Healthcare_Agents.md) |
| Check that your evaluation can see a real change | [instrument qualification](docs/10_SAFE-CARE_Instrument_Qualification.md) · [`tools/repeat_run_floor.py`](tools/repeat_run_floor.py) |
| Decide go / no-go for release | [release gate](docs/07_SAFE-CARE_Release_Gate_Checklist.md) · [safety case](docs/08_SAFE-CARE_Healthcare_AI_Agent_Safety_Case_Template.md) |
| Plan re-testing after a change | [change control](docs/11_SAFE-CARE_Change_Control.md) · [`templates/change_control_map.yaml`](templates/change_control_map.yaml) |
| Use the machine-readable templates | [`templates/`](templates/) |

If SAFE-CARE helps your work, please star the repository and [cite it](#how-to-cite).

## What is new in 1.3.0

SAFE-CARE 1.3.0 adds the step that comes before every gate: qualifying the evaluation instrument. Because an unchanged agent does not give the same answers twice, a single benchmark run cannot tell a real change from noise, as the figure below shows.

![An unchanged agent can pass and fail the same gate](assets/figures/gate-noise.png)

- **Instrument qualification** ([docs/10](docs/10_SAFE-CARE_Instrument_Qualification.md)): repeat runs, a null comparison of the unchanged agent against itself, judge calibration against a clinician band, and bounds on how large a scenario library must be.
- **Release gates on repeat runs and confidence bounds** ([docs/07](docs/07_SAFE-CARE_Release_Gate_Checklist.md)): zero misses across K runs on critical scenarios, one-sided lower bounds on every rate, a prespecified margin for declines, and missed and unnecessary escalation reported separately.
- **Safety as a gate in the judge rubric** ([docs/06](docs/06_SAFE-CARE_AI_Judge_Rubric_for_Healthcare_Agents.md)): hard fails first, a new clarification dimension, and bridge tests when the judge changes.
- **Change control** ([docs/11](docs/11_SAFE-CARE_Change_Control.md)): re-testing scaled to the type of change around a fixed safety core.
- **Scenario schema 1.1** ([docs/05](docs/05_SAFE-CARE_Scenario_Simulation_Schema.md)): optional fields for escalation warranted, clarification expected, required-action turn and observation window, with two new examples.
- **White paper v2.0** in [`release_assets/`](release_assets/), reorganized around the lifecycle, with ten figures.

```bash
python tools/repeat_run_floor.py --demo              # see a stable and a variable agent
python tools/repeat_run_floor.py --runs runs/*.jsonl --threshold 0.95
python tools/repeat_run_floor.py --min-scenarios 0.95  # smallest library that can support a 95% gate
```

## The operating model

Beneath these checks sit the eight principles below, each with a practical requirement.

![The SAFE-CARE operating model, with eight principles: Scope, Anchor, Fence, Evaluate, Contextualize, Act, Route, Evidence](assets/operating-model.png)

| | Principle | Practical requirement |
|---|---|---|
| **S** | Scope | Define intended use, prohibited actions, claims, users, and the escalation boundary. |
| **A** | Anchor | Ground health claims in approved evidence and make support traceable. |
| **F** | Fence | Layer input, output, retrieval, tool, memory, and monitoring guardrails. |
| **E** | Evaluate | Use simulations, ablations, AI judges, human calibration, and regression tests. |
| **C** | Contextualize | Personalize from confirmed, time-stamped, correctable health context. |
| **A** | Act | Use permissioned tools with confirmation, audit logs, and rollback. |
| **R** | Route | Escalate urgent, uncertain, severe, or regulated cases to humans. |
| **E** | Evidence | Maintain a safety case, registries, a release report, and production monitoring. |

## The minimum safe agent

Taken together, these principles give the minimum safe agent in the figure below.

![The minimum safe agent architecture: user request flows through an input safety gateway, evidence and context, an orchestrator, governed tools, and an output safety gateway; risk escalates to a human; governance and monitoring underpin everything](assets/architecture.png)

## What is included

To build that agent, use the paths below, each mapped to its purpose.

| Path | Purpose |
|---|---|
| [`docs/SAFE-CARE_Framework.md`](docs/SAFE-CARE_Framework.md) | The full framework: lifecycle, architecture, guardrails, evaluation, release, governance. |
| [`docs/01_SAFE-CARE_One_Pager.md`](docs/01_SAFE-CARE_One_Pager.md) | Executive overview: a shareable summary of the framework. |
| [`docs/02_SAFE-CARE_Healthcare_AI_Agent_Risk_Taxonomy.md`](docs/02_SAFE-CARE_Healthcare_AI_Agent_Risk_Taxonomy.md) | Failure modes, severity, controls, tests, ownership. |
| [`docs/03_SAFE-CARE_Menopause-Support_Companion_Case_Study.md`](docs/03_SAFE-CARE_Menopause-Support_Companion_Case_Study.md) | Anonymized applied case study. |
| [`docs/04_SAFE-CARE_Agent_Ablation_Evaluation_Template.md`](docs/04_SAFE-CARE_Agent_Ablation_Evaluation_Template.md) | Compare A0–A4 agent configurations. |
| [`docs/05_SAFE-CARE_Scenario_Simulation_Schema.md`](docs/05_SAFE-CARE_Scenario_Simulation_Schema.md) | Scenario generation and datasets. |
| [`docs/06_SAFE-CARE_AI_Judge_Rubric_for_Healthcare_Agents.md`](docs/06_SAFE-CARE_AI_Judge_Rubric_for_Healthcare_Agents.md) | Evaluation rubric with hard overrides. |
| [`docs/07_SAFE-CARE_Release_Gate_Checklist.md`](docs/07_SAFE-CARE_Release_Gate_Checklist.md) | Evidence-backed go / no-go. |
| [`docs/08_SAFE-CARE_Healthcare_AI_Agent_Safety_Case_Template.md`](docs/08_SAFE-CARE_Healthcare_AI_Agent_Safety_Case_Template.md) | Safety case template. |
| [`docs/09_SAFE-CARE_Conference_Talk_Deck_Outline.md`](docs/09_SAFE-CARE_Conference_Talk_Deck_Outline.md) | Talk / deck outline. |
| [`docs/10_SAFE-CARE_Instrument_Qualification.md`](docs/10_SAFE-CARE_Instrument_Qualification.md) | Noise floor, judge calibration, bounds and library size. |
| [`docs/11_SAFE-CARE_Change_Control.md`](docs/11_SAFE-CARE_Change_Control.md) | Re-testing scaled to the type of change. |
| [`tools/`](tools/) | Repeat-run tool (standard-library Python) with tests. |
| [`templates/`](templates/) | Apache-2.0 machine-readable templates (YAML/JSON). |
| [`examples/`](examples/) | Generalized synthetic scenarios. |
| [`release_assets/`](release_assets/) | Branded DOCX + PDF of every document. |

## Use SAFE-CARE on a new project

Based on these documents, start before anyone chooses a model, in this order:

1. Complete the **Use-Case Safety Card** *before* choosing a model.
2. Build a **risk taxonomy** and a red-flag escalation map.
3. Establish **approved evidence** and citation-support checks.
4. Add tools only after **permission, confirmation, audit, and rollback** rules exist.
5. **Evaluate** incremental agent configurations against the same held-out scenarios, with K repeat runs and a measured noise floor.
6. **Block release** on any critical safety failure in any run, even when the average score is high, and read every other gate on its lower bound.
7. Maintain a **safety case**, re-test by change type, and convert production incidents into regression tests.

## Templates & examples

- [`templates/use_case_safety_card.yaml`](templates/use_case_safety_card.yaml): scope, non-use, escalation triggers, evidence standard.
- [`templates/scenario.schema.json`](templates/scenario.schema.json): scenario format with hidden ground truth and hard-fail conditions.
- [`templates/ai_judge_rubric.yaml`](templates/ai_judge_rubric.yaml): scoring dimensions and hard overrides.
- [`templates/release_gate_checklist.yaml`](templates/release_gate_checklist.yaml): release requirements on repeat runs and bounds.
- [`templates/instrument_qualification.yaml`](templates/instrument_qualification.yaml): the qualification record.
- [`templates/change_control_map.yaml`](templates/change_control_map.yaml): change type to re-test scope.
- [`examples/critical_red_flag_scenario.json`](examples/critical_red_flag_scenario.json) · [`examples/medication_boundary_scenario.json`](examples/medication_boundary_scenario.json) · [`examples/clarification_needed_scenario.json`](examples/clarification_needed_scenario.json) · [`examples/no_escalation_scenario.json`](examples/no_escalation_scenario.json)

## Public case-study boundary

The design case study is **anonymized and generalized**. Specifically, this repository does **not** publish client names, proprietary prompts, exact prediction logic, private content libraries, production data, screenshots, credentials, or deployment protocols. See [`NOTICE.md`](NOTICE.md).

## How to cite

If you use SAFE-CARE, please cite it (see [`CITATION.cff`](CITATION.cff)):

> Eltayeb, Y. (2026). *SAFE-CARE: A Framework for Designing and Evaluating Safe Healthcare AI Agents.* Conefia. DOI: [10.5281/zenodo.21330841](https://doi.org/10.5281/zenodo.21330841).

## License

- **Documentation and narrative artifacts:** [CC BY 4.0](LICENSE-DOCUMENTATION-CC-BY-4.0.txt)
- **Code, JSON/YAML schemas, and reusable machine-readable templates:** [Apache License 2.0](LICENSE-CODE-APACHE-2.0.txt)

SAFE-CARE is a trademark of Yassen Eltayeb / Conefia. © 2026 Yassen Eltayeb / Conefia.

## Maintainer

Created and maintained by **[Yassen Eltayeb](mailto:dev@conefia.com)**, founder of **Conefia** (applied, safe AI for healthcare). Contributions welcome; see [`CONTRIBUTING.md`](CONTRIBUTING.md) and report safety concerns via [`SECURITY.md`](SECURITY.md).

> **Disclaimer.** Public framework for educational and engineering use. It is not medical, legal, privacy, security, or regulatory advice; qualified review is required for each deployment.
