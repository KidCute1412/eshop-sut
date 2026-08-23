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

Use the three bug sections in `bug-reports/bug_report.md` as issue bodies:

1. `BUG-FR09-001 - Percent coupon formula returns negative discount`
2. `BUG-FR13-001 - Admin orders endpoint accepts any valid user token`
3. `BUG-FR09-002 - Coupon application is public despite using user_id-sensitive rules`

After creating each issue, update the line `GitHub issue screenshot/link: TODO` with the real issue URL and screenshot filename.

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

Use a temporary branch or temporary commit. One simple option is to change one expected status in `hw06/submit/postman/fr09-data.json`, for example set `FR09-001` expected status from `200` to `201`, then commit and push:

```powershell
git add hw06/submit/postman/fr09-data.json
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
