---
name: mini-api-testing
description: >
  Execute the Mini Exercise — API Testing assignment for the eshop-sut project
  using a gated workflow: Analyze → Generate → Audit → Extend → Execute →
  Newman → CI/CD → Final Packaging. The agent must stop at defined checkpoints,
  show evidence, and wait for user approval before continuing to the next major phase.
---

# Mini API Testing Skill

## 1. Purpose

Use this skill to complete the **Mini Exercise — Thực hành API Testing** assignment
for exactly **one API** in the `eshop-sut` project.

The required overall pipeline is:

```text
Generate with AI
    ↓
Audit (human review)
    ↓
Extend
    ↓
Execute with Postman
    ↓
Execute with Newman
    ↓
CI/CD with GitHub Actions
    ↓
Final submission package
```

The agent MUST NOT perform the entire assignment in one uncontrolled pass.

The workflow is divided into checkpoints. At each checkpoint:

1. Finish only the work allowed in that phase.
2. Show the user the relevant evidence.
3. Summarize what was found or changed.
4. Explicitly state whether the checkpoint is PASS or BLOCKED.
5. STOP and wait for user approval before entering the next gated phase.

---

# 2. Non-negotiable rules

## Rule 1 — Do not guess API behavior

Expected status codes, response fields, validation rules, authentication behavior,
and state transitions must be verified from:

1. source code;
2. existing API documentation in the repository;
3. actual local API execution when needed.

Never invent behavior from the endpoint name alone.

---

## Rule 2 — Do not modify the SUT just to make tests pass

If a test fails:

```text
Fail
 ↓
Inspect test
 ↓
Inspect data
 ↓
Inspect environment
 ↓
Inspect API implementation
 ↓
Determine root cause
```

Possible classifications:

```text
TEST BUG
TEST DATA BUG
ENVIRONMENT BUG
SUT BUG
EXPECTED / INTENTIONAL FAILURE
```

Do not change the expected result merely because the current SUT returns something
different.

Do not modify production/backend implementation unless the user explicitly authorizes it.

---

## Rule 3 — Preserve evidence

Do not claim that:

- Postman passed;
- Newman passed;
- CI passed;
- CI failed intentionally;
- a report exists;

unless the corresponding command or pipeline was actually executed and evidence exists.

Never fabricate:

- screenshots;
- command output;
- GitHub Actions results;
- Newman reports.

---

## Rule 4 — One API only

The assignment is for exactly one selected API.

Do not switch APIs midway unless the user explicitly requests it.

---

## Rule 5 — Do not overwrite important existing work blindly

Before editing any existing file:

1. inspect it;
2. explain whether it is being reused, modified, or replaced;
3. preserve unrelated content.

---

# 3. Required user inputs

Before implementation, determine:

```text
MSSV:
Selected API:
Repository path:
Current branch:
```

The following are mandatory:

- `MSSV`
- selected API
- repository / working directory

If any of those cannot be inferred reliably, ask the user.

Do not self-select the API.

---

# 4. Expected final artifacts

The final submission must contain:

```text
<MSSV>_Mini_API_Testing/
│
├── test-design.md
├── mini-<api-name>.data.json
├── mini-<api-name>.postman_collection.json
├── mini-local.postman_environment.json
├── mini-newman-report.json
├── newman-api-test.yml
├── ci-pass.png
└── ci-fail.png
```

Final archive:

```text
<MSSV>_Mini_API_Testing.zip
```

The workflow file may physically live in:

```text
.github/workflows/newman-api-test.yml
```

but a copy named `newman-api-test.yml` should be included in the final submission package
if needed for packaging.

---

# 5. Global checkpoint policy

Major checkpoints are:

```text
CP0 — Assignment & Repository Ready
CP1 — API Contract Verified
CP2 — AI Test Design Generated
CP3 — Human Audit Completed
CP4 — Manual Extension Completed
CP5 — Automation Data Design Approved
CP6 — Postman Collection Ready
CP7 — Local Postman/Newman Execution Passed
CP8 — CI Workflow Ready
CP9 — CI PASS Captured
CP10 — Intentional CI FAIL Captured
CP11 — CI Restored to PASS
CP12 — Final Submission Validated
```

For every checkpoint, output:

