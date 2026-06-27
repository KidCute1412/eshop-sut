Use the `domain-testing-bva` skill for FR-01 Account Registration.

Phase 1 and Phase 2 have been human-reviewed and approved for Domain Modeling.

## Objective

Perform only:

- Phase 3: Domain Modeling

This phase should follow the Domain Testing slide style:

1. Identify Input & Output variables.
2. Identify equivalence classes for each input and output.
3. Find a best representative for each equivalence class.

Do not perform Step 4 / Boundary Value Analysis yet. Boundary values are reserved for Phase 4.

Do not generate test cases, execute tests, capture evidence, infer bugs, or report bugs.

## Precondition Check

Before starting, read:

```text
reports/FR-01/requirement-analysis.md
```

Verify that the file contains human review approval for Phase 3:

- Status: Completed
- Approved for Domain Modeling: Yes
- Approved for Test Execution: No

If Phase 1 and Phase 2 are not approved for Domain Modeling, stop and report that Phase 3 is blocked.

## Input

Use only the approved Black-box rules, API specifications, ambiguities, assumptions, and coverage gaps recorded in:

```text
reports/FR-01/requirement-analysis.md
```

Do not inspect:

- Application implementation source code
- Frontend implementation source
- Backend implementation source
- Database schema or records
- Controllers, services, routes, middleware, or models
- Internal implementation tests

Do not derive expected results from implementation behaviour.

## Files to Create or Update

Create or update only these files:

```text
reports/FR-01/domain-testing.md
evidence/agent-skill/FR-01/phase-03-domain-modeling-prompt.md
evidence/agent-skill/FR-01/phase-03-domain-modeling-ai-output.md
ai-audit/ai-audit.md
```

Do not modify application source code.

## Required Report

Create or update:

```text
reports/FR-01/domain-testing.md
```

Use this structure:

```markdown
# Domain Testing - FR-01 Account Registration

## Black-box Test Basis Summary

## Step 1. Identify Input & Output Variables

## Step 2. Identify Equivalence Classes

## Step 3. Best Representatives

## Partition Derivation

## Coverage Decisions

## Human Review - Phase 3

- Reviewer:
- Review Date and Time:
- Corrections Made:
- Missing Partitions Added:
- Duplicate Partitions Removed:
- Status: Pending
- Approved for BVA: No
- Approved for Test-Case Derivation: No
- Approved for Test Execution: No
```

## Black-box Test Basis Summary

In `## Black-box Test Basis Summary`, briefly state:

- The analysis is based only on `reports/FR-01/requirement-analysis.md`.
- Phase 1 and Phase 2 were human-reviewed and approved for Domain Modeling.
- No implementation source, database, internal tests, or execution behaviour was used.
- No BVA, test cases, execution results, evidence, or bugs are created in this phase.

## Step 1. Identify Input & Output Variables

Create a table following the slide style.

Use this table:

```markdown
| Type | Variable or Output | Description | Related Rule IDs | Applies To |
| ---- | ------------------ | ----------- | ---------------- | ---------- |
```

Classify each item as either `Input`, `Output`, or `State / Condition`.

Cover at least:

- Full name
- Email
- Password
- Confirm password
- API request body
- Guest or unauthenticated actor state
- UI required-field markers
- Email input control type
- Password input control type and masking
- Error-message placement
- API success response
- UI successful registration outcome
- Redirect to Login page
- Validation rejection for invalid registration

## Step 2. Identify Equivalence Classes

Create one row for each individual equivalence class / partition.

Use this table:

```markdown
| Partition ID | Type | Variable or Condition | Equivalence Class Description | Validity | Representative Value | Dependencies | Rule IDs | Test Basis Reference | Assumptions |
| ------------ | ---- | --------------------- | ----------------------------- | -------- | -------------------- | ------------ | -------- | -------------------- | ----------- |
```

Use only these values in the `Type` column:

- Input
- Output
- State / Condition
- UI Form Rule
- API Contract

Use only these values in the `Validity` column:

- Valid
- Invalid

Normative `Valid` and `Invalid` equivalence classes must come directly from approved rules in `requirement-analysis.md`.

`Ambiguous` and `Exploratory` classes must not be treated as required expected behaviour.

Use one row for each individual equivalence class.

Do not put multiple valid and invalid classes under one Partition ID.

Use stable and specific Partition IDs, for example:

```text
NAME-PRESENCE-V01
NAME-PRESENCE-I01
NAME-WHITESPACE-A01
EMAIL-PRESENCE-V01
EMAIL-PRESENCE-I01
EMAIL-FORMAT-V01
EMAIL-FORMAT-I01
EMAIL-UNIQUENESS-V01
EMAIL-UNIQUENESS-I01
EMAIL-CASE-A01
PASSWORD-PRESENCE-V01
PASSWORD-PRESENCE-I01
PASSWORD-LENGTH-V01
PASSWORD-LENGTH-I01
PASSWORD-UPPERCASE-V01
PASSWORD-UPPERCASE-I01
PASSWORD-LOWERCASE-V01
PASSWORD-LOWERCASE-I01
PASSWORD-DIGIT-V01
PASSWORD-DIGIT-I01
PASSWORD-SPECIAL-V01
PASSWORD-SPECIAL-I01
PASSWORD-SPECIAL-A01
CONFIRM-PRESENCE-V01
CONFIRM-PRESENCE-I01
CONFIRM-MATCH-V01
CONFIRM-MATCH-I01
REGISTRATION-COMPLETE-V01
API-REQUEST-V01
API-REQUEST-I01
API-SUCCESS-V01
FORM-REQUIRED-MARKER-V01
FORM-REQUIRED-MARKER-I01
FORM-EMAIL-TYPE-V01
FORM-EMAIL-TYPE-I01
FORM-PASSWORD-TYPE-V01
FORM-PASSWORD-TYPE-I01
FORM-ERROR-PLACEMENT-V01
FORM-ERROR-PLACEMENT-I01
FORM-STEP-INDICATOR-A01
REDIRECT-SUCCESS-V01
ACTOR-GUEST-V01
```

