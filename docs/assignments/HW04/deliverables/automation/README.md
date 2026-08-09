# HW04 Playwright automation — 23127404

Fresh TypeScript automation for EShop FR-06 Product Detail (16 cases), FR-10 Order State Machine (16 cases), and FR-12 Access Control (19 cases): **51 data-driven cases total**. Every case is defined in an external JSON file and runs in Chromium, Firefox, and WebKit.

No generated report in this directory is submission evidence until the suite has actually run and been reviewed. Runtime reports are created under `reports/<feature>-<browser>-<ISO timestamp>/` with a visible title containing `Run by: 23127404` and the ISO timestamp. The selected nine report directories are intentionally versioned for submission; `run-metadata.json` records the same identity, feature, browser, status, duration, and test count.

## Prerequisites and SUT

Use three terminals from the repository root:

```powershell
Set-Location backend; npm install; node server.js
Set-Location frontend-web; npm install; npm run dev -- --host 127.0.0.1 --port 5173
Set-Location frontend-admin; npm install; npm run dev -- --host 127.0.0.1 --port 5174
```

Starting the backend executes its existing database initialization, which resets seed data. Do not start it against data you intend to preserve.

Install this bundle from `docs/assignments/HW04/deliverables/automation`:

```powershell
npm install
npx playwright install chromium firefox webkit
npm run check:sut
npm run check
```

Default URLs can be overridden with `API_URL`, `WEB_URL`, and `ADMIN_URL`.
The Firefox project uses the Playwright-managed headless binary with an
option-free context. The previous `Desktop Firefox` device options caused
`browserContext.newPage()` failures on this Windows environment; removing
those options was verified by a smoke test and a complete 51-case Firefox
rerun. Chromium and WebKit remain headless.

## Execution

Run the complete nine-run matrix:

```powershell
npm run run:matrix
npm run reports:validate
```

Run a subset while developing:

```powershell
node scripts/run-matrix.mjs --feature fr06 --browser chromium
node scripts/validate-reports.mjs --allow-partial
```

Direct `npm run test:fr06`, `test:fr10`, and `test:fr12` commands run all three projects into one local report; use the matrix runner for required separate feature/browser evidence. The matrix continues after a failed run so every genuine result can be preserved, then returns a non-zero exit code if any run failed.

FR-10 creates uniquely identified orders because the SUT has no order-delete API. FR-12 sends cleanup requests for disposable records created during authorization probes in a `finally` block; the current helper does not assert the cleanup response or verify absence, which is a documented limitation. Tests are serial (`workers: 1`) to avoid shared SQLite state races. Failures against known or new SUT behavior remain failures; no expected-failure annotations mask defects.

## Traceability and outputs

- `test-data/*.json`: executable external case rows, priorities, EP/BVA IDs, actions, and expected statuses/states.
- `tests/*.spec.ts`: one generated Playwright test per JSON row; FR-10 and FR-12 combine API oracles with browser-visible UI checks.
- `TEST-DESIGN.md`: requirement partitions, boundaries, and suite mapping.
- `src/api-driver.ts`: login, isolated order arrangement, transitions, and state retrieval.
- `scripts/check-sut.mjs`: read-only availability check for all three components.
- `scripts/run-matrix.mjs`: nine separate report runs with runtime identity metadata.
- `scripts/validate-reports.mjs`: verifies the nine-cell structure, report/data-directory presence, student ID, ISO timestamp, completion, expected case counts, and JSON/metadata totals. Manual opening is still required to verify interactive links and rendering.
- `scripts/generate-traceability.mjs`: rebuilds the actual 51-row case/data/spec/browser-result matrix from external data and selected JSON reports.
- `scripts/export-git-log.mjs`: exports committed `.spec.ts` history; it refuses to invent an empty history.
- `scripts/package-source.mjs`: creates an automation-source-only convenience ZIP and excludes dependencies, runtime results, and selected submission reports.

After qualifying commits exist, use `npm run git:export`. `npm run package:source` creates `dist/23127404_HW04_Automation_Source.zip`; this is a source convenience archive, not the assignment's final self-assessed submission archive.
