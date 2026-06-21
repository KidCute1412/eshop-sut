---
name: domain-testing-bva
description: Guides an AI testing agent through auditable Domain Testing and Boundary Value Analysis for EShop or similar software features. Use when asked to analyze requirements, inspect frontend/backend/API/database evidence, design DT/BVA test cases, create traceability, identify AI gaps, prepare assignment-ready Markdown reports, or validate test-case reports without fabricating execution results.
---

# Domain Testing and BVA

Use this skill to design auditable Domain Testing and Boundary Value Analysis (BVA) reports for one feature at a time. Keep feature-specific results out of this skill folder; write them to the requested output directory.

## Load When Needed

- Read `references/assignment-requirements.md` before preparing HW02 submission material.
- Read `references/eshop-analysis-guide.md` before inspecting this EShop repository.
- Read `references/domain-testing-method.md` for equivalence partitioning details.
- Read `references/bva-method.md` for boundary selection rules.
- Read `references/test-case-schema.md` before writing or validating test cases.
- Read `references/human-review-checklist.md` before finalizing reports.
- Use templates from `assets/` to initialize or format report files.
- Use scripts in `scripts/` for workspace creation, test-case validation, and AI audit entries.

## Input Contract

Collect or discover:

- Feature ID, feature name, pool, user role, application module, and requirement source.
- Repository root and output directory.
- Frontend paths, backend paths, API endpoints, database models and constraints.
- Authentication or authorization role.
- Preconditions, existing test data, and testing environment if execution is requested.

Default EShop mapping:

| Area | Path |
| --- | --- |
| Backend | `backend/` |
| Admin frontend | `frontend-admin/` |
| Mobile frontend | `frontend-mobile/` |
| User web frontend | `frontend-web/` |
| API specification | `api_specification.md` |
| Setup instructions | `setup_guide.md` |
| Server script | `run_servers.sh` |

If information is missing, search the repository, record what is missing, ask the user only when correctness materially depends on the answer, and mark temporary conclusions as assumptions. Never invent a requirement.

## Phase 1: Feature Intake

1. Confirm the feature ID, feature name, pool, user role, and application module.
2. Locate the feature in the assignment, requirement documents, API specification, UI, backend, and database.
3. Create a feature workspace:
   `python .agents/skills/domain-testing-bva/scripts/create_feature_workspace.py --feature-id <FR-ID> --feature-name "<name>" --pool <pool> --output <output-dir>`
4. Record unknown, contradictory, or inconsistent information.
5. If the selected feature allocation conflicts with the assignment selection rule, document the inconsistency instead of choosing an unassigned feature.

## Phase 2: Evidence Collection

Inspect, when applicable:

- UI forms, input widgets, client-side validation, labels, messages, and state changes.
- API request and response schemas.
- Backend routes, controllers, middleware, services, DTO-like logic, and validation code.
- Database schema, seed data, indexes, defaults, uniqueness, and foreign-key behavior.
- Authentication, authorization, roles, tokens, and protected routes.
- State transitions, temporal rules, business calculations, and error messages.
- Existing tests and test commands.

For every rule, record the source file plus symbol, route, section, or line reference. Separate these evidence classes:

- Documented requirement
- API specification
- Implemented frontend behavior
- Implemented backend behavior
- Database enforcement
- Assumption
- Contradiction

Do not mark source-inspection findings as executed test results.

## Phase 3: Domain Modeling

For every input, state, or condition, record:

- Variable name, data type, and input source.
- Constraints and business rules.
- Valid and invalid equivalence partitions.
- Dependencies and cross-field interactions.
- Evidence source and assumptions.

Consider only categories relevant to the selected feature: missing, empty, null, format, length, numeric range, collection size, duplicate, existing/non-existing entity, authentication state, authorization role, resource state, temporal condition, and state transition.

Do not treat fields as independent when the requirement creates a dependency, such as password confirmation, coupon eligibility, lockout attempt count, or order-state transition.

## Phase 4: Boundary Value Analysis

Apply BVA only to ordered or bounded domains. Use `min-1`, `min`, `min+1`, nominal, `max-1`, `max`, and `max+1` where justified by the rule.

Also consider:

- Empty, one, many for collections.
- Zero, one, capacity-1, capacity, capacity+1 for quantities and limits.
- Date/time boundaries, expiration boundaries, lockout attempt boundaries, stock/quantity boundaries, string-length boundaries, and state-transition boundaries.

Do not mechanically apply numeric BVA to unordered categories such as roles, coupon type names, or order statuses. For every boundary, record variable, rule, source, test values, expected classification, and justification.

## Phase 5: Test-Case Design

Generate separate Domain Testing and BVA cases. Use IDs:

- `FR01-DT-001`
- `FR01-BVA-001`

Each test case must include:

- Test Case ID
- Technique
- Objective
- Requirement or Rule Reference
- Preconditions
- Test Data
- Steps
- Expected Result
- Actual Result
- Status
- Evidence
- Partition or Boundary Covered
- Source Code Reference
- Notes and Assumptions

Until a test is genuinely executed, write exactly:

- `Actual Result: Not Executed`
- `Status: Not Executed`
- `Evidence: None`

Never infer Pass or Fail from source inspection alone.

## Phase 6: Quality Review

Before finalizing, verify:

- Every relevant requirement has coverage or an explicit gap.
- Valid partitions, invalid partitions, and applicable boundaries are covered or justified.
- Expected results are observable, preconditions reproducible, and test data concrete.
- Unjustified duplicate tests are removed.
- DT and BVA cases are correctly classified.
- Security tests are not mislabeled as Domain Testing unless they are input-domain tests.
- Requirement, code, partition, boundary, and test traceability exists.
- Assumptions and contradictions are visible.
- No result, screenshot, bug, or evidence is fabricated.
- Human review is explicitly required.

Run:

`python .agents/skills/domain-testing-bva/scripts/validate_test_cases.py <feature-report-dir>`

Fix all validation errors before submission.

## Phase 7: Output

For each feature, produce:

```text
reports/<FEATURE-ID>/
├── requirement-analysis.md
├── domain-testing.md
├── boundary-value-analysis.md
├── test-cases.md
├── traceability-matrix.md
├── ai-gap-analysis.md
└── evidence/
```

Append AI usage with:

`python .agents/skills/domain-testing-bva/scripts/append_ai_audit.py --audit-file ai-audit/agent-skill-creation.md --ai-tool "<tool>" --task "<task>" --feature-id <FR-ID> --prompt-file <file> --output-refs "<files>" --human-review "Pending" --human-corrections "None yet"`
