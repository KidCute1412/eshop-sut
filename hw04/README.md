# HW04 — Automation Testing — Submission

**Student ID:** 23127296
**SUT:** EShop (`eshop-sut`)
**Features automated:** FR-03 (Forgot Password & Reset — Pool A), FR-09 (Discount Coupons — Pool B), FR-13 (Admin Dashboard — Pool C). Self-declared per the assignment's rule for when HW02 is unavailable — the HW02 submission folder was found to contain no actual content (empty `.git` only). These three match the manual test-design backlog already present in the SUT's own `README.md`.

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
|---|---|---|---|
| 1 | Task 1 — Feature A (FR-03) | 25 | _fill in_ |
| 1 | Task 1 — Feature B (FR-09) | 25 | _fill in_ |
| 1 | Task 1 — Feature C (FR-13) | 25 | _fill in_ |
| 2 | Task 2 — Demo video | 15 | 0 (not yet recorded — see below) |
| 3 | Agent Skills | 10 | _fill in_ |
| | **Total** | **100** | _fill in_ |

**Note:** the self-assessed grade column and the filename's `<SelfAssessedGrade>` must be filled in by you after you've watched the reports/read the review doc — do not submit with placeholder zeros still in the grade column.

## Test Summary

| Metric | Count |
|---|---|
| Features automated | 3 (FR-03, FR-09, FR-13) |
| Test cases designed (`01_test_design/`) | 43 (17 + 14 + 12) |
| Test cases automated (distinct `test()` blocks, incl. data-driven rows) | 37 per browser |
| Browser runs | 3 (Chromium, Firefox, WebKit) × 37 tests = 111 executions — 9+ required, exceeded |
| Passed (per browser, identical across all 3) | 29 |
| Failed (per browser, identical across all 3 — all mapped to genuine spec violations) | 8 |
| Bugs found | 7 (5 previously known, re-confirmed by automation; 2 newly discovered) |
| GitHub Issues filed for HW04 | 6 — [`KidCute1412/eshop-sut` #135–#140](https://github.com/KidCute1412/eshop-sut/issues) |
| Demo video (Task 2) | **not yet recorded** — see `04_demo_video/video-link.txt` |

## Directory structure

| Folder | Contents |
|---|---|
| `00_report/` | `Review_And_GapAnalysis.md` — what the first AI draft got wrong, why, and the fix applied for each issue. **Read and confirm this before submitting.** |
| `01_test_design/` | Test case design tables (≥12 cases each) for FR-03, FR-09, FR-13. |
| `02_bug_reports/` | `Bug_Report.md` + `screenshots/` — the 7 defects found by automation, linked to GitHub Issues #135–#140. |
| `03_html_reports/` | The 3 stamped Playwright HTML reports (Chromium/Firefox/WebKit), each showing "Run by: 23127296" + ISO timestamp. |
| `04_demo_video/` | `video-link.txt` — **TODO: record and link the Task 2 demo video.** |
| `05_agent_skill/` | `data-driven-automation-runner/SKILL.md` — reusable skill for this workflow, + its own demo-video placeholder. |
| `06_ai_audit/` | `AI_Audit_Report.md` + `AI_Critique.md`. |
| `07_git_log/` | `git_commit_log.txt` — full branch history (see gap below). |

The actual test code (`tests/`, `playwright.config.js`, `scripts/`) lives at the repository root, not inside `hw04/`, and is already committed/pushed to `origin/23127296-NguyenThanhLuan` — see the "Public repository" section below.

## What is genuinely done vs. what is still on you

**Done, real, and verifiable:**
- All 3 features have ≥12 designed test cases (43 total) and a working, data-driven, 3-browser Playwright suite (`tests/*.spec.js`, `tests/data/*.json`) using ≥3 assertion patterns (`toBe`, `toHaveText`/`not.toHaveText`, `toBeVisible`, `toHaveCount`, `toEqual`, status-code checks).
- The suite was actually executed on Chromium, Firefox, and WebKit against a freshly-seeded backend each time; all three runs produced identical pass/fail results (29/8), which is itself evidence the suite is deterministic, not flaky.
- 7 real defects were found, each backed by a screenshot of the actual failing Playwright assertion; 6 GitHub issues were filed with your explicit approval.
- The AI Audit Report and Review/Gap-Analysis document real mistakes the AI made while writing this suite (not hypothetical ones) and the fixes actually applied, verified by re-running the suite after each fix.

**Not done — needs your action before submission:**
1. **Demo video (Task 2, 15 pts)** — not recorded. Must be ≥5 min, narrated in Vietnamese, show an automation script running end-to-end (multi-browser + HTML report), narrate at least one real fix from `00_report/Review_And_GapAnalysis.md`, and show your face-cam or a terminal running `whoami`/`hostname`.
2. **Agent Skill demo video** — same gap, smaller scope; see `05_agent_skill/demo-video.txt`.
3. **Git commit log requirement (§12)** — the assignment requires ≥8 commits that touch `.spec.js`/`.spec.ts` files, spread across ≥4 days. As of this session there is only **one** commit touching the spec files (today). This cannot be fabricated or backdated — you'll need to make real incremental commits to `tests/*.spec.js` (refinements, additional cases, fixes you make while reviewing) across at least 4 separate days before the deadline. Re-export `07_git_log/git_commit_log.txt` (via `git log --date=iso --pretty=fuller <branch>`) once that's done.
4. **Human review sign-off** — read `00_report/Review_And_GapAnalysis.md` end-to-end and add your own confirmation (or corrections) before this goes in the zip; per the assignment, submitting AI output without your own review is not acceptable.
5. **Self-assessed grade** — fill in the table above and the submission filename (`23127296_HW04_AI_Automation_<Grade>.zip`).
6. Fix phần gap analysis.

## Public repository

- Repo: https://github.com/KidCute1412/eshop-sut
- Branch: `23127296-NguyenThanhLuan`
- Commit with the automation added: [`44a6d28`](https://github.com/KidCute1412/eshop-sut/commit/44a6d287b783130654174c6e9dd0afb622547b50)
