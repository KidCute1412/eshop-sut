# HW03 Report — GUI and Usability Testing

## Submission identity

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc (23127404) |
| Contact email | 23127404@student.hcmus.edu.vn |
| Required screenshot identity overlay | 23127404@hcmus.edu.vn |
| System under test | EShop |
| Desktop execution date | 2 August 2026 |
| Evidence consolidation date | 3 August 2026 |
| Primary desktop environment | Google Chrome 151.0.7922.72 on Windows NT 10.0.26200 |

The contact email is the student's real reporting address. The shorter `23127404@hcmus.edu.vn` string is retained specifically as the screenshot identity prescribed by the assignment PDF.

## Executive summary

The submission evaluates EShop across the assigned FR-07, FR-10, FR-11, FR-18, and FR-23 scope. The GUI checklist contains 45 non-duplicate items: 31 Web/Admin/API checks and 14 Mobile Product Detail checks. All 45 are classified, with 25 Passed and 20 Failed. The failures map to 19 runtime-observed defects: 15 desktop defects and four Mobile defects.

Chrome and Firefox each provide five screenshots of the same Customer Web purchase journey. Four additional Mobile captures support narrowly scoped, visible FR-23 assertions. The moderated Customer Web usability study includes one pilot and seven official participants; all seven official participants completed the task independently. The structured results report a median task duration of 75 seconds, 14 errors, 14 hesitations, no moderator interventions, and a mean SUS score of 73.6/100.

The principal remaining external gaps are Mobile overlay/environment qualification, anonymous Drive-access confirmation, correction of the Issue #118 title prefix, and the Agent Skill demonstration video. These limitations do not alter the reported executed results, but they affect final evidence compliance where stated.

## 1. GUI checklist and defect reporting

### 1.1 Assigned scope

| Requirement | Evaluation surface |
|---|---|
| FR-07 | Customer Web cart behavior |
| FR-10 | Order creation and state behavior |
| FR-11 | Customer order history |
| FR-18 | Admin order and product management |
| FR-23 | Mobile Product Detail, equivalent to FR-06 on Mobile |

FR-23 is the only assigned requirement evaluated through the Expo/Mobile frontend in Task 1. Web Product Detail is used as a supporting FR-06 step in the usability journey and is not labeled as FR-23 evidence.

### 1.2 Checklist design

| Interface aspect | Items |
|---|---:|
| IA-01 — General UI standards | 13 |
| IA-02 — Forms and validation | 14 |
| IA-03 — Navigation | 6 |
| IA-04 — Feedback and state | 12 |
| **Total** | **45** |

The checklist workbook contains a machine-readable `Test Summary` sheet and a detailed `GUI Checklist` sheet. Each row records Item ID, FR ID, interface aspect, screen, UI element, precondition, procedure, expected result, actual result, status, severity, evidence, Bug ID, notes, provenance, execution state, environment, and execution time.

### 1.3 Execution method

AI assisted with initial checklist drafting, source-oriented hypotheses, automation structure, and editorial reconciliation. Executed results were established through live interaction; source inspection was used to explain likely causes and was not treated as execution evidence.

The desktop execution process was:

1. Preserve the tracked SQLite database state.
2. Initialize documented seed data and start Backend, Customer Web, and Admin Web.
3. Execute the checklist in Google Chrome using the controlled automation workflow.
4. Capture authentic screenshots for failed desktop checks.
5. Reset the database and repeat the complete run.
6. Correct automation-only selector, dialog, or timing faults without modifying the SUT.
7. Reconcile checklist rows, defect records, evidence paths, and summary counts.
8. Restore the original database state.

Mobile classifications are limited to conditions visible in the four supplied runtime captures. No unshown loading sequence, delayed transition, repeated-add sequence, or data variant is claimed.

### 1.4 Results

| Measure | Result |
|---|---:|
| Items designed | 45 |
| Items executed/classified | 45 |
| Desktop/API checks | 31: 16 Passed, 15 Failed |
| FR-23 Mobile checks | 14: 9 Passed, 5 Failed |
| **Combined Passed** | **25** |
| **Combined Failed** | **20** |
| Not Executed | 0 checklist items |
| Unique verified defects | 19 |

All 20 Failed rows reference a Bug ID and evidence. Five failed Mobile rows map to four defects because CHK-GUI-012 and CHK-GUI-041 capture different effects of the same zero-quantity validation behavior.

### 1.5 Defect profile

| Severity | Count | Representative risk |
|---|---:|---|
| Critical | 3 | Editable authoritative total, stored HTML execution, and incorrect percentage-coupon calculation |
| High | 8 | Broken primary action, invalid quantities, invalid order transitions, incorrect revenue, and corrupted product state |
| Medium | 3 | Silent decimal truncation, valid-phone rejection, and unavailable order details |
| Low | 5 | Visual, content, navigation, loading, and success-feedback defects |

Detailed reproduction procedures, expected and actual results, evidence images, and GitHub Issue URLs are provided in `bugs/bug_report.md`. All 19 public Issue URLs and their hosted attachments were verified through the GitHub API on 3 August 2026. Issue #118 still requires correction of a missing digit in its student-ID title prefix.

## 2. Moderated usability evaluation

### 2.1 Objective and scope

The study evaluates whether typical online shoppers can independently complete the Customer Web journey FR-07 → FR-10 → FR-11. Web Product Detail is a supporting FR-06 entry step; participants are not claimed to have evaluated Mobile FR-23.

The task requires the participant to locate an iPhone 15 Pro Max, review it, add one unit to the cart, complete checkout without a coupon, and identify the newest order status. The success criterion is completion of the order and identification of the visible newest status without procedural assistance.

### 2.2 Protocol and measures

