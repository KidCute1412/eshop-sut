# FR01 - AI Audit

## Purpose

This file preserves the detailed prompt and raw AI output for FR01 - Account registration. The table below is the AI-generated candidate suite before human review, execution cleanup, and testcase removal. Because it is raw AI output, it may include rows that were later removed from the final `test-cases.md`.

## AI Prompt

```text
You are an AI-assisted API test designer for HW6 EShop API Testing.
Use only the assignment, README.md, api_specification.md, and setup_guide.md as source of truth.
For FR01 Account registration, analyse POST /api/register for a guest user.

Generate the initial AI candidate suite before human filtering. The suite must cover:
- successful registration with unique email;
- required fields name, email, password;
- email format and duplicate email partitions;
- password length and complexity boundaries;
- null, empty, malformed, and wrong-type body values;
- security probes for SQL injection, XSS-like input, sensitive-data leakage, and role injection;
- response schema checks for success and validation responses.

Return the raw output as a Markdown test-case table. Keep the expected result tied to the source of truth, not to current buggy implementation behavior. Do not add human-added cases in this initial output.
```

## Prompt Context Given To AI

| Field | Value |
|---|---|
| Feature | FR01 - Account registration |
| Endpoint(s) | POST /api/register |
| Tooling target | Postman collection with Newman execution evidence |
| Required evidence rule | Every executed request must include `X-Student-Id` during real execution |
| Oracle rule | Expected behaviour must come from README.md, api_specification.md, setup_guide.md, and HW6 assignment, not from implementation source |
| Raw-output status | Preserved before human filtering and before final testcase pruning |

## Raw AI Output - Candidate Test Cases

| ID | Category | Objective | Expected Status | Expected Response / Schema |
|---|---|---|---:|---|
| FR01-API-001 | Domain | Register with all valid fields and a unique email | 200 | JSON has message='User registered successfully' and numeric id |
| FR01-API-002 | Domain | Reject missing name | 400 | Error response explains name is required |
| FR01-API-003 | Domain | Reject empty name | 400 | Error response explains name is required |
| FR01-API-004 | Domain | Reject whitespace-only name | 400 | Error response explains name is required after trimming |
| FR01-API-005 | Boundary | Accept one-character non-empty name | 200 | User registered successfully |
| FR01-API-006 | Domain | Accept long but valid name | 200 | User registered successfully |
| FR01-API-007 | Security | Store/display name safely when it contains script payload | 200 | Registration succeeds or safely rejects; no script execution in downstream UI evidence |
| FR01-API-008 | Domain | Reject missing email | 400 | Error response explains email is required |
| FR01-API-009 | Domain | Reject empty email | 400 | Error response explains valid email is required |
| FR01-API-010 | Domain | Reject email without at sign | 400 | Error response explains valid email format is required |
| FR01-API-011 | Domain | Reject email without domain | 400 | Error response explains valid email format is required |
| FR01-API-012 | Domain | Reject email without local part | 400 | Error response explains valid email format is required |
| FR01-API-013 | Domain | Reject email with spaces | 400 | Error response explains valid email format is required |
| FR01-API-014 | Domain | Accept plus-tag valid email | 200 | User registered successfully |
| FR01-API-015 | Domain | Accept mixed-case valid email | 200 | User registered successfully |
| FR01-API-016 | Domain | Reject duplicate email | 400 | Second registration is rejected because email must be unique |
| FR01-API-017 | Security | Reject SQL injection-looking email without server error | 400 | No auth bypass or database error; safe JSON error |
| FR01-API-018 | Security | Reject SQL injection-looking name without server error | 200 | Registration succeeds or safely rejects; database remains available |
| FR01-API-019 | Domain | Reject missing password | 400 | Error response explains password is required |
| FR01-API-020 | Domain | Reject empty password | 400 | Error response explains password is required/weak |
| FR01-API-021 | Boundary | Reject password length 7 | 400 | Password length boundary below 8 rejected |
| FR01-API-022 | Boundary | Accept password length 8 with all required classes | 200 | User registered successfully |
| FR01-API-023 | Domain | Reject password missing uppercase | 400 | Password complexity rejection |
| FR01-API-024 | Domain | Reject password missing lowercase | 400 | Password complexity rejection |
| FR01-API-025 | Domain | Reject password missing digit | 400 | Password complexity rejection |
| FR01-API-026 | Domain | Reject password missing special character | 400 | Password complexity rejection |
| FR01-API-027 | Domain | Accept password with @ special character | 200 | User registered successfully |
| FR01-API-028 | Domain | Accept password with dollar special character | 200 | User registered successfully |
| FR01-API-029 | Domain | Accept password with ampersand special character | 200 | User registered successfully |
| FR01-API-030 | Schema | Success response schema contains only message and numeric id | 200 | JSON object with string message and number id; no password field |
| FR01-API-031 | Security | Success response must not expose password | 200 | Response does not contain password or password hash |
| FR01-API-032 | Domain | Reject null name | 400 | Name validation error |
| FR01-API-033 | Domain | Reject null email | 400 | Email validation error |
| FR01-API-034 | Domain | Reject null password | 400 | Password validation error |
| FR01-API-035 | Domain | Reject unexpected role field during registration | 400 | Registration rejects role injection or ignores role; created user is not admin |

## Human Review Note

A human reviewer later checked these AI-generated candidates against the source of truth, execution feasibility, and assignment constraints. Some rows may have been corrected, extended, or removed in the final `test-cases.md`; this file intentionally keeps the raw AI candidate output for auditability.
