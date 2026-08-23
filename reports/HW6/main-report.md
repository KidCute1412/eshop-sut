# HW6 - API Testing Main Report

Generated at: 2026-08-22T03:42:16.294Z

## Scope and Selected APIs

This submission targets three API-backed features selected by the student:

| Feature                     | Pool | Endpoints                                                                |
| --------------------------- | ---- | ------------------------------------------------------------------------ |
| FR01 Account registration   | A    | POST /api/register                                                       |
| FR07 Shopping cart          | B    | GET /api/cart; POST /api/cart                                            |
| FR17 Coupon management CRUD | C    | GET /api/coupons; POST /api/admin/coupons; DELETE /api/admin/coupons/:id |

The selected tool is Postman + Newman. All artifacts are stored under reports/HW6.

## Test Environment

- Backend: Node.js + Express + SQLite
- Base URL: http://localhost:3000
- Startup: cd backend; npm install; node database.js when clean seed is needed; node server.js
- Default user: test@eshop.com / Test1234!
- Default admin: admin@eshop.com / Admin123!
- Student ID: TODO_STUDENT_ID

## Source-of-Truth Mapping

Expected behavior is derived from README.md, api_specification.md, setup_guide.md, and the HW6 assignment. Implementation source was used only to understand route availability and build executable requests, not as the expected-behavior oracle.

## API 1 - FR01 Generate, Audit, Extend, Execute, Bugs

See FR01/test-cases.md, FR01/api-mapping.md, FR01/ai-audit.md, and FR01/ai-gap-analysis.md. Designed 35 AI-generated cases plus 5 human-added cases covering required fields, email partitions, password boundaries, duplicate email, SQL injection, response schema, sensitive-data leakage, and API/UI confirm-password ambiguity.

## API 2 - FR07 Generate, Audit, Extend, Execute, Bugs

See FR07/test-cases.md, FR07/api-mapping.md, FR07/ai-audit.md, and FR07/ai-gap-analysis.md. Designed 35 AI-generated cases plus 5 human-added cases covering authentication, cart item fields, quantity boundaries, duplicate-add behavior, client-side price/name tampering, and X-Student-Id evidence.

## API 3 - FR17 Generate, Audit, Extend, Execute, Bugs

See FR17/test-cases.md, FR17/api-mapping.md, FR17/ai-audit.md, and FR17/ai-gap-analysis.md. Designed 35 AI-generated cases plus 5 human-added cases covering admin authorization, role enforcement, required fields, coupon enum/range/date boundaries, uniqueness, SQL/XSS probes, and delete behavior.

## Postman/Newman Features Used

The collection uses collection variables, environment variables, collection-level pre-request script, collection-level X-Student-Id header injection, token extraction, test scripts, grouped folders, and a CSV data file. Newman command and output should be stored in newman/newman-output.txt and newman/report.html after final execution.

Draft local execution has been completed with `studentId=00000000` against `http://127.0.0.1:3000`. Newman executed 127 requests and 253 assertions; 80 assertions failed. See `execution-summary.md`, `newman/newman-output.txt`, and `newman/report.html`. This draft run must be repeated with the real Student ID before final submission.

## CI/CD Integration

See ci-cd-report.md and ci/github-actions-api-tests.yml. Real GitHub Actions links are pending because they require a public GitHub repository and two actual workflow runs.

## AI-Driven API Test Generator

See generator-design.md and generator-pseudocode.py. The diagram placeholder must be replaced by a self-drawn student diagram before submission.

## AI Audit Summary

See ai-audit.md. The audit records step-by-step prompt decomposition: source extraction, domain partitioning, security/state/schema generation, human review, and artifact generation.

## AI Critique

See ai-critique.md.

## Git Commit Log

See git-commit-log.txt after exporting the real Git history.