The moderator protocol defines environment preparation, consent language, neutral prompts, timer boundaries, completion categories, and post-task questions. The study records:

- Completion outcome.
- Task duration.
- Errors and hesitations.
- Moderator interventions.
- Ten standard SUS responses.
- Qualitative feedback about clarity, recovery, speed, and trust.

The pilot is excluded from official participant frequencies and SUS aggregates. P1–P7 form the official dataset. Participant contacts are masked in the submission register.

### 2.3 Results

| Measure | Result |
|---|---:|
| Pilot | Completed; excluded from official aggregates |
| Official sessions | 7 of 7 |
| Independent completions | 7 of 7 (100%) |
| Median recorded task duration | 75 seconds |
| Total recorded errors | 14 |
| Total recorded hesitations | 14 |
| Moderator interventions | 0 |
| Mean SUS | 73.6 / 100 |

Individual SUS scores are P1 75.0, P2 82.5, P3 67.5, P4 67.5, P5 77.5, P6 75.0, and P7 70.0. The unrounded mean is 73.5714. SUS is calculated by subtracting one from odd-item responses, subtracting even-item responses from five, summing the adjusted values, and multiplying by 2.5. SUS is a 0–100 usability benchmark, not a percentage grade.

### 2.4 Consolidated findings

| ID | Finding | Frequency | Severity | Related defect |
|---|---|---:|---|---|
| UF-01 | Missing first-action add-to-cart feedback caused repeated action and uncertainty. | 7/7 | High | BUG-001 |
| UF-02 | An editable checkout total reduced confidence that the payable amount was authoritative. | 4/7 | High | BUG-006 |
| UF-03 | Retained post-checkout cart contents caused uncertainty about completion or duplicate purchase risk. | 3/7 | Medium | BUG-007 |

The detailed coding basis, recommendations, operational definitions, and technical comparison oracle are provided in `usability/usability_findings.md`. Runtime defect analysis is kept separate from participant observations.

### 2.5 Evidence status

| Evidence | Status |
|---|---|
| Participant register | P1–P7 listed with masked contacts and recorded consent status |
| Structured workbook | Sessions, Observations, SUS, and Recordings sheets complete |
| Recording manifest | Pilot and P1–P7 mapped to `Pilot.mp4` and `P1.mp4`–`P7.mp4` |
| Shared Drive folder | Supplied; anonymous/signed-out access not independently confirmed |
| Final documentation pass | Aggregates recalculated; supplied session timestamps retained without independent video recoding |

This evidence status distinguishes a recorded dataset from independently reperforming the video coding. It avoids claiming a verification step that was not completed during final document formatting.

## 3. Cross-browser and cross-platform verification

### 3.1 Desktop environments

Google Chrome 151.0.7922.72 and Playwright Firefox 144.0.2 completed the Product List → Product Detail → Cart → Checkout → Order History journey on Windows at the tested desktop viewport. Each environment provides five authentic screenshots. No browser-specific layout or navigation difference was observed in the selected flow.

The ten desktop captures remain unchanged. Their captions contain the required `23127404@hcmus.edu.vn` identity together with browser, operating-system, and URL context.

### 3.2 Mobile environment

Four iPhone-sized Expo/Mobile captures cover the FR-23 basic detail screen, default quantity, valid add result, and invalid-zero feedback. These captures support only visible-state assertions in the checklist and defect report.

| Environment | Status | Evidence |
|---|---|---|
| Google Chrome Desktop | Executed | Five screenshots |
| Firefox Desktop | Executed | Five screenshots |
| iPhone / Expo Mobile | Runtime evidence supplied; qualification pending | Four screenshots |

CP-03 is not yet a fully qualifying third platform because the exact device model, iOS version, Expo version, SUT location, and required identity overlay have not been supplied. No emulator image is represented as physical-device evidence.

## 4. Agent Skill and AI documentation

The reusable skill under `agent_skills/gui-usability-tester/` contains operating modes, evidence-state controls, traceable output schemas, severity guidance, quality gates, a validator, and unit tests. Its normalized submission mirror is distinct from the installed development copy under the repository-root `.agents` directory. The demonstration video remains an external pending artifact.

The AI Audit Report preserves the history of AI-assisted work, including the correction of the earlier FR-23 scope interpretation. The AI Critique remains within the required 200–300 words and explains why plausible source analysis cannot replace runtime evidence.

## 5. Limitations and final external actions

1. Mobile captures still require the PDF-prescribed identity overlay and exact device/iOS/Expo/SUT metadata for complete CP-03 qualification.
2. The shared usability Drive folder must be tested in a signed-out browser.
3. GitHub Issue #118 requires correction of its student-ID title prefix.
4. The Agent Skill demonstration video must be recorded, uploaded, and access-tested.
5. `git_commit_log.txt` and the submission ZIP must be regenerated after the final commit.

The final ZIP must contain only the contents of `docs/assignments/HW03/deliverables`. Specifications, workbench files, source CSV data, archives, caches, previous ZIP files, and the root `.agents` installation are excluded.

## Conclusion

The submission provides 45 classified GUI checks, 20 evidenced failures, 19 normalized runtime defects, ten desktop cross-browser captures, four Mobile FR-23 captures, and a structured seven-participant usability dataset with a mean SUS score of 73.6. The results and scope are internally aligned across the checklist, defect report, usability workbook, and this report.

The remaining work is limited to external evidence-compliance steps: Mobile overlay/environment completion, signed-out Drive access confirmation, one GitHub Issue title correction, and the Agent Skill demonstration video. The report contact address remains `23127404@student.hcmus.edu.vn`; the screenshot identity overlay remains `23127404@hcmus.edu.vn` as prescribed by the assignment PDF.
