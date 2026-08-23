# HW06 Run Notes

## What the agent completed

- Generated 3 API test-case workbooks plus a test summary workbook.
- Generated Postman collection, local environment, and data-driven files for FR03, FR09, and FR13.
- Generated Markdown reports for main report, README, bug report, CI/CD notes, AI audit, AI critique, and git log.
- Prepared a reusable API-test-generator skill design and flow.

## Important limitation

The spreadsheet skill's required `@oai/artifact-tool` loader was not available in this Codex session, so the workbooks were generated as minimal OpenXML `.xlsx` files by a local script. They are intended to be opened and visually checked in Excel/LibreOffice before final Moodle submission.

Poppler (`pdfinfo`/`pdftoppm`) was not available in PATH for visual PDF rendering. The generated PDFs were structurally checked for `%PDF-` headers and EOF markers; please open them once before final upload.

## Local execution

1. From repository root, install backend dependencies if needed: `cd backend && npm ci && cd ..`.
2. Start the backend: `cd backend && node server.js`.
3. In another terminal, run Newman:
   - `npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder "FR03 Password Recovery" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr03-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr03-newman-report.json`
   - `npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder "FR09 Apply Coupon" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr09-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr09-newman-report.json`
   - `npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder "FR13 Admin Orders" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr13-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr13-newman-report.json`
4. Every request injects `X-Student-Id: 23127296` in the pre-request script and request headers.
5. Optional secure-oracle failing run: adjust the expected assertion for the known bug case or use the CI note in `ci-cd/ci_cd_report.md`.

## Verified local run

The suite was executed locally on 2026-08-24 00:38-00:39 Asia/Saigon against `http://localhost:3000`.

| API | Iterations | Requests | Assertions | Failed |
|---|---:|---:|---:|---:|
| FR03 | 42 | 68 | 168 | 0 |
| FR09 | 37 | 37 | 148 | 0 |
| FR13 | 36 | 68 | 144 | 0 |

Report files:

- `newman/fr03-newman-report.json`
- `newman/fr09-newman-report.json`
- `newman/fr13-newman-report.json`

These JSON reports are complete and show 0 failed assertions.

## Additional technical requirements checklist

- Postman collection: ready.
- Environment variables: `baseUrl`, `studentId`.
- Data-driven runs: one JSON data file per selected API.
- Pre-request script: injects `X-Student-Id` and obtains tokens where needed.
- Newman JSON reports: generated after local execution.
- HTML report: TODO if required. No `.html` Newman report exists in `hw06` at the time of this update.
- CI/CD: workflow template and report notes are prepared; real GitHub screenshots/links must be filled after pushing commits.

## What is still missing

The following items require manual action because they need real external evidence:

| Item | Current status | What to do next |
|---|---|---|
| GitHub bug issues | TODO | Create one GitHub Issue for each bug in `bug-reports/bug_report.md`, attach a screenshot, then paste each issue URL into that file. |
| Bug screenshots | TODO | Capture Newman console output or API response evidence for each bug and attach it to the GitHub Issues. |
| CI passing run | TODO | Commit/push the current HW06 files and wait for `.github/workflows/newman-api-test.yml` to pass. Paste the run URL and screenshot into `ci-cd/ci_cd_report.md`. |
| CI failing run | TODO | Make a temporary secure-oracle assertion that should fail for one known bug, commit/push it, capture the failed run URL/screenshot, then restore the passing version. |
| Passing/failing commit hashes | TODO | Paste the two real commit hashes into `ci-cd/ci_cd_report.md` and `git_commit_log.txt`. |
| Self-drawn generator diagram | TODO if not exported | Redraw or manually confirm the design in `flow.md`, export it as PNG/PDF, and place it under `agent-skill/` or another clear folder. |
| Demo video link | Optional/TODO | If your lecturer/TA requires it, record a short demo of the generator design or artifact creation and add the YouTube link to `main_report.md`. |
| Newman HTML report | Optional/TODO | Generate only if required by the grader; JSON reports are already present and valid. |

## How to complete the remaining evidence

### 1. Create GitHub bug issues

Create three separate GitHub Issues using the issue bodies below:

1. `BUG-FR09-001 - Percent coupon formula returns negative discount`
2. `BUG-FR13-001 - Admin orders endpoint accepts any valid user token`
3. `BUG-FR09-002 - Coupon application is public despite using user_id-sensitive rules`

After creating each issue, update the line `GitHub issue screenshot/link: TODO` with the real issue URL and screenshot filename.

#### Issue body for BUG-FR09-001

````markdown
## Description

The `POST /api/apply-coupon` endpoint calculates percentage coupon discounts incorrectly. For a percent coupon such as `SAVE10`, the backend treats the percentage value as a multiplier in the wrong formula, which produces a negative discount and an inflated final amount.

## Affected endpoint

`POST /api/apply-coupon`

## Steps to reproduce

1. Start the backend with `cd backend && node server.js`.
2. Send a request to `POST http://localhost:3000/api/apply-coupon`.
3. Use this request body:

```json
{
  "code": "SAVE10",
  "total_amount": 500000,
  "user_id": 1
}
```

4. Observe the returned `discount` and `final_amount`.

## Expected result

For a 10 percent coupon on `500000`, the discount should be `50000` and the final amount should be `450000`.

## Actual result

The implementation calculates the discount with `Math.floor(total_amount * (1 - coupon.discount_value))`. With `discount_value = 10`, this becomes a negative discount and makes the final amount larger than the original amount.

Observed example:

- `discount`: `-4500000`
- `final_amount`: `5000000`

## Impact

This is a high severity pricing bug. Customers may see incorrect checkout totals, coupon validation becomes unreliable, and the system can return impossible financial values.

