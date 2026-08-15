# HW05 TODO Status

Last reviewed: 2026-08-15.

## Completed In Workspace

- [x] Read and reviewed `2026.HW05.Performance Testing_En.md`.
- [x] Audited current `hw05/submit` artifacts.
- [x] Renamed JMeter plans from sample ID `25127001` to `23127296`.
- [x] Updated plan dates to `20260815`.
- [x] Verified JMX endpoint coverage:
  - Auth-heavy: `POST /api/login`
  - Read-heavy: product/category endpoints
  - Transactional: cart/checkout/order endpoints
- [x] Verified three different JMeter listener/report views:
  - Load: Summary Report
  - Stress: View Results Tree
  - Spike: Aggregate Report
- [x] Verified JWT extraction and `Authorization: Bearer ${auth_token}` usage in protected requests.
- [x] Added `seed_performance_data.js` because CSV users were not present in the default SQLite seed data.
- [x] Added `runbook.md` with JMeter execution commands.
- [x] Added `analyze_jtl.mjs` for computing samples, errors, average, p95, p99, and throughput from JTL CSV logs.
- [x] Rewrote `README.md` with real status and file list.
- [x] Rewrote `task1/test_plan_review_notes.md`.
- [x] Rewrote `task2/ai_analysis_and_review.md` without fabricated metrics.
- [x] Rewrote `task3/continuous_testing_proposal.md` with a clean flow chart and trade-off discussion.
- [x] Rewrote `ai_audit_report.md` with 5 AI interactions.
- [x] Rewrote `ai_critique.md` in the required 200-300 word range.
- [x] Added `git_commit_log.txt`.

## Still Required From Real Execution

These cannot be fabricated and must be generated on the student's machine with JMeter, Node.js, and screen recording available.

- [ ] Install or add Apache JMeter to PATH.
- [ ] Add Node.js to PATH if it is installed but unavailable in the terminal.
- [ ] Start backend on `http://localhost:3000`.
- [ ] Run `node hw05\submit\task1\seed_performance_data.js`.
- [ ] Run Load test and save:
  - `hw05/submit/task1/23127296_Load_20260815.jtl`
  - `hw05/submit/task1/23127296_Load_20260815_html/`
- [ ] Run Stress test and save:
  - `hw05/submit/task1/23127296_Stress_20260815.jtl`
  - `hw05/submit/task1/23127296_Stress_20260815_html/`
- [ ] Run Spike test and save:
  - `hw05/submit/task1/23127296_Spike_20260815.jtl`
  - `hw05/submit/task1/23127296_Spike_20260815_html/`
- [ ] Capture JMeter + Task Manager screenshots for Load, Stress, and Spike.
- [ ] Capture hardware-spec screenshot.
- [ ] Run or identify the 10-15 minute soak/endurance result.
- [ ] Fill endurance threshold values in:
  - `hw05/submit/README.md`
  - `hw05/submit/task1/test_plan_review_notes.md`
  - `hw05/submit/task3/continuous_testing_proposal.md`
- [ ] Run AI analysis on the real `.jtl` logs and fill:
  - `hw05/submit/task2/ai_analysis_and_review.md`
- [ ] Record Vietnamese narration demo video, at least 6 minutes, showing JMeter and resource monitor in the same frame.
- [ ] Add unlisted YouTube link to:
  - `hw05/submit/README.md`
  - `hw05/submit/task1/test_plan_review_notes.md`
- [ ] File GitHub Issues for real bugs/performance issues if found, with screenshots.
- [ ] Create a final zip named `23127296_HW05_AI_Performance_<SelfAssessedGrade>.zip`.

## Information Needed From Student

- [ ] Confirm full name: currently inferred as `Nguyen Thanh Luan` from branch name.
- [ ] Provide final self-assessed grade.
- [ ] Provide YouTube demo link and duration.
- [ ] Provide actual `.jtl` logs and screenshots after running JMeter.
- [ ] Confirm whether GitHub Issues were filed and provide links.
