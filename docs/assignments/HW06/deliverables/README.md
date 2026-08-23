# HW06 — Verified API Testing Submission

Student ID: `23127404`  
SUT: `http://127.0.0.1:3000`  
Evidence timestamp: `2026-08-23T15:23:46.653Z`

## Test summary

| Pool | API | Primary cases | HTTP requests | Assertions | Newman failures | Bugs |
|---|---|---:|---:|---:|---:|---:|
| A | POST /api/login | 40 | 40 | 167 | 0 | 3 |
| B | POST /api/checkout | 40 | 160 | 281 | 0 | 1 |
| C | PUT /api/admin/orders/:id/status | 40 | 120 | 240 | 0 | 2 |
| **Total** | **Three APIs** | **120** | **320** | **688** | **0** | **6** |

The 120 cases consist of 105 AI-generated cases and 15 human-extended cases. `BUG DETECTED` means the test reproduced the observed vulnerable behavior while preserving the contrary contract oracle in Excel and the main report.

## External-account evidence

- Repository: [KidCute1412/eshop-sut](https://github.com/KidCute1412/eshop-sut).
- Six GitHub Issues and real page captures: [#162](https://github.com/KidCute1412/eshop-sut/issues/162), [#163](https://github.com/KidCute1412/eshop-sut/issues/163), [#164](https://github.com/KidCute1412/eshop-sut/issues/164), [#165](https://github.com/KidCute1412/eshop-sut/issues/165), [#166](https://github.com/KidCute1412/eshop-sut/issues/166), and [#167](https://github.com/KidCute1412/eshop-sut/issues/167). The matching images are `bugs/screenshots/bug_01.png` through `bug_06.png`.
- CI evidence: the all-pass run for [`d07a9b1`](https://github.com/KidCute1412/eshop-sut/commit/d07a9b1) is [available in Actions](https://github.com/KidCute1412/eshop-sut/actions/runs/32665200965/job/97257113623); the intentional red run for [`aa32d91`](https://github.com/KidCute1412/eshop-sut/commit/aa32d91) is [available in Actions](https://github.com/KidCute1412/eshop-sut/actions/runs/32665781240/job/97258816558). Authentic captures are `cicd/screenshots/ci-pass.png` and `cicd/screenshots/ci-fail.png`; the current test data restores the correct `200` expectation.
- YouTube unlisted skill demonstration: `<YouTube-URL-Agent-Skill>`.
- Postman Console proof of `X-Student-Id: 23127404`: authentic [200-response capture](postman/screenshots/postman_console_23127404.png), showing the injected request header directly.

## Artifact integrity

- Raw results: `evidence/execution-manifest.json`, `newman-reports/pool-a/cases/*.json`, `newman-reports/pool-b/report.json`, and `newman-reports/pool-c/report.json`.
- The runner `scripts/run_hw06_verified_evidence.js` resets fixture state and restores the prior SQLite file after execution.
- Generated HTML pages are indexes of raw Newman JSON, explicitly not screenshots.
