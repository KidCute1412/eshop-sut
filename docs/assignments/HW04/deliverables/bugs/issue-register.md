# HW04 GitHub Issue Register

> **Generated reconciliation index.** `bug_report.md` is the single source of truth for detailed defect entries,
> screenshots, dispositions, and Issue URLs. The student should not maintain the same URL twice: update
> `bug_report.md` once, then ask the automation agent to refresh this index before packaging.

## Current status

The final reports contain 19 unique logical candidates. Agent triage confirmed 17 defects and rejected two feedback-oracle candidates. All 17 confirmed defects now have public GitHub Issue URLs recorded below.

Current verified public HW04 Issue count: **17**.

| Candidate | Requirement | Case | Assertion evidence | Issue state | Public Issue URL | Local screenshot captured |
|---|---|---|---|---|---|---|
| `HW04-CAND-001` | FR-06 | `FR06-07` | Chromium, Firefox, WebKit | Confirmed → BUG-001 | https://github.com/KidCute1412/eshop-sut/issues/141 | Yes |
| `HW04-CAND-002` | FR-06 | `FR06-09` | Chromium, Firefox, WebKit | Confirmed → BUG-002 | https://github.com/KidCute1412/eshop-sut/issues/142 | Yes |
| `HW04-CAND-003` | FR-06 | `FR06-11` | Chromium, Firefox, WebKit | Rejected — oracle gap | N/A | Yes |
| `HW04-CAND-004` | FR-06 | `FR06-12` | Chromium, Firefox, WebKit | Rejected — oracle gap | N/A | Yes |
| `HW04-CAND-005` | FR-06 | `FR06-13` | Chromium, Firefox, WebKit | Confirmed → BUG-003 | https://github.com/KidCute1412/eshop-sut/issues/143 | Yes |
| `HW04-CAND-006` | FR-06 | `FR06-14` | Chromium, Firefox, WebKit | Confirmed → BUG-004 | https://github.com/KidCute1412/eshop-sut/issues/144 | Yes |
| `HW04-CAND-007` | FR-10 | `FR10-06` | Chromium, Firefox, WebKit | Confirmed → BUG-005 | https://github.com/KidCute1412/eshop-sut/issues/145 | Yes |
| `HW04-CAND-008` | FR-10 | `FR10-11` | Chromium, Firefox, WebKit | Confirmed → BUG-006 | https://github.com/KidCute1412/eshop-sut/issues/146 | Yes |
| `HW04-CAND-009` | FR-10 | `FR10-12` | Chromium, Firefox, WebKit | Confirmed → BUG-007 | https://github.com/KidCute1412/eshop-sut/issues/147 | Yes |
| `HW04-CAND-010` | FR-10 | `FR10-16` | Chromium, Firefox, WebKit | Confirmed → BUG-008 | https://github.com/KidCute1412/eshop-sut/issues/148 | Yes |
| `HW04-CAND-011` | FR-12 | `FR12-03` | Chromium, Firefox, WebKit | Confirmed → BUG-009 | https://github.com/KidCute1412/eshop-sut/issues/149 | Yes |
| `HW04-CAND-012` | FR-12 | `FR12-06` | Chromium, Firefox, WebKit | Confirmed → BUG-010 | https://github.com/KidCute1412/eshop-sut/issues/150 | Yes |
| `HW04-CAND-013` | FR-12 | `FR12-08` | Chromium, Firefox, WebKit | Confirmed → BUG-011 | https://github.com/KidCute1412/eshop-sut/issues/151 | Yes |
| `HW04-CAND-014` | FR-12 | `FR12-09` | Chromium, Firefox, WebKit | Confirmed → BUG-012 | https://github.com/KidCute1412/eshop-sut/issues/152 | Yes |
| `HW04-CAND-015` | FR-12 | `FR12-11` | Chromium, Firefox, WebKit | Confirmed → BUG-013 | https://github.com/KidCute1412/eshop-sut/issues/153 | Yes |
| `HW04-CAND-016` | FR-12 | `FR12-12` | Chromium, Firefox, WebKit | Confirmed → BUG-014 | https://github.com/KidCute1412/eshop-sut/issues/154 | Yes |
| `HW04-CAND-017` | FR-12 | `FR12-14` | Chromium, Firefox, WebKit | Confirmed → BUG-015 | https://github.com/KidCute1412/eshop-sut/issues/155 | Yes |
| `HW04-CAND-018` | FR-12 | `FR12-17` | Chromium, Firefox, WebKit | Confirmed → BUG-016 | https://github.com/KidCute1412/eshop-sut/issues/156 | Yes |
| `HW04-CAND-019` | FR-12 | `FR12-19` | Chromium, Firefox, WebKit | Confirmed → BUG-017 | https://github.com/KidCute1412/eshop-sut/issues/157 | Yes |

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

The 17 confirmed defects have complete copy-ready packets under `issue-packets/BUG-001/` through
`issue-packets/BUG-017/`. Their public GitHub URLs are now recorded in this index and the canonical
`bug_report.md` table.