```text
CHECKPOINT: CPx — <name>
STATUS: PASS | BLOCKED

Evidence:
- ...

Created/modified:
- ...

Important findings:
- ...

Risks / unresolved items:
- ...

Next phase:
- ...

WAITING FOR USER APPROVAL
```

Do not continue automatically past a gated checkpoint.

---

# 6. CP0 — Assignment & Repository Ready

## Objective

Confirm the project can be inspected and the required tools are available.

## Actions

1. Read the assignment completely.
2. Inspect repository structure.
3. Confirm the selected API.
4. Locate backend.
5. Locate package configuration.
6. Determine how backend starts.
7. Determine current Git branch.
8. Check:

```bash
node --version
npm --version
newman --version
git status
git branch --show-current
```

9. If dependencies are missing:

```bash
cd backend
npm install
```

Do not yet create test artifacts.

## Required evidence

Show:

```text
Node version:
npm version:
Newman version:
Repo path:
Branch:
Selected API:
Backend command:
```

## PASS criteria

CP0 is PASS only if:

- repository is accessible;
- selected API is known;
- MSSV is known;
- backend location is known;
- Node/npm are available;
- Newman is available or installation plan is clear.

## STOP

Do not inspect or alter test implementation until user approves CP0.

---

# 7. CP1 — API Contract Verified

## Objective

Reverse-engineer the actual behavior of the selected API.

## Actions

Locate:

```text
route
controller
service
model / database access
validation
authentication middleware
authorization middleware
related constants / enums
```

Build a verified API contract.

## Required contract format

```md
# API Under Test

## Endpoint
- Method:
- Path:

## Authentication
- Required:
- Token/header:
- Role requirements:

## Request
- Params:
- Query:
- Body:

## Validation rules
- Field:
- Type:
- Required:
- Constraints:

## Success response
- Status:
- Fields:

## Error responses
- Condition:
- Status:
- Body:

## State / database prerequisites
- ...

## Source files inspected
- ...
```

## Runtime verification

If implementation behavior is ambiguous, start backend and make minimal manual requests.

For example:

```bash
cd backend
npm run dev
```

Then use curl/Postman as appropriate.

Do not run destructive requests without understanding their effects.

## PASS criteria

CP1 is PASS only if the agent can explain:

- exact method/path;
- required inputs;
- validation constraints;
- auth requirements;
- expected status behavior;
- expected response shape;
- API-specific state assumptions.

## Checkpoint output

Present the contract to the user.

Highlight uncertainty separately:

```text
Verified:
- ...

Still uncertain:
- ...
```

## STOP

Wait for the user to approve the API contract before generating test cases.

---

# 8. CP2 — Generate with AI

## Objective

Generate at least 12 AI-proposed test cases based on the verified contract.

## Important

The prompt itself is part of the assignment evidence and must be preserved.

Do not use a vague prompt such as:

```text
Generate all tests.
```

Use a structured prompt.

## Prompt template

```text
You are designing API test cases for:

METHOD <method>
ENDPOINT <endpoint>

Verified implementation contract:
<insert verified contract>

Step 1: identify all inputs and constraints.
Step 2: identify valid equivalence partitions.
Step 3: identify invalid equivalence partitions.
Step 4: identify boundary values.
Step 5: identify relevant authentication/security scenarios.
Step 6: identify response schema checks.
Step 7: if applicable, identify legal and illegal state transitions.

Generate at least 12 test cases.

Coverage should include, where applicable:
- valid input
- invalid input
- missing required field
- empty input
- boundary values
- wrong type
- non-existent resource
- authentication
- malformed/invalid token
- expired token if supported
- security-oriented input
- schema validation
- state transitions

Return columns:
- tc_id
- input
- expected_status
- expected_fields
- rationale

Do not assume undocumented behavior.
Mark uncertain assumptions explicitly.
```

## Output

Add to:

```text
test-design.md
```

Structure:

```md
# Step 1 — Generate with AI

## Prompt

...

## AI-generated test cases

| TC ID | Input | Expected Status | Expected Fields | Rationale |
|---|---|---:|---|---|
| AI-01 | ... | ... | ... | ... |
```

## Target

Prefer 12–15 cases.

Do not exceed the scope merely to create a large number.

