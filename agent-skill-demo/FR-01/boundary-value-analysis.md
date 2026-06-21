# Boundary Value Analysis - FR-01 Account registration

## Boundary Model

| Variable | Boundary Rule | Boundary Source | Test Values | Expected Classification | Justification |
| --- | --- | --- | --- | --- | --- |
| Password length | Minimum 8 characters | `README.md` FR-01 | 7 chars, 8 chars, 9 chars | 7 invalid; 8 and 9 valid when complexity is satisfied | Ordered lower-bound string length |
| Password uppercase count | At least 1 uppercase | `README.md` FR-01 | 0 uppercase, 1 uppercase | 0 invalid; 1 valid when other complexity rules are satisfied | Count boundary at one required uppercase |
| Password lowercase count | At least 1 lowercase | `README.md` FR-01 | 0 lowercase, 1 lowercase | 0 invalid; 1 valid when other complexity rules are satisfied | Count boundary at one required lowercase |
| Password digit count | At least 1 digit | `README.md` FR-01 | 0 digits, 1 digit | 0 invalid; 1 valid when other complexity rules are satisfied | Count boundary at one required digit |
| Password allowed-special count | At least 1 allowed special char | `README.md` FR-01 | 0 allowed specials, 1 allowed special | 0 invalid; 1 valid when other complexity rules are satisfied | Count boundary at one required special character |
| Duplicate email count | Existing matching email count must be 0 | `README.md`; `backend/database.js` | 0 existing, 1 existing | 0 valid; 1 invalid | Count boundary around uniqueness |

## Non-Boundary Domains

| Domain | Reason BVA Does Not Apply |
| --- | --- |
| Email format categories | Format categories are not ordered; use Domain Testing for valid/malformed emails |
| Confirm-password match/mismatch | Binary relation, not an ordered range |
| Redirect destination | State outcome, not a bounded input |
