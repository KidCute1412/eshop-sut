# Traceability Matrix - FR-01 Account registration

| Requirement / Rule | Evidence Source | Domain Partition | Boundary | Test Case IDs | Status |
| --- | --- | --- | --- | --- | --- |
| Required name/email/password | `README.md` FR-01; `frontend-web/src/pages/Register.jsx` | Valid required fields; missing/empty fields to add in expanded suite | Not applicable | FR01-DT-001 | Not Executed |
| Email valid format | `README.md` FR-01; `frontend-web/src/pages/Register.jsx`; `backend/server.js` | Valid email, malformed email | Not applicable | FR01-DT-001, FR01-DT-002 | Not Executed |
| Email uniqueness | `README.md` FR-01; `backend/database.js`; `backend/server.js` | Unique, duplicate | Existing email count 0/1 | FR01-DT-003, FR01-BVA-004 | Not Executed |
| Password complexity | `README.md` FR-01; `frontend-web/src/pages/Register.jsx` | Strong, missing special | Length min-1/min/min+1 | FR01-DT-005, FR01-BVA-001, FR01-BVA-002, FR01-BVA-003 | Not Executed |
| Confirm password | `README.md` FR-01; `frontend-web/src/pages/Register.jsx` | Match, mismatch | Not applicable | FR01-DT-001, FR01-DT-004 | Not Executed |
| Redirect to login after success | `README.md` FR-01; `frontend-web/src/pages/Register.jsx` | Successful outcome | Not applicable | FR01-DT-001 | Not Executed |

## Uncovered Items

- Expanded suite should add separate cases for missing name, missing email, missing password, whitespace-only name, missing uppercase, missing lowercase, and missing digit.
- Backend API-only tests should be added to confirm whether invalid input is accepted server-side.
