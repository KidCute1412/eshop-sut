# FR01 - Account registration API Mapping

| Field | Value |
|---|---|
| Feature | FR-01 Account registration |
| Pool | A - Authentication, Categories, and Products |
| Primary endpoint | POST /api/register |
| Actor | Guest user |
| Authentication | Not required |
| Request body | `name`, `email`, `password` |
| Source of truth | `README.md` FR-01, SEC-01/SEC-05; `api_specification.md` 1.1 |
| Key rules | name/email/password required; email format valid and unique; password >= 8 chars with uppercase/lowercase/digit/special; API success returns message and id |
| Documented ambiguity | `README.md` requires confirm password at UI level, but `api_specification.md` does not expose `confirmPassword` in `POST /api/register` body; API tests record confirm-password cases as contract ambiguity rather than executable API oracle. |
