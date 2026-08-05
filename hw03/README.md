# HW03 — GUI & Usability Testing — Submission

**Student ID:** 23127296
**SUT:** EShop (`eshop-clone`)

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
|---|---|---|---|
| 1 | Task 1 — GUI Checklist (design + execution + bug report) | 30 | 30 |
| 2 | Task 2 — Usability Evaluation (task scenario + sessions + analysis) | 40 | 33 |
| 3 | Task 3 — Cross-Browser/Cross-Platform (≥3 platforms) | 20 | 20 |
| 4 | Agent Skills | 10 | 10 |
| | **Total** | **100** | **93** |

**Note on Task 2:** the assignment requires 7 real participants; only 4 (Long, Linh, Tiến, Khải) were recruited in time, all real, verifiable, screen-recorded people — not fabricated substitutes. This is a known, self-reported gap (see `03_usability_evaluation/00_report` equivalent, `../00_report/Task2_Usability_Evaluation_Report.md`, "Known gap / follow-up").

## Test Summary

| Metric | Count |
|---|---|
| Screens/flows tested (Task 1) | 8 (Home/Search, Login, Register, Forgot Password, Profile + Order History, Product Detail, Cart, Checkout + Coupon) |
| Checklist items designed | 42 |
| Checklist items executed | 42 |
| Passed | 32 |
| Failed | 10 |
| Bugs filed (GitHub Issues, screenshot attached to each) | 10 — [`KidCute1412/eshop-sut` issues #106–#115](https://github.com/KidCute1412/eshop-sut/issues) |
| Usability flow tested (Task 2) | Forgot Password (email → OTP → new password) |
| Usability participants | 4 of 7 required (Long, Linh, Tiến, Khải) — real, screen-recorded, contact-masked |
| Mean SUS score | 34.4 / 100 |
| Cross-platform coverage (Task 3) | 3 platforms — Chrome (Windows), Firefox (Windows), Safari 26/macOS 26 (Sauce Labs Live) |
| Agent Skills built | 2 — `gui-checklist-runner`, `usability-evaluation-kit` (see `05_agent_skills/`) |

## Demo videos

- Usability session recordings (4 participants): `03_usability_evaluation/videos/` (`long.mp4`, `linh.mp4`, `tien.mp4`, `khai.mp4`).
- Agent Skills demo (YouTube): see `05_agent_skills/README.md`.

## Directory structure

| Folder | Contents |
|---|---|
| `00_report/` | Main Task 1/2/3 reports (Markdown + PDF). |
| `01_gui_checklist/` | GUI checklist (CSV, 42 items) + test execution summary. |
| `02_bug_reports/` | Bug report + GitHub Issue screenshots. |
| `03_usability_evaluation/` | Phase 1 plan, Phase 2 sessions (4 participants), Phase 3 analysis, session recordings. |
| `04_cross_platform/` | Cross-platform test log + screenshots (Chrome/Firefox/Safari). |
| `05_agent_skills/` | Reusable Agent Skills (`gui-checklist-runner`, `usability-evaluation-kit`) + demo video links. |
| `06_ai_audit/` | AI Audit Report + AI Critique (Markdown + PDF). |
| `07_git_log/` | Full Git commit log (text file). |
