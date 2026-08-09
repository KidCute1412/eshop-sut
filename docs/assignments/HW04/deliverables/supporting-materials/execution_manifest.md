# HW04 Multi-Browser Execution Manifest

## Reconciled status

All nine selected feature/browser runs were attempted and their complete HTML/JSON/metadata directories passed structural identity, timestamp, case-count, completion, and totals validation. The Playwright runner recorded 153 attempts: 131 reached assertions (79 passed and 52 failed) while 22 Firefox attempts failed during `newPage()` fixture setup before SUT observation.

The suite workflow is `npm run run:matrix`; a verbatim shell invocation for each individual selected run was not separately retained. The environment was Windows 10 Home Single Language / NT `10.0.26200.0`, Node.js `22.17.0`, npm `10.9.2`, Playwright `1.55.0`, Chromium `140.0.7339.16`, Firefox `141.0`, and WebKit `26.0`. Final URLs are not embedded in the selected report metadata. The reports predate `aa316e0`; their exact execution revision is not provable and was likely a pre-`aa316e0` local state around `238cf27` or `532ebc2`, depending on the run.

| Run ID | Feature | Browser/mode | ISO timestamp | Report directory | Attempted | Passed | Recorded failed | Environment failures within failed | Assertion failures | Run status | Validator |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| `RUN-A-CHR` | FR-06 | Chromium / headless | `2026-08-09T09:50:04.895Z` | `automation/reports/fr06-chromium-2026-08-09T09-50-04-895Z/` | 16 | 10 | 6 | 0 | 6 | Fail | Passed |
| `RUN-A-FF` | FR-06 | Firefox / headful | `2026-08-09T10:07:59.582Z` | `automation/reports/fr06-firefox-2026-08-09T10-07-59-582Z/` | 16 | 5 | 11 | 7 | 4 | Fail | Passed |
| `RUN-A-WK` | FR-06 | WebKit / headless | `2026-08-09T09:52:14.569Z` | `automation/reports/fr06-webkit-2026-08-09T09-52-14-569Z/` | 16 | 10 | 6 | 0 | 6 | Fail | Passed |
| `RUN-B-CHR` | FR-10 | Chromium / headless | `2026-08-09T10:26:40.345Z` | `automation/reports/fr10-chromium-2026-08-09T10-26-40-345Z/` | 16 | 12 | 4 | 0 | 4 | Fail | Passed |
| `RUN-B-FF` | FR-10 | Firefox / headful | `2026-08-09T10:27:32.954Z` | `automation/reports/fr10-firefox-2026-08-09T10-27-32-954Z/` | 16 | 5 | 11 | 7 | 4 | Fail | Passed |
| `RUN-B-WK` | FR-10 | WebKit / headless | `2026-08-09T10:32:34.318Z` | `automation/reports/fr10-webkit-2026-08-09T10-32-34-318Z/` | 16 | 12 | 4 | 0 | 4 | Fail | Passed |
| `RUN-C-CHR` | FR-12 | Chromium / headless | `2026-08-09T09:56:03.803Z` | `automation/reports/fr12-chromium-2026-08-09T09-56-03-803Z/` | 19 | 10 | 9 | 0 | 9 | Fail | Passed |
| `RUN-C-FF` | FR-12 | Firefox / headful | `2026-08-09T10:18:54.806Z` | `automation/reports/fr12-firefox-2026-08-09T10-18-54-806Z/` | 19 | 5 | 14 | 8 | 6 | Fail | Passed |
| `RUN-C-WK` | FR-12 | WebKit / headless | `2026-08-09T09:57:54.553Z` | `automation/reports/fr12-webkit-2026-08-09T09-57-54-553Z/` | 19 | 10 | 9 | 0 | 9 | Fail | Passed |
| **Total** | **3 features** | **3 browsers** | — | **9 selected directories** | **153** | **79** | **74** | **22** | **52** | **9 failed runs** | **9 passed validation** |

Arithmetic checks:

- `79 passed + 52 assertion-failed + 22 fixture-failed = 153 attempted`; `131` reached assertions.
- `52 assertion failures + 22 environment failures = 74 recorded failed`.
- Logical cases: `16 + 16 + 19 = 51`; each was scheduled once in each of three browsers.

## Assertion-failing logical cases

| Feature | Unique case IDs | Unique cases | Assertion failures across browsers |
|---|---|---:|---:|
| FR-06 | `FR06-07`, `FR06-09`, `FR06-11`, `FR06-12`, `FR06-13`, `FR06-14` | 6 | 16 |
| FR-10 | `FR10-06`, `FR10-11`, `FR10-12`, `FR10-16` | 4 | 12 |
| FR-12 | `FR12-03`, `FR12-06`, `FR12-08`, `FR12-09`, `FR12-11`, `FR12-12`, `FR12-14`, `FR12-17`, `FR12-19` | 9 | 24 |
| **Total** | — | **19** | **52** |

## Firefox environment failures

Firefox was intentionally configured headful because headless Firefox launched but failed before `newPage()` in this Windows environment. The selected headful runs still contain intermittent page-setup failures with:

```text
Test timeout of 30000ms exceeded while setting up "page".
browserContext.newPage: Test timeout of 30000ms exceeded.
```

| Feature | Environment-failing case IDs | Count |
|---|---|---:|
| FR-06 | `FR06-02`, `FR06-04`, `FR06-06`, `FR06-08`, `FR06-11`, `FR06-12`, `FR06-16` | 7 |
| FR-10 | `FR10-01`, `FR10-03`, `FR10-05`, `FR10-08`, `FR10-10`, `FR10-13`, `FR10-15` | 7 |
| FR-12 | `FR12-02`, `FR12-04`, `FR12-05`, `FR12-08`, `FR12-11`, `FR12-14`, `FR12-16`, `FR12-18` | 8 |
| **Total** | — | **22** |

These outcomes remain runner failures but are excluded from assertion-failure and SUT-defect counts because the target behavior was not observed.

## Superseded-run reconciliation

Diagnostic, pre-fix, and partial rerun directories were removed from the submission package; `automation/reports/` now contains only the nine selected directories above. An earlier WebKit FR-10 run contained a false `FR10-02` failure caused by substring row matching. Human review changed the locator to an exact order-ID cell and reran all FR-10 browsers; `FR10-02` passes in all three selected final reports.

Current source at `aa316e0` attaches the full external case contract to each newly generated result. The selected reports predate that enhancement and must not be labelled as `aa316e0` executions; their test titles and stable case IDs provide the retained data/report linkage.

## Remaining manual verification

- [x] Nine complete HTML/JSON/metadata report directories preserved.
- [x] Report validator accepted identity, timestamps, feature/browser matrix, case counts, completion, report/data-directory presence, and JSON/metadata totals.
- [ ] Student manually opens every selected HTML report and records reviewer/date.
- [x] OS, Node.js, npm, Playwright, and browser versions are recorded.
- [ ] Exact execution revision and final URLs remain unavailable from report metadata; retain the explicit qualification.
- [ ] Assertion failures are deduplicated, reproduced as needed, and linked to genuine public Issues/screenshots.
- [ ] Firefox environment limitations are explained in the video and oral defense if relevant.
