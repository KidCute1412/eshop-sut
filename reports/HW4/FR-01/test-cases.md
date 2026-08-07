# Automation Test Cases - FR-01 Account Registration

Seeded from `reports/HW2/FR-01/test-cases.md`. Fifteen cases were selected to cover successful registration, password validation, required fields, duplicate email, documented special characters, and boundary-style minimum/long password inputs.

| ID | Type | Steps | Test Data | Expected Result | Assertion Pattern(s) | Automatable | Spec File |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FR01-DT-001 | Positive | Open Register, fill valid data, submit | `FR01-DT-001` | Redirect to Login | API response, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-002 | Positive | Open Register, fill alternate valid data, submit | `FR01-DT-002` | Redirect to Login | API response, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-003 | Negative | Submit weak short password | `FR01-DT-003` | Password error remains on Register | Visibility, URL | Yes |  `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-004 | Negative | Submit password without uppercase | `FR01-DT-004` | Password error remains on Register | Visibility, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-005 | Negative | Submit password without digit | `FR01-DT-005` | Password error remains on Register | Visibility, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-006 | Positive | Submit documented `!` special-character password | `FR01-DT-006` | Redirect to Login | API response, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-007 | Edge | Submit minimum accepted current password | `FR01-DT-007` | Redirect to Login | API response, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-008 | Negative | Leave name empty and submit | `FR01-DT-008` | Browser required validation blocks submit | Native validity state | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-009 | Negative | Leave email empty and submit | `FR01-DT-009` | Browser required validation blocks submit | Native validity state | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-010 | Negative | Leave password empty and submit | `FR01-DT-010` | Browser required validation blocks submit | Native validity state | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-011 | Negative | Pre-create email, then register same email | `FR01-DT-011` | Duplicate email is rejected | API response, visibility | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-DT-012 | Edge | Submit long multi-word name with valid data | `FR01-DT-012` | Redirect to Login | API response, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-BVA-009 | Edge | Submit documented `@` special-character password | `FR01-BVA-009` | Redirect to Login | API response, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-BVA-010 | Edge | Submit 20-character password with documented special character | `FR01-BVA-010` | Redirect to Login | API response, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |
| FR01-BVA-011 | Edge | Submit 20-character password with whitespace workaround | `FR01-BVA-011` | Redirect to Login | API response, URL | Yes | `FR-01/tests/fr-01-register.spec.js` |

## Not Automated

| ID | Reason |
| --- | --- |
| None | All 12 selected cases were automated. |

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-08-06T14:03:05Z
- Confirmed at least 12 cases selected with a genuine positive/negative/edge mix: Yes, 15 selected
- Confirmed every "Not Automated" row has a real, specific reason: Yes
