# HW04 Automation Testing Report

## Document control

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc |
| Student ID | 23127404 |
| Class | **PENDING — enter official class code** |
| Repository | https://github.com/KidCute1412/eshop-sut |
| Branch inspected | `23127404-LeTuanLoc` |
| Report status | Nine-run execution evidence reconciled; manual submission artifacts pending |
| Final submission timestamp | **PENDING — ISO 8601** |
| Execution revision | `656991a598bafe43cbed13b54bf1ac3f429c30f2`; recorded in every selected report metadata file |

## Executive summary

HW04 requires data-driven automation for the same three web features selected in HW02: FR-06 Product detail view, FR-10 Order state machine, and FR-12 Access control. Each feature requires at least 12 cases and execution on three browsers, producing at least nine attributable HTML reports overall.

The deliverables suite defines 51 external-data cases: 16 for FR-06, 16 for FR-10, and 19 for FR-12. All cases were scheduled on Chromium, Firefox, and WebKit in nine selected feature/browser runs. The nine complete HTML/JSON/metadata report directories passed structural identity, timestamp, case-count, completion, and totals validation. Across 153 browser attempts, 102 reached assertions: 64 passed and 38 failed across 19 unique logical cases. The other 51 attempts failed during Firefox `browserContext.newPage()` fixture setup before the test body could observe the SUT.

FR-06 produced 20 passes and 28 recorded failures across 48 executions; 16 failures were environmental and 12 were assertions. FR-10 produced 24 passes and 24 recorded failures across 48 executions; 16 were environmental and 8 were assertions. FR-12 produced 20 passes and 37 recorded failures across 57 executions; 19 were environmental and 18 were assertions.

Firefox was run headful after headless Firefox failed before `newPage()` on the assignment Windows environment. The headful final runs remained intermittently affected by `newPage()` timeouts; those failures are not counted as SUT defect candidates. The Markdown/PDF report set is complete. No public HW04 Issue URL or demo video is currently verified, and the four-day Git-history span remains noncompliant.

The full HW04 Git history contains nine qualifying test-script commits across 27 July and 9 August 2026, so the commit-count minimum is met. The separate four-calendar-day requirement remains noncompliant. This report does not infer, manufacture, or backdate missing history.

## 1. Scope and test oracle

| Pool | Requirement | Observable obligation | Source continuity |
|---|---|---|---|
| A | FR-06 — Product detail view | Show image, name, formatted price, description, and category; accept only positive integer quantity with minimum 1; provide visible add-to-cart feedback | HW02 FR-06 design and root `README.md` |
| B | FR-10 — Order state machine | Enforce permitted transitions across `pending`, `confirmed`, `shipping`, `delivered`, and `canceled`; preserve final states and role restrictions | HW02 FR-10 design and root `README.md` |
| C | FR-12 — Access control | Restrict Admin UI, `/api/admin/*`, and data-changing product/category/coupon APIs to a valid JWT with `role = 'admin'` | HW02 FR-12 design and root `README.md` |

The final 51-row matrix is in `../supporting-materials/test_case_matrix.md`, with IDs `FR06-01`–`FR06-16`, `FR10-01`–`FR10-16`, and `FR12-01`–`FR12-19`. It maps every actual external-data row to its spec and to the Chromium, Firefox, and WebKit outcome/report path.

## 2. Test design and traceability

### 2.1 Coverage targets

| Feature | Planned IDs | Positive | Negative/boundary/edge focus | Automated now | Final evidence |
|---|---|---|---|---:|---|
| FR-06 | Source `FR06-01`–`FR06-16` | Existing products and valid quantity boundaries | Content/format, quantity constraints, feedback, unknown ID | 16 cases × 3 browsers | 48 attempted; 32 reached assertions: 20 pass, 12 fail; 16 fixture failures |
| FR-10 | Source `FR10-01`–`FR10-16` | Permitted admin/user transitions | Skipped transitions, role limits, and final-state exits | 16 cases × 3 browsers | 48 attempted; 32 reached assertions: 24 pass, 8 fail; 16 fixture failures |
| FR-12 | Source `FR12-01`–`FR12-19` | Authorized Admin UI/API operations | Guest/user/malformed authorization and protected mutations | 19 cases × 3 browsers | 57 attempted; 38 reached assertions: 20 pass, 18 fail; 19 fixture failures |

### 2.2 Required row-level traceability

Every final case must map through the following chain:

`Requirement → case ID → external data ID → test title/spec path → browser run ID → HTML report/evidence → defect/Issue when failed`

The final matrix must record concrete preconditions, test data, steps, expected result, priority, automation decision, script path, and evidence reference. A case marked `Fail` must reference a defect or a documented non-SUT failure classification.

## 3. Automation implementation

### 3.1 Current inventory

