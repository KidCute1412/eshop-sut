# AI Audit

## AI Interaction - 2026-06-21T17:39:55+07:00

- AI Tool: OpenAI Codex
- Date and Time: 2026-06-21T17:39:55+07:00
- Feature ID: FR-01
- Task: Create reusable domain-testing-bva Agent Skill and FR-01 dry run
- Prompt: You are a senior software testing engineer, Python engineer, and Agent Skills architect.

Create a complete Agent Skill for my Software Testing HW02 project. You have filesystem and terminal access to the current project directory.

Do not stop after writing a plan. Inspect the project, create the actual files, run validation, test the scripts, perform a dry run, and fix discovered problems.

# 1. Current project structure

The current working directory is the root of my `HW2` project:

```text
HW2/
├── backend/
├── frontend-admin/
├── frontend-mobile/
├── frontend-web/
├── 2026.HW02.Domain Testing_En.pdf
├── api_specification.md
├── README.md
├── run_servers.sh
└── setup_guide.md
```

The PDF file in the project root is the official HW02 assignment.

If its exact filename differs slightly, locate the single HW02 PDF in the project root. Do not rename or modify it.

Do not clone another repository. The complete EShop source code is already present in this project.

# 2. Mandatory inspection

Before creating the skill:

1. Read the complete HW02 PDF.
2. Read `README.md`.
3. Read `api_specification.md`.
4. Read `setup_guide.md`.
5. Inspect `run_servers.sh` before executing it.
6. Inspect the relevant source code in:

   * `backend/`
   * `frontend-admin/`
   * `frontend-mobile/`
   * `frontend-web/`
7. Identify the frameworks, validation libraries, API routes, database models, constraints, authentication rules, and test conventions.
8. Do not modify application source code while creating the skill.
9. Check `git status` before editing.
10. Preserve all existing and uncommitted user changes.

Summarise what you learned before implementing the skill.

# 3. Assignment context

My currently allocated features are:

| Pool | ID    | Feature                   |
| ---- | ----- | ------------------------- |
| A    | FR-01 | Account registration      |
| A    | FR-02 | Login and account lockout |
| B    | FR-07 | Shopping cart             |
| C    | FR-17 | Coupon management (CRUD)  |

The assignment PDF appears to require one feature from each pool, while this allocation contains two Pool A features and no Pool D feature.

Record this as an allocation inconsistency in the documentation. Do not silently choose or invent a Pool D feature.

The Agent Skill must remain reusable for all EShop features, including future Mobile App features. Do not hard-code the skill only for FR-01, FR-02, FR-07, or FR-17.

# 4. Skill objective

Create one Agent Skill named:

```text
domain-testing-bva
```

Create it at:

```text
.agents/skills/domain-testing-bva/
```

The skill must guide an AI agent through an auditable and reusable workflow that:

1. Reads the selected feature requirements.
2. Inspects relevant frontend, backend, API, and database code.
3. Extracts input variables, constraints, states, and business rules.
4. Creates a domain model.
5. Identifies valid and invalid equivalence partitions.
6. Identifies justified boundary values.
7. Generates Domain Testing test cases.
8. Generates Boundary Value Analysis test cases.
9. Removes unjustified duplicate tests.
10. Builds requirement-to-test traceability.
11. Identifies assumptions, contradictions, and coverage gaps.
12. Requires human review.
13. Produces assignment-ready Markdown reports.
14. Never fabricates execution results, screenshots, evidence, or bugs.

# 5. Agent Skills standard

Follow the current Agent Skills specification:

* https://agentskills.io/home
* https://agentskills.io/specification
* https://agentskills.io/skill-creation/best-practices

The folder name and the `name` in `SKILL.md` must match.

Use only these fields in the YAML frontmatter:

```yaml
---
name: domain-testing-bva
description: [Write a precise description of what the skill does and when it must activate.]
---
```

Requirements:

* Keep `SKILL.md` below 500 lines.
* Make the instructions concise, procedural, and reusable.
* Store detailed methods and templates in supporting files.
* Reference supporting files using relative paths.
* Do not include completed feature-specific test cases inside `SKILL.md`.
* Write all skill files and generated reports in English.

