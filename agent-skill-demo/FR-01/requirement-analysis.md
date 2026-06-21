# Requirement Analysis - FR-01 Account registration

## Feature Intake

| Field | Value |
| --- | --- |
| Feature ID | FR-01 |
| Feature Name | Account registration |
| Pool | A |
| User Role | Guest user |
| Application Module | User web frontend and backend API |
| Requirement Source | `README.md`, official PDF, `api_specification.md` |
| Output Directory | `agent-skill-demo/FR-01` |

## Allocation Notes

The current allocated features are FR-01, FR-02, FR-07, and FR-17. The assignment requires four features, one from each pool A, B, C, and D. This allocation contains two Pool A features and no Pool D feature. This is recorded as an allocation inconsistency; no Pool D feature is invented.

## Evidence Summary

| Rule ID | Rule | Evidence Class | Source Reference | Notes |
| --- | --- | --- | --- | --- |
| R-FR01-01 | User must provide full name, email, and password | Documented requirement | `README.md` FR-01; PDF section 4/6 | Required registration inputs |
| R-FR01-02 | Email must be valid `user@domain.com` format and unique | Documented requirement | `README.md` FR-01 | API spec shows email field but no uniqueness rule |
| R-FR01-03 | Password requires min 8 chars, uppercase, lowercase, digit, and one of `@ $ ! % * ? &` | Documented requirement | `README.md` FR-01 | Strong password rule |
| R-FR01-04 | Confirm password field is required and mismatches must be rejected | Documented requirement | `README.md` FR-01 | Not present in API spec body |
| R-FR01-05 | Successful registration redirects user to Login page | Documented requirement | `README.md` FR-01; `frontend-web/src/pages/Register.jsx` | Frontend calls `navigate('/login')` after successful API call |
| API-FR01-01 | `POST /api/register` accepts `name`, `email`, `password` | API specification | `api_specification.md` section 1.1 | No confirm password in API body |
| FE-FR01-01 | Web register form has state for `name`, `email`, `password`, and `error` only | Implemented frontend behavior | `frontend-web/src/pages/Register.jsx` | No confirm password state/input |
| FE-FR01-02 | Email input uses `type="text"` | Implemented frontend behavior | `frontend-web/src/pages/Register.jsx` | Contradicts general email field expectation |
| FE-FR01-03 | Password regex requires whitespace and disallows the listed special characters | Implemented frontend behavior | `frontend-web/src/pages/Register.jsx` | `flawedStrongPasswordRegex` conflicts with requirement |
| BE-FR01-01 | Backend inserts name, email, and password directly into `users` | Implemented backend behavior | `backend/server.js` `/api/register` | No validation for required fields, email, password, or confirmation |
| DB-FR01-01 | `users.email` has no UNIQUE constraint | Database enforcement | `backend/database.js` `CREATE TABLE users` | Contradicts unique email requirement |
| DB-FR01-02 | Seed users include `admin@eshop.com` and `test@eshop.com` | Database seed data | `backend/database.js` seed users | Useful duplicate-email data |

## Assumptions

- Registration is tested through the user web app and backend API, not admin or mobile, unless stated otherwise.
- Source inspection only was performed; application test cases were not executed.

## Contradictions

- Requirement says email must be unique, but database has no uniqueness constraint and backend has no duplicate-email check.
- Requirement says confirm password is required, but frontend and API contract omit it.
- Requirement says special characters are allowed/required, but web regex requires whitespace instead.
- Requirement expects email format validation, but the web input is `type="text"` and backend validates nothing.

## Coverage Gaps

- No execution evidence, screenshots, or bug issue links were produced in this dry run.
- Mobile FR-01 was inspected only at a high level; this dry run focuses on `frontend-web/` plus backend evidence.