## PASS criteria

- at least 12 cases;
- all required columns present;
- coverage is not redundant;
- prompt is preserved;
- output is tied to the verified API contract.

## STOP

Show the generated design to the user before auditing.

---

# 9. CP3 — Human Audit

## Objective

Audit every AI-generated test case against the actual implementation.

Each test must receive exactly one label:

```text
VALID
INVALID
INCOMPLETE
```

## Audit method

For each test case:

```text
AI proposal
   ↓
Compare with verified implementation
   ↓
Run API manually if necessary
   ↓
Assign label
   ↓
Explain reason
   ↓
Correct if needed
```

## Classification definitions

### VALID

The case is correctly specified and has enough information to implement.

### INVALID

The expected result or premise conflicts with the verified implementation/specification.

### INCOMPLETE

The idea is useful but lacks required detail, such as:

- missing expected field;
- missing precondition;
- missing auth state;
- ambiguous input;
- unspecified expected status.

## Required audit table

```md
# Step 2 — Audit

| TC | Label | Review / Correction |
|---|---|---|
| AI-01 | VALID | ... |
| AI-02 | INVALID | ... |
| AI-03 | INCOMPLETE | ... |
```

Every row requires at least one explanatory sentence.

## Mandatory correction

At least one of the following must exist:

1. one corrected `INVALID` case;
2. one completed `INCOMPLETE` case.

If all AI tests appear valid, identify one unstated assumption and explicitly add/correct it.

## Defect handling

If:

```text
expected behavior from verified requirement != actual runtime behavior
```

do not silently align the test to runtime.

Record:

```text
Potential SUT defect
Expected:
Actual:
Evidence:
```

## PASS criteria

- all AI-generated tests audited;
- every row labeled;
- every label explained;
- at least one correction or added assumption;
- no expected result changed only to force green tests.

## STOP

Show the audit table and wait for approval.

---

# 10. CP4 — Extend

## Objective

Add at least 2 manually designed tests that AI missed.

Prefer 2–3 cases.

## Candidate areas

Where relevant:

```text
Content-Type
response time
empty string
negative number
very large number
special characters
unexpected HTTP status convention
API-specific invariant
authorization edge case
state-transition edge case
```

## Required format

```md
# Step 3 — Extend

## EXT-01 — <name>

Input:
Expected:
Reason:
Why AI missed it:

## EXT-02 — <name>

Input:
Expected:
Reason:
Why AI missed it:
```

"Why AI missed it" should use one of these kinds of explanations:

```text
prompt limitation
model limitation
API-specific behavior
missing implementation context
```

## PASS criteria

- at least 2 genuinely new cases;
- not duplicates of AI cases;
- each has a reason;
- each explains why AI missed it.

## STOP

Wait for user approval before selecting automation cases.

---

# 11. CP5 — Automation Data Design Approved

## Objective

Select 5 representative cases for data-driven execution.

## Selection strategy

Prefer this mix:

```text
1 positive
2 negative
1 boundary / edge
1 security / extend / API-specific
```

The five cases should demonstrate meaningful variation.

Avoid:

```text
5 almost-identical success cases
```

## Required output

```md
# Selected Automation Cases

| Iteration | Source TC | Category | Purpose |
|---:|---|---|---|
| 1 | AI-01 | Positive | ... |
| 2 | AI-04 | Negative | ... |
| 3 | AI-07 | Negative | ... |
| 4 | AI-10 | Boundary | ... |
| 5 | EXT-01 | Extend | ... |
```

Then design the data schema.

Example:

```json
{
  "tc_id": "TC-01",
  "email": "...",
  "password": "...",
  "expected_status": 200
}
```

## PASS criteria

- exactly 5 intended iteration rows selected;
- each maps to an audited or extended case;
- expected values are justified;
- data fields are sufficient for Postman assertions.

## STOP

Wait for approval before creating Postman files.

---

# 12. CP6 — Postman Collection Ready

## Objective

Create all local Postman automation artifacts.

## Files

Create:

```text
mini-<api-name>.data.json
mini-<api-name>.postman_collection.json
mini-local.postman_environment.json
```

## Environment variables

Minimum:

```text
baseUrl = http://localhost:3000
studentId = <MSSV>
```

