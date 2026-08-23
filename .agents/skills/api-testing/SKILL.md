---
name: api-testing
description: Guides an AI testing agent through auditable HW6 API Testing for EShop using Postman/Newman or equivalent tools, including AI-generated and human-audited API test cases, security/state/schema coverage, real execution evidence, CI/CD runs, bug reporting, AI audit, AI critique, Git log, and a reusable AI-driven API test generator design without fabricated results.
---

# AI-Assisted API Testing

Use this skill for HW6 - API Testing. It guides an AI testing agent through the complete EShop
API-testing workflow: selecting three backend APIs from Pools A, B, and C; generating, auditing,
extending, executing, and reporting API tests; creating Postman/Newman artifacts; integrating them
into CI/CD; and documenting the reusable AI-driven API test generator required for the Create level.

## Required References

Read these first, in this order, because they are the assignment and SUT source of truth:

- `2026.HW6.API_Testing_En.md`
- `README.md`
- `api_specification.md`
- `setup_guide.md`

Then read the skill references as needed:

- `references/assignment-requirements.md` for HW6 scope, minimums, grading, and anti-cheat rules.
- `references/eshop-api-guide.md` for EShop endpoint mapping, default credentials, security rules,
  and state-machine risks.
- `references/api-test-design-method.md` before generating or reviewing test cases.
- `references/postman-newman-ci.md` before creating collections, environments, Newman runs, or CI.
- `references/human-review-checklist.md` before marking test cases or execution as final.
- Use `assets/` and `scripts/` to scaffold reports, data files, and validation checks.

## Integrity Rules

- Never fabricate a test case review decision, execution status, Newman report, console screenshot,
  `X-Student-Id` evidence, bug, GitHub Issue URL, CI/CD run, commit hash, video link, or Git log.
- A run only counts if it was executed against the real backend or is explicitly labelled as a
  non-submission dry run. A hand-written HTML file is not a Newman report.
- Every executed request must include `X-Student-Id: {StudentID}`. Capture real evidence that the
  header is sent, preferably through a Postman pre-request script console screenshot or Newman
  request evidence.
- Expected behavior comes from `README.md`, `api_specification.md`, and documented security rules
  SEC-01 through SEC-07, not from current buggy behavior or implementation source.
- Preserve the initial AI-generated test cases for each selected API before human edits. The audit
  and gap analysis compare that preserved output against the reviewed final suite.
- The AI may draft tests, collections, scripts, schemas, and analysis. The human must review every
  result, label AI cases as VALID / INVALID / INCOMPLETE, correct them, and add at least five
  human-designed cases per API.
- The AI test-generator diagram must be self-drawn by the student. The agent may help with
  pseudocode, requirements, and checklist review, but must not claim to have produced the required
  self-drawn diagram.

## Phase 0: Scope, Tooling, and Environment

Ask the human to confirm and record:

- Student ID and repository link.
- Three selected APIs: exactly one from Pool A, one from Pool B, and one from Pool C. Do not choose
  automatically unless the user explicitly delegates selection.
- Confirmation that the same three-API selection is not duplicated with groupmates, if the class
  enforces that rule.
- Tool choice: Postman + Newman by default; Karate or RestAssured only when intentionally chosen.
- Backend base URL: `http://localhost:3000`.
- Setup/reset plan from `setup_guide.md`: `npm install`, `node database.js` only when a clean seed
  is needed, and `node server.js` for backend execution.

Prefer API choices that naturally cover different risk classes, for example:

- Pool A: `POST /api/login`, `POST /api/register`, or `GET /api/products?search=...`.
- Pool B: `POST /api/cart`, `POST /api/checkout`, `POST /api/apply-coupon`, or order cancel/history.
- Pool C: `PUT /api/admin/orders/:id/status`, product/category/coupon admin CRUD, or admin users.

## Phase 1: Map Requirements to API Contracts

For each selected API, document:

- Feature ID, pool, endpoint method/path, actor, authentication and role requirement.
- Request parameters, body fields, headers, path/query parameters, and dependencies.
- Expected response status, response schema, side effects, and error behavior.
- Relevant domain rules, state transitions, and SEC-01 through SEC-07 rules.
- Ambiguities or contradictions between `README.md` and `api_specification.md`.

Do not use backend implementation source as the oracle. Public API observation may be recorded as
execution evidence or an observed contradiction, but not as the expected requirement.

## Phase 2: AI-Assisted Test Case Generation

Drive AI step by step, never with one generic "generate all API tests" prompt:

1. Prompt for endpoint contract extraction for one API.
2. Prompt for domain partitions for every parameter and condition.
3. Prompt for security and authorization cases mapped to SEC-01 through SEC-07.
4. Prompt for state-transition cases where the API changes or depends on state.
5. Prompt for response schema validation cases.
6. Prompt for a reviewed candidate suite targeting at least 35 test cases for that API.

Preserve the raw AI prompt and output in `reports/HW6/<API-ID>/ai-initial-output.md` and append the
interaction to `ai-audit.md`. Repeat per selected API; keep the APIs separate enough that coverage
and human review are auditable.

## Phase 3: Human Audit and Extension

