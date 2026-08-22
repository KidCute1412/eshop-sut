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

The suite was executed locally on 2026-08-22 against `http://localhost:3000`.

| API | Iterations | Requests | Assertions | Failed |
|---|---:|---:|---:|---:|
| FR03 | 42 | 68 | 168 | 0 |
| FR09 | 37 | 37 | 148 | 0 |
| FR13 | 36 | 68 | 144 | 0 |

Report files:

- `newman/fr03-newman-report.json`
- `newman/fr09-newman-report.json`
- `newman/fr13-newman-report.json`

## Additional technical requirements checklist

- Postman collection: ready.
- Environment variables: `baseUrl`, `studentId`.
- Data-driven runs: one JSON data file per selected API.
- Pre-request script: injects `X-Student-Id` and obtains tokens where needed.
- Newman JSON reports: generated after local execution.
- HTML report: can be produced by adding `htmlextra` or `html` reporter if installed; currently marked TODO if unavailable.
- CI/CD: workflow template and report notes are prepared; real GitHub screenshots/links must be filled after pushing commits.
