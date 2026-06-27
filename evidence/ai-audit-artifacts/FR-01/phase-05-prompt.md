# Use `domain-testing-bva` Skill for FR-01 Phase 5

Use the `domain-testing-bva` skill to perform **Phase 5: Test-Case Design** for **FR-01 Account Registration**.

## Project Information

- Project root: current repository
- Feature ID: FR-01
- Feature name: Account Registration
- Pool: A
- Actor: Guest / unauthenticated user
- Surfaces: User Web UI and public Registration API

## Approval Gates

Before creating any test case, verify:

### Phase 3 gate

Read:

`reports/FR-01/domain-testing.md`

It must contain:

- `Status: Completed`
- `Approved for BVA: Yes`

### Phase 4 gate

Read:

`reports/FR-01/boundary-value-analysis.md`

It must contain:

- `Status: Completed`
- `Approved for Test-Case Derivation: Yes`

If either gate is missing, incomplete, or set to `No`, stop without modifying files and report the missing approval.

## Required Sources

Read only the following test-design sources:

- `.agents/skills/domain-testing-bva/SKILL.md`
- `.agents/skills/domain-testing-bva/references/domain-testing-method.md`
- `.agents/skills/domain-testing-bva/references/bva-method.md`
- `.agents/skills/domain-testing-bva/references/test-case-schema.md`
- `.agents/skills/domain-testing-bva/references/human-review-checklist.md`
- `.agents/skills/domain-testing-bva/references/instructor-clarifications.md`
- `.agents/skills/domain-testing-bva/assets/test-case-template.md`
- `reports/FR-01/requirement-analysis.md`
- `reports/FR-01/domain-testing.md`
- `reports/FR-01/boundary-value-analysis.md`

Treat the three reviewed reports as the approved Black-box test basis.

## Prohibited Sources and Actions

Do not:

- Inspect frontend or backend implementation source.
- Inspect controllers, routes, services, middleware, models, database schemas, seed data, or internal tests.
- Start the application or servers.
- Make HTTP requests.
- Execute any test case.
- Create screenshots or runtime evidence.
- Record Pass, Fail, Blocked, bugs, defects, or GitHub Issues.
- Invent requirements, endpoints, URLs, messages, status codes, limits, or validation behaviour.
- Modify Phase 1, Phase 2, Phase 3, or Phase 4 reports.
- Create the final traceability matrix, execution summary, AI gap analysis, or bug report.
- Update the AI Audit.
- Create Git commits.

## Phase 5 Objective

Create auditable and executable test cases derived directly from the approved Domain Testing partitions and BVA boundaries.

Produce separate:

- Domain Testing cases with IDs `FR01-DT-001`, `FR01-DT-002`, and so on.
- Boundary Value Analysis cases with IDs `FR01-BVA-001`, `FR01-BVA-002`, and so on.

Do not target an arbitrary test-case count. Create enough distinct cases to cover every approved normative partition, applicable boundary, surface-specific behaviour, and shared-form rule without unjustified duplication.

## Step 1: Establish Test Data and Preconditions

Define concrete reusable test data, including:

- A normal full name such as `Nguyen Van A`.
- A valid unused email such as `new.user@example.com`.
- A controlled existing email such as `registered@example.com`.
- A nominal valid password such as `ValidPass1!`.
- Matching Confirm Password value for UI cases.
- Guest or unauthenticated actor state.
- Registration UI location from the approved report.
- Registration API endpoint and base URL from the approved report.

Do not assume an email is unused or existing without stating it as a controlled precondition.

If an exact UI location, API endpoint, or observable result is missing from the approved reports, record a design gap instead of inventing it.

## Step 2: Design Domain Testing Cases

Create cases covering the approved normative Domain Testing model.

### Coverage rules

- Use nominal valid UI and API cases to cover compatible valid partitions.
- Create isolated invalid cases where one relevant condition is invalid and unrelated variables remain nominal.
- Separate UI and API cases when their steps, inputs, or observable outcomes differ.
- Do not combine multiple unrelated invalid inputs in one test unless testing their interaction is explicitly justified.
- Map every case to exact partition IDs and Rule IDs.
- Ensure every normative partition is either covered by a test case or listed as an explicit justified gap.
- Remove unjustified duplicate cases.

Cover, where supported by the approved reports:

- Full-name presence.
- Email presence.
- Email format.
- Email uniqueness.
- Password presence.
- Password uppercase requirement.
- Password lowercase requirement.
- Password digit requirement.
- Password special-character requirement.
- Confirm Password control presence.
- Confirm Password value presence.
- Password and confirmation equality.
- Complete valid UI registration.
- Complete valid API request.
- Missing API request properties.
- Documented successful API response.
- Required-field markers.
- Email input type.
- Password input type and masking.
- Error placement.
- Successful redirect to Login.
- Guest actor precondition.
- Validation rejection.

For UI conformance rules, the expected result must describe the compliant UI. Do not create a test that requires forcing the implementation into an invalid UI state. Record the invalid output partition as the possible non-conforming observation that would cause the case to fail during later execution.

### Ambiguous candidates

Do not convert the following ambiguous candidates into normative Pass/Fail test cases:

- Whitespace-only full name.
- Email case-normalization behaviour.
- Unlisted password special characters.
- Conditional registration step indicator.

List them in an `Exploratory Backlog` section with:

- Candidate ID
- Input or observation
- Missing oracle
- Clarification required
- Reason excluded from normative coverage

## Step 3: Design BVA Cases

Use the approved password-length boundary model.

Create separate UI and API cases for each value because the interaction steps and observable interfaces differ.

### UI BVA cases

Create one UI case for each:

- 7 characters: `Abcd1!x`, Invalid, `min-1`
- 8 characters: `Abcd1!xy`, Valid, `min`
- 9 characters: `Abcd1!xyz`, Valid, `min+1`
- 11 characters: `ValidPass1!`, Valid nominal

For every UI case:

- Use nominal name and unique email.
- Enter the selected password.
- Enter the identical value in Confirm Password.
- Keep all other password character-class conditions valid.
- State that execution depends on the Confirm Password control being available.

### API BVA cases

Create one API case for each:

- 7 characters: `Abcd1!x`, Invalid, `min-1`
- 8 characters: `Abcd1!xy`, Valid, `min`
- 9 characters: `Abcd1!xyz`, Valid, `min+1`
- 11 characters: `ValidPass1!`, Valid nominal

For every API case:

- Use a complete request body containing approved `name`, `email`, and `password` properties.
- Do not add Confirm Password to the API request unless it exists in the approved API contract.
- Use the approved API endpoint and base URL.
- Do not invent exact invalid HTTP status codes or response bodies.
- Use only the approved observable rejection or success oracle.

This should produce eight distinct BVA cases when both UI and API surfaces are supported by the reviewed reports.

## Required Test-Case Fields

Every test case must contain:

- Test Case ID
- Feature ID
- Test Case Title
- Technique
- Objective
- Requirement or Rule Reference
- Test Basis Reference
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

For Black-box cases, write:

```text
Source Code Reference: Not Applicable - Black-box testing
```

Until genuine execution occurs, write exactly:

```text
Actual Result: Not Executed
Status: Not Executed
Evidence: None
```

Do not use synonyms such as `Pending`, `TBD`, `Not Run`, or `To Be Executed`.

## Test-Case Quality Rules

Every case must:

- Have one clear objective.
- Contain concrete test data.
- Have numbered and reproducible steps.
- Keep unrelated inputs nominal.
- Include an observable expected result.
- Reference exact Rule IDs.
- Reference exact partition or boundary IDs.
- Identify whether it applies to UI or API.
- Avoid undocumented error messages and status codes.
- Avoid implementation details.
- Avoid fabricated execution results.
- Be independently understandable.

For an invalid API case where the exact error status or body is undocumented, state only the approved rejection oracle and explicitly note that the exact status and response body require clarification.

## Coverage Summary

Include a preliminary coverage table containing:

- Rule ID
- Partition or Boundary ID
- Technique
- Covering Test Case ID
- Surface
- Coverage Status
- Notes

Use only:

- `Covered`
- `Justified Gap`
- `Exploratory - No Oracle`

Verify that:

- Every normative Domain Testing partition is covered or justified.
- Every approved BVA value is covered on every applicable surface.
- Ambiguous candidates are not counted as normative coverage.
- A valid nominal case does not hide missing invalid coverage.
- Duplicate cases are removed or explicitly justified.

This table is a Phase 5 design-coverage summary, not the final Phase 6 traceability matrix.

## Required Report Structure

Create:

`reports/FR-01/test-cases.md`

Use this structure:

1. Title
2. Black-box Test Basis and Approval Summary
3. Test Design Strategy
4. Shared Preconditions and Test Data
5. Domain Testing Test Cases
6. Boundary Value Analysis Test Cases
7. Exploratory Backlog
8. Preliminary Coverage Summary
9. Design Gaps and Assumptions
10. Human Review - Phase 5

End with:

```markdown
## Human Review - Phase 5

- Reviewer:
- Review Date and Time:
- Corrections Made:
- Missing Cases Added:
- Duplicate Cases Removed:
- Incorrect Cases Removed:
- Status: Pending
- Approved for Validation: No
- Approved for Traceability and Quality Review: No
- Approved for Test Execution: No
```

## Raw AI Output

Save an unchanged copy of the initial generated report at:

`evidence/agent-skill/FR-01/phase-05-test-case-design-ai-output.md`

The initial contents of this raw AI output and `reports/FR-01/test-cases.md` must be identical.

Do not modify the raw AI output during later Human Review. Apply Human Review corrections only to the official report.

## Completion Checks

Before finishing, verify:

- Approval gates passed.
- DT and BVA IDs are unique and sequential.
- UI and API cases are not mixed into a single execution procedure.
- Every normative partition is covered or justified.
- All eight surface-specific BVA cases exist when both surfaces apply.
- Each case contains every required field.
- All unexecuted fields use the exact required values.
- No test has Pass, Fail, runtime evidence, screenshot, bug, or Issue link.
- No exact invalid API status or message is invented.
- Human Review remains Pending.
- Only the two requested files are created or modified.
