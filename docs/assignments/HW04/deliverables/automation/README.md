# HW04 Playwright automation — 23127404

Fresh TypeScript automation for EShop FR-06 Product Detail (16 cases), FR-10 Order State Machine (16 cases), and FR-12 Access Control (19 cases): **51 data-driven cases total**. Every case is defined in an external JSON file and runs in Chromium, Firefox, and WebKit.

No generated report in this directory is submission evidence until the suite has actually run. Runtime reports are ignored by Git and are created under `reports/<feature>-<browser>-<ISO timestamp>/` with a visible title containing `Run by: 23127404` and the ISO timestamp. `run-metadata.json` records the same identity, feature, browser, status, duration, and test count.

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
The Firefox project intentionally runs headful on this Windows environment:
headless Firefox launches but fails in Playwright before `newPage()`, while a
minimal headful smoke test succeeds. Chromium and WebKit remain headless.

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

FR-10 creates uniquely identified orders because the SUT has no order-delete API. FR-12 uses disposable records and cleans up any record created during an authorization probe in a `finally` block. Tests are serial (`workers: 1`) to avoid shared SQLite state races. Failures against known or new SUT behavior remain failures; no expected-failure annotations mask defects.

## Traceability and outputs

- `test-data/*.json`: executable external case rows, priorities, EP/BVA IDs, actions, and expected statuses/states.
- `tests/*.spec.ts`: one generated Playwright test per JSON row; FR-10 and FR-12 combine API oracles with browser-visible UI checks.
- `TEST-DESIGN.md`: requirement partitions, boundaries, and suite mapping.
- `src/api-driver.ts`: login, isolated order arrangement, transitions, and state retrieval.
- `scripts/check-sut.mjs`: read-only availability check for all three components.
- `scripts/run-matrix.mjs`: nine separate report runs with runtime identity metadata.
- `scripts/validate-reports.mjs`: verifies full HTML assets, student ID, ISO timestamp, completion, and matrix coverage.
- `scripts/export-git-log.mjs`: exports committed `.spec.ts` history; it refuses to invent an empty history.
- `scripts/package-source.mjs`: creates an automation-only ZIP and excludes dependencies/results.

After qualifying commits exist, use `npm run git:export`. `npm run package:source` creates `dist/23127404_HW04_Automation_Source.zip`; this is a source convenience archive, not the assignment's final self-assessed submission archive.
