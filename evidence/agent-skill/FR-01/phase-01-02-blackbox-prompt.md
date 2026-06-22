Use the `domain-testing-bva` skill for FR-01 Account Registration.

## Objective

Perform only:

1. Phase 1: Feature Intake
2. Phase 2: Black-box Test Basis Collection

Stop after Phase 2 for human review.

## Feature Information

- Feature ID: FR-01
- Feature name: Account Registration
- Pool: A
- Actor: Guest or unauthenticated user
- Application surface: EShop User Web and public registration API
- UI location: `/register`
- Output root: `reports`

## Approved Test Bases

Read only:

- `2026.HW02.Domain Testing_En.pdf`
- FR-01 requirements in `README.md`
- Shared form requirements in `README.md` that apply to registration
- Registration API contract in `api_specification.md`
- Public UI controls, labels, messages, and navigation if already observable

Do not inspect:

- `frontend-web` implementation source
- Backend implementation source
- Database schema or records
- Controllers, services, routes, middleware, or models
- Internal implementation tests

Do not derive expected results from implementation behaviour.

## Report Creation

Create a new Black-box requirement analysis report at:

```text
reports/FR-01/requirement-analysis.md
```

If the file already exists, do not overwrite it silently. Inspect it first and preserve any real human review notes or real execution evidence. If the file is empty or only contains placeholder content, replace it with the new Phase 1 and Phase 2 analysis.

This report must be created as a Black-box analysis from approved test bases only. Do not include source-code line references, frontend implementation evidence, backend implementation evidence, database enforcement evidence, or bugs inferred from source inspection.

## Required Analysis

For each FR-01 rule, record:

- Rule ID
- Rule
- Test Basis Type
- Test Basis Reference
- Observable Expected Behaviour
- Ambiguity
- Assumption

Cover at least:

- Required full name
- Required email
- Required password
- Valid email format
- Unique email
- Password minimum length
- Required uppercase letter
- Required lowercase letter
- Required digit
- Required special character
- Confirm-password field
- Matching password and confirmation
- Successful registration outcome
- Redirect to Login after success
- Relevant shared form requirements
- Public registration API request
- Public registration API success response

Record missing or ambiguous requirements without inventing answers, including:

- Maximum field lengths
- Whitespace handling
- Email case sensitivity
- Duplicate-email error response
- Invalid-input API status and message
- Exact full-name rules

## Required Output

Create or update only:

```text
reports/FR-01/requirement-analysis.md
```

Use this structure:

```markdown
# Requirement Analysis - FR-01 Account Registration

## Feature Intake

## Approved Black-box Test Bases

## Requirement Rules

## API Specification Rules

## Shared Form Rules

## Requirement Ambiguities

## Assumptions

## Coverage Gaps

## Human Review

- Status: Pending
- Approved for Domain Modeling: No
```

Every rule must reference an approved Black-box test basis such as:

```text
README.md - FR-01
README.md - Shared Form Requirements
api_specification.md - POST /api/register
2026.HW02.Domain Testing_En.pdf
```

Do not create:

- Domain partitions
- Boundary analysis
- Test cases
- Pass/Fail results
- Screenshots
- Bug reports
- GitHub Issues

Do not start or execute the application.

## AI Audit

After creating the report, append this interaction using:

```bash
python .agents/skills/domain-testing-bva/scripts/append_ai_audit.py \
  --audit-file ai-audit/ai-audit.md \
  --ai-tool "ChatGPT 5.5" \
  --task "FR-01 Phase 1 Feature Intake and Phase 2 Black-box Test Basis Collection" \
  --feature-id "FR-01" \
  --prompt-file "evidence/agent-skill/FR-01/phase-01-02-blackbox-prompt.md" \
  --output-refs "reports/FR-01/requirement-analysis.md" \
  --human-review "Pending" \
  --human-corrections "None yet"
```

If the script interface differs, inspect `--help` and use the equivalent valid command.

## Completion Response

Report:

1. File created or updated.
2. Number of requirement rules identified.
3. Approved test bases used.
4. Ambiguities and assumptions found.
5. Confirmation that the report was created as a new Black-box requirement analysis.
6. Confirmation that no implementation source was inspected.
7. Confirmation that no test was executed.
8. Confirmation that human review is still pending.

Stop after Phase 2.
