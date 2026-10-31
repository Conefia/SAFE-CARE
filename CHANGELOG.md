# Changelog

## v1.3.1 · October 2026

A consistency release: one title, one trademark notice and one hard-fail list across the repository, the white paper and Zenodo.

- The title now reads "SAFE-CARE: A framework for designing, evaluating and releasing safe patient-facing healthcare AI agents", identical across `CITATION.cff`, `.zenodo.json`, `NOTICE.md`, the README, every document's "How to cite" line and both Zenodo records, with Conefia LLC as publisher.
- White paper v2.0.1 carries the new title and the trademark wording below. Its content is otherwise unchanged from v2.0.
- Trademark wording: SAFE-CARE is a claimed unregistered trademark of Yassen Eltayeb, used by Conefia LLC under license. It now reads the same in the README, NOTICE, every document footer and the white paper.
- Judge rubric (`docs/06`, `templates/ai_judge_rubric.yaml`): the document and the template now list the same seven hard-fail conditions, adding protected-data exposure to the document and encouraging delay of urgent care to the template. Clarification, citation quality and uncertainty handling are stated to carry no weight in the illustrative composite.
- `MANIFEST.md` now lists every file in the repository (105 files).
- The Zenodo deposit description in `.zenodo.json` is rewritten for v1.3.0 and links white paper v2.0.1 (10.5281/zenodo.23826962).

## v1.3.0 · October 2026

This release adds the step that comes before every gate: qualifying the evaluation instrument. It draws on the author's public comment FDA-2026-N-7874-0091 and on lessons from repeat-run tests on patient-facing triage benchmarks.

- **New:** `docs/10_SAFE-CARE_Instrument_Qualification.md`, covering:
  - the reference standard and the observation window;
  - judge calibration against a clinician band, with a proposed per-dimension acceptance rule;
  - the null comparison (noise floor);
  - bounds and the library sizes they require;
  - judged-turn coverage and a positive control for every hard-fail gate;
  - what the first published SAFE-CARE Bench run found, with links to its results.
- **New:** `docs/11_SAFE-CARE_Change_Control.md`: re-testing scaled to the type of change around a fixed safety core; bridge tests when the judge changes.
- **New templates:** `templates/instrument_qualification.yaml`, `templates/change_control_map.yaml`.
- **New tool:** `tools/repeat_run_floor.py`, standard-library Python with tests in `tools/tests/`. It computes the noise floor, the smallest detectable differences, one-sided lower bounds (Wilson, or a scenario-clustered bootstrap capped by Wilson), comparisons and minimum library sizes.
- **Changed:** `templates/release_gate_checklist.yaml` (2.0) and `docs/07`:
  - critical gates require zero misses across K repeat runs, with K fixed in advance;
  - rates are read on one-sided lower 95% bounds;
  - declines are judged against a prespecified margin, and critical scenarios stay zero-miss;
  - a positive control proves each hard-fail gate can fire;
  - missed and unnecessary escalation are reported separately, with timeliness;
  - an unchanged rerun cannot overturn a failed gate.
- **Changed:** `templates/ai_judge_rubric.yaml` (2.0) and `docs/06`:
  - safety is a gate before any score, and dimensions are reported separately;
  - weights are optional, secondary and prespecified;
  - new dimensions for clarification and timely escalation;
  - a changed judge must pass a bridge test.
- **Changed:** `templates/scenario.schema.json` (1.1), backward compatible. New optional fields: `escalation_warranted`, `clarification_expected`, `required_action_turn`, `observation_window_turns`, `user_turns` and `reference_standard`. Two new examples: `clarification_needed_scenario.json` and `no_escalation_scenario.json`.
- **White paper v2.0:**
  - reorganized around the five-stage lifecycle, with ten figures (sources in `assets/figures/`);
  - an abstract, contributions stated as claims, numbered references, limitations, and maps to TRIPOD-LLM, DECIDE-AI and CONSORT-AI;
  - internal tags and the conference-positioning sections removed.
- **Fixed:**
  - `MANIFEST.md` listed files that are not in the repository;
  - the README white paper link had a space in the file name;
  - the example weights named an escalation-quality dimension that the rubric did not score; escalation quality is now a scored row in `docs/06`.
- **Added** `.zenodo.json`, so keywords, ORCID and related works carry over to every release.
- **Editorial:** two wording passes across `README.md`, `docs/01` to `docs/11`, `docs/SAFE-CARE_Framework.md` and white paper v2.0. Every paragraph now opens on its headline claim, and explicit transitions link sentences and sections, so each document reads as one argument. The method, thresholds, numbers and citations are unchanged. `docs/SAFE-CARE_Framework.md` keeps the v1.2.0 method, with notes pointing to the v1.3.0 documents. The scenario example in `docs/05` is shown again as one JSON block.

## v1.2.0 — July 2026

- Editorial and accuracy pass following independent review.
- Replaced the "Founder-led credibility strategy" section with "Public dissemination and implementation resources," describing the published reusable artifacts objectively rather than as outreach strategy.
- Retitled "Failure modes SAFE-CARE prevents" to "Failure modes SAFE-CARE is designed to mitigate" to avoid an absolute claim prior to validation.
- Added an explicit statement that release-gate thresholds are proposed release criteria and are not performance claims unless supported by a completed evaluation report.
- Retitled the conference-outline section to "How SAFE-CARE addresses common healthcare-AI deployment challenges" so the framework stands independently of any presentation.
- Corrected the WHO large multi-modal model guidance citation year to 2024 (released 18 January 2024) and retagged it [WHO 2024b].
- Clarified rights: author and copyright are Yassen Eltayeb; SAFE-CARE™ is a claimed unregistered trademark used by Conefia LLC in connection with its healthcare-AI framework and related services.
- Standardized the version string to 1.2.0 and the term "white paper" throughout.

## v1.1 — July 2026

- Added NIST AI 600-1 (Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, U.S. Dept. of Commerce / NIST, July 2024, https://doi.org/10.6028/NIST.AI.600-1) to the references and standards grounding.
- Version bumped to v1.1 across documents, README, and CITATION.cff.
- Note: cutting a new GitHub release archives v1.1 on Zenodo and mints a new version DOI; update the "How to cite" DOI to the v1.1 version DOI after release (the concept DOI continues to resolve to the latest version).

## v1.0 — July 2026

- Public-release edition authored by Yassen Eltayeb, Conefia.
- Anonymized the applied menopause-support case study and removed all client brand names.
- Removed generated stamps and private labels.
- Added licensing, citation, trademark, copyright, and public-use disclaimer.
- Added control ownership, 30-day implementation path, evidence maturity model, dataset splits, judge calibration, hard-fail overrides, release authority, residual risk acceptance, and a live demonstration storyboard.
- Added clean GitHub Markdown, branded DOCX/PDF assets, machine-readable templates, synthetic examples, publication checklist, and private redline review copies.
- DOIs minted via Zenodo: framework `10.5281/zenodo.21330159`; public release repository `10.5281/zenodo.21330842`. Repository: https://github.com/Conefia/SAFE-CARE.
