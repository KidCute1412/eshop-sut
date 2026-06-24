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
- Use `references/human-review-checklist.md` in Phase 6 before any test execution.
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

## Phase 5: AI Test-Case Generation

The AI derives test cases from the approved partitions and boundaries. IDs are `<compact-feature>-DT-###` or `<compact-feature>-BVA-###`, for example `FR01-DT-001` and `D01-BVA-001`.

Every case must include:

- Test Case ID, Technique, and Objective.
- Requirement or Rule Reference.
- Preconditions, Test Data, Steps, and Expected Result.
- Actual Result, Status, and Evidence.
- Test Basis Reference.

Keep DT and BVA cases separate. Remove unjustified duplication, but do not omit distinct partitions, boundaries, surfaces, or dependency conditions merely to reduce the number of cases.

The AI must not execute tests in this phase. Before genuine execution, write exactly:

```text
Actual Result: Not Executed
Status: Not Executed
Evidence: None
```

Preserve the initial prompt and AI-generated output before any human correction. Stop after generating the cases and request human review.

## Phase 6: Human Review and Black-box Test Execution

This phase requires human control and explicit confirmation. The AI may assist with execution, recording, formatting, and validation, but it must not approve its own test cases or fabricate observations.

### Step 1: Human Review

The human reviewer uses `references/human-review-checklist.md` to verify:

- Feature scope, requirements, and test bases are correct.
- Valid and invalid partitions are complete and correctly represented.
- BVA is applied only to ordered or bounded domains.
- Boundary values and adjacent values are correct.
- Preconditions and test data are concrete and reproducible.
- Expected results are observable and supported by an approved test basis.
- DT and BVA classifications are correct.
- Duplicate or unjustified cases are removed.
- Missing cases and dependency conditions are added.
- Assumptions, ambiguities, and contradictions are explicit.
- No result, evidence, screenshot, bug, or Issue link is fabricated.

Record in `test-cases.md` or the AI Audit:

- Reviewer and review date/time.
- Review scope.
- Human corrections.
- Human-added, removed, or reclassified cases.
- Duplicate-case decisions.
- `Approved for Test Execution: Yes/No`.

Do not execute tests while approval is `No` or missing.

### Step 2: Black-box Test Execution

After human approval, execute each case through only the public UI or public API. The human may execute manually or explicitly supervise AI-assisted browser/API execution.

For every attempted case, record:

- Execution date and time.
- Environment.
- Actual Result.
- Status: `Pass`, `Fail`, or `Blocked`.
- Blocking Reason when status is `Blocked`.
- Real evidence reference.

Determine the status as follows:

- `Pass`: the observable actual result matches the documented expected result.
- `Fail`: the observable actual result contradicts the documented expected result.
- `Blocked`: execution cannot reach the intended observation because a real precondition, environment, dependency, or product condition prevents it.

Do not infer results from source inspection. A result is not final until its evidence is captured and human-verified in Phase 7.

## Phase 7: Human-verified Evidence and Bug Reporting

This phase requires human verification. The AI may assist with capturing, organizing, naming, linking, and summarizing evidence, but the human must confirm that every evidence file represents the actual observed execution result.

Capture evidence during or immediately after each test execution while the observable result is still available. Save it under:

`reports/<FEATURE-ID>/evidence/<TEST-CASE-ID>.<extension>`

Evidence requirements:

- UI evidence shows the relevant input, displayed result, error, navigation, state, or blocking condition.
- API evidence shows the method, URL, request body, status code, and response body.
- Blocked evidence clearly demonstrates the real blocking condition.
- Evidence belongs to the exact test case and execution being reported.
- Evidence does not expose unnecessary secrets or personal information.

After human verification, update the corresponding case with the real evidence path. Do not leave a `Pass`, `Fail`, or `Blocked` case with `Evidence: None`.

### Bug Reporting

Create a bug report only when:

1. The test has a documented expected result.
2. The observable actual result contradicts it.
3. The failure has been reproduced.
4. Human-verified evidence exists.

For every confirmed bug, record:

- Bug ID, title, severity, and status.
- Related test case and requirement.
- Preconditions and reproduction steps.
- Expected and actual results.
- Evidence links.
- GitHub Issue link.

Create the bug on the group's GitHub Issues page and attach the relevant screenshots. Leave the Issue link as `Pending` until a real issue exists, then replace it with the actual link. Do not create separate bug records for identical failures unless they have materially different causes or observable impacts.

## Phase 8: AI Gap Analysis

Create `reports/<FEATURE-ID>/ai-gap-analysis.md`.

Compare:

- Initial AI-generated partitions, boundaries, and test cases.
- Human corrections and reclassifications.
- Human-added or removed test cases.
- Incorrect, incomplete, or unsupported AI assumptions.
- Behaviours and bugs discovered during execution.
- Important cases or bugs missed by the AI.
- The reason for every identified gap.

For each gap, record:

- Gap ID and category.
- Initial AI output.
- Human correction or runtime finding.
- Why the AI missed or mishandled it.
- Corrective action.
- Related requirement, partition, boundary, test case, evidence, or bug.

Distinguish prompt-quality gaps, AI reasoning limitations, missing test-basis information, application complexity, and findings that were knowable only through execution. Do not claim the AI missed a runtime bug before that bug was actually observed.

Preserve the original AI output and append the relevant interactions to the AI Audit with `scripts/append_ai_audit.py`. Human review is required before the AI gap analysis is final.

## Phase 9: Traceability and Final Validation

Create `reports/<FEATURE-ID>/traceability-matrix.md`.

Trace:

- Requirement or rule to partition.
- Partition to Domain Testing test case.
- Requirement or rule to boundary.
- Boundary to BVA test case.
- Test case to execution status and evidence.
- Failed test case to Bug ID and GitHub Issue.
- Explicit gaps, ambiguities, and exclusions.

Validate:

- Every relevant requirement has coverage or an explicit justified gap.
- Every selected partition and boundary maps to at least one appropriate case.
- Test data, expected results, and technique classifications are correct.
- Execution statuses and evidence links are complete and consistent.
- Blocked cases contain real blocking reasons and evidence.
- Confirmed bugs are reproducible and traceable to failed cases.
- AI-gap entries are supported by preserved AI output and human corrections.
- Human-review approval is recorded.
- All internal links resolve.

Run:

`python .agents/skills/domain-testing-bva/scripts/validate_test_cases.py reports/<FEATURE-ID>/test-cases.md`

Correct every validation error before finalizing. Record feature-level metrics in the assignment's final `README.md`; do not require a separate per-feature execution-summary file.

The complete feature workspace is:

```text
reports/<FEATURE-ID>/
|-- requirement-analysis.md
|-- domain-testing.md
|-- boundary-value-analysis.md
|-- test-cases.md
|-- traceability-matrix.md
|-- bug-report.md
|-- ai-gap-analysis.md
`-- evidence/
    |-- <TEST-CASE-ID>.png
    `-- <other-real-evidence-files>
```

Demonstrate end-to-end use on one complete feature. A demonstration video may use voice-over or captions. More comprehensive, high-quality cases, real evidence, and confirmed bugs improve the assessment, but volume never permits fabrication.