Add only variables actually needed, for example:

```text
authToken
productId
orderId
```

## Request URL

Prefer:

```text
{{baseUrl}}/api/...
```

## Iteration data

Request fields should use iteration variables where possible.

Example:

```json
{
  "email": "{{email}}",
  "password": "{{password}}"
}
```

## Required pre-request script

The API request must inject:

```javascript
pm.request.headers.upsert({
  key: "X-Student-Id",
  value: pm.environment.get("studentId")
});
```

## Assertions

At minimum:

### Status assertion

```javascript
pm.test(`[${pm.iterationData.get("tc_id")}] Correct status`, () => {
  pm.response.to.have.status(
    Number(pm.iterationData.get("expected_status"))
  );
});
```

### Content-Type or response-time assertion

Example:

```javascript
pm.test("[MINI] Response is JSON", () => {
  pm.expect(
    pm.response.headers.get("Content-Type")
  ).to.include("application/json");
});
```

or:

```javascript
pm.test("[MINI] Response time acceptable", () => {
  pm.expect(pm.response.responseTime).to.be.below(1000);
});
```

### API-specific assertions

Validate relevant fields for success/error responses.

Do not overfit assertions to one iteration in a way that breaks the data-driven design.

## Static inspection before execution

Check:

```text
Collection JSON parses
Environment JSON parses
Data JSON parses
Exactly 5 data objects
baseUrl exists
studentId exists
X-Student-Id pre-request script exists
expected_status is used by assertions
```

## PASS criteria

Files exist and are structurally correct.

## STOP

Show the created file names and important scripts before executing them.

---

# 13. CP7 — Local Postman/Newman Execution Passed

## Objective

Prove the local automated suite works.

## Step 1 — Start provider

Run backend in the correct directory.

Typical command:

```bash
cd backend
npm run dev
```

Wait until provider is actually ready.

## Step 2 — Smoke test

Use a known safe endpoint/request to confirm backend availability.

Do not assume "process started" means API ready.

## Step 3 — Postman / equivalent local verification

Confirm five intended iterations execute.

## Step 4 — Newman

Run:

```bash
newman run mini-<api-name>.postman_collection.json \
  --environment mini-local.postman_environment.json \
  --iteration-data mini-<api-name>.data.json \
  --reporters cli,json \
  --reporter-json-export mini-newman-report.json
```

On PowerShell, use syntax appropriate to PowerShell instead of blindly copying
Bash line continuations.

## Required checks

```text
Iteration count = 5
Assertion failures = 0
mini-newman-report.json exists
X-Student-Id = correct MSSV
```

## Failure investigation

If any test fails, create a table:

```text
Iteration:
TC:
Expected:
Actual:
Likely cause:
Classification:
Fix:
```

Classifications:

```text
TEST BUG
DATA BUG
ENVIRONMENT BUG
SUT BUG
UNKNOWN
```

Do not continue while failures remain unless they are confirmed SUT defects and the user
explicitly decides how to handle them.

## PASS criteria

CP7 = PASS only if:

- five intended iterations execute;
- Newman completes successfully;
- no assertion fail remains;
- JSON report exists;
- student header is confirmed.

## STOP

Show Newman summary and report path. Wait for approval before CI.

---

# 14. CP8 — CI Workflow Ready

## Objective

Create the GitHub Actions workflow.

## File

```text
.github/workflows/newman-api-test.yml
```

## Workflow responsibilities

It must:

```text
checkout
 ↓
setup Node.js
 ↓
install backend dependencies
 ↓
start backend/provider
 ↓
wait for provider readiness
 ↓
install Newman
 ↓
run collection + environment + iteration data
 ↓
produce JSON report
 ↓
upload report artifact
```

## Important CI rules

Do not use arbitrary long sleeps as the only readiness strategy if a health/smoke check can
be used.

The workflow must fail if Newman tests fail.

Do not suppress failure with constructs equivalent to:

```text
|| true
continue-on-error: true
```

unless there is a narrowly justified non-test step.

## PASS criteria

- YAML exists;
- trigger targets the correct branch/workflow intent;
- backend is started;
- readiness is checked;
- Newman command uses correct files;
- report upload step exists;
- test failures propagate to CI failure.

