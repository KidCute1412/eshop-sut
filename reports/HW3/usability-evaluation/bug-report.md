# Bug Report - Usability Evaluation (Register -> Login -> Update Profile)

## BUG-USE-001: Update Profile Phone Validation Blocks Submission Even When the Field Is Left Blank or Already Valid

- Bug ID: BUG-USE-001
- Title: Update Profile phone validation blocks submission even when the field is left blank or already valid
- Related Finding: `FIND-004` in `findings.md`
- Related Session(s): P01, P02, P03, P04, P05, P06, P07 (7 of 7 real sessions)
- Related Requirement or Heuristic: `README.md` FR-04 (Personal profile management); Nielsen
  heuristic "Error Prevention" / "Help users recognize, diagnose, and recover from errors"
- Severity: Blocker
- Status: Confirmed

### Preconditions

- A registered, logged-in user on the Profile page (`http://localhost:5173/profile`).

### Reproduction Steps

1. Log in and open the Profile page.
2. Either (a) leave the Phone Number field exactly as it was (unedited), or (b) clear it entirely,
   or (c) enter a value that already matches the stated "9-10 digits" rule.
3. Edit only the shipping address field.
4. Click Update.

### Expected Result

The update should succeed for the address change; a phone-number error should only appear if the
phone field was actually edited to an invalid value. `README.md` FR-04 does not document the phone
field as unconditionally re-validated on every unrelated update.

### Actual Result

Across all 7 real sessions, the Update Profile submission was blocked by
`"Invalid phone number. Please enter 9-10 digits."`, even in cases where the participant had not
touched the phone field, had cleared it, or had entered a value that visibly matched the stated
digit-count rule. Every session's Task Outcome is recorded as `Partial` for this reason — this is
the single most consistent blocker across the entire evaluation. One participant (P05) explicitly
stopped attempting further corrections after repeated failures. See `observation-log-summary.md`
for the full per-session quotes.

### Evidence

- [session-notes/P01.md](session-notes/P01.md)
- [session-notes/P05.md](session-notes/P05.md)

### GitHub Issue

- [Github issue](https://github.com/KidCute1412/eshop-sut/issues/105)

## Failed Item / Finding to Bug Mapping

| Failed Item or Finding                               | Bug ID                                                                      | Evidence                                             | GitHub Issue Link                                                   |
| ---------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------- |
| FIND-001 (password rule mismatch)                    | BUG-GUI-006 (filed under Task 1, `reports/HW3/gui-checklist/bug-report.md`) | `session-notes/P01.md`..`P07.md`, all sessions       | [Github issue](https://github.com/KidCute1412/eshop-sut/issues/89)  |
| FIND-002 (stale "Register" heading on Login)         | BUG-GUI-015 (filed under Task 1)                                            | `session-notes/P01.md`, `P03.md`, `P04.md`, `P06.md` | [Github issue](https://github.com/KidCute1412/eshop-sut/issues/98)  |
| FIND-003 ("Username" field mislabeling)              | BUG-GUI-017 (filed under Task 1)                                            | `session-notes/P02.md`, `P04.md`, `P07.md`           | [Github issue](https://github.com/KidCute1412/eshop-sut/issues/100) |
| FIND-004 (phone validation blocks blank/valid field) | BUG-USE-001 (new, Task 2 only)                                              | `session-notes/P01.md`..`P07.md`, all sessions       | [Github issue](https://github.com/KidCute1412/eshop-sut/issues/105) |

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-07-30
- Review Scope: All 4 bugs referenced from the usability sessions (1 new: `BUG-USE-001`; 3 shared
  with Task 1: `BUG-GUI-006`, `BUG-GUI-015`, `BUG-GUI-017`)
- Confirmed every bug is reproducible and traces to real session-notes evidence.
- Corrections Made: None required at this review pass; severity (Blocker for `BUG-USE-001`) was set
  based on it being the single most consistent cause of `Task Outcome: Partial` across all 7
  sessions, not assumed.
- Approved: Yes
