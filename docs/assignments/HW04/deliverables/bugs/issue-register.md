# HW04 GitHub Issue Register

> **Generated reconciliation index.** `bug_report.md` is the single source of truth for detailed defect entries,
> screenshots, dispositions, and Issue URLs. The student should not maintain the same URL twice: update
> `bug_report.md` once, then ask the automation agent to refresh this index before packaging.

## Current status

The final reports contain 19 unique logical candidates. Agent triage confirmed 17 defects and rejected two feedback-oracle candidates. No verified public HW04 Issue URL has been supplied.

Current verified public HW04 Issue count: **0**.

| Candidate | Requirement | Case | Assertion evidence | Issue state | Public Issue URL | Screenshot verified |
|---|---|---|---|---|---|---|
| `HW04-CAND-001` | FR-06 | `FR06-07` | Chromium, Firefox, WebKit | Confirmed → BUG-001 | URL pending | Yes |
| `HW04-CAND-002` | FR-06 | `FR06-09` | Chromium, Firefox, WebKit | Confirmed → BUG-002 | URL pending | Yes |
| `HW04-CAND-003` | FR-06 | `FR06-11` | Chromium, Firefox, WebKit | Rejected — oracle gap | N/A | Yes |
| `HW04-CAND-004` | FR-06 | `FR06-12` | Chromium, Firefox, WebKit | Rejected — oracle gap | N/A | Yes |
| `HW04-CAND-005` | FR-06 | `FR06-13` | Chromium, Firefox, WebKit | Confirmed → BUG-003 | URL pending | Yes |
| `HW04-CAND-006` | FR-06 | `FR06-14` | Chromium, Firefox, WebKit | Confirmed → BUG-004 | URL pending | Yes |
| `HW04-CAND-007` | FR-10 | `FR10-06` | Chromium, Firefox, WebKit | Confirmed → BUG-005 | URL pending | Yes |
| `HW04-CAND-008` | FR-10 | `FR10-11` | Chromium, Firefox, WebKit | Confirmed → BUG-006 | URL pending | Yes |
| `HW04-CAND-009` | FR-10 | `FR10-12` | Chromium, Firefox, WebKit | Confirmed → BUG-007 | URL pending | Yes |
| `HW04-CAND-010` | FR-10 | `FR10-16` | Chromium, Firefox, WebKit | Confirmed → BUG-008 | URL pending | Yes |
| `HW04-CAND-011` | FR-12 | `FR12-03` | Chromium, Firefox, WebKit | Confirmed → BUG-009 | URL pending | Yes |
| `HW04-CAND-012` | FR-12 | `FR12-06` | Chromium, Firefox, WebKit | Confirmed → BUG-010 | URL pending | Yes |
| `HW04-CAND-013` | FR-12 | `FR12-08` | Chromium, Firefox, WebKit | Confirmed → BUG-011 | URL pending | Yes |
| `HW04-CAND-014` | FR-12 | `FR12-09` | Chromium, Firefox, WebKit | Confirmed → BUG-012 | URL pending | Yes |
| `HW04-CAND-015` | FR-12 | `FR12-11` | Chromium, Firefox, WebKit | Confirmed → BUG-013 | URL pending | Yes |
| `HW04-CAND-016` | FR-12 | `FR12-12` | Chromium, Firefox, WebKit | Confirmed → BUG-014 | URL pending | Yes |
| `HW04-CAND-017` | FR-12 | `FR12-14` | Chromium, Firefox, WebKit | Confirmed → BUG-015 | URL pending | Yes |
| `HW04-CAND-018` | FR-12 | `FR12-17` | Chromium, Firefox, WebKit | Confirmed → BUG-016 | URL pending | Yes |
| `HW04-CAND-019` | FR-12 | `FR12-19` | Chromium, Firefox, WebKit | Confirmed → BUG-017 | URL pending | Yes |

`ENV-FIREFOX-NEWPAGE` is retained only as historical diagnosis; the selected final Firefox rerun reached all 51 assertions after the project-context fix. It is not an HW04 SUT defect.

## Reconciliation rules

1. Deduplicate candidates by root behavior before assigning final `BUG-___` IDs.
2. Add an Issue only after current evidence rules out script, data, and environment faults.
3. Use a student-ID-prefixed title, for example `[23127404][FR-06] Product category is absent on detail page`.
4. Include the exact environment, SUT revision, preconditions, numbered steps, test data, expected/actual result, severity, and affected case/run IDs.
5. Attach an authentic screenshot and confirm the public Issue and attachment render for a logged-out viewer where practical.
6. Update `bug_report.md`, the main report, and README from verified URLs; never copy an HW02/HW03 URL as a new HW04 Issue.
7. If a candidate is rejected, preserve the disposition (`test defect`, `data defect`, `environment defect`, `duplicate`, or `not reproducible`) without inflating the defect count.

## Final Issue mapping

The 17 confirmed defects already have complete copy-ready packets under `issue-packets/BUG-001/` through
`issue-packets/BUG-017/`. Their only intentionally incomplete field is the public GitHub URL, which is supplied
after the student files each Issue. The canonical URL entry belongs in `bug_report.md`; this index is refreshed from
that file after URLs are returned.
