# HW04 — AI-Assisted Automation Testing Submission

> Submission status: **EXECUTION EVIDENCE, REPORT PDFs, BUG/ISSUE PACKETS, VIDEO LINKS, AND SOURCE PACKAGE ARE PREPARED; final submission remains pending timestamp, logged-out link checks, ZIP generation, and student sign-off.**

## Identity

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc |
| Student ID | 23127404 |
| Class | `CSC13003_23KTPM3` (student-confirmed) |
| Repository | https://github.com/KidCute1412/eshop-sut (student-confirmed public repository) |
| Working branch observed | `23127404-LeTuanLoc` |
| Submission date/time | **PENDING — record final ISO 8601 submission time** |
| Execution source/SUT revision | Final Firefox rerun: `a390bc125713a1759443a4e84929641d432a45dc`; each report records its own exact revision |
| Environment | Windows 10 Home Single Language, NT `10.0.26200.0`; Node.js 22.17.0; npm 10.9.2; Playwright 1.55.0 |
| Browsers | Chromium 140.0.7339.16 headless; Firefox 141.0 headless; WebKit 26.0 headless |
| Main demo video | https://youtu.be/Uz9ogf7fKFY (YouTube Unlisted) |
| Agent Skill | Source present at `agent-skill/playwright-data-driven-multibrowser/`; demo video supplied |
| Agent Skill demo | https://youtu.be/PL3qLI-KcPE (YouTube Unlisted) |

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
| Cases reaching assertions | 153 | All selected Firefox cases now reached assertions |
| Passed executions | 96 | Derived from the nine selected reports |
| Recorded failed executions | 57 | Assertion failures only; no Firefox fixture failures |
| Assertion failures | 57 across 19 unique logical cases | FR-06: 18; FR-10: 12; FR-12: 27 |
| Environment failures | 0 | Firefox context creation fixed by removing incompatible device options |
| Separate final HTML/JSON/metadata report directories | 9 validated | Complete selected set under `automation/reports/` |
| HW04 defects with verified public Issue URLs | 17 | BUG-001…BUG-017; rejected candidates excluded |
| Qualifying test-script commits | 9 | Count met; two calendar days, so four-day span not met |
| Main demo videos | 1 | 1 unlisted video, at least 5 minutes |

The selected final report set is listed in `supporting-materials/execution_manifest.md`; `automation/reports/` now contains only those nine directories. All nine contain HTML, JSON, and metadata and passed the report validator. Firefox now runs headless with an option-free Playwright context; all 51 Firefox attempts reached test assertions. A legacy July report outside `deliverables/` remains historical input only and is not included in the totals above.

## Critical compliance disclosure

The exported log contains the complete current-branch HW04 history snapshot (26 meaningful commits touching `docs/assignments/HW04`) plus a separate qualifying section with nine commits that touch HW04 Playwright `.spec.ts` files. The export-only refresh commit is intentionally not self-listed. The qualifying count requirement is met, but those commits span only two calendar days, so the separate four-day requirement remains **not satisfied**. Documentation changes are retained in the complete-history section but do not count toward the qualifying total. No history has been invented or backdated. See `git/23127404_HW04_git_commit_log.txt`.

## Deliverable map

| Artifact | Purpose | Status |
|---|---|---|
| `reports/main_report.md` | Main automation report and gap analysis | Updated with validated final execution evidence |
| `reports/main_report.pdf` | Rendered main report | Generated and text-validated (8 pages) |
| `reports/ai_critique.md` | Mandatory 200–300-word critique | Complete draft; student must confirm it reflects the final work |
| `reports/ai_critique.pdf` | Rendered mandatory critique | Generated and text-validated (1 page) |
| `reports/ai_audit_report.md` | AI interaction log | Partial; missing historical exact prompts are disclosed |
| `reports/ai_audit_report.pdf` | Rendered AI audit | Generated and text-validated (5 pages) |
| `bugs/bug_report.md` | Runtime failure analysis | 17 agent-confirmed defects, 2 rejected oracle candidates; 17 Issue URLs recorded |
| `bugs/issue-register.md` | Test-to-Issue reconciliation | 17 packets mapped to BUG-001…BUG-017; 17 public Issue URLs recorded |
| `bugs/triage-decisions.md` | Agent triage audit | All 19 candidates classified with rationale and screenshot path |
| `bugs/issue-packets/` | Copy-ready GitHub Issue bodies | 17 packets; each includes reproduction, severity and evidence references |
| `bugs/evidence/` | Authentic runtime evidence | 19 PNG screenshots, 19 traces and per-candidate metadata |
| `video/demo_video.md` | Main demo link record | URL supplied; student must retain final publication settings |
| `../specs/HW04_vietnamese_narration_script.md` | Vietnamese recording script | Preparation material outside the submission package |
| `video/agent_skill_demo.md` | Optional Agent Skill source/demo record | Source present; end-to-end demo URL supplied |
| `supporting-materials/test_case_matrix.md` | Final case/data/spec/browser-result traceability | 51 actual source rows with 153 per-browser outcomes |
| `supporting-materials/execution_manifest.md` | Nine-run evidence ledger | Complete and reconciled: 153/96/57; 0 environment failures |
| `supporting-materials/evidence_register.md` | Evidence provenance and integrity ledger | Nine selected report directories verified |
| `23127404_HW04_AI_Automation_098.zip` | Final self-assessed submission archive target | Not yet generated; run `npm run package:submission` after final manual checks |

The three required Markdown reports have equivalent PDFs generated by the reproducible `npm run reports:pdf` workflow. HTML report directories, screenshots, videos, Issue pages, timestamps, and execution results must come from genuine student-controlled execution and must not be AI-generated.

## Self-assessment

The following self-assessment reflects the evidence currently present in this package. The final archive should use suffix `098`; no score is claimed for the unmet four-day history condition beyond the documented self-assessment.

| No. | Criterion | Maximum | Self-assessed grade | Evidence |
|---:|---|---:|---:|---|
| 1 | Task 1 — Feature A (FR-06) | 25 | **21** | 16 cases × 3 browsers; four confirmed Issue URLs and two oracle-gap candidates documented |
| 2 | Task 1 — Feature B (FR-10) | 25 | **22** | 16 cases × 3 browsers; four confirmed Issue URLs documented |
| 3 | Task 1 — Feature C (FR-12) | 25 | **20** | 19 cases × 3 browsers; nine confirmed Issue URLs documented |
| 4 | Task 2 — Demo video | 15 | **15** | Unlisted Vietnamese demo URL supplied |
| 5 | Agent Skills | 10 | **10** | Reusable source and separate end-to-end demo URL supplied |
|  | **Total** | **100** | **98 / 100 (self-assessed)** | Four-day Git-history requirement remains noncompliant |

## Submission gate

Do not submit this folder as complete until the final ISO 8601 submission timestamp is recorded, the YouTube and GitHub Issue links/attachments are checked while logged out, the `23127404_HW04_AI_Automation_098.zip` archive is generated and inspected, and the student approves the final package. Follow `../specs/manual.md`; preserve the validated reports and do not recalculate totals from superseded runs.