# 6. Required skill structure

Create this structure:

```text
HW2/
└── .agents/
    └── skills/
        └── domain-testing-bva/
            ├── SKILL.md
            ├── references/
            │   ├── assignment-requirements.md
            │   ├── domain-testing-method.md
            │   ├── bva-method.md
            │   ├── eshop-analysis-guide.md
            │   ├── test-case-schema.md
            │   └── human-review-checklist.md
            ├── assets/
            │   ├── feature-report-template.md
            │   ├── requirement-analysis-template.md
            │   ├── domain-table-template.md
            │   ├── bva-table-template.md
            │   ├── test-case-template.md
            │   ├── traceability-template.md
            │   ├── ai-gap-analysis-template.md
            │   └── ai-audit-entry-template.md
            └── scripts/
                ├── create_feature_workspace.py
                ├── validate_test_cases.py
                └── append_ai_audit.py
```

Do not leave unused placeholder files.

# 7. Assignment reference

Create:

```text
references/assignment-requirements.md
```

Summarise only requirements relevant to using this skill:

* Four-feature selection rule
* Domain Testing requirement
* Boundary Value Analysis requirement
* Detailed step-by-step explanation
* AI gap analysis
* Human review responsibility
* Bug reporting expectations
* Agent Skill and YouTube demo requirements
* AI Audit requirements
* Git commit requirements
* Required submission materials
* Test summary requirements

Use the PDF as the authoritative source. Do not copy the entire PDF.

# 8. Skill input contract

When activated, the skill must request or discover:

* Feature ID
* Feature name
* Pool
* Requirement source
* Relevant application module
* Repository root
* Frontend source paths
* Backend source paths
* API endpoints
* Database models and constraints
* Authentication role
* Preconditions
* Existing test data
* Output directory
* Testing environment, if test execution is requested

The skill should use this project mapping by default:

| Application area   | Default path           |
| ------------------ | ---------------------- |
| Backend            | `backend/`             |
| Admin frontend     | `frontend-admin/`      |
| Mobile frontend    | `frontend-mobile/`     |
| User web frontend  | `frontend-web/`        |
| API specification  | `api_specification.md` |
| Setup instructions | `setup_guide.md`       |
| Server script      | `run_servers.sh`       |

If required information cannot be found:

1. Search the repository.
2. Record the missing information.
3. Ask the user when it materially affects correctness.
4. Mark temporary conclusions as assumptions.
5. Never invent a requirement.

# 9. Required workflow in SKILL.md

## Phase 1: Feature intake

* Confirm the feature ID, name, pool, user role, and application module.
* Locate the feature in the assignment, API specification, UI, backend, and database.
* Create a feature workspace.
* Record unknown or contradictory information.

## Phase 2: Evidence collection

Inspect, when applicable:

* UI forms and client-side validation
* Request and response schemas
* Backend controllers and routes
* Services and business logic
* DTOs and validation annotations
* Database models and constraints
* Authentication and authorisation
* State transitions
* Error messages
* Existing tests
* Seed data

For each discovered rule, record its source file and relevant symbol, route, or section.

Clearly separate:

* Documented requirement
* API specification
* Implemented frontend behaviour
* Implemented backend behaviour
* Database enforcement
* Assumption
* Contradiction

## Phase 3: Domain modelling

For every input, state, or condition, record:

* Variable name
* Data type
* Input source
* Constraints
* Valid equivalence partitions
* Invalid equivalence partitions
* Dependencies
* Business rules
* Evidence source
* Assumptions

Include interactions between variables. Do not always treat fields independently.

Consider:

* Missing values
* Empty values
* Null values
* Valid and invalid formats
* Length ranges
* Numeric ranges
* Collection sizes
* Duplicate values
* Existing and non-existing entities
* Authentication state
* Authorisation role
* Resource state
* Cross-field dependencies
* Temporal conditions
* State transitions

Only include categories relevant to the selected feature.

