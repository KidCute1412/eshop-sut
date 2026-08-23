# HW06 API Testing Main Report

**Student ID:** 23127296  
**Student:** Nguyen Thanh Luan  
**Generated at:** 2026-08-22 22:30 Asia/Saigon  
**Latest local execution:** 2026-08-24 00:38-00:39 Asia/Saigon

## Scope

Three selected APIs were tested from three different feature pools:

| Pool | Feature | Endpoint(s) | Test cases |
|---|---|---|---:|
| A | FR-03 Password recovery | `POST /api/forgot-password`, `POST /api/reset-password` | 42 |
| B | FR-09 Apply coupon | `POST /api/apply-coupon` | 37 |
| C | FR-13 Admin orders | `GET /api/admin/orders` | 36 |

## Pipeline

1. Read `api_specification.md` and `backend/server.js`.
2. Generate AI draft cases by equivalence partitioning, boundary value analysis, security testing, schema validation, state transition testing, fuzzing, and error guessing.
3. Human-audit each AI case as VALID / INVALID / INCOMPLETE and correct the weak cases.
4. Add five human cases per API, especially for security and workflow risks.
5. Export Excel workbooks and Postman/Newman execution artifacts.

## Test Case Summary

| API | AI VALID | AI INVALID/INCOMPLETE | HUMAN VALID | Total |
|---|---:|---:|---:|---:|
| FR03 | 33 | 4 | 5 | 42 |
| FR09 | 29 | 3 | 5 | 37 |
| FR13 | 27 | 4 | 5 | 36 |

## Postman Features Used

| Feature | Used | Evidence |
|---|---|---|
| Collection | Yes | `postman/hw06-api.postman_collection.json` |
| Environment variables | Yes | `baseUrl`, `studentId` |
| Collection folders | Yes | One folder per selected API |
| Pre-request scripts | Yes | Adds `X-Student-Id`, prepares dynamic bodies, logs in users |
| Test scripts | Yes | Status, content type, response time, schema-level checks |
| Data-driven runs | Yes | `fr03-data.json`, `fr09-data.json`, `fr13-data.json` |
| Newman CLI | Yes | Commands documented in `run-notes.md` |
| Mock servers | No | Real local SUT was used |
| Monitors | No | Local and CI execution are the required targets |

## Bugs Found

| Bug ID | Endpoint | Summary | Severity |
|---|---|---|---|
| BUG-FR09-001 | `POST /api/apply-coupon` | Percent coupon formula computes negative discount. | High |
| BUG-FR13-001 | `GET /api/admin/orders` | Any valid user token can access admin order list. | Critical |
| BUG-FR09-002 | `POST /api/apply-coupon` | Public endpoint trusts body `user_id` for usage-sensitive logic. | Medium |

Detailed bug report is in `bug-reports/bug_report.md`. GitHub issue links/screenshots are marked TODO because real issue evidence must be created manually and cannot be fabricated.

## Execution Result

Local Newman execution was completed on 2026-08-24 00:38-00:39 Asia/Saigon against `http://localhost:3000` with `X-Student-Id: 23127296` injected by the pre-request script.

| API | Iterations | Requests | Assertions | Failed Assertions |
|---|---:|---:|---:|---:|
| FR03 | 42 | 68 | 168 | 0 |
| FR09 | 37 | 37 | 148 | 0 |
| FR13 | 36 | 68 | 144 | 0 |
| **Total** | **115** | **173** | **460** | **0** |

JSON reports are stored in `newman/fr03-newman-report.json`, `newman/fr09-newman-report.json`, and `newman/fr13-newman-report.json`.

## Remaining Evidence To Complete

The local API execution evidence is complete. The following items still require real external evidence and must not be fabricated:

- GitHub Issues for the documented bugs, each with a screenshot and issue URL.
- GitHub Actions passing run link and screenshot after pushing the HW06 workflow.
- GitHub Actions failing run link and screenshot from a temporary secure-oracle failing commit.
- Optional Newman HTML reports if the grader expects HTML in addition to the generated JSON reports.
- A manually confirmed self-drawn/exported generator diagram image and optional demonstration video link.

## AI Audit Declaration

I use AI tools for the following tasks: generating initial test-case ideas, auditing against source code, designing Postman data-driven automation, drafting the generator skill, and preparing Markdown report templates. Full interaction log is summarized in `ai_audit_report.md`.

## AI Critique

See `ai_critique.md`.
