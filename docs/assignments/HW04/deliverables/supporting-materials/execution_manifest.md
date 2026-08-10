# HW04 Multi-Browser Execution Manifest

## Reconciled status

All nine selected feature/browser runs and their complete HTML/JSON/metadata directories passed structural identity, timestamp, case-count, completion, and totals validation. The Playwright runner recorded 153 attempts: all 153 reached assertions (96 passed and 57 failed). The Firefox rerun used revision `a390bc125713a1759443a4e84929641d432a45dc` with an option-free headless context.

The suite workflow is `npm run run:matrix`; each selected report now records the exact command and revision in `run-metadata.json`. The environment was Windows 10 Home Single Language / NT `10.0.26200.0`, Node.js `22.17.0`, npm `10.9.2`, Playwright `1.55.0`, Chromium `140.0.7339.16`, Firefox `141.0`, and WebKit `26.0`. Final URLs remain documented as local defaults.

| Run ID | Feature | Browser/mode | ISO timestamp | Report directory | Attempted | Passed | Recorded failed | Environment failures within failed | Assertion failures | Run status | Validator |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| `RUN-A-CHR` | FR-06 | Chromium / headless | `2026-08-09T17:11:54.712Z` | `automation/reports/fr06-chromium-2026-08-09T17-11-54-712Z/` | 16 | 10 | 6 | 0 | 6 | Fail | Passed |
| `RUN-A-FF` | FR-06 | Firefox / headless | `2026-08-09T18:19:41.178Z` | `automation/reports/fr06-firefox-2026-08-09T18-19-41-178Z/` | 16 | 10 | 6 | 0 | 6 | Fail | Passed |
| `RUN-A-WK` | FR-06 | WebKit / headless | `2026-08-09T17:16:10.035Z` | `automation/reports/fr06-webkit-2026-08-09T17-16-10-035Z/` | 16 | 10 | 6 | 0 | 6 | Fail | Passed |
| `RUN-B-CHR` | FR-10 | Chromium / headless | `2026-08-09T17:17:32.516Z` | `automation/reports/fr10-chromium-2026-08-09T17-17-32-516Z/` | 16 | 12 | 4 | 0 | 4 | Fail | Passed |
| `RUN-B-FF` | FR-10 | Firefox / headless | `2026-08-09T18:21:10.553Z` | `automation/reports/fr10-firefox-2026-08-09T18-21-10-553Z/` | 16 | 12 | 4 | 0 | 4 | Fail | Passed |
| `RUN-B-WK` | FR-10 | WebKit / headless | `2026-08-09T17:21:22.978Z` | `automation/reports/fr10-webkit-2026-08-09T17-21-22-978Z/` | 16 | 12 | 4 | 0 | 4 | Fail | Passed |
| `RUN-C-CHR` | FR-12 | Chromium / headless | `2026-08-09T17:22:38.418Z` | `automation/reports/fr12-chromium-2026-08-09T17-22-38-418Z/` | 19 | 10 | 9 | 0 | 9 | Fail | Passed |
| `RUN-C-FF` | FR-12 | Firefox / headless | `2026-08-09T18:22:31.674Z` | `automation/reports/fr12-firefox-2026-08-09T18-22-31-674Z/` | 19 | 10 | 9 | 0 | 9 | Fail | Passed |
| `RUN-C-WK` | FR-12 | WebKit / headless | `2026-08-09T17:27:20.694Z` | `automation/reports/fr12-webkit-2026-08-09T17-27-20-694Z/` | 19 | 10 | 9 | 0 | 9 | Fail | Passed |
| **Total** | **3 features** | **3 browsers** | — | **9 selected directories** | **153** | **96** | **57** | **0** | **57** | **9 failed runs** | **9 passed validation** |

Arithmetic checks:

- `96 passed + 57 assertion-failed = 153 attempted`; all `153` reached assertions.
- `57 recorded failures = 57 assertion failures + 0 environment failures`.
- Logical cases: `16 + 16 + 19 = 51`; each was scheduled once in each of three browsers.

## Assertion-failing logical cases

| Feature | Unique case IDs | Unique cases | Assertion failures across browsers |
|---|---|---:|---:|
| FR-06 | `FR06-07`, `FR06-09`, `FR06-11`, `FR06-12`, `FR06-13`, `FR06-14` | 6 | 18 |
| FR-10 | `FR10-06`, `FR10-11`, `FR10-12`, `FR10-16` | 4 | 12 |
| FR-12 | `FR12-03`, `FR12-06`, `FR12-08`, `FR12-09`, `FR12-11`, `FR12-12`, `FR12-14`, `FR12-17`, `FR12-19` | 9 | 27 |
| **Total** | — | **19** | **57** |

## Firefox configuration correction

The prior Firefox reports failed during `browserContext.newPage()` because the `Desktop Firefox` device options were incompatible with this Windows/Firefox combination. The final project uses the Playwright-managed headless binary with an option-free context. A smoke test and all 51 Firefox cases completed fixture setup; final Firefox failures are assertion results, not environment failures. The following signature/table describe only the superseded diagnostic run, not final totals:

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

The old environment-failure reports were removed from the selected evidence set and are not included in final totals.

## Superseded-run reconciliation

Diagnostic, pre-fix, and partial rerun directories were removed from the submission package; `automation/reports/` now contains only the nine selected directories above. An earlier WebKit FR-10 run contained a false `FR10-02` failure caused by substring row matching. Human review changed the locator to an exact order-ID cell and reran all FR-10 browsers; `FR10-02` passes in all three selected final reports.

The final Firefox reports were generated from `a390bc125713a1759443a4e84929641d432a45dc`; each selected report metadata file records its exact automation/SUT revision.

## Remaining manual verification

- [x] Nine complete HTML/JSON/metadata report directories preserved.
- [x] Report validator accepted identity, timestamps, feature/browser matrix, case counts, completion, report/data-directory presence, and JSON/metadata totals.
- [ ] Student manually opens every selected HTML report and records reviewer/date.
- [x] OS, Node.js, npm, Playwright, and browser versions are recorded.
- [x] Exact execution revision is recorded in every selected report metadata file; the selected runs intentionally use the documented local SUT defaults and make no public-deployment claim.
- [x] Assertion failures are deduplicated, triaged, and linked to genuine public Issues/local screenshots; two oracle-gap candidates are explicitly rejected.
- [ ] Firefox environment limitations are explained in the video and oral defense if relevant.
