# HW03 — GUI and Usability Testing

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc |
| Student ID | 23127404 |
| Contact email | 23127404@student.hcmus.edu.vn |
| Required screenshot identity overlay | 23127404@hcmus.edu.vn |
| System under test | EShop |
| Final automated execution | 2 August 2026 |

## Submission status

This package contains an executed GUI checklist, verified desktop defect evidence, completed Chrome and Firefox cross-browser runs, usability-study instruments, AI documentation, and a reusable Agent Skill. Results requiring real participants, a qualifying mobile device, GitHub Issue pages, or a demonstration video remain explicitly incomplete rather than being simulated.

## Selected scope

- Shopping cart and checkout-related behavior (FR-07 and FR-08 interactions)
- Order state machine (FR-10)
- User order history (FR-11)
- Admin order and product management (FR-18 context)
- Mobile Product Detail (FR-23, the Mobile equivalent of FR-06); only this assigned FR uses Expo/Mobile in Task 1

## Self-assessment

| Criterion | Maximum | Self-assessed score | Basis |
|---|---:|---:|---|
| Task 1 — GUI checklist, execution, and defects | 30 | 24 | 45 classified: 31 runtime-executed and 14 source-reviewed Mobile checks; 20 defects; Mobile screenshots and GitHub Issue evidence pending |
| Task 2 — Usability evaluation | 40 | 8 | Scenario, instruments, moderator protocol, and analysis templates complete; no participant session is claimed |
| Task 3 — Cross-browser / cross-platform | 20 | 13 | Google Chrome and Firefox flows executed with five captures each; mobile not executed |
| Task 4 — Agent Skill | 10 | 6 | Reusable skill supplied; demonstration video pending |
| **Total** | **100** | **51** | Evidence-based assessment; not a claim of 90% rubric completion |

If packaged before the missing evidence is added, the corresponding filename grade component would be `051`, not `090`.

## Test summary

| Measure | Result |
|---|---|
| Screens evaluated at runtime | Product Detail, Cart, Checkout, Profile/Order History, Admin Dashboard, Admin Orders, Admin Products |
| Additional behavior evaluated | Coupon API and order-state transitions |
| Checklist items designed | 45 |
| Checklist items executed | 45 (31 runtime-executed; 14 source-reviewed) |
| Passed | 24 |
| Failed | 21 |
| Not executed | 0 checklist items; CP-03 device run remains pending |
| Verified defects | 20: 3 Critical, 11 Major, 6 Minor |
| FR-23 evidence status | 8 source-derived Passed; 6 source-derived Failed; screenshots pending |
| Completed qualifying environments | 2: Google Chrome Desktop and Firefox Desktop |
| Pending environment | Physical or approved cloud mobile device |
| Official usability participants | 0 of 7; sessions pending |
| Demo videos | 0; link pending |

## Evidence index

- `main_report.md` and `main_report.pdf`: integrated report and limitations.
- `checklist/gui_checklist.xlsx`: submission-ready checklist with 45 detailed items and a reconciled `Test Summary` sheet. The editable CSV source is retained outside the submission package under `workbench/data/`.
- `bugs/bug_report.md`: 15 runtime-verified defects plus 5 source-confirmed Mobile defects and evidence mapping.
- `bugs/evidence_images/`: authentic failed-item screenshots.
- `usability/`: one complete test script, participant register, consolidated results workbook, combined reference/findings report, and recording-link index.
- `cross_platform/`: Chrome and Firefox evidence plus the documented mobile gap.
- `ai_reports/`: mandatory AI Critique and AI Audit Report.
- `agent_skills/`: reusable GUI/usability testing skill, output contract, artifact validator, and pending demo link. The same executable package is installed at repository root under `.agents/skills/gui-usability-tester/`.
- `git_commit_log.txt`: genuine repository history export.

## Outstanding evidence

1. Access-test the supplied shared Drive folder in a signed-out browser, map each Pilot/P1–P7 file, and reconcile the recordings with notes, SUS responses, timestamps, and synthesis.
2. Execute a physical or approved cloud mobile environment and add the required identity overlay.
3. Create GitHub Issues for the verified defects, attach the runtime images, and add genuine Issue-page screenshots.
4. Record, upload, and access-test the Agent Skill demonstration video.

## Evidence integrity statement

The [shared Google Drive folder](https://drive.google.com/drive/u/0/folders/1_3wIHUVqJGG-mPwcZotoAStgRjd6X9x_) for the Pilot and P1–P7 recordings has been supplied and indexed under `usability/recordings/video_links.md`; signed-out access and individual-file mapping remain to be verified. No mobile screenshot or GitHub Issue page has been generated or represented as completed. The 31 Web/Admin/API results come from live Google Chrome execution. The 14 FR-23 results are explicitly labeled static source review and remain subject to real-device confirmation. All cross-browser images are captures of the running SUT in the browser identified by their captions.

The report contact address is `23127404@student.hcmus.edu.vn`. The shorter `23127404@hcmus.edu.vn` string visible in cross-platform captures is the identity overlay required by the assignment PDF, not the contact email. Only the contents of this `deliverables` directory are intended for the final submission ZIP.