## STOP

Show the workflow summary to the user before pushing.

---

# 15. CP9 — CI PASS Captured

## Objective

Produce a real successful GitHub Actions run.

## Actions

1. Commit current correct version.
2. Push to the student's branch.
3. Open/check GitHub Actions.
4. Wait for workflow completion.
5. Verify all Newman tests pass.
6. Capture the required screenshot:

```text
ci-pass.png
```

## Evidence to record

```text
Commit hash:
Branch:
Workflow name:
Run conclusion:
Screenshot:
```

## PASS criteria

- GitHub Actions actually completed successfully;
- screenshot clearly shows passing pipeline;
- screenshot saved as `ci-pass.png`.

## STOP

Do not create the intentional failure until the user approves CP9.

---

# 16. CP10 — Intentional CI FAIL Captured

## Objective

Demonstrate that CI correctly detects a failing assertion.

## Safety rule

Create the failure only after a valid PASS has already been captured.

## Recommended method

Modify one expected value in the iteration data.

Example:

```json
"expected_status": 200
```

temporarily becomes:

```json
"expected_status": 999
```

Do not break unrelated project code.

## Actions

1. Make one deliberate test-expectation change.
2. Commit with a clear message.
3. Push.
4. Wait for workflow.
5. Confirm Newman assertion failure causes CI failure.
6. Capture:

```text
ci-fail.png
```

## Evidence

Record:

```text
Changed test/data:
Original expected value:
Temporary expected value:
Commit hash:
Workflow result:
Screenshot:
```

## PASS criteria

- failure is intentional and explainable;
- GitHub Actions actually fails;
- screenshot saved as `ci-fail.png`.

## STOP

Do not leave the repository in this state. Wait for approval to restore.

---

# 17. CP11 — CI Restored to PASS

## Objective

Return the repository to the correct final state.

## Actions

1. Revert the intentional incorrect expectation.
2. Confirm all files contain valid final values.
3. Commit.
4. Push.
5. Wait for GitHub Actions.
6. Confirm final run is PASS.

## Required evidence

```text
Restoration commit:
Final workflow conclusion:
Final Newman result:
```

## PASS criteria

The latest/final commit on the student's branch must pass.

## STOP

Wait for user approval before packaging.

---

# 18. CP12 — Final Submission Validated

## Objective

Validate every required artifact and create the final submission archive.

## `test-design.md` must contain

```text
[ ] API description
[ ] verified API contract
[ ] AI prompt
[ ] AI output / test cases
[ ] >= 12 AI-generated test cases
[ ] audit table
[ ] VALID / INVALID / INCOMPLETE labels for every AI case
[ ] reason for every audit label
[ ] >= 1 correction or explicit unstated assumption
[ ] >= 2 manually extended cases
[ ] explanation why AI missed each extension
[ ] selected 5 automation cases
[ ] Postman features table
```

## Postman feature table

Include:

```md
| Feature | Đã dùng? | Ghi chú |
|---|---|---|
| Collections | Có/Không | ... |
| Environment variables | Có/Không | ... |
| Collection variables | Có/Không | ... |
| Pre-request scripts | Có/Không | ... |
| Test scripts (assertions) | Có/Không | ... |
| Data-driven runs | Có/Không | ... |
| Newman CLI | Có/Không | ... |
| Monitors | Có/Không | ... |
| Mock servers | Có/Không | ... |
| Workspaces | Có/Không | ... |
```

At least 6 features must actually have been used.

A safe baseline is:

```text
Collections
Environment variables
Pre-request scripts
Test scripts
Data-driven runs
Newman CLI
```

Do not mark unused features as used merely to reach six.

## Artifact checklist

```text
[ ] test-design.md
[ ] mini-<api-name>.data.json
[ ] mini-<api-name>.postman_collection.json
[ ] mini-local.postman_environment.json
[ ] mini-newman-report.json
[ ] newman-api-test.yml
[ ] ci-pass.png
[ ] ci-fail.png
```

## Content verification

Do not only check that files exist.

Verify:

```text
JSON files parse successfully
YAML is syntactically valid
Newman report reflects 5 intended iterations
No temporary expected_status=999 remains
MSSV is correct
baseUrl is correct
studentId is correct
X-Student-Id logic exists
Final CI is PASS
Screenshots are real
```