| Feature | Spec file | External data | Data-driven proof | Assertion patterns | Setup/cleanup | State |
|---|---|---|---|---|---|---|
| FR-06 | `../automation/tests/fr06-product-detail.spec.ts` | `../automation/test-data/fr06-product-detail.json` | `loadCases(..., 12)` loads 16 rows | Text/content, visibility, count, attribute, value/validity | View cases plus cart-state-sensitive actions | Attempted in 3 selected reports |
| FR-10 | `../automation/tests/fr10-order-state-machine.spec.ts` | `../automation/test-data/fr10-order-state-machine.json` | `loadCases(..., 12)` loads 16 rows | HTTP status/body, persisted state, visibility and button count | API driver arranges a fresh order state per row | Attempted in 3 selected reports |
| FR-12 | `../automation/tests/fr12-access-control.spec.ts` | `../automation/test-data/fr12-access-control.json` | `loadCases(..., 12)` loads 19 rows | HTTP status/content type/body plus Admin/Login UI visibility | Disposable mutations with cleanup helper | Attempted in 3 selected reports |

### 3.2 Current Playwright configuration

The deliverables suite pins Playwright `1.55.0` and defines Chromium, Firefox, and WebKit projects. It uses Playwright web-first assertions, `workers: 1`, CI-only retry, screenshots/traces/videos on failure, and a custom metadata reporter. Its report key includes feature, browser, and an ISO-derived timestamp; metadata includes `Run by: 23127404`, feature, browser, and timestamp.

The legacy bundle outside deliverables still produces one combined `playwright-report` directory. The new `run:matrix` workflow is intended to preserve distinct feature/browser report directories under the automation workspace. Each generated directory must still be opened and verified before it enters the final manifest.

### 3.3 Final implementation inventory template

| Feature | Case count | Spec file(s) | Data file(s) | Locator strategy | Assertions | Isolation/reset | Reviewer approval |
|---|---:|---|---|---|---|---|---|
| FR-06 | 16 source rows | `../automation/tests/fr06-product-detail.spec.ts` | `../automation/test-data/fr06-product-detail.json` | Roles plus scoped CSS where no stable semantic locator exists | Text, visibility, count, attribute, value/validity | Executed serially on 3 browsers | Human evidence triage recorded; final student sign-off pending |
| FR-10 | 16 source rows | `../automation/tests/fr10-order-state-machine.spec.ts` | `../automation/test-data/fr10-order-state-machine.json` | API arrangement plus exact order-cell/row locators | Status/body, persisted state, visibility/count | Fresh arranged order per row | Substring locator corrected and all FR-10 runs repeated |
| FR-12 | 19 source rows | `../automation/tests/fr12-access-control.spec.ts` | `../automation/test-data/fr12-access-control.json` | API assertions plus Admin/Login headings | Status, content type/body, visibility | Cleanup helper for created probes | Executed; access-control failures retained |

## 4. Execution and multi-browser evidence

### 4.1 Environment record

| Field | Final value |
|---|---|
| Operating system | Windows 10 Home Single Language; Windows NT `10.0.26200.0` |
| Node.js / npm | Node.js `22.17.0`; npm `10.9.2` |
| Playwright | `1.55.0` |
| Browser modes/versions | Chromium `140.0.7339.16` headless; Firefox `141.0` headful; WebKit `26.0` headless |
| Frontend URL | Current default `http://localhost:5173`; **confirm final URL** |
| Backend URL | Current default `http://localhost:3000`; **confirm final URL** |
| Execution revision/data seed | `656991a598bafe43cbed13b54bf1ac3f429c30f2`; reports generated from clean seed database and metadata records the revision/command |
| Execution operator | Lê Tuấn Lộc — 23127404 |

### 4.2 Historical repository evidence — excluded from final totals

| Evidence | Repository-recorded value | Qualification |
|---|---|---|
| Logical case | `FR06-DT-01` | One view-only FR-06 case |
| Browsers represented | Chromium, Firefox, WebKit | Stored in one combined report |
| Recorded timestamp | `2026-07-27T08:11:08.301Z` | Taken from the existing student report/report metadata |
| Recorded result | 0 passed, 3 failed | Report says each browser failed at the category assertion |
| Preserved report | `../../schools/23127404-automation/playwright-report/index.html` plus assets | Historical only; not copied into the final nine-run structure |
| Defect status | Candidate only for this HW04 package | No verified HW04 public Issue URL recorded here |

The preceding row is provenance-aware reporting of an existing artifact. It does not establish that the environment remains unchanged or that the current SUT still exhibits the behavior.

### 4.3 Final execution ledger

