---
name: domain-testing
description: Apply course-aligned, black-box Domain Testing and Boundary Value Analysis to a selected software feature, design comprehensive and traceable test cases, execute approved cases against an available test environment, capture real evidence, and report design coverage and execution results. Use when an AI agent must perform an end-to-end feature testing workflow without inspecting implementation code or inventing requirements, expected behavior, execution results, or evidence.
---

# Domain Testing and Boundary Value Analysis

Perform an end-to-end black-box testing workflow for one selected feature. Follow the course materials for all technique definitions, procedures, notation, coverage rules, and value-selection conventions. Design Domain Testing and BVA cases separately, execute approved cases, and generate a report showing the work and evidence.

## Mandatory Rules

- Read the relevant course materials in `ref/` before applying either technique.
- Treat the course materials as authoritative over general knowledge and external sources.
- Cite course material by filename or title and page, slide, or section.
- Use only approved requirements, acceptance criteria, business rules, API/UI specifications, and other user-approved sources as the test basis.
- Do not invent limits, formats, dependencies, validation rules, expected messages, or system behavior.
- Record missing, ambiguous, and contradictory information instead of silently resolving it.
- Clearly label assumptions; do not treat unconfirmed assumptions as requirements or test oracles.
- Keep Domain Testing and BVA test cases separately identifiable.
- Add cases beyond minimum technique coverage only when needed for uncovered conditions, dependencies, combinations, or material risks.
- Let course coverage rules determine the number of cases; do not target an arbitrary count.
- Do not execute against production, use real payments, send real communications, or perform destructive operations unless the user explicitly authorizes them.
- Never fabricate an execution result, screenshot, log, request, response, issue, or evidence link.
- Do not change an expected result after execution merely to match actual behavior.
- Perform black-box testing only. Do not inspect or rely on implementation code, database schema, seed files, fixtures, migrations, route handlers, controllers, services, models, serializers, middleware, validators, hidden configuration, or internal constants to derive requirements, domains, boundaries, test data, expected results, or test oracles.
- Use source code only as an operational artifact when explicitly needed to start or operate the SUT, and only after recording why it is necessary. Operational inspection must not influence the test basis, domain model, BVA boundaries, or expected results.
- If a required rule, limit, format, dependency, boundary, expected message, or expected result is unavailable from approved black-box sources, record it as missing, ambiguous, or blocked. Do not recover it by reading implementation files.
- For each selected feature, create a real `.xlsx` workbook file containing the generated test cases. Do not provide test cases only as Markdown tables.
- If the agent cannot create the Excel file, mark the relevant phase `Blocked` and explain the blocker.

## Black-Box Source Policy

Use these sources as test basis:

- Course materials in `ref/`.
- User-approved requirements, acceptance criteria, business rules, UI/API specifications, and feature descriptions.
- Public UI behavior observed through normal user interaction.
- Public API documentation or API behavior observed through documented endpoints.
- User-approved test accounts, roles, states, and test data.

Use these sources only for operation, not as test basis:

- README, package scripts, environment setup notes, docker compose files, and startup commands.
- Existing generated reports, test-case files, and evidence folders.

Do not inspect these sources:

- Source code implementation files.
- Validation logic, controllers, services, models, serializers, middleware, and route handlers.
- Database schema, migrations, seed files, fixtures, and hidden test data.
- Internal constants, environment variables, private configuration, stack traces, and logs when used to infer hidden behavior.

If the SUT is already running at a user-provided URL, do not inspect the codebase for startup or configuration.

## Phase Tracking

Create and maintain this table at the beginning of the report:

`Phase | Name | Status | Required output | Blocker/notes`

Use only these phase statuses:

- `Not Started`
- `In Progress`
- `Blocked`
- `Completed`

Update the table whenever a phase starts, becomes blocked, or completes. Mark a phase `Completed` only after its completion conditions are satisfied. Do not mark later phases complete when an earlier required phase is blocked.

## Phase 0 - Initialize and Validate Inputs

### Actions

Obtain and inspect only allowed black-box and operational inputs:

1. Course materials for Domain Testing and BVA in `ref/`.
2. Feature ID, name, actor, and UI/API/mobile surface.
3. Approved feature requirements and business rules.
4. Preconditions, roles, states, dependencies, and available test data.
5. SUT location, startup instructions, test environment, and permitted tools.
6. Required report or test-case template, if provided.

