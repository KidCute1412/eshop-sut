# FR-07 Shopping Cart - Design and Execution Prompt

Interpreted scope:

- Use the `domain-testing-bva` skill exactly as written.
- Complete FR-07 from approved black-box bases only.
- Treat FR-07 as the Shopping Cart feature in Pool B.
- Produce the standard FR-07 artifacts in the same report style and quality level as the completed FR-01/FR-02 artifacts.
- Execute only after the test cases have been reviewed and approved by a human reviewer.
- Use only public UI and public API behaviour as the oracle.
- Capture real evidence screenshots or other real evidence files for every executed case.
- Record each execution result in `reports/FR-07/test-cases.md` as Pass, Fail, or Blocked.
- Do not inspect implementation source code, frontend source, backend source, database schema, database records, controllers, services, routes, middleware, models, or internal tests.

Project context:

- Project root: current repository
- Feature ID: FR-07
- Feature name: Shopping Cart
- Output directory: `reports/FR-07/`
- AI evidence directory: `evidence/ai-audit-artifacts/FR-07/`
- AI audit file: `ai-audit/ai-audit.md`

Follow the current skill references exactly:

- `.agents/skills/domain-testing-bva/SKILL.md`
- `.agents/skills/domain-testing-bva/references/instructor-clarifications.md`
- `.agents/skills/domain-testing-bva/references/assignment-requirements.md`
- `.agents/skills/domain-testing-bva/references/eshop-analysis-guide.md`
- `.agents/skills/domain-testing-bva/references/domain-testing-method.md`
- `.agents/skills/domain-testing-bva/references/bva-method.md`
- `.agents/skills/domain-testing-bva/references/test-case-schema.md`
- `.agents/skills/domain-testing-bva/references/human-review-checklist.md`

Use FR-01 and FR-02 only as style and structure models for:

- File layout.
- Heading structure.
- Table format.
- Rule ID naming style.
- Partition ID naming style.
- Test case format.
- Coverage summary format.
- Human review block format.
- Bug report format.
- AI gap analysis format.
- Evidence naming style.

Do not copy FR-01 or FR-02 requirements, partitions, test data, bugs, execution results, or conclusions into FR-07 unless they are explicitly supported by the FR-07 approved test basis.

Strict rules:

1. This is black-box functional testing.
2. Do not inspect implementation source code.
3. Do not inspect frontend source, backend source, database schema, database records, controllers, services, routes, middleware, models, or internal tests.
4. Do not modify application source code.
5. Do not use implementation behaviour as the oracle.
6. Expected results must come only from approved requirements, API specification, observable public UI/API behaviour, explicit assumptions, ambiguities, or real execution evidence.
7. Do not fabricate requirements, test results, screenshots, evidence, bugs, or GitHub Issue links.
8. Leave GitHub Issue links as `Pending` unless real GitHub Issues already exist.
9. Preserve every prompt and AI output under `evidence/ai-audit-artifacts/FR-07/`.
10. Append every AI interaction to `ai-audit/ai-audit.md`.
11. Do not commit or stage database files, build artifacts, `node_modules`, logs, or unrelated files.

Feature focus for FR-07:

- Cart page structure and visible columns.
- Duplicate add-to-cart merge behaviour.
- Delete confirmation behaviour.
- Continue shopping navigation.
- Total label text.
- Empty-cart state.
- Add-to-cart visual feedback.
- Navbar cart badge.
- Breadcrumb on cart page.
- Active cart navigation highlight.
- Quantity increase and decrease controls.
- Public authenticated cart API behaviour.

Create the FR-07 workspace artifacts in this final structure:

```text
reports/FR-07/
|-- requirement-analysis.md
|-- domain-testing.md
|-- boundary-value-analysis.md
|-- test-cases.md
|-- execution-summary.md
|-- bug-report.md
|-- traceability-matrix.md
|-- ai-gap-analysis.md
`-- evidence/
    |-- evidence-index.md
    `-- <TEST-CASE-ID>.png
```

Do not create or require any other output files unless the approved skill workflow explicitly produces them.

For FR-07, extract the official shopping cart requirements from approved black-box bases only. Pay attention to any documented rules about:

- Cart page columns and labels.
- Duplicate product handling in cart.
- Delete/remove confirmation.
- Continue-shopping navigation.
- Total label wording.
- Empty-cart visual state.
- Add-to-cart feedback.
- Navbar cart badge count.
- Breadcrumb or page-location indicator.
- Active navigation highlight.
- Quantity increment/decrement controls.
- Public cart API authentication.
- `GET /api/cart`.
- `POST /api/cart`.
- Required request body fields for cart APIs.

For `reports/FR-07/requirement-analysis.md`, follow the same structure and level of detail as the completed FR-01/FR-02 requirement analysis artifacts. Create FR-07-specific rule IDs and test-basis references. Record ambiguities, assumptions, observable behaviours, and exclusions clearly.

For `reports/FR-07/domain-testing.md`, follow the same structure and level of detail as the completed FR-01/FR-02 domain-model artifacts. Identify FR-07-specific variables, states, outputs, dependencies, valid partitions, invalid partitions, representatives, and assumptions. Use stable FR-07 partition IDs only when they are actually supported by the test basis.

For `reports/FR-07/boundary-value-analysis.md`, follow the same structure and level of detail as the completed FR-01/FR-02 BVA artifacts. Apply BVA only to documented ordered or bounded domains. For FR-07, likely candidates may include add-to-cart quantity, quantity adjustment thresholds, or any documented numeric limits, but use them only if they are explicitly documented in an approved test basis. Do not invent thresholds, limits, or durations.

For `reports/FR-07/test-cases.md`, follow the same format as the completed FR-01/FR-02 test-case artifacts. Generate both Domain Testing and BVA cases according to the current skill schema. Before execution, every test case must contain exactly:

```text
Actual Result: Not Executed
Status: Not Executed
Evidence: None
```

The AI must not execute tests during test-case generation.

Inside `reports/FR-07/test-cases.md`, include a coverage summary in the same style as the completed FR-01/FR-02 artifacts. The coverage summary must map:

- Each normative FR-07 partition to at least one DT case on each applicable public surface.
- Each selected FR-07 boundary value to at least one BVA case on each applicable public surface.
- Each omitted surface, partition, or boundary to a documented exclusion reason.
- Each dependency or blocking-prone conformance condition to a dedicated case when it can affect many later cases.

Run the validator after test-case generation only if the validator exists and matches the current skill schema:

```bash
python .agents/skills/domain-testing-bva/scripts/validate_test_cases.py reports/FR-07/test-cases.md
```

Fix only safe schema, formatting, reference, or validation errors. Do not invent execution results.

When the skill reaches a human review gate, stop and request human confirmation. The AI must not approve its own test cases.

After human review, record in `reports/FR-07/test-cases.md` or `ai-audit/ai-audit.md`:

- Reviewer.
- Review date and time.
- Review scope.
- Human corrections.
- Human-added, removed, or reclassified cases.
- Duplicate-case decisions.
- `Approved for Test Execution: Yes/No`.

Do not execute tests while approval is `No` or missing.

After approval, execute only through public UI or public API. Do not inspect implementation code or database contents. For each attempted case, record:

- Execution date and time.
- Environment.
- Actual Result.
- Status: `Pass`, `Fail`, or `Blocked`.
- Blocking Reason when status is `Blocked`.
- Real evidence reference.

Save evidence under:

```text
reports/FR-07/evidence/<TEST-CASE-ID>.png
```

Evidence must match the exact test case and execution result. Do not leave a `Pass`, `Fail`, or `Blocked` case with `Evidence: None`.

After execution evidence is available, create or update:

- `reports/FR-07/bug-report.md`
- `reports/FR-07/ai-gap-analysis.md`

For `reports/FR-07/bug-report.md`, follow the same format as the completed FR-01/FR-02 bug reports. Create bug records only when:

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

For `reports/FR-07/ai-gap-analysis.md`, follow the same format as the completed FR-01/FR-02 AI gap analysis artifacts. Compare preserved initial AI outputs with the current human-reviewed and executed artifacts. Separate:

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
git add reports/FR-07 evidence/ai-audit-artifacts/FR-07 ai-audit/ai-audit.md
git commit -m "test(fr07): complete black-box DT and BVA workflow"
```