| Run ID | Feature/browser | ISO timestamp | Attempted | Passed | Recorded failed | Environment failures within failed | Selected report directory |
|---|---|---|---:|---:|---:|---:|---|
| `RUN-A-CHR` | FR-06 / Chromium | `2026-08-09T17:11:54.712Z` | 16 | 10 | 6 | 0 | `automation/reports/fr06-chromium-2026-08-09T17-11-54-712Z/` |
| `RUN-A-FF` | FR-06 / Firefox | `2026-08-09T17:13:19.066Z` | 16 | 0 | 16 | 16 | `automation/reports/fr06-firefox-2026-08-09T17-13-19-066Z/` |
| `RUN-A-WK` | FR-06 / WebKit | `2026-08-09T17:16:10.035Z` | 16 | 10 | 6 | 0 | `automation/reports/fr06-webkit-2026-08-09T17-16-10-035Z/` |
| `RUN-B-CHR` | FR-10 / Chromium | `2026-08-09T17:17:32.516Z` | 16 | 12 | 4 | 0 | `automation/reports/fr10-chromium-2026-08-09T17-17-32-516Z/` |
| `RUN-B-FF` | FR-10 / Firefox | `2026-08-09T17:18:43.660Z` | 16 | 0 | 16 | 16 | `automation/reports/fr10-firefox-2026-08-09T17-18-43-660Z/` |
| `RUN-B-WK` | FR-10 / WebKit | `2026-08-09T17:21:22.978Z` | 16 | 12 | 4 | 0 | `automation/reports/fr10-webkit-2026-08-09T17-21-22-978Z/` |
| `RUN-C-CHR` | FR-12 / Chromium | `2026-08-09T17:22:38.418Z` | 19 | 10 | 9 | 0 | `automation/reports/fr12-chromium-2026-08-09T17-22-38-418Z/` |
| `RUN-C-FF` | FR-12 / Firefox | `2026-08-09T17:28:39.697Z` | 19 | 0 | 19 | 19 | `automation/reports/fr12-firefox-2026-08-09T17-28-39-697Z/` |
| `RUN-C-WK` | FR-12 / WebKit | `2026-08-09T17:27:20.694Z` | 19 | 10 | 9 | 0 | `automation/reports/fr12-webkit-2026-08-09T17-27-20-694Z/` |
| **Total** | **3 features / 3 browsers** | — | **153 attempts** | **64** | **89** | **51** | **Nine structurally validated directories** |

The 89 runner failures equal 38 assertion failures plus 51 Firefox environment failures. All nine selected HTML/JSON/metadata report sets passed structural identity, timestamp, case-count, completion, report/data-directory presence, and totals validation. Each selected report metadata file records the exact `node scripts/run-matrix.mjs` command and revision `656991a598bafe43cbed13b54bf1ac3f429c30f2`.

The selected reports were generated from revision `656991a598bafe43cbed13b54bf1ac3f429c30f2`; the revision is embedded in every report metadata file and HTML attribution banner.

## 5. Human review and AI gap analysis

Human review retained strict requirement assertions, corrected one demonstrated locator defect, reran FR-10, and separated Firefox infrastructure symptoms from SUT behavior.

| Feature/case | AI proposal or risk | Why insufficient | Human correction visible/documented | Evidence state |
|---|---|---|---|---|
| FR-06 / `FR06-07` | A happy-path check could omit category | FR-06 explicitly requires category; a reduced oracle could create a false pass | Exact category assertion was retained | Failed by assertion in all three final browser runs |
| FR-06 / locators | CSS selectors could couple tests to styling | Classes are not stable user-facing contracts | Roles, accessible names, and exact text are preferred; scoped CSS remains only for price styling where semantic hooks are absent | Visible in final spec and reports |
| FR-06 / data | Inline literals would violate data-driven requirement | Inline test arrays/objects are explicitly disallowed | Input and expected values were moved to external JSON | Visible in current spec/data |
| FR-06 / waits | Fixed sleeps could hide timing defects and cause flakiness | Duration is environment-dependent | Playwright assertions and auto-waiting are used | Visible in current spec |
| FR-10 / `FR10-02` | Initial row filtering used substring matching for an order ID | Order `#2` could match rows such as `#20`, producing a false WebKit failure | Filter now requires an exact table cell for `#<orderId>`; all three FR-10 runs were repeated | `FR10-02` no longer fails in the selected final Chromium, Firefox, or WebKit reports |
| Firefox environment | A browser failure could be misreported as a product defect | Headless Firefox failed before `newPage()`; headful runs still had page-setup timeouts | Firefox configured headful; 51 `newPage()` timeouts classified as environment failures | Final Firefox JSON reports: 16 FR-06, 16 FR-10, 19 FR-12 environment failures |
| FR-12 / authorization assertions | Passing over status mismatches would hide security behavior | FR-12 requires valid admin JWT and role for protected endpoints | Expected 401/403 assertions were retained; actual 200/400 responses remain failures | 18 assertion failures across nine logical cases in the selected reports |

