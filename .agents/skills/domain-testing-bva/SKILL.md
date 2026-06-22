---
name: domain-testing-bva
description: Guides an AI testing agent through auditable black-box Domain Testing and Boundary Value Analysis using requirements, API specifications, observable UI or API behaviour, equivalence partitions, and boundary values. Use when designing, reviewing, executing, or validating DT/BVA tests without inspecting implementation source code or fabricating results.
---

# Black-box Domain Testing and Boundary Value Analysis

Use this skill for one selected feature at a time. Domain Testing (DT) and Boundary Value Analysis (BVA) are functional black-box techniques: derive tests and expected results only from requirements, specifications, input/output domains, and observable behaviour. Never inspect application implementation source, internal tests, database schema, controllers, middleware, services, or models as a test basis.

## Required References

- Read `references/instructor-clarifications.md` first.
- Read `references/assignment-requirements.md` for HW02 selection and submission rules.
- Read `references/eshop-analysis-guide.md` for approved EShop test bases and safe startup guidance.
- Read `references/domain-testing-method.md` and `references/bva-method.md` while modeling.
- Read `references/test-case-schema.md` before deriving or validating cases.
- Use `references/human-review-checklist.md` at the review gate.
- Use `assets/` and `scripts/` to create and validate the feature workspace.

## Integrity Rules

- Never invent a requirement, expected result, Pass, Fail, Blocked reason, bug, screenshot, execution result, evidence path, or GitHub Issue link.
- Treat ambiguities, assumptions, and contradictions explicitly. An observed contradiction does not silently replace an official requirement.
- Do not use implementation behaviour as the oracle. A public observation may become execution evidence or an observed contradiction, but documented expected behaviour comes from an approved test basis.
- Explain the complete derivation of every partition, boundary, and test case.
- Preserve initial AI output so human changes and gaps remain auditable.
- Encourage frequent, focused Git commits for every demonstrated step.
- Agent Skills are normally individual work; never assume another member's allocation or work.

## Phase 1: Feature Intake

Ask the user to select the feature; never select one automatically. Collect and record:

- Feature ID (`FR-01` or `D-01`) and feature name.
- Pool (`A`, `B`, `C`, or `D`).
- Actor and application surface.
- Requirement source.
- Public API endpoint or observable UI location.
- Output directory and execution environment.

Record the feature's supplied pool. Compare the selection with the official pool rule and warn if it appears inconsistent, but do not substitute a feature or assume another group member's allocation. Initialize the workspace with `scripts/create_feature_workspace.py`.

## Phase 2: Black-box Test Basis Collection

Collect rules only from approved bases: the official HW02 PDF, `README.md` requirements, `api_specification.md`, setup instructions, observable UI behaviour, observable public API requests/responses, user-visible messages, public application states, and real execution evidence. `run_servers.sh` may be read only for safe startup guidance.

For every rule, record:

- Rule ID and rule.
- Test basis type and Test Basis Reference.
- Observable expected behaviour.
- Ambiguity and assumption.

Use only these evidence classes: Official requirement, API specification, Observable UI behaviour, Observable API behaviour, Execution evidence, Assumption, Requirement ambiguity, and Observed contradiction.

## Phase 3: Domain Modeling

For every input, state, or condition, record:

- Variable or condition, type, and input source.
- Constraint.
- Valid and invalid partitions.
- Representative values.
- Dependencies.
- Test Basis Reference and assumptions.

Explain how every partition follows from a rule, specification, observable domain, or explicit assumption. Model relevant missing, empty, null, format, length, range, count, uniqueness, identity, actor, state, time, and cross-field partitions without forcing irrelevant categories.

## Phase 4: Boundary Value Analysis

Apply BVA only to ordered or bounded domains. For each boundary record Boundary ID, variable, rule, test basis, on point, off point, in point when relevant, selected values, expected classification, and justification.

Support lower-only, upper-only, inclusive-range, count, length, date, time, quantity, attempt, capacity, and ordered-state boundaries. Do not apply numeric BVA to unordered categories. Use only justified adjacent values; account for domain precision and whether the boundary is inclusive.

## Phase 5: Test-Case Derivation

Derive every case from identified partitions or boundaries. IDs are `<compact-feature>-DT-###` or `<compact-feature>-BVA-###`, for example `FR01-DT-001` and `D01-BVA-001`.

Every case must include:

- Test Case ID, Technique, Objective.
- Requirement or Rule Reference.
- Preconditions, Test Data, Steps, Expected Result.
- Actual Result, Status, Evidence.
- Partition or Boundary Covered.
- Test Basis Reference.
- Notes and Assumptions.

For each case, explain which rule produced the partition or boundary, why the chosen data represents it, and why the expected result is observable. Before genuine execution use exactly:

```text
Actual Result: Not Executed
Status: Not Executed
Evidence: None
```

## Phase 6: Human Review Gate

Stop before execution and require explicit user confirmation that a human reviewed the work. The reviewer verifies requirement accuracy, partition completeness, boundary correctness, concrete data, observable expected results, duplicate removal, technique classification, traceability, assumptions, and missing cases. Record corrections and review status. Do not mark reports final or execute tests while review is pending.

## Phase 7: Black-box Test Execution

Execute only when the user explicitly requests it, the environment is available, and human review is complete. Use only UI or public API interfaces. For each executed case record date/time, environment, Actual Result, status (`Pass`, `Fail`, or `Blocked`), and real evidence; include a blocking reason for `Blocked`. Never infer results from source inspection.

## Phase 8: Evidence and Bug Reporting

Save evidence as `reports/<FEATURE-ID>/evidence/<TEST-CASE-ID>.<extension>` and add it to `evidence/evidence-index.md` with Test Case ID, path, type, execution time, environment, and notes.

Report a bug only after reproducing an observable failure against a documented expected result. Record Bug ID, title, related case, requirement, preconditions, reproduction steps, expected and actual results, severity, evidence, GitHub Issue link, and status. Leave the Issue link explicitly pending until a real issue exists.

## Phase 9: AI Gap Analysis

Compare initial AI-generated tests, human corrections, human-added tests, behaviours or bugs missed by AI, runtime findings, and the reason for every gap. Do not claim AI missed a runtime bug before execution. Preserve generated output files for audit and append AI interactions with `scripts/append_ai_audit.py`.

## Phase 10: Final Validation and Output

Validate requirement, partition, and boundary coverage; execution metrics; evidence completeness; bug traceability; AI-gap completeness; and human-review status. Run `scripts/validate_test_cases.py` and correct every error.

The complete workspace is:

```text
reports/<FEATURE-ID>/
|-- requirement-analysis.md
|-- domain-testing.md
|-- boundary-value-analysis.md
|-- test-cases.md
|-- traceability-matrix.md
|-- execution-summary.md
|-- bug-report.md
|-- ai-gap-analysis.md
`-- evidence/
    `-- evidence-index.md
```

Demonstrate end-to-end use on one complete feature. A demonstration video may use voice-over or captions. More comprehensive, high-quality cases, real evidence, and confirmed bugs improve the assessment, but volume never permits fabrication.