For every AI-generated case, the human labels it:

- `VALID`: correct and executable as written or with only formatting edits.
- `INVALID`: contradicted by the source of truth, unsafe, duplicate without value, or not testable.
- `INCOMPLETE`: useful intent but missing data, preconditions, oracle, schema assertion, security
  check, or state setup.

Correct invalid/incomplete cases before execution. Add at least five human-designed cases per API,
especially for security, authorization bypass, IDOR, role escalation, state-machine constraints,
schema strictness, and boundary/domain gaps. For each added case, explain why AI missed it: prompt
quality, model limitation, or SUT-specific behavior.

Run `scripts/validate_hw6_workspace.py reports/HW6` before final packaging and fix reported issues.

## Phase 4: Build Postman/Newman Artifacts

Create a Postman collection and environment for the selected APIs. The collection should include:

- Variables for `baseUrl`, `studentId`, user/admin credentials, tokens, entity IDs, and reusable
  request data.
- A pre-request script or collection-level header that sends `X-Student-Id: {{studentId}}` on every
  request.
- Login/token extraction where protected APIs are tested.
- Test scripts asserting status code, required fields, response schema, security rejection, and
  state changes where observable.
- Data-driven runs using CSV or JSON input when the same case template covers multiple values.

Save collection/environment/data files under `reports/HW6/postman/` or an equivalent documented
location. Do not hardcode secrets beyond the seeded demo credentials documented by the SUT.

## Phase 5: Real Execution and Evidence

Run the collection with Newman or the chosen equivalent against the real backend. For Newman,
preserve command output and HTML report, for example:

```powershell
newman run reports/HW6/postman/collection.json `
  -e reports/HW6/postman/environment.json `
  -d reports/HW6/postman/data.csv `
  --reporters cli,html `
  --reporter-html-export reports/HW6/newman/report.html
```

Capture:

- Newman CLI output and HTML report.
- Evidence that `X-Student-Id` was sent.
- Per-API execution summary: generated, reviewed, human-added, executed, passed, failed, blocked.
- Screenshots for genuine bugs and GitHub Issues once actually filed.

Mark results only from real execution: `Pass`, `Fail`, `Blocked`, or `Not Executed`. A failed test is
not automatically a SUT bug; first rule out wrong expected behavior, bad setup, stale data, token
failure, and test script error.

## Phase 6: Bug Reporting

Report a bug only when:

1. The expected result is supported by the source of truth.
2. The real API response contradicts that expected result.
3. The failure is reproducible.
4. Evidence exists.

For each confirmed bug, write a Markdown bug entry and file a real GitHub Issue with screenshot or
Newman/Postman evidence attached. Replace `Pending` with the actual Issue URL only after it exists.

## Phase 7: CI/CD Integration

Add the API tests to a CI/CD pipeline, normally GitHub Actions running Newman. Document:

- Workflow file path and command.
- Environment variables or secrets needed.
- One commit and pipeline run where all API tests pass.
- One separate commit and pipeline run where one test intentionally fails.
- Screenshots and links to both real runs.

Do not simulate CI logs. If CI cannot run because the repository is local-only or network access is
not available, label it as blocked and record the exact blocker instead of inventing links.

## Phase 8: AI Test Generator Design

Design the reusable API test generator for the SUT:

- Inputs: API specification, selected endpoint, requirement/security rules, state model, and student
  configuration.
- Processing: parse contract, derive domains, derive security/state/schema cases, rank/deduplicate,
  emit test cases and Postman/Newman artifacts.
- Outputs: Excel/Markdown test cases, Postman collection/environment/data, audit log, and summary.
- Include pseudocode in text form.
- Include a self-drawn diagram created by the student. The agent may provide diagram requirements
  or review a diagram, but must not claim the diagram itself is AI-generated submission evidence.
- Demonstrate the skill generating tests for one API in a video if the student elects to submit the
  optional/recommended demo.

## Phase 9: AI Audit, AI Critique, and Git Log

- Maintain `ai-audit.md` with AI tool name, date/time, prompt, raw output reference, and human
  corrections for every distinct AI interaction.
- Write `ai-critique.md` in 200-300 words using concrete examples from invalid/incomplete AI cases,
  missed security/state/schema tests, weak assertions, or CI/reporting mistakes.
- Commit each demonstrated step separately: generation, audit, extension, execution, bug reporting,
  CI/CD, and generator design. Export the real commit log to `git-commit-log.txt`.

## Phase 10: Final Assembly

Final `reports/HW6/` should include:

```text
README.md
main-report.md
ai-audit.md
ai-critique.md
git-commit-log.txt
bug-report.md
ci-cd-report.md
generator-design.md
postman/
  collection.json
  environment.json
  data.csv or data.json
newman/
  report.html
  newman-output.txt
<API-ID>/
  api-mapping.md
  test-cases.md
  ai-initial-output.md
  ai-gap-analysis.md
  evidence/
```

Export Markdown/PDF versions when required by Moodle packaging. The final README must contain the
self-assessment table and test summary: number of APIs, generated cases, human-added cases,
executed cases, passed, failed, blocked, bugs, Postman features used, CI runs, and links.
