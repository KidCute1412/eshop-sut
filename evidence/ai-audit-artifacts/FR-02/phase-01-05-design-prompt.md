Use the `domain-testing-bva` Agent Skill to complete FR-02 using the same report style, formatting, naming conventions, and quality level as the completed FR-01 artifacts.

Project root: current repository
Feature ID: FR-02
Feature name: Login and account lockout
Pool: A
Output directory: `reports/FR-02/`
AI evidence directory: `evidence/agent-skill/FR-02/`
AI audit file: `ai-audit/ai-audit.md`

Follow the current skill exactly:

`.agents/skills/domain-testing-bva/SKILL.md`

Do not redesign the workflow, do not add extra phases, and do not create Phase 9. Execute only the phases currently defined in the skill, from Feature Intake through AI Gap Analysis, while respecting all human review and execution gates.

Use FR-01 as the formatting and quality model. Study these completed FR-01 artifacts before creating FR-02:

- `reports/FR-01/requirement-analysis.md`
- `reports/FR-01/domain-testing.md`
- `reports/FR-01/boundary-value-analysis.md`
- `reports/FR-01/test-cases.md`
- `reports/FR-01/bug-report.md`
- `reports/FR-01/ai-gap-analysis.md`
- `ai-audit/ai-audit.md`
- `evidence/agent-skill/FR-01/`

Use FR-01 only as a template for:

- File structure.
- Heading structure.
- Table format.
- Rule ID naming style.
- Partition ID naming style.
- Test case format.
- Coverage summary format.
- Human review block format.
- Bug report format.
- AI gap analysis format.
- AI audit style.
- Evidence naming style.

Do not copy FR-01 requirements, partitions, test data, bugs, execution results, or conclusions into FR-02 unless they are explicitly supported by the FR-02 approved test basis.

Read all required skill references before working:

- `.agents/skills/domain-testing-bva/references/instructor-clarifications.md`
- `.agents/skills/domain-testing-bva/references/assignment-requirements.md`
- `.agents/skills/domain-testing-bva/references/eshop-analysis-guide.md`
- `.agents/skills/domain-testing-bva/references/domain-testing-method.md`
- `.agents/skills/domain-testing-bva/references/bva-method.md`
- `.agents/skills/domain-testing-bva/references/test-case-schema.md`
- `.agents/skills/domain-testing-bva/references/human-review-checklist.md`

Strict rules:

1. This is black-box functional testing.
2. Do not inspect implementation source code.
3. Do not inspect frontend source, backend source, database schema, database records, controllers, services, routes, middleware, models, or internal tests.
4. Do not modify application source code.
5. Do not use implementation behaviour as the oracle.
6. Expected results must come only from approved requirements, API specification, observable public UI/API behaviour, explicit assumptions, ambiguities, or real execution evidence.
7. Do not fabricate requirements, test results, screenshots, evidence, bugs, or GitHub Issue links.
8. Leave GitHub Issue links as `Pending` unless real GitHub Issues already exist.
9. Preserve every prompt and AI output under `evidence/agent-skill/FR-02/`.
10. Append every AI interaction to `ai-audit/ai-audit.md`.
11. Do not commit or stage database files, build artifacts, `node_modules`, logs, or unrelated files.

Create the FR-02 workspace with this final structure:

```text
reports/FR-02/
|-- requirement-analysis.md
|-- domain-testing.md
|-- boundary-value-analysis.md
|-- test-cases.md
|-- bug-report.md
|-- ai-gap-analysis.md
`-- evidence/
    |-- <TEST-CASE-ID>.png
    `-- <other-real-evidence-files>
```

Do not create or require:

- `traceability-matrix.md`
- `execution-summary.md`
- `evidence-index.md`

The final execution summary will be written in the assignment-level `README.md` later.

For FR-02, extract the official login and account lockout requirements from approved black-box bases only. Pay attention to any documented rules about:

- Login identifier, such as email or username.
- Password.
- Required login fields.
- Successful login.
- Failed login.
- Invalid credentials.
- Existing and non-existing accounts.
- Account lockout.
- Failed-attempt threshold.
- Lockout duration.
- Unlock or reset conditions.
- Error message or error placement.
- Post-login redirect or user state.
- Shared form requirements relevant to the login form.
- Public login API contract, if documented.

For `reports/FR-02/requirement-analysis.md`, follow the same structure and level of detail as `reports/FR-01/requirement-analysis.md`. Create FR-02-specific rule IDs and test basis references. Record ambiguities, assumptions, observable behaviours, and exclusions clearly.