Search the supplied workspace only for course materials, approved requirements, user-provided specifications, report templates, generated artifacts, and operational startup documents. Do not open implementation files or forbidden sources listed in the Black-Box Source Policy.

Before using any source, classify it as:

- `Test basis`: may be used to derive requirements, domains, boundaries, test data, and expected results.
- `Operational`: may be used only to run or operate the SUT.
- `Forbidden`: must not be inspected or used.

### Required Output

Create an Input Inventory:

`Input | Location/source | Available | Notes`

Create a Source Classification table:

`Source | Classification | Allowed use | Used? | Notes`

List blocking questions for missing information.

### Completion Conditions

- Relevant course materials are available.
- The selected feature and approved test basis are identifiable.
- The agent can distinguish the test environment from production.
- The agent has separated test-basis sources from operational and forbidden sources.

If course materials are missing, mark this phase `Blocked`, request them, and stop. Do not substitute a generic Domain Testing or BVA procedure.

## Phase 1 - Extract Course Technique Rules

### Actions

Read the relevant course materials and extract:

- Domain Testing concepts, procedure, notation, selection rules, and coverage criteria.
- BVA concepts, permitted domains, variants, value-selection rules, notation, and coverage criteria.
- Required intermediate artifacts and test-case format.

If several BVA variants are defined, identify the assignment-required variant. If it cannot be determined, record the ambiguity and request clarification before finalizing BVA cases.

### Required Output

Create and include a Course Technique Rules table:

`Course Ref | Technique | Rule/convention | Application in this feature`

### Completion Conditions

- Every technique rule that will be applied has a course reference.
- The required Domain Testing procedure and BVA variant are known.
- No external convention has silently replaced the course rules.

## Phase 2 - Establish Feature Scope and Test Basis

### Actions

Define:

- Included feature behavior.
- Actor, entry point, and interface.
- Preconditions and dependent system states.
- Inputs, outputs, and observable side effects.
- Explicit exclusions.

Separate specified behavior and approved public observations from implementation details. Do not use implementation observations or forbidden sources as test basis.

### Required Output

Create a Test Basis table:

`Basis ID | Source | Location | Requirement/rule | Ambiguity or contradiction`

Assign a stable `Basis ID` to every rule used for a test input, expected result, domain, or boundary.

Do not assign a `Basis ID` to implementation code, database content, seed data, hidden configuration, logs, or other forbidden sources.

Create an Issues and Assumptions table:

`Item ID | Type | Description | Impact | Status`

Use `Missing information`, `Ambiguity`, `Contradiction`, or `Assumption` as the type.

### Completion Conditions

- Scope, actor, interface, and exclusions are explicit.
- Every usable test rule has a `Basis ID`.
- Issues that prevent a reliable oracle are resolved or marked as blockers.
- No test-basis rule is derived from implementation code or forbidden sources.

## Phase 3 - Design Domain Testing Cases

### Actions

1. Apply the Domain Testing procedure from the course materials exactly.
2. Identify the feature elements, domains, constraints, dependencies, and intermediate artifacts required by that procedure.
3. Derive test inputs and expected behavior from the approved test basis.
4. Select test cases according to the course coverage criteria.
5. Add cases only when coverage analysis identifies an uncovered domain, interaction, constraint, state, or required condition.
6. Preserve the terminology, notation, and naming rules used by the course.

Do not introduce partition types, representative-value rules, combination strategies, or coverage criteria that are unsupported by the course materials.

### Required Output

Produce every Domain Testing artifact required by the course materials.

Use the course test-case format when one is specified. Otherwise use:

`Test Case ID | Technique | Title | Objective | Basis ID | Technique reference | Preconditions | Test data | Steps | Expected result | Coverage type | Status`

Use `Domain Testing` as the technique, `Technique minimum` or `Additional coverage` as the coverage type, and `Not Executed` as the initial status.

Create a Domain Testing Coverage Matrix using the course coverage items. If the course provides no table format, use:

`Coverage item | Course rule | Test Case IDs | Covered | Gap justification`

Append all Domain Testing test cases to the feature `.xlsx` workbook in the `Domain Testing Cases` sheet.

Write a feature-specific explanation covering:

1. Course rules applied.
2. Feature analysis performed.
3. Derivation of domains, test data, and expected results.
4. Test-case selection process.
5. Coverage verification.
6. Reasons for additional cases.
7. Remaining ambiguities, exclusions, and risks.

### Completion Conditions

- All required course artifacts are present.
- Every Domain Testing case traces to the course rules and test basis.
- Required coverage is complete or each gap is justified.
- The explanation describes the actual feature analysis, not generic theory.

## Phase 4 - Design Boundary Value Analysis Cases

### Actions

1. Apply the BVA procedure and variant required by the course materials.
2. Identify only domains that are eligible for BVA under those materials.
3. Derive boundaries, positions, adjacent values, units, and precision exactly as the selected variant requires.
4. Derive expected behavior from the approved test basis.
5. Keep non-target variables at justified nominal values unless the course procedure or a relational boundary requires otherwise.
6. Add cases only when coverage analysis identifies an uncovered boundary, position, relation, or required condition.

Do not introduce `min-1`, `max+1`, below/on/above positions, robustness variants, or a fixed number of values unless supported by the course materials and the data type.

### Required Output

Produce every BVA artifact required by the course materials.

Use the course test-case format when one is specified. Otherwise use:

`Test Case ID | Technique | Title | Objective | Basis ID | Boundary reference | Preconditions | Test data | Steps | Expected result | Coverage type | Status`

Use `BVA` as the technique, `Technique minimum` or `Additional coverage` as the coverage type, and `Not Executed` as the initial status.

Create a BVA Coverage Matrix using the course coverage items. If the course provides no table format, use:

`Coverage item | Course rule | Test Case IDs | Covered | Gap justification`

Append all BVA test cases to the same feature `.xlsx` workbook in the `BVA Cases` sheet.

Write a feature-specific explanation covering:

1. Course rules and BVA variant applied.
2. Selection of eligible domains.
3. Derivation of boundaries, positions, units, and precision.
4. Calculation of concrete test values.
5. Control of nominal values and dependencies.
6. Test-case selection and coverage verification.
7. Reasons for additional cases.
8. Infeasible values, ambiguities, exclusions, and risks.

### Completion Conditions

- All required course BVA artifacts are present.
- Every BVA case traces to a course rule, boundary, and test basis.
- Required boundary coverage is complete or each gap is justified.
- The explanation describes the actual feature analysis, not generic theory.

## Phase 5 - Review and Prepare Test Execution

### Actions

1. Review Domain Testing and BVA cases for correctness, duplication, traceability, concrete data, and observable expected results.
2. Confirm the SUT build/version, base URL or app build, environment, accounts, roles, dependencies, and reset mechanism using black-box or operational sources only.
3. Map each case to an execution method such as API request, test script, browser/UI interaction, mobile interaction, or manual-only action.
4. Prepare non-production test data and restore or cleanup steps.
5. Confirm evidence methods: screenshot for UI, request/response log for API, and command output or test report for scripts.
6. Record any case that the available tools cannot execute.

Do not use unavailable credentials, bypass authorization controls, or execute manual-only actions by pretending they occurred.

Do not inspect implementation code during execution setup unless the SUT cannot be operated from the user-provided URL, documentation, or approved startup instructions. If operational inspection is unavoidable, record the inspected file, reason, and confirmation that it was not used as test basis.

### Required Output

Create an Execution Readiness table:

`Test Case ID | Execution method | Environment/data ready | Evidence method | Cleanup/reset | Ready | Blocker`

Create the review gate:

```markdown
## Execution Approval

- Reviewer:
- Review date/time:
- Course alignment verified: Yes/No
- Test basis and expected results verified: Yes/No
- Test data and environment verified: Yes/No
- Approved for execution: Yes/No
```

The agent must not self-approve this gate. An explicit user instruction to execute already reviewed cases may serve as approval only when the approved cases and environment are unambiguous; record that instruction as the approval source.

### Completion Conditions

- Each test case has an execution and evidence method or a documented blocker.
- The environment is confirmed as safe for testing.
- `Approved for execution` is `Yes`.

If approval is absent, mark the phase `Blocked` and do not execute.

## Phase 6 - Execute Test Cases and Capture Evidence

### Actions

For each ready and approved test case:

1. Record the execution timestamp, SUT build/version, environment, and executor.
2. Establish the stated preconditions and reset the SUT when required.
3. Use the exact approved test data and steps.
4. Observe and record the actual result without altering the expected result.
5. Capture genuine evidence with a stable file path or link.
6. Assign the execution status using the definitions below.
7. Perform cleanup or state reset before the next case when required.

Use these statuses:

- `Passed`: actual result matches the approved expected result.
- `Failed`: actual result contradicts the approved expected result.
- `Blocked`: execution cannot complete because of environment, dependency, access, or tooling problems.
- `Not Executed`: execution has not been attempted.

Continue after a failed case when it is safe and later cases do not depend on the failed state. Do not classify an environment problem as a product failure.

### Required Output

Create an Execution Results table:

`Execution ID | Test Case ID | Date/time | Environment/build | Actual test data | Actual result | Status | Evidence | Executor | Notes`

Store evidence using stable names that include the feature ID, test case ID, and evidence type. Redact secrets, tokens, and personal data.

### Completion Conditions

- Every ready approved case was attempted.
- Every attempted case has an actual result, status, and genuine evidence.
- Every unexecuted or blocked case has a reason.
- Required cleanup was completed or recorded as a blocker.

## Phase 7 - Validate and Summarize Execution Results

### Actions

1. Reconcile each execution record with its test case and evidence.
2. Reproduce failed cases when feasible and safe to distinguish repeatable failures from flaky behavior or environment problems.
3. Do not automatically call every failed test a confirmed bug; label it a defect candidate until its oracle, reproducibility, and evidence are reviewed.
4. Calculate summary counts from the detailed tables rather than entering them manually without verification.
5. Identify coverage items that remain unexecuted because of blockers.

### Required Output

Create an Execution Summary:

`Designed | Executed | Passed | Failed | Blocked | Not Executed | Pass rate`

Calculate:

- `Executed = Passed + Failed`.
- `Designed = Passed + Failed + Blocked + Not Executed`.
- `Pass rate = Passed / Executed * 100`, or `N/A` when `Executed = 0`.

Create an Evidence Index:

`Test Case ID | Status | Evidence path/link | Evidence type | Verified`

Create a Defect Candidate list when failures exist:

`Candidate ID | Test Case ID | Expected | Actual | Reproducible | Evidence | Review status`

### Completion Conditions

- Summary counts reconcile with individual test cases.
- Evidence references resolve.
- Failed, blocked, and unexecuted cases are clearly distinguished.
- Defect candidates are not misrepresented as confirmed bugs.

## Phase 8 - Finalize the Report

### Required Report Structure

Produce one Markdown report per feature:

1. Phase Tracking
2. Input Inventory
3. Feature Scope
4. Applied Course Rules
5. Test Basis
6. Issues and Assumptions
7. Domain Testing
   - Course-required intermediate artifacts
   - Test cases
   - Coverage matrix
   - Detailed step-by-step explanation
8. Boundary Value Analysis
   - Course-required intermediate artifacts
   - Test cases
   - Coverage matrix
   - Detailed step-by-step explanation
9. Execution Readiness and Approval
10. Execution Results
11. Execution Summary
12. Evidence Index
13. Defect Candidates
14. Traceability Summary
15. Limitations, Blockers, and Residual Risks

### Final Quality Check

Verify:

- Relevant course materials were read and cited.
- Every applied technique rule matches the course materials.
- Every test case and expected result traces to an approved test basis.
- Domain Testing and BVA coverage is complete or justified.
- Domain Testing and BVA remain separately identifiable.
- Test data is concrete and expected results are observable.
- The work followed black-box testing rules, and no requirement, domain, boundary, expected result, or oracle was derived from implementation code or forbidden sources.
- Execution occurred only after approval and only in an authorized test environment.
- Actual results, statuses, and evidence are genuine and consistent.
- Summary counts reconcile with the detailed records.
- Additional cases are labeled and justified.
- All IDs, references, evidence paths, and links resolve.
- The feature `.xlsx` workbook exists on disk and contains all Domain Testing and BVA test cases.

### Completion Conditions

- Phases 0 through 8 are `Completed`, or blockers are explicitly documented.
- The report contains every required design and execution artifact.
- No requirement, approval, execution result, evidence, or bug has been fabricated.

If any required condition is unmet, keep the relevant phase `Blocked` or `In Progress`, list the open item, and do not describe the work as final.
