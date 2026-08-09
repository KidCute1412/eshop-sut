# HW04 Multi-Browser Execution Manifest

## Reconciled status

All nine selected feature/browser runs were attempted from automation/SUT revision `656991a598bafe43cbed13b54bf1ac3f429c30f2` and their complete HTML/JSON/metadata directories passed structural identity, timestamp, case-count, completion, and totals validation. The Playwright runner recorded 153 attempts: 102 reached assertions (64 passed and 38 failed) while 51 Firefox attempts failed during `newPage()` fixture setup before SUT observation.

The suite workflow is `npm run run:matrix`; each selected report now records the exact command and revision in `run-metadata.json`. The environment was Windows 10 Home Single Language / NT `10.0.26200.0`, Node.js `22.17.0`, npm `10.9.2`, Playwright `1.55.0`, Chromium `140.0.7339.16`, Firefox `141.0`, and WebKit `26.0`. Final URLs remain documented as local defaults.

| Run ID | Feature | Browser/mode | ISO timestamp | Report directory | Attempted | Passed | Recorded failed | Environment failures within failed | Assertion failures | Run status | Validator |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| `RUN-A-CHR` | FR-06 | Chromium / headless | `2026-08-09T17:11:54.712Z` | `automation/reports/fr06-chromium-2026-08-09T17-11-54-712Z/` | 16 | 10 | 6 | 0 | 6 | Fail | Passed |
| `RUN-A-FF` | FR-06 | Firefox / headful | `2026-08-09T17:13:19.066Z` | `automation/reports/fr06-firefox-2026-08-09T17-13-19-066Z/` | 16 | 0 | 16 | 16 | 0 | Fail | Passed |
| `RUN-A-WK` | FR-06 | WebKit / headless | `2026-08-09T17:16:10.035Z` | `automation/reports/fr06-webkit-2026-08-09T17-16-10-035Z/` | 16 | 10 | 6 | 0 | 6 | Fail | Passed |
| `RUN-B-CHR` | FR-10 | Chromium / headless | `2026-08-09T17:17:32.516Z` | `automation/reports/fr10-chromium-2026-08-09T17-17-32-516Z/` | 16 | 12 | 4 | 0 | 4 | Fail | Passed |
| `RUN-B-FF` | FR-10 | Firefox / headful | `2026-08-09T17:18:43.660Z` | `automation/reports/fr10-firefox-2026-08-09T17-18-43-660Z/` | 16 | 0 | 16 | 16 | 0 | Fail | Passed |
| `RUN-B-WK` | FR-10 | WebKit / headless | `2026-08-09T17:21:22.978Z` | `automation/reports/fr10-webkit-2026-08-09T17-21-22-978Z/` | 16 | 12 | 4 | 0 | 4 | Fail | Passed |
| `RUN-C-CHR` | FR-12 | Chromium / headless | `2026-08-09T17:22:38.418Z` | `automation/reports/fr12-chromium-2026-08-09T17-22-38-418Z/` | 19 | 10 | 9 | 0 | 9 | Fail | Passed |
| `RUN-C-FF` | FR-12 | Firefox / headful | `2026-08-09T17:28:39.697Z` | `automation/reports/fr12-firefox-2026-08-09T17-28-39-697Z/` | 19 | 0 | 19 | 19 | 0 | Fail | Passed |
| `RUN-C-WK` | FR-12 | WebKit / headless | `2026-08-09T17:27:20.694Z` | `automation/reports/fr12-webkit-2026-08-09T17-27-20-694Z/` | 19 | 10 | 9 | 0 | 9 | Fail | Passed |
| **Total** | **3 features** | **3 browsers** | — | **9 selected directories** | **153** | **64** | **89** | **51** | **38** | **9 failed runs** | **9 passed validation** |

Arithmetic checks:

- `64 passed + 38 assertion-failed + 51 fixture-failed = 153 attempted`; `102` reached assertions.
- `38 assertion failures + 51 environment failures = 89 recorded failed`.
- Logical cases: `16 + 16 + 19 = 51`; each was scheduled once in each of three browsers.

## Assertion-failing logical cases

| Feature | Unique case IDs | Unique cases | Assertion failures across browsers |
|---|---|---:|---:|
| FR-06 | `FR06-07`, `FR06-09`, `FR06-11`, `FR06-12`, `FR06-13`, `FR06-14` | 6 | 12 |
| FR-10 | `FR10-06`, `FR10-11`, `FR10-12`, `FR10-16` | 4 | 8 |
| FR-12 | `FR12-03`, `FR12-06`, `FR12-08`, `FR12-09`, `FR12-11`, `FR12-12`, `FR12-14`, `FR12-17`, `FR12-19` | 9 | 18 |
| **Total** | — | **19** | **38** |

## Firefox environment failures

Firefox was intentionally configured headful because headless Firefox launched but failed before `newPage()` in this Windows environment. The selected headful runs still contain intermittent page-setup failures with:

```text
Test timeout of 30000ms exceeded while setting up "page".
browserContext.newPage: Test timeout of 30000ms exceeded.
```

| Feature | Environment-failing case IDs | Count |
|---|---|---:|
| FR-06 | all 16 logical cases | 16 |
| FR-10 | all 16 logical cases | 16 |
| FR-12 | all 19 logical cases | 19 |
| **Total** | — | **51** |

These outcomes remain runner failures but are excluded from assertion-failure and SUT-defect counts because the target behavior was not observed.

## Superseded-run reconciliation

Diagnostic, pre-fix, and partial rerun directories were removed from the submission package; `automation/reports/` now contains only the nine selected directories above. An earlier WebKit FR-10 run contained a false `FR10-02` failure caused by substring row matching. Human review changed the locator to an exact order-ID cell and reran all FR-10 browsers; `FR10-02` passes in all three selected final reports.

The selected reports were generated from `656991a598bafe43cbed13b54bf1ac3f429c30f2`; the exact automation/SUT revision is recorded in every selected report metadata file.

## Remaining manual verification

- [x] Nine complete HTML/JSON/metadata report directories preserved.
- [x] Report validator accepted identity, timestamps, feature/browser matrix, case counts, completion, report/data-directory presence, and JSON/metadata totals.
- [ ] Student manually opens every selected HTML report and records reviewer/date.
- [x] OS, Node.js, npm, Playwright, and browser versions are recorded.
- [x] Exact execution revision is recorded in every selected report metadata file; final URLs remain local defaults pending student confirmation.
- [ ] Assertion failures are deduplicated, reproduced as needed, and linked to genuine public Issues/screenshots.
- [ ] Firefox environment limitations are explained in the video and oral defense if relevant.
