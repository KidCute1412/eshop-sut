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

## Required human-account placeholders

- Public repository: `PENDING HUMAN ACTION — insert public GitHub URL after push`.
- Six GitHub Issue URLs and screenshots: `PENDING HUMAN ACTION — create issues from bugs/bug-report.md and replace bugs/screenshots/bug_01.png` through `bug_06.png` with real GitHub Issue-page screenshots.
- CI pass/fail Action URLs, commit hashes, and screenshots: `PENDING HUMAN ACTION`.
- YouTube unlisted skill demonstration: `<YouTube-URL-Agent-Skill>`.
- Postman Console proof of `X-Student-Id: 23127404`: `PENDING HUMAN ACTION`.

## Artifact integrity

- Raw results: `evidence/execution-manifest.json`, `newman-reports/pool-a/cases/*.json`, `newman-reports/pool-b/report.json`, and `newman-reports/pool-c/report.json`.
- The runner `scripts/run_hw06_verified_evidence.js` resets fixture state and restores the prior SQLite file after execution.
- Generated HTML pages are indexes of raw Newman JSON, explicitly not screenshots.
