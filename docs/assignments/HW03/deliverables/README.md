# HW03 — GUI and Usability Testing

## Submission identity

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc |
| Student ID | 23127404 |
| Contact email | 23127404@student.hcmus.edu.vn |
| Required screenshot identity overlay | 23127404@hcmus.edu.vn |
| System under test | EShop |
| Desktop execution date | 2 August 2026 |
| Evidence consolidation date | 3 August 2026 |

The contact email and screenshot identity are intentionally different. `23127404@student.hcmus.edu.vn` is the student's contact address; `23127404@hcmus.edu.vn` is the identity string prescribed by the assignment PDF for screenshot overlays.

## Submission overview

This package contains the executed GUI checklist, normalized defect report, public GitHub Issue references, Chrome and Firefox cross-browser evidence, four Mobile Product Detail captures, a moderated usability-study dataset for seven official participants, AI documentation, and a reusable Agent Skill.

## Assigned scope

| Requirement | Evaluation surface |
|---|---|
| FR-07 | Customer Web cart behavior |
| FR-10 | Order creation and state behavior |
| FR-11 | Customer order history |
| FR-18 | Admin order and product management |
| FR-23 | Mobile Product Detail, equivalent to FR-06 on Mobile |

Only FR-23 is evaluated through the Expo/Mobile frontend for Task 1. Web Product Detail appears in the usability journey only as a supporting FR-06 step and is not presented as FR-23 evidence.

## Current results

### Task 1 — GUI checklist and defects

| Measure | Result |
|---|---|
| Checklist items designed | 45 |
| Checklist items executed | 45 (31 desktop/API; 14 FR-23, including screenshot-backed Mobile checks) |
| Passed | 25 |
| Failed | 20 |
| Not executed | 0 checklist items; CP-03 metadata/overlay completion remains pending |
| Verified defects | 19 runtime-observed; four Mobile screenshots still need the required identity overlay |
| FR-23 evidence status | 14 classified: 9 Passed and 5 Failed |

All 20 failed checklist rows reference a Bug ID and evidence. The 19 normalized defects comprise 15 desktop defects and four Mobile defects; two failed Mobile checks map to different effects of the same quantity-validation defect.

### Task 2 — Moderated usability evaluation

| Measure | Result |
|---|---:|
| Pilot | Completed and excluded from official aggregates |
| Official participants | 7 of 7 |
| Independent completions | 7 of 7 (100%) |
| Median recorded task duration | 75 seconds |
| Recorded errors | 14 |
| Recorded hesitations | 14 |
| Moderator interventions | 0 |
| Mean SUS | 73.6 / 100 |

The study evaluates the Customer Web journey FR-07 → FR-10 → FR-11. Structured session, observation, SUS, and recording data are consolidated in `usability/usability_results.xlsx`. The final formatting pass retained the supplied session timestamps without independently recoding every timestamp from video.

### Task 3 — Cross-browser and cross-platform

| Environment | Status | Evidence |
|---|---|---|
| Google Chrome Desktop | Executed | Five screenshots |
| Firefox Desktop | Executed | Five screenshots |
| iPhone / Expo Mobile | Runtime evidence supplied; qualification pending | Four FR-23 screenshots |

Chrome and Firefox completed the same five-screen purchase journey without an observed browser-specific difference. The Mobile captures support visible FR-23 assertions but still require the exact device/iOS/Expo/SUT metadata and the PDF-required identity overlay to qualify CP-03 fully.

### Task 4 — Agent Skill and AI documentation

The reusable `gui-usability-tester` skill includes its operating instructions, evidence rules, output contract, analysis references, automated validator, and unit tests. The AI Audit Report preserves the AI-assistance history and human review decisions. The [Agent Skill demonstration video](https://youtu.be/Um16nCulTtQ) is supplied and its YouTube endpoint was access-tested without authentication on 3 August 2026.

## Evidence index

| Path | Contents |
|---|---|
| `main_report.md`, `main_report.pdf` | Integrated methods, results, limitations, and conclusion |
| `checklist/gui_checklist.xlsx` | Two-sheet checklist workbook with summary and 45 classified checks |
| `bugs/bug_report.md` | Nineteen normalized defects with reproduction details, evidence, and GitHub URLs |
| `bugs/evidence_images/` | Desktop failed-check evidence |
| `usability/` | Participant register, protocol, results workbook, findings, and recording index |
| `cross_platform/` | Chrome, Firefox, and Mobile evidence with comparison report |
| `ai_reports/` | AI Audit Report and 200–300-word AI Critique in Markdown and PDF |
| `agent_skills/` | Submission mirror of the reusable skill and its validator |
| `git_commit_log.txt` | Exported repository history |

Editable CSV sources, internal scripts, specifications, archives, caches, and previous ZIP files are intentionally kept outside this deliverables directory.

## Evidence integrity and limitations

- The 31 Web/Admin/API results were established through live Google Chrome execution; source inspection was used for diagnosis, not as execution evidence.
- The ten Chrome/Firefox screenshots are preserved unchanged and contain the PDF-prescribed identity caption.
- The four Mobile screenshots are authentic runtime captures mapped only to assertions visible in those captures. They still lack the required overlay and complete environment metadata.
- Pilot and P1–P7 recording files are mapped in `usability/recordings/video_links.md`. Public access was verified on 3 August 2026, and the folder page listed all eight expected recordings.
- Usability aggregates are calculated from the structured workbook entries. The final documentation pass did not independently recode each video timestamp.
- All 19 GitHub Issue URLs and hosted attachments were verified through the public GitHub API on 3 August 2026. Issue #118 was rechecked after its student-ID title prefix was corrected to `23127404`.

## Final external checks

1. Add the required `23127404@hcmus.edu.vn` overlay and exact device/iOS/Expo/SUT metadata to qualifying Mobile evidence.
2. Regenerate `git_commit_log.txt` after the final commit.
3. Create the final ZIP exclusively from the contents of this `deliverables` directory.

## Packaging rule

Only the contents inside `docs/assignments/HW03/deliverables` are intended for the final submission ZIP. Do not include `specs`, `workbench`, archives, source CSV files, caches, internal scripts, previous ZIP files, or the root `.agents` installation.
