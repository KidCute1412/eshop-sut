# Usability Findings - Register -> Login -> Update Profile

## Pain Point Synthesis

| Finding ID | Description | Participants Affected (of 7) | Type | Severity | Related Session(s) | Related Bug ID |
| --- | --- | --- | --- | --- | --- | --- |
| FIND-001 | Register password-strength hint says a special character is required, but `!`/`@` are rejected; only a password containing a space is accepted | 7 / 7 (P01-P07) | Isolated bug | Major | P01, P02, P03, P04, P05, P06, P07 | BUG-GUI-006 |
| FIND-002 | Login page retains the "Register" page heading after a successful registration, causing users to doubt the redirect worked | 4 / 7 (P01, P03, P04, P06) | Isolated bug | Minor | P01, P03, P04, P06 | BUG-GUI-015 |
| FIND-003 | Login form's first field is labeled "Username" even though the user only ever provided an email address at registration | 3 / 7 (P02, P04, P07) | Isolated bug | Medium | P02, P04, P07 | BUG-GUI-017 |
| FIND-004 | Update Profile's phone-number validation fires and blocks the whole form submission even when the phone field is left blank/untouched, or already matches the stated 9-10 digit rule | 7 / 7 (P01-P07) | Isolated bug | Blocker | P01, P02, P03, P04, P05, P06, P07 | BUG-USE-001 |

## Severity Definitions

- **Blocker**: prevented task completion for most/all participants.
- **Major**: significant friction/hesitation or required facilitator intervention; task eventually
  completed.
- **Minor**: noticed, mildly annoying, did not block completion.
- **Cosmetic**: visual/wording only, no functional impact.


## Recommendations

| Finding ID | Recommendation | Priority |
| --- | --- | --- |
| FIND-001 | Fix the client-side password regex to actually accept the special characters the hint text describes (or fix the hint text to describe what is actually accepted); do not accept whitespace as a substitute for a special character | High |
| FIND-002 | Set the Login page's heading/title independently from Register's, instead of sharing or copy-pasting the same string | High |
| FIND-003 | Relabel the Login field to "Email" (matching what Register actually collects), or explicitly state in the UI that the registered email doubles as the username | Medium |
| FIND-004 | Change the phone-number check in the Update Profile handler to run only when the phone value is non-empty and has actually changed, and mark the field as visually optional if it is meant to be skippable | Critical |

## Human Review

- Reviewer: Nguyen Thanh Tien 
- Review Date and Time: 2026-07-30
- Confirmed every finding traces to real session-notes evidence: Yes — every participant count
  above was re-verified against each session's Observation Log text before this table was written
  (see the per-finding participant lists), not estimated from memory.
