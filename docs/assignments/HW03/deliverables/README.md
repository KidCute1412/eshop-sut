# HW03 — GUI and Usability Testing

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc |
| Student ID | 23127404 |
| Email | 23127404@hcmus.edu.vn |
| System under test | EShop |
| Final automated execution | 2 August 2026 |

## Submission status

This package contains an executed GUI checklist, verified desktop defect evidence, completed Chrome and Firefox cross-browser runs, usability-study instruments, AI documentation, and a reusable Agent Skill. Results requiring real participants, a qualifying mobile device, GitHub Issue pages, or a demonstration video remain explicitly incomplete rather than being simulated.

## Selected scope

- Shopping cart and checkout-related behavior (FR-07 and FR-08 interactions)
- Order state machine (FR-10)
- User order history (FR-11)
- Admin order and product management (FR-18 context)
- Pool D Mobile Product Detail and cart behavior; the assignment specification assigns no FR number to this pool

## Self-assessment

| Criterion | Maximum | Self-assessed score | Basis |
|---|---:|---:|---|
| Task 1 — GUI checklist, execution, and defects | 30 | 24 | 45 designed; 31 executed twice; 15 verified bugs with runtime screenshots; Mobile and GitHub Issue evidence pending |
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
| Checklist items executed | 31 |
| Passed | 16 |
| Failed | 15 |
| Not executed | 14 Mobile-dependent items |
| Verified defects | 15: 3 Critical, 9 Major, 3 Minor |
| Unverified Mobile hypotheses | 4; excluded from the bug total |
| Completed qualifying environments | 2: Google Chrome Desktop and Firefox Desktop |
| Pending environment | Physical or approved cloud mobile device |
| Official usability participants | 0 of 7; sessions pending |
| Demo videos | 0; link pending |

## Evidence index

- `main_report.md` and `main_report.pdf`: integrated report and limitations.
- `checklist/`: canonical CSV and generated Excel checklist.
- `bugs/bug_report.md`: 15 runtime-verified defects and evidence mapping.
- `bugs/evidence_images/`: authentic failed-item screenshots.
- `usability/`: scenario, complete session runbook, verified technical reference results, participant register, session metrics, SUS instruments, checkpoint notes, findings structure, and recording index.
- `cross_platform/`: Chrome and Firefox evidence plus the documented mobile gap.
- `ai_reports/`: mandatory AI Critique and AI Audit Report.
- `agent_skills/`: reusable GUI/usability testing skill and pending demo link.
- `git_commit_log.txt`: genuine repository history export.

## Outstanding evidence

1. Conduct one pilot and seven moderated sessions with eligible participants; add consented recordings, notes, SUS responses, and synthesis.
2. Execute a physical or approved cloud mobile environment and add the required identity overlay.
3. Create GitHub Issues for the verified defects, attach the runtime images, and add genuine Issue-page screenshots.
4. Record, upload, and access-test the Agent Skill demonstration video.

## Evidence integrity statement

No participant identity, usability response, mobile screenshot, GitHub Issue page, or video URL has been generated or represented as completed. Every checklist `Passed` or `Failed` status comes from live Google Chrome execution; all cross-browser images are captures of the running SUT in the browser identified by their captions.
