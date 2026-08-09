# HW04 Evidence Register

## Evidence-state policy

- `Verified existing`: file and relevant metadata were inspected in this repository.
- `Historical claim`: described by a preserved report but not rerun during this preparation.
- `Not Collected`: required evidence does not yet exist in this deliverables package.
- `PENDING verification`: a student-controlled external artifact must be opened and checked.

## Current register

| Evidence ID | Artifact | Requirement/run linkage | State | Integrity/provenance note |
|---|---|---|---|---|
| `EV-LEG-001` | `../../schools/23127404-automation/tests/fr06-product-detail.spec.ts` | FR-06 / historical `FR06-DT-01` | Verified existing | Source code only; does not prove runtime outcome |
| `EV-LEG-002` | `../../schools/23127404-automation/test-data/fr06-product-detail.json` | FR-06 / historical `FR06-DT-01` | Verified existing | External test data; encoding/content should be revalidated before rerun |
| `EV-LEG-003` | `../../schools/23127404-automation/playwright-report/` | Historical FR-06 / Chromium, Firefox, WebKit | Verified existing directory; historical outcome | Combined report with assets; not a final nine-report set |
| `EV-LEG-004` | `../../schools/23127404.md` | Historical run narrative and AI summary | Verified existing; historical claim | Secondary narrative; exact first prompt/time absent |
| `EV-SRC-001` | `../automation/tests/` and `../automation/test-data/` | FR-06/FR-10/FR-12 source suite | Verified current source at `aa316e0` | 51 JSON-defined cases; current source postdates selected runs and now attaches full case contracts to future results |
| `EV-SRC-002` | `../automation/playwright.config.ts` and matrix/report scripts | Nine-run orchestration | Verified source and structurally validated outputs | Identity, timestamp, case-count, completion, report/data-directory presence, and JSON/metadata totals validated; interactive links remain manual |
| `EV-SKILL-SRC` | `../agent-skill/playwright-data-driven-multibrowser/` | Optional Agent Skill source | Verified existing source | No qualifying end-to-end demo evidence yet |
| `EV-GIT-001` | `../git/23127404_HW04_git_commit_log.txt` | Git-history assessment | Verified snapshot | 9 qualifying commits across 2 days: count met; four-day rule noncompliant |
| `EV-PDF-001` | `../reports/main_report.pdf` | Main report | Generated and text-validated | 8 pages; student ID and extractable text verified after final reconciliation |
| `EV-PDF-002` | `../reports/ai_critique.pdf` | Mandatory AI Critique | Generated and text-validated | 1 page; Markdown source is one 246-word paragraph |
| `EV-PDF-003` | `../reports/ai_audit_report.pdf` | AI Audit Report | Generated and text-validated | 5 pages; known transcript gaps remain disclosed |
| `EV-ZIP-001` | `../23127404_HW04_AI_Automation_063.zip` | Provisional package | Generated and content-validated | 476 entries before final documentation refresh; required files and nine report HTML/JSON/metadata triplets present; forbidden dependency/result directories absent; regenerate after any evidence change |
| `EV-RUN-A-CHR` | `../automation/reports/fr06-chromium-2026-08-09T09-50-04-895Z/` | `RUN-A-CHR` | Attempted; structural validator passed | 16 total / 10 pass / 6 assertion fail; `2026-08-09T09:50:04.895Z` |
| `EV-RUN-A-FF` | `../automation/reports/fr06-firefox-2026-08-09T10-07-59-582Z/` | `RUN-A-FF` | Attempted; structural validator passed | 16 / 5 / 11; 7 `newPage()` environment + 4 assertion; Firefox headful |
| `EV-RUN-A-WK` | `../automation/reports/fr06-webkit-2026-08-09T09-52-14-569Z/` | `RUN-A-WK` | Attempted; structural validator passed | 16 / 10 / 6 assertion fail |
| `EV-RUN-B-CHR` | `../automation/reports/fr10-chromium-2026-08-09T10-26-40-345Z/` | `RUN-B-CHR` | Attempted; structural validator passed | 16 / 12 / 4 assertion fail; post-locator-fix rerun |
| `EV-RUN-B-FF` | `../automation/reports/fr10-firefox-2026-08-09T10-27-32-954Z/` | `RUN-B-FF` | Attempted; structural validator passed | 16 / 5 / 11; 7 environment + 4 assertion; post-fix, headful |
| `EV-RUN-B-WK` | `../automation/reports/fr10-webkit-2026-08-09T10-32-34-318Z/` | `RUN-B-WK` | Attempted; structural validator passed | 16 / 12 / 4 assertion fail; `FR10-02` passes after exact-cell fix |
| `EV-RUN-C-CHR` | `../automation/reports/fr12-chromium-2026-08-09T09-56-03-803Z/` | `RUN-C-CHR` | Attempted; structural validator passed | 19 / 10 / 9 assertion fail |
| `EV-RUN-C-FF` | `../automation/reports/fr12-firefox-2026-08-09T10-18-54-806Z/` | `RUN-C-FF` | Attempted; structural validator passed | 19 / 5 / 14; 8 environment + 6 assertion; Firefox headful |
| `EV-RUN-C-WK` | `../automation/reports/fr12-webkit-2026-08-09T09-57-54-553Z/` | `RUN-C-WK` | Attempted; structural validator passed | 19 / 10 / 9 assertion fail |
| `EV-VIDEO-001` | Main unlisted YouTube demo | Task 2 | Not Collected | Student voice/authorship and 5+ minutes required |
| `EV-SKILL-001` | Optional Agent Skill end-to-end demo | Agent Skills | Not Collected | Source exists; demo/category evidence not yet qualified |

## Evidence-entry template

| Evidence ID | Relative path or public URL | Case/run/defect IDs | Created at (ISO) | Created by | Environment | Verification state | Verified by/date | Notes |
|---|---|---|---|---|---|---|---|---|
| `EV-___` | **PENDING** | **PENDING** | **PENDING** | 23127404 | **PENDING** | Not Collected | **PENDING** | **PENDING** |

## Integrity checks

- Screenshots prove only the visible state at capture time.
- HTML reports prove the recorded execution only when their full assets and metadata are preserved.
- Traces/logs support diagnosis but do not replace a user-visible oracle where the requirement is visual.
- Source code supports design and root-cause hypotheses; it does not justify `Pass` or `Fail`.
- The selected reports were produced from pre-`aa316e0` local states (likely around `238cf27` or `532ebc2`); current `aa316e0` source improvements must not be retroactively attributed to them.
- External links must be tested for access and must not be replaced by invented placeholders in final claims.
- Evidence must not expose passwords, reusable JWTs, secrets, or unnecessary personal data.
