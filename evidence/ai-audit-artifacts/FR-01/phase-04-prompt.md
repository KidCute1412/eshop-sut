# Use `domain-testing-bva` Skill for FR-01 Phase 4

Use the `domain-testing-bva` skill to perform **Phase 4: Boundary Value Analysis** for **FR-01 Account Registration**.

## Project Information

- Project root: current repository
- Feature ID: FR-01
- Feature name: Account Registration
- Pool: A
- Actor: Guest / unauthenticated user
- Surfaces: User Web UI and public API

## Approval Gate

Before doing any analysis, read:

- `reports/FR-01/domain-testing.md`

Verify that its Phase 3 Human Review contains:

- `Status: Completed`
- `Approved for BVA: Yes`

If approval is absent or set to `No`, stop without modifying any file and report the missing approval.

## Required Sources

Read only:

- `.agents/skills/domain-testing-bva/SKILL.md`
- `.agents/skills/domain-testing-bva/references/bva-method.md`
- `.agents/skills/domain-testing-bva/references/instructor-clarifications.md`
- `.agents/skills/domain-testing-bva/assets/bva-table-template.md`
- `reports/FR-01/requirement-analysis.md`
- `reports/FR-01/domain-testing.md`

Treat the two reviewed reports as the approved Black-box test basis.

## Prohibited Sources and Actions

Do not:

- Inspect frontend or backend implementation source.
- Inspect database schemas, internal tests, controllers, services, routes, middleware, or models.
- Start or execute the application.
- Make HTTP requests.
- Create Domain Testing or BVA test cases.
- Record execution results, screenshots, evidence, bugs, Pass/Fail statuses, or GitHub Issues.
- Invent maximum lengths or undocumented boundaries.
- Modify Phase 1, Phase 2, or Phase 3 reports.
- Update the AI Audit.
- Create Git commits.

## Phase 4 Scope

Perform only Boundary Value Analysis.

### Step 1: Identify Candidate Domains

Review every normative domain from Phase 3 and determine whether BVA is:

- Applicable: ordered or explicitly bounded.
- Not applicable: categorical, Boolean, relational, state-based, format-based, or unbounded.
- Undetermined: a possible boundary exists but the approved test basis does not define it.

Include an applicability table containing:

- Domain or variable
- Rule ID
- Domain type
- Documented constraint
- BVA applicability
- Reason
- Test Basis Reference

Explicitly assess:

- Full-name presence
- Email presence
- Email format
- Email uniqueness
- Password presence
- Password length
- Uppercase presence
- Lowercase presence
- Digit presence
- Special-character presence
- Confirm-password presence
- Password-confirmation equality
- API request properties
- Actor state
- UI control properties
- Error placement
- Success response and redirect outcomes

Do not apply numeric BVA to unordered categories.

### Step 2: Derive Boundary Values

Apply BVA only when supported by an approved explicit boundary.

For password length, use approved rule `FR01-R06`, which specifies a minimum length of 8 characters.

Derive:

- `min-1`: 7 characters, Invalid
- `min`: 8 characters, Valid
- `min+1`: 9 characters, Valid
- Nominal internal value: 11 characters, Valid

Use concrete password values that satisfy uppercase, lowercase, digit, and documented special-character requirements so that only password length changes:

- 7 characters: `Abcd1!x`
- 8 characters: `Abcd1!xy`
- 9 characters: `Abcd1!xyz`
- 11 characters: `ValidPass1!`

Verify the character count of every value before writing it.

Do not derive `max-1`, `max`, or `max+1` because no maximum password length is documented.

### Step 3: Document Each Boundary

For every boundary value, record:

- Boundary ID
- Variable
- Rule ID
- Boundary position
- Concrete value
- Character count or measurable value
- Expected classification
- Dependencies and nominal values
- Applicable surface
- Test Basis Reference
- Justification
- Assumptions

Use boundary IDs such as:

- `FR01-PASSWORD-LENGTH-B01`
- `FR01-PASSWORD-LENGTH-B02`
- `FR01-PASSWORD-LENGTH-B03`
- `FR01-PASSWORD-LENGTH-N01`

Classification is not test execution. Do not write Actual Result, Pass, Fail, or evidence.

### Step 4: Explain Exclusions

Explicitly explain why BVA is not applied to domains such as:

- Email format and uniqueness
- Character-class presence
- Confirm-password equality
- Actor state
- API request property names
- UI input types
- Error placement
- Redirect destination

Record undocumented maximum lengths and other missing numeric limits as coverage gaps, not invented boundaries.

## Required Report Structure

Create:

`reports/FR-01/boundary-value-analysis.md`

Use this structure:

1. Title
2. Black-box Test Basis Summary
3. Step 1: Candidate Domain Assessment
4. Step 2: Applicable Boundary Model
5. Step 3: Concrete Boundary Values
6. Boundary Derivation
7. Coverage Decisions and Exclusions
8. Assumptions and Gaps
9. Human Review - Phase 4

End with:

```markdown
## Human Review - Phase 4

- Reviewer:
- Review Date and Time:
- Corrections Made:
- Missing Boundaries Added:
- Incorrect Boundaries Removed:
- Status: Pending
- Approved for Test-Case Derivation: No
- Approved for Test Execution: No
```

## Raw AI Output

Save an unchanged copy of the initial generated report at:

`evidence/agent-skill/FR-01/phase-04-bva-ai-output.md`

The raw AI output and initial report must be identical. Do not modify the raw AI output during later human correction.

## Completion Rules

Before finishing, verify:

- Every Phase 3 domain has an applicability decision.
- Only documented ordered or bounded domains receive BVA.
- Password values have lengths 7, 8, 9, and 11 exactly.
- Other password requirements remain valid in every boundary value.
- No undocumented maximum is invented.
- No test cases or execution results are created.
- Human Review remains Pending.
- Only the two requested files are created or modified.
