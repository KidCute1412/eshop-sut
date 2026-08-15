# HW04 - Automation Testing - Final Submission

**Student ID:** 23127296  
**SUT:** EShop (`eshop-sut`)  
**Repository:** https://github.com/KidCute1412/eshop-sut  
**Branch:** `23127296-NguyenThanhLuan`

## Feature Selection

| Pool | Feature | Description |
|---|---|---|
| A | FR-03 | Forgot Password & Reset Password |
| B | FR-09 | Discount Coupons |
| C | FR-13 | Admin Dashboard |

## Test Summary

| Metric | Count / Evidence |
|---|---|
| Features automated | 3 (FR-03, FR-09, FR-13) |
| Test cases designed | 43 total: FR-03 = 17, FR-09 = 14, FR-13 = 12 |
| Automated executions | 37 tests per browser |
| Browser runs | 3 projects: Chromium, Firefox, WebKit |
| Total browser executions | 111 |
| Passed | 29 per browser |
| Failed | 8 per browser, all mapped to documented SUT defects |
| HTML reports | `03_html_reports/playwright-report-chromium/`, `playwright-report-firefox/`, `playwright-report-webkit/` |
| Bugs found / documented | 7 defects in `02_bug_reports/Bug_Report.md` |
| GitHub Issues filed for HW04 | #135-#140 |
| Demo video | https://youtu.be/ftJ5TKZbfsk |
| Agent skill demo video | https://youtu.be/-UgwzqWETzM |

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
|---|---|---:|---:|
| 1 | Task 1 - Feature A (FR-03) | 25 | 25 |
| 2 | Task 1 - Feature B (FR-09) | 25 | 25 |
| 3 | Task 1 - Feature C (FR-13) | 25 | 25 |
| 4 | Task 2 - Demo video | 15 | 15 |
| 5 | Agent Skill | 10 | 10 |
| | **Total** | **100** | **100** |

## Submission Contents

| Path | Contents |
|---|---|
| `00_report/Review_And_GapAnalysis.md` | Human review and gap analysis of the AI-generated automation scripts, including concrete fixes applied. |
| `01_test_design/` | Test case design documents, Playwright specs, and JSON data fixtures for FR-03, FR-09, and FR-13. |
| `02_bug_reports/` | Bug report and screenshot evidence for automation-detected defects. |
| `03_html_reports/` | Stamped Playwright HTML reports for Chromium, Firefox, and WebKit. |
| `04_demo_video/video-link.txt` | Main HW04 demo video link. |
| `05_agent_skill/` | Reusable `data-driven-automation-runner` agent skill and its demo video link. |
| `06_ai_audit/` | AI Audit Report and AI Critique appendix. |
| `07_git_log/git_commit_log.txt` | Exported Git commit history for submission evidence. |

## Automation Evidence

The final Playwright suite is data-driven: input and expected values are stored in JSON fixtures under `01_test_design/tests/data/`, while the spec files under `01_test_design/tests/` read those fixtures and assert against the system requirements rather than the current buggy implementation.

The HTML reports in `03_html_reports/` are stamped with visible authorship evidence: `Run by: 23127296` plus an ISO timestamp. The same pass/fail pattern appears across Chromium, Firefox, and WebKit, showing deterministic execution against the seeded SUT.

## AI Usage Declaration

I use AI tools for this exercise. The detailed interaction log, prompts, outputs, human review notes, and critique are documented in:

- `06_ai_audit/AI_Audit_Report.md`
- `06_ai_audit/AI_Critique.md`

## Public Repository Evidence

- Repository: https://github.com/KidCute1412/eshop-sut
- Branch: `23127296-NguyenThanhLuan`
- Automation commit: https://github.com/KidCute1412/eshop-sut/commit/44a6d287b783130654174c6e9dd0afb622547b50
- Issue list: https://github.com/KidCute1412/eshop-sut/issues