The mandatory critique is in `ai_critique.md`. The interaction record is in `ai_audit_report.md`.

## 6. Defects and issue tracking

The final runs produced 38 assertion failures across 19 unique logical cases: six FR-06, four FR-10, and nine FR-12 cases. These are documented as runtime-observed candidates in `../bugs/bug_report.md`; the 51 Firefox `newPage()` failures are documented separately as environment failures. No candidate is represented as a filed GitHub defect because no verified public HW04 Issue URL or attached public screenshot has been supplied.

For every final failure:

1. complete case-level triage and rule out any remaining locator, assertion, data, authentication, state-reset, browser-installation, or infrastructure fault;
2. retest once when safe;
3. preserve the report, trace, and authentic screenshot;
4. create one deduplicated GitHub Issue for the root behavior; and
5. reconcile case IDs, run IDs, evidence references, and Issue URL in both bug files.

Prior HW02/HW03 issues may support regression context but are not evidence that a new HW04 Issue was filed or verified.

## 7. AI use

Required declaration: **I use AI tools for the following tasks,** preparing automation and submission documentation, reviewing traceability and evidence integrity, and drafting structured templates. The surviving audit history is incomplete: one historical exact prompt was not retained, and that omission is disclosed rather than reconstructed. See `ai_audit_report.md`.

## 8. Git history

The exported log in `../git/23127404_HW04_git_commit_log.txt` contains nine qualifying `.spec.ts` commits: legacy `f905546` on 27 July 2026 plus eight deliverables-suite commits from `f732b2c` through `aa316e0` on 9 August 2026. The commit minimum is met across two calendar days. The separate four-day requirement remains **noncompliant**; documentation commits do not change the qualifying span, and the shortfall must not be hidden through backdating or altered timestamps.

## 9. Demonstration videos and Agent Skill

| Item | Requirement | Current status | Evidence |
|---|---|---|---|
| Main demo | Unlisted YouTube, at least 5 minutes, Vietnamese narration, end-to-end script, multi-browser run/report, one human fix, authorship evidence | Not recorded | `../video/demo_video.md` |
| Agent Skill | Reusable data-driven multi-browser workflow plus separate end-to-end video | Source present; end-to-end validation/demo not verified | `../agent-skill/playwright-data-driven-multibrowser/`; `../video/agent_skill_demo.md` |

The Agent Skills assessment category is currently claimed as 0/10. Complete source exists, but this must change only after a valid end-to-end demonstration is recorded and verified.

## 10. Limitations and remaining work

- The 51 cases have qualifying selected reports, but the exact execution commit and verbatim per-run shell commands were not embedded/retained. Environment and browser versions are recorded.
- The 19 assertion-failing cases require final root-cause deduplication, public GitHub Issues, and authentic Issue screenshots before they can be claimed as submitted defects.
- Firefox produced 51 `newPage()` environment failures even in headful mode; those cases were not observed by the SUT assertions.
- Historical and current AI logs still require complete prompt/output coverage for every generation/review interaction.
- Environment and browser versions are recorded; the exact execution revision remains unavailable because it was not embedded in the selected reports.
- No HW04 public Issue URL or final defect screenshot is verified.
- Both video links are absent; the main demo is mandatory, and Agent Skill points cannot be claimed from source alone.
- Historical AI logging lacks at least one exact prompt and timestamp.
- Nine qualifying commits are present across two days; the four-calendar-day history requirement remains unsatisfied.
- Markdown-to-PDF exports are complete and text-validated; the final archive must be regenerated after student-controlled URLs and identity fields are supplied.

## 11. Final reconciliation table

This table is reconciled from the nine selected final JSON reports and their environment triage.

| Measure | FR-06 | FR-10 | FR-12 | Total |
|---|---:|---:|---:|---:|
| Designed logical cases | 16 | 16 | 19 | **51** |
| Automated logical cases | 16 | 16 | 19 | **51** |
| Browser attempts | 48 | 48 | 57 | **153** |
| Attempts reaching assertions | 32 | 32 | 38 | **102** |
| Passed assertions | 20 | 24 | 20 | **64** |
| Recorded runner failures | 28 | 24 | 37 | **89** |
| Environment failures within recorded failures | 16 | 16 | 19 | **51** |
| Assertion failures | 12 | 8 | 18 | **38** |
| Unique assertion-failing logical cases | 6 | 4 | 9 | **19** |
| Verified public HW04 Issues | 0 | 0 | 0 | **0** |

The arithmetic reconciles: `64 + 38 + 51 = 153`, `64 + 38 = 102`, and `38 + 51 = 89`. Issue counts must be updated only from verified public URLs.