## Create final package

Create:

```text
<MSSV>_Mini_API_Testing.zip
```

The archive should contain only the required submission artifacts plus any clearly useful
supporting file that does not conflict with the assignment.

## Final report to user

Return:

```text
FINAL STATUS: PASS / BLOCKED

API:
MSSV:
Final branch:
Final CI:
Newman:
Iterations:
Assertions:
Submission archive:

Files included:
- ...

Known issues:
- ...
```

---

# 19. Postman feature strategy

To reliably satisfy the requirement of at least six used features, prefer these six:

```text
1. Collections
2. Environment variables
3. Pre-request scripts
4. Test scripts / assertions
5. Data-driven runs
6. Newman CLI
```

Optional:

```text
Collection variables
Workspaces
```

Do not unnecessarily add:

```text
Monitors
Mock servers
```

unless the assignment implementation genuinely uses them.

---

# 20. Recommended repository working structure

A clean structure may be:

```text
repo/
│
├── backend/
│
├── .github/
│   └── workflows/
│       └── newman-api-test.yml
│
└── mini-api-testing/
    ├── test-design.md
    ├── mini-<api-name>.data.json
    ├── mini-<api-name>.postman_collection.json
    ├── mini-local.postman_environment.json
    ├── mini-newman-report.json
    ├── ci-pass.png
    └── ci-fail.png
```

But do not force this structure if the instructor/repository already defines another
required location.

---

# 21. Suggested Git commit sequence

Use small commits to make the CI demonstration clear.

Example:

```text
1. docs: add API test design and audit
2. test: add Postman data-driven API collection
3. ci: add Newman API test workflow
4. test: demonstrate intentional CI failure
5. fix: restore valid API test expectation
```

The final commit must be passing.

---

# 22. Agent behavior when blocked

If blocked, do not improvise.

Use:

```text
CHECKPOINT: <current checkpoint>
STATUS: BLOCKED

Blocking issue:
- ...

What I verified:
- ...

What is missing:
- ...

User action needed:
- ...
```

Examples of blockers:

```text
MSSV unknown
API not selected
repository unavailable
backend cannot start
database prerequisite missing
auth credentials unavailable
Newman unavailable
GitHub branch permission denied
GitHub Actions disabled
CI cannot access required secret
```

---

# 23. Minimal commands checklist

## Environment

```bash
node --version
npm --version
newman --version
git status
git branch --show-current
```

## Backend

```bash
cd backend
npm install
npm run dev
```

## Newman

```bash
newman run mini-<api-name>.postman_collection.json \
  --environment mini-local.postman_environment.json \
  --iteration-data mini-<api-name>.data.json \
  --reporters cli,json \
  --reporter-json-export mini-newman-report.json
```

Adapt line continuation syntax to the active shell.

## Git

```bash
git status
git add .
git commit -m "<message>"
git push
```

Do not commit secrets, local-only credentials, or unrelated generated files.

---

# 24. Definition of Done

The assignment is DONE only when all conditions below are true:

```text
[ ] Exactly one API was used.
[ ] >= 12 AI-generated cases exist.
[ ] All AI cases were audited.
[ ] Every AI case has VALID / INVALID / INCOMPLETE.
[ ] Every label has a written explanation.
[ ] At least one case/assumption was corrected.
[ ] >= 2 manual extension cases exist.
[ ] Exactly 5 intended cases were automated as iteration data.
[ ] X-Student-Id uses the correct MSSV.
[ ] Postman assertions are data-driven where appropriate.
[ ] Content-Type or response-time assertion exists.
[ ] Local Newman run succeeds.
[ ] 5 iterations are shown.
[ ] 0 assertion failures remain in the correct final version.
[ ] mini-newman-report.json exists.
[ ] GitHub Actions workflow runs Newman.
[ ] Real CI PASS evidence exists.
[ ] Real intentional CI FAIL evidence exists.
[ ] Final CI state is PASS.
[ ] At least 6 Postman features are documented and genuinely used.
[ ] Final archive contains all required files.
[ ] No intentional failure remains in final submission.
```

If any item is false, final status must be:

```text
BLOCKED / INCOMPLETE
```

not PASS.