## Required Equivalence Classes

Analyze only domains supported by the reviewed test basis.

Cover at least:

- Full name provided
- Full name missing or empty
- Whitespace-only full name as ambiguity
- Email provided
- Email missing or empty
- Valid email format
- Invalid email format
- Unique email
- Duplicate email
- Email case sensitivity as ambiguity
- Password provided
- Password missing or empty
- Password length at least 8 characters
- Password shorter than 8 characters
- Uppercase presence
- Uppercase absence
- Lowercase presence
- Lowercase absence
- Digit presence
- Digit absence
- Documented special-character presence
- Documented special-character absence
- Undocumented special character as ambiguity
- Confirm-password field presence
- Missing confirm-password field on UI
- Matching password and confirmation
- Mismatching password and confirmation
- Complete valid registration input
- Missing API request properties
- Successful API response shape
- Successful redirect to Login page
- UI required-field marker present
- UI required-field marker missing
- Email control uses `type="email"`
- Email control does not use `type="email"`
- Password control uses `type="password"` and masks input
- Password control does not use `type="password"` or exposes input in clear text
- Error message appears above submit button
- Error message appears below submit button
- Step Indicator only as ambiguous or conditional unless registration is proven multi-step by approved test basis
- Guest or unauthenticated actor state

## Step 3. Best Representatives

Create a table showing one best representative for each equivalence class.

Use this table:

```markdown
| Partition ID | Representative Value | Why This Representative Was Chosen | Required Nominal Values for Other Variables | Applies To |
| ------------ | -------------------- | ---------------------------------- | ------------------------------------------- | ---------- |
```

The representative value must belong clearly to the equivalence class.

For invalid classes, keep unrelated variables nominally valid so that the selected representative isolates the partition being tested later.

Do not create test cases yet. This table only lists representative values for partitions.

Do not create Boundary Value Analysis yet.

For ordered domains such as password length, identify representative values only at partition level. Do not enumerate boundary sets such as 7, 8, and 9. Boundary values are reserved for Phase 4.

Example:

- Partition: password length is at least 8 characters
- Representative value: `Abcdef1!`
- Do not create BVA set: 7, 8, 9

## Do Not Invent

Do not invent:

- Maximum lengths
- Exact undocumented error messages
- Undocumented invalid-input status codes
- Duplicate-email status codes or response bodies
- Email normalization rules
- Email case-sensitivity rules
- Unicode handling rules
- Additional accepted special-character rules
- Exact Login URL
- Redirect timing
- UI success message text

Mark unsupported behaviours as `Ambiguous` or `Exploratory`, not as specified `Valid` or `Invalid` partitions.

## Partition Derivation

After the Step 3 table, create:

```markdown
## Partition Derivation
```

For every Partition ID, explain:

1. Which requirement or rule produced it.
2. Why it is Valid, Invalid, Ambiguous, or Exploratory.
3. Why the representative value belongs to that partition.
4. Which other variables must remain nominally valid.
5. Any dependency or assumption.
6. Whether the partition applies to UI, API, or both.

## Coverage Decisions

After `Partition Derivation`, create:

```markdown
## Coverage Decisions
```

Include:

- Partitions included in normative domain coverage
- Ambiguous partitions excluded from normative coverage
- Exploratory candidates
- Potential combinations reserved for test-case derivation
- Any intentionally uncovered domain and justification
- Explicit note that test cases providing coverage of partitions are reserved for Phase 5

## Human Review

End `reports/FR-01/domain-testing.md` with:

```markdown
## Human Review - Phase 3

- Reviewer:
- Review Date and Time:
- Corrections Made:
- Missing Partitions Added:
- Duplicate Partitions Removed:
- Status: Pending
- Approved for BVA: No
- Approved for Test-Case Derivation: No
- Approved for Test Execution: No
```

Do not mark Phase 3 as completed. Human review must remain pending.

## AI Audit

Save this Phase 3 prompt to:

```text
evidence/agent-skill/FR-01/phase-03-domain-modeling-prompt.md
```

Save the AI output or completion response to:

```text
evidence/agent-skill/FR-01/phase-03-domain-modeling-ai-output.md
```

Append a concise Phase 3 AI Audit entry to:

```text
ai-audit/ai-audit.md
```

The audit entry should link to the prompt file and AI output file instead of pasting the full prompt and full output.

The audit entry must include:

- AI Tool
- Date and Time
- Feature ID
- Task
- Prompt file reference
- AI output file reference
- Generated report reference
- AI output summary
- Human Review: Pending
- Human Corrections: None yet

## Integrity Rules

- Do not claim Pass or Fail.
- Do not create screenshots or execution evidence.
- Do not infer bugs.
- Do not inspect implementation source.
- Do not create boundary values yet.
- Do not generate test cases yet.
- Do not execute the application.
- Do not create GitHub Issues.
- Do not use implementation behaviour as the expected result.

## Completion Response

Report:

1. File created or updated.
2. Number of input variables identified.
3. Number of output variables identified.
4. Number of valid equivalence classes.
5. Number of invalid equivalence classes.
6. Number of ambiguous or exploratory equivalence classes.
7. Cross-field dependencies identified.
8. Coverage exclusions and reasons.
9. Confirmation that no BVA or test cases were created.
10. Confirmation that no execution, evidence capture, bug reporting, or GitHub Issues were created.
11. Confirmation that human review remains Pending.

Stop after Phase 3.