## Evidence

- Test cases: `FR09-001`, `FR09-004`, `FR09-006`, and the human formula oracle case.
- Local Newman report: `hw06/submit/newman/fr09-newman-report.json`.
- Source location: `backend/server.js`, percentage coupon branch in `/api/apply-coupon`.

## Suggested fix

For percentage coupons, calculate the discount as:

```js
Math.floor(total_amount * coupon.discount_value / 100)
```
````

#### Issue body for BUG-FR13-001

````markdown
## Description

The `GET /api/admin/orders` endpoint allows any authenticated user to access the admin order list. The endpoint validates that the JWT is valid, but it does not verify that the authenticated user has the `admin` role.

## Affected endpoint

`GET /api/admin/orders`

## Steps to reproduce

1. Start the backend with `cd backend && node server.js`.
2. Log in as a normal non-admin user and obtain a valid JWT.
3. Send a request to `GET http://localhost:3000/api/admin/orders` using that normal user's token:

```http
Authorization: Bearer <normal_user_token>
```

4. Observe that the endpoint returns the order list instead of rejecting the request.

## Expected result

Only admin users should be able to access all orders. A normal authenticated user should receive `403 Forbidden`.

## Actual result

The endpoint returns admin order data for a normal authenticated user because it only calls `authenticateToken` and does not check `req.user.role === "admin"`.

## Impact

This is a critical authorization bug. A normal user can access order information that should be restricted to administrators, which may expose customer, order, and business data.

## Evidence

- Test cases: `FR13-006` through `FR13-010`, plus the human IDOR/role tests.
- Local Newman report: `hw06/submit/newman/fr13-newman-report.json`.
- Source location: `backend/server.js`, `app.get("/api/admin/orders", authenticateToken, ...)`.

## Suggested fix

Add an admin authorization middleware after token authentication, for example:

```js
if (req.user.role !== "admin") {
  return res.status(403).json({ error: "Admin access required" });
}
```
````

#### Issue body for BUG-FR09-002

````markdown
## Description

The `POST /api/apply-coupon` endpoint is public even though coupon eligibility and usage checks depend on user-specific rules. The endpoint trusts the optional `user_id` value sent in the request body instead of deriving the user identity from an authenticated token.

## Affected endpoint

`POST /api/apply-coupon`

## Steps to reproduce

1. Start the backend with `cd backend && node server.js`.
2. Send a request to `POST http://localhost:3000/api/apply-coupon` without an `Authorization` header.
3. Include a body with a coupon code, amount, and any `user_id` value:

```json
{
  "code": "SAVE10",
  "total_amount": 500000,
  "user_id": 1
}
```

4. Observe that the endpoint processes the coupon request even though the caller is unauthenticated.

## Expected result

Coupon application should require authentication when user-specific coupon usage or eligibility rules are enforced. The backend should identify the user from the verified JWT, not from a client-supplied `user_id`.

## Actual result

The endpoint accepts unauthenticated requests and trusts `user_id` from the request body. This creates a trust-boundary issue because a client can omit or change `user_id`.

## Impact

This is a medium severity security and business-logic bug. A caller may bypass per-user coupon rules, test another user's coupon eligibility, or produce inconsistent coupon usage behavior.

## Evidence

- Test cases: `BUG-FR09-002` and related FR09 trust-boundary cases.
- Local Newman report: `hw06/submit/newman/fr09-newman-report.json`.
- Source location: `backend/server.js`, `/api/apply-coupon`.

## Suggested fix

Require authentication for coupon application when user-specific checks are used, and derive the user id from the token:

```js
const userId = req.user.id;
```

Do not trust `user_id` from the request body for authorization or eligibility decisions.
````

### 2. Produce a passing CI run

Recommended commands:

```powershell
git add .github/workflows/newman-api-test.yml hw06/submit
git commit -m "hw06 add api testing artifacts and newman workflow"
git push
```

Then open GitHub Actions, wait for `Newman API Tests` to pass, and update `ci-cd/ci_cd_report.md` with:

- passing run URL
- passing screenshot filename
- passing commit hash

### 3. Produce a failing CI run

Important: `.github/workflows/newman-api-test.yml` must run the HW06 collection files under `hw06/submit/postman`. If the workflow still points to `mini_exercise_api/...`, changing `hw06/submit/postman/fr09-data.json` will not affect CI and the run can still pass.

Also make sure the pushed branch name matches the workflow trigger pattern `23127296*`. If you use a temporary branch with a different name, the push workflow may not run.

Use a temporary branch or temporary commit. One simple option is to change one expected status in `hw06/submit/postman/fr09-data.json`, for example set `FR09-001` expected status from `200` to `201`, then commit and push:

```powershell
git add .github/workflows/newman-api-test.yml hw06/submit/postman/fr09-data.json
git commit -m "hw06 demonstrate failing newman oracle"
git push
```

Capture the failed GitHub Actions run URL and screenshot. Then restore `fr09-data.json` to the passing version and commit/push the fix.

### 4. Optional Newman HTML report

If HTML is required, run:

```powershell
npm install -g newman-reporter-htmlextra
npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder "FR03 Password Recovery" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr03-data.json --reporters cli,htmlextra --reporter-htmlextra-export hw06/submit/newman/fr03-newman-report.html
npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder "FR09 Apply Coupon" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr09-data.json --reporters cli,htmlextra --reporter-htmlextra-export hw06/submit/newman/fr09-newman-report.html
npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder "FR13 Admin Orders" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr13-data.json --reporters cli,htmlextra --reporter-htmlextra-export hw06/submit/newman/fr13-newman-report.html
```

After generating HTML reports, add them to `README.md`, `main_report.md`, and `newman/execution_summary.md`.
