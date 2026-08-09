# HW04 — AI-Assisted Automation Testing Submission

> Submission status: **EXECUTION EVIDENCE, REPORT PDFs, AND SOURCE PACKAGE ARE COMPLETE; submission remains incomplete until manual identity, Issue, video, and public-link requirements are resolved.**

## Identity

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc |
| Student ID | 23127404 |
| Class | **PENDING — enter official class code** |
| Repository | https://github.com/KidCute1412/eshop-sut |
| Working branch observed | `23127404-LeTuanLoc` |
| Submission date/time | **PENDING — record final ISO 8601 submission time** |
| Execution source/SUT revision | `656991a598bafe43cbed13b54bf1ac3f429c30f2` for all nine rerun reports; recorded in every `run-metadata.json` |
| Environment | Windows 10 Home Single Language, NT `10.0.26200.0`; Node.js 22.17.0; npm 10.9.2; Playwright 1.55.0 |
| Browsers | Chromium 140.0.7339.16; Firefox 141.0 headful; WebKit 26.0 |
| Main demo video | **PENDING — unlisted YouTube URL not supplied** |
| Agent Skill | Source present at `agent-skill/playwright-data-driven-multibrowser/`; structural validation and independent forward-use audit passed; video pending |
| Agent Skill demo | **Not recorded; no URL supplied** |

## Scope

| Pool | Requirement | Feature | HW02 continuity |
|---|---|---|---|
| A | FR-06 | Product detail view | Selected in HW02 |
| B | FR-10 | Order state machine | Selected in HW02 |
| C | FR-12 | Access control | Selected in HW02 |

This submission excludes Pool D/mobile. The requirement oracle is the repository root `README.md`; the assignment rules are in `specs/2026.HW04.Automation Testing_En.pdf`.

## Honest current test summary

| Measure | Current repository evidence | Required/final value |
|---|---:|---|
| Features in scope | 3 | 3 |
| Features with current HW04 spec files | 3 | 3 |
| Source-defined logical cases | 51 (FR-06: 16; FR-10: 16; FR-12: 19) | At least 36 total; at least 12 per feature |
| Selected final browser runs | 9 (3 features × 3 browsers) | At least 9 |
| Scheduled/attempted browser cases | 153 | Derived from the nine selected reports |
| Cases reaching assertions | 102 | 64 passed + 38 assertion-failed |
| Passed executions | 64 | Derived from the nine selected reports |
| Recorded failed executions | 89 | 38 assertion failures + 51 Firefox environment failures |
| Assertion failures | 38 across 19 unique logical cases | FR-06: 12; FR-10: 8; FR-12: 18 |
| Environment failures | 51 | Firefox `newPage()` timeouts: FR-06 16, FR-10 16, FR-12 19 |
| Separate final HTML/JSON/metadata report directories | 9 validated | Complete selected set under `automation/reports/` |
| HW04 defects with verified public Issue URLs | 0 | Actual verified total only |
| Qualifying test-script commits | 9 | Count met; two calendar days, so four-day span not met |
| Main demo videos | 0 | 1 unlisted video, at least 5 minutes |

The selected final report set is listed in `supporting-materials/execution_manifest.md`; `automation/reports/` now contains only those nine directories. All nine contain HTML, JSON, and metadata and passed the report validator. Firefox ran headful because headless Firefox failed before `newPage()` on this Windows environment; all 51 Firefox attempts in this rerun failed during `newPage()` setup and are recorded separately as environment failures. A legacy July report outside `deliverables/` remains historical input only and is not included in the totals above.

## Critical compliance disclosure

The exported full HW04 history contains nine qualifying `.spec.ts` commits: legacy `f905546` on 27 July 2026 and eight deliverables-suite commits ending at `aa316e0` on 9 August 2026. The count requirement is met, but the history spans only two calendar days, so the separate four-day requirement remains **not satisfied**. Documentation changes do not count, and no history has been invented or backdated. See `git/23127404_HW04_git_commit_log.txt`.

## Deliverable map

| Artifact | Purpose | Status |
|---|---|---|
| `reports/main_report.md` | Main automation report and gap analysis | Updated with validated final execution evidence |
| `reports/main_report.pdf` | Rendered main report | Generated and text-validated (8 pages) |
| `reports/ai_critique.md` | Mandatory 200–300-word critique | Complete draft; student must confirm it reflects the final work |
| `reports/ai_critique.pdf` | Rendered mandatory critique | Generated and text-validated (1 page) |
| `reports/ai_audit_report.md` | AI interaction log | Partial; missing historical exact prompts are disclosed |
| `reports/ai_audit_report.pdf` | Rendered AI audit | Generated and text-validated (5 pages) |
| `bugs/bug_report.md` | Runtime failure analysis | 19 assertion-failing logical cases documented as Issue-pending candidates |
| `bugs/issue-register.md` | Test-to-Issue reconciliation | 19 candidates; no public HW04 Issue URL verified |
| `video/demo_video.md` | Main demo plan and link record | Not recorded |
| `video/vietnamese_narration_script.md` | Vietnamese recording script | Ready for student recording |
| `video/agent_skill_demo.md` | Optional Agent Skill source/demo record | Source present; end-to-end validation and demo pending |
| `supporting-materials/test_case_matrix.md` | Final case/data/spec/browser-result traceability | 51 actual source rows with 153 per-browser outcomes |
| `supporting-materials/execution_manifest.md` | Nine-run evidence ledger | Complete and reconciled: 153/64/89; 51 environment failures |
| `supporting-materials/evidence_register.md` | Evidence provenance and integrity ledger | Nine selected report directories verified |
| `23127404_HW04_AI_Automation_063.zip` | Provisional current-evidence submission archive | Generated and content-validated; regenerate after manual evidence changes |

The three required Markdown reports have equivalent PDFs generated by the reproducible `npm run reports:pdf` workflow. HTML report directories, screenshots, videos, Issue pages, timestamps, and execution results must come from genuine student-controlled execution and must not be AI-generated.

## Self-assessment

The following **provisional** score reflects only evidence currently present in this package. The student must update the table and ZIP suffix after adding genuine Issue/video/Skill evidence.

| No. | Criterion | Maximum | Self-assessed grade | Evidence |
|---:|---|---:|---:|---|
| 1 | Task 1 — Feature A (FR-06) | 25 | **21** | 16 cases × 3 browsers and diagnostics; Issue evidence and one cart-state oracle gap remain |
| 2 | Task 1 — Feature B (FR-10) | 25 | **22** | 16 cases × 3 browsers; exact-cell locator correction and rerun documented; Issues pending |
| 3 | Task 1 — Feature C (FR-12) | 25 | **20** | 19 cases × 3 browsers; access-control candidates retained; cleanup verification and Issues pending |
| 4 | Task 2 — Demo video | 15 | **0** | Mandatory student-narrated URL not supplied |
| 5 | Agent Skills | 10 | **0 at this stage** | Skill source exists, but no qualifying execution/demo URL is verified |
|  | **Total** | **100** | **63 / 100 (provisional)** | Current package suffix: `063`; recalculate after manual evidence |

## Submission gate

Do not submit this folder as complete while identity, Issue URLs/screenshots, videos, public-link checks, or final student approval remain pending. Follow `../specs/manual.md`; preserve the validated reports and do not recalculate totals from superseded runs.
