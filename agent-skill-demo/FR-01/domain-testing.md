# Domain Testing - FR-01 Account registration

## Domain Model

| Variable / Condition | Type | Input Source | Constraint / Rule | Valid Partitions | Invalid Partitions | Dependencies | Evidence Source | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Full name | String | Web form / API body `name` | Required | Non-empty human name | Missing, empty, whitespace-only, null | Required with email/password | `README.md` FR-01; `frontend-web/src/pages/Register.jsx`; `backend/server.js` | No documented max length |
| Email | String | Web form / API body `email` | Required, valid format, unique | Valid email not already registered | Missing, empty, malformed, duplicate existing email | Duplicate check should use database state | `README.md` FR-01; `api_specification.md`; `backend/database.js` | Email uniqueness should be case-insensitive unless clarified |
| Password | String | Web form / API body `password` | Min 8 chars; uppercase, lowercase, digit, special char from allowed set | Meets all complexity rules | Missing, too short, missing uppercase, missing lowercase, missing digit, missing allowed special char, contains only whitespace as special | Must match confirmation | `README.md` FR-01; `frontend-web/src/pages/Register.jsx` | Allowed special set is exactly the documented set |
| Confirm password | String | Required UI field | Required and must match password | Matches password exactly | Missing, empty, mismatch | Depends on password | `README.md` FR-01 | API may not need separate field if checked client-side, but UI must provide it |
| Existing account state | Database row | `users.email` | Email must be unique | Email absent from users table | Email already exists | Depends on submitted email | `backend/database.js`; `backend/server.js` | Seed user `test@eshop.com` can represent duplicate |
| Registration outcome | UI/API state | Submit action | Success creates account and redirects to login | 200 response then `/login` route | Validation error, duplicate error, no account created | Depends on all required inputs valid | `api_specification.md`; `frontend-web/src/pages/Register.jsx` | Redirect observed only in code, not executed |

## Domain Test Design Notes

The representative Domain Testing set covers valid registration, required-field invalid partitions, email format and uniqueness, each password-complexity invalid partition, confirm-password mismatch, and the frontend/backend contradiction around whitespace versus allowed special characters. Combinatorial explosion is avoided by holding all other variables valid while varying one partition, except where password and confirmation interact.