For `reports/FR-02/domain-testing.md`, follow the same structure and level of detail as `reports/FR-01/domain-testing.md`. Identify FR-02-specific variables, states, outputs, dependencies, valid partitions, invalid partitions, representatives, and assumptions. Use stable FR-02 partition IDs such as `LOGIN-EMAIL-PRESENCE-V01`, but only create IDs that are actually supported by the test basis.

For `reports/FR-02/boundary-value-analysis.md`, follow the same structure and level of detail as `reports/FR-01/boundary-value-analysis.md`. Apply BVA only to documented ordered or bounded domains. For FR-02, likely candidates may include failed-attempt count, lockout threshold, lockout duration, or time window, but use them only if they are explicitly documented in an approved test basis. Do not invent thresholds, limits, or durations.

For `reports/FR-02/test-cases.md`, follow the same format as `reports/FR-01/test-cases.md`. Generate both Domain Testing and BVA cases according to the current skill schema. Use IDs such as:

- `FR02-DT-001`
- `FR02-DT-002`
- `FR02-BVA-001`
- `FR02-BVA-002`

Before execution, every test case must contain exactly:

```text
Actual Result: Not Executed
Status: Not Executed
Evidence: None
```

The AI must not execute tests during test-case generation.

Inside `reports/FR-02/test-cases.md`, include a coverage summary in the same style as FR-01. The coverage summary must map:

- Each normative FR-02 partition to at least one DT case on each applicable public surface.
- Each selected FR-02 boundary value to at least one BVA case on each applicable public surface.
- Each omitted surface, partition, or boundary to a documented exclusion reason.
- Each dependency or blocking-prone conformance condition to a dedicated case when it can affect many later cases.

Run the validator after test-case generation only if the validator exists and matches the current skill schema:

```bash
python .agents/skills/domain-testing-bva/scripts/validate_test_cases.py reports/FR-02/test-cases.md
```

Fix only safe schema, formatting, reference, or validation errors. Do not invent execution results.

When the skill reaches a human review gate, stop and request human confirmation. The AI must not approve its own test cases.

After human review, record in `reports/FR-02/test-cases.md` or `ai-audit/ai-audit.md`:

- Reviewer.
- Review date and time.
- Review scope.
- Human corrections.
- Human-added, removed, or reclassified cases.
- Duplicate-case decisions.
- `Approved for Test Execution: Yes/No`.

Do not execute tests while approval is `No` or missing.

After human approval, execute only through public UI or public API. Do not inspect implementation code or database contents. For each attempted case, record:

- Execution date and time.
- Environment.
- Actual Result.
- Status: `Pass`, `Fail`, or `Blocked`.
- Blocking Reason when status is `Blocked`.
- Real evidence reference.

Save evidence under:

```text
reports/FR-02/evidence/<TEST-CASE-ID>.png
```

Evidence must match the exact test case and execution result. Do not leave a `Pass`, `Fail`, or `Blocked` case with `Evidence: None`.

After execution evidence is available, create or update:

- `reports/FR-02/bug-report.md`
- `reports/FR-02/ai-gap-analysis.md`

For `reports/FR-02/bug-report.md`, follow the same format as `reports/FR-01/bug-report.md`. Create bug records only when:

1. The test has a documented expected result.
2. The observable actual result contradicts it.
3. The failure has been reproduced.
4. Human-verified evidence exists.

For every confirmed bug, record:

- Bug ID.
- Title.
- Severity.
- Status.
- Related test case.
- Related requirement.
- Preconditions.
- Reproduction steps.
- Expected result.
- Actual result.
- Evidence links.
- GitHub Issue link.

Leave GitHub Issue links as `Pending` until real GitHub Issues are created.

For `reports/FR-02/ai-gap-analysis.md`, follow the same format as `reports/FR-01/ai-gap-analysis.md`. Compare preserved initial AI outputs with the current human-reviewed and executed artifacts. Separate:

- AI-missed test cases.
- Human improvements to existing tests.
- Runtime bugs exposed by AI-generated tests.
- Runtime bugs exposed by human-added tests.
- Runtime-only findings.
- Prompt-quality or reasoning gaps.

Do not claim runtime bugs were missed by AI if the AI generated the tests that exposed them.

At the end, report:

- Created and modified files.
- DT case count.
- BVA case count.
- Total test case count.
- Execution status counts.
- Evidence count.
- Confirmed bug count.
- Pending GitHub Issue count.
- Validator result, if the validator was run.
- Remaining blockers.
- Suggested git commits.

Suggested commit:

```bash
git add reports/FR-02 evidence/agent-skill/FR-02 ai-audit/ai-audit.md
git commit -m "test(fr02): complete black-box DT and BVA workflow"
```