## Phase 4: Boundary Value Analysis

Apply BVA only when the domain is ordered or bounded.

Depending on the boundary, consider:

```text
min-1, min, min+1, nominal, max-1, max, max+1
```

Also consider:

* Empty, one, and many items for collections
* Zero, one, capacity-1, capacity, and capacity+1
* Date and time boundaries
* Expiration boundaries
* State transition boundaries
* Lockout attempt boundaries
* Quantity and stock boundaries
* String-length boundaries

Do not mechanically apply numeric BVA to unordered categories.

For every boundary, record:

* Variable
* Boundary rule
* Boundary source
* Test values
* Expected classification
* Justification

## Phase 5: Test-case design

Generate separate Domain Testing and BVA test cases.

Each test case must contain:

* Test Case ID
* Technique
* Objective
* Requirement or rule reference
* Preconditions
* Test data
* Steps
* Expected result
* Actual result
* Status
* Evidence
* Partition or boundary covered
* Source-code reference
* Notes and assumptions

Use ID formats:

```text
FR01-DT-001
FR01-BVA-001
```

Until the test is genuinely executed, use:

```text
Actual Result: Not Executed
Status: Not Executed
Evidence: None
```

Never infer Pass or Fail from source-code inspection alone.

## Phase 6: Quality review

Verify:

* Every relevant requirement has test coverage.
* Every valid partition is covered or justified.
* Every invalid partition is covered or justified.
* Every applicable boundary is covered.
* Expected results are precise and observable.
* Preconditions are reproducible.
* Test data is concrete.
* Test cases are not unjustified duplicates.
* Domain tests and BVA tests are correctly classified.
* Security tests are not incorrectly presented as Domain Testing.
* Requirement, code, partition, boundary, and test traceability exists.
* Assumptions are visible.
* No bug or result is fabricated.
* Human review is explicitly required.

## Phase 7: Output

For each analysed feature, produce:

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

# 10. Script requirements

## `create_feature_workspace.py`

Requirements:

* Use Python standard library where practical.
* Accept feature ID, feature name, pool, and output directory.
* Validate the feature ID.
* Create the required report structure.
* Initialise reports using templates.
* Never overwrite existing files unless `--force` is provided.
* Print clear success and error messages.
* Provide `--help`.

Example:

```bash
python .agents/skills/domain-testing-bva/scripts/create_feature_workspace.py \
  --feature-id FR-01 \
  --feature-name "Account registration" \
  --pool A \
  --output reports
```

## `validate_test_cases.py`

Validate Markdown test cases for:

* Duplicate IDs
* Invalid ID format
* Missing required fields
* Missing expected results
* Pass or Fail without evidence
* Executed status with `Evidence: None`
* Missing partition or boundary reference
* Missing requirement or source reference
* Missing traceability
* Duplicate or highly similar test cases
* Incorrect Domain/BVA classification when detectable

Requirements:

* Print actionable validation errors.
* Return exit code `0` when valid.
* Return a non-zero exit code when invalid.
* Provide `--help`.
* Do not silently modify reports.

## `append_ai_audit.py`

Append an interaction to a Markdown AI Audit file.

Required fields:

* AI tool
* Date and time
* Task
* Feature ID
* Prompt
* AI output or output-file references
* Human review
* Human corrections

Requirements:

* Never overwrite previous entries.
* Create the audit file if it does not exist.
* Use an ISO-compatible timestamp.
* Provide `--help`.
* Clearly handle missing required arguments.

# 11. Supporting documentation

Create:

```text
agent-skill-docs/
├── README.md
├── design-and-usage.md
├── evaluation.md
└── demo-video-script.md
```

## `README.md`

Include:

* Skill name
* Purpose
* Folder location
* Requirements
* Installation or discovery
* Example invocation
* Inputs
* Outputs
* Script commands
* Known limitations
* Link placeholder for the YouTube demo

## `design-and-usage.md`

Explain:

* Why one reusable skill was selected
* Progressive disclosure
* Role of `SKILL.md`
* Role of references
* Role of templates
* Role of deterministic scripts
* Human review gates
* How repository evidence is used
* Why the skill does not fabricate results

## `evaluation.md`

Include an evaluation table with:

* Evaluation case
* Input
* Expected behaviour
* Actual behaviour
* Pass or Fail
* Problem found
* Improvement applied

Evaluate at least:

* Correct feature input
* Missing feature ID
* Missing repository evidence
* Numeric boundary
* String-length boundary
* Unordered category
* Duplicate test IDs
* Pass result without evidence
* Re-running workspace creation
* Invalid audit input

## `demo-video-script.md`

Write a complete step-by-step script for a YouTube demonstration showing:

1. The project structure.
2. The official assignment PDF.
3. The skill structure.
4. Skill discovery.
5. Skill activation.
6. FR-01 input.
7. Requirement and source inspection.
8. Domain modelling.
9. BVA.
10. Test-case generation.
11. Validation script execution.
12. Human review.
13. AI gap analysis.
14. Generated reports.
15. AI Audit entry.

# 12. Dry run

Perform a dry run on:

```text
FR-01 - Account registration
```

Use the actual project files:

* `backend/`
* `frontend-web/`
* `api_specification.md`
* Other relevant files discovered during inspection

Store the dry-run output at:

```text
agent-skill-demo/FR-01/
```

The dry run must:

1. Identify actual requirement and code evidence.
2. Build a domain table.
3. Build a BVA table.
4. Generate representative test cases.
5. Build a traceability matrix.
6. Run the validator.
7. Identify skill weaknesses.
8. Improve the skill.
9. Run validation again.

Do not execute application test cases during this dry run unless the application is deliberately started and actual evidence is captured.

Source inspection alone must result in `Not Executed`.

# 13. AI Audit support

Create:

```text
ai-audit/
└── agent-skill-creation.md
```

Record this Agent Skill creation session with:

* AI tool name
* Date and time
* The task prompt
* Created output-file references
* Important AI decisions
* Human review status
* Corrections still required

Do not claim that the human has reviewed anything unless I explicitly confirm it.

# 14. Validation

After implementation:

1. Validate `SKILL.md` against the Agent Skills specification.
2. Confirm the folder name matches the skill name.
3. Check all relative references.
4. Run all scripts with `--help`.
5. Run successful and failing examples for every script.
6. Confirm scripts do not overwrite existing work.
7. Run the FR-01 dry run.
8. Run the test-case validator.
9. Fix all discovered errors.
10. Repeat validation after fixes.
11. Show the final directory tree.
12. Report every command executed and its result.

If `skills-ref` is available, run:

```bash
skills-ref validate .agents/skills/domain-testing-bva
```

If it is unavailable, perform equivalent manual validation and report that `skills-ref` was unavailable.

# 15. Git requirements

If the project is a Git repository:

1. Inspect `git status` first.
2. Never stage unrelated or pre-existing changes.
3. Stage only files created or modified for this Agent Skill.
4. Create separate commits for major steps, for example:

```text
feat(skill): scaffold domain testing and bva skill
feat(skill): add testing workflow and report templates
feat(skill): add workspace audit and validation scripts
test(skill): evaluate skill with FR-01 dry run
docs(skill): add usage and demo documentation
```

If committing is unsafe because of unrelated changes, do not commit. Explain the issue and provide the exact recommended commit commands.

# 16. Final response

At completion, report:

* Files created
* Files modified
* Project evidence inspected
* Script test results
* Skill validation result
* FR-01 dry-run result
* Improvements made after evaluation
* Known limitations
* Allocation inconsistency concerning Pool D
* Git commits created
* Exact command to invoke the skill
* Exact next steps for recording the YouTube video

Do not stop after analysis or planning. Create and verify the complete Agent Skill.
- AI Output or Output File References: .agents/skills/domain-testing-bva; agent-skill-docs; agent-skill-demo/FR-01; ai-audit/agent-skill-creation.md
- Human Review: Pending - not yet confirmed by user
- Human Corrections: None yet
