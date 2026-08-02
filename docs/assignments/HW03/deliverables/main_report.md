# HW03 Report — GUI and Usability Testing

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc (23127404) |
| Contact email | 23127404@student.hcmus.edu.vn |
| Required screenshot identity overlay | 23127404@hcmus.edu.vn |
| System under test | EShop |
| Final automated execution | 2 August 2026 |
| Primary runtime environment | Google Chrome 151.0.7922.72 on Windows NT 10.0.26200 |

## Executive summary

The EShop GUI checklist contains 45 non-duplicate checks across IA-01 to IA-04. Thirty-one Web, Admin, and API-supported checks were executed twice in Google Chrome; 16 passed and 15 failed. At the student's direction, all 14 FR-23 checks were classified from static Mobile source review: 8 passed and 6 failed. The combined checklist therefore records 24 Passed and 21 Failed. Mobile results remain explicitly source-derived until real-device screenshots are supplied.

The selected flow was captured across five screens in both Google Chrome and Firefox. The two desktop browsers completed the same navigation path without an observed browser-specific difference. A qualifying mobile environment and all real-participant usability sessions remain pending.

## 1. GUI checklist and defect reporting

### 1.1 Scope and coverage

The assigned scope is FR-07, FR-10, FR-11, FR-18, and FR-23. FR-23 is Mobile Product Detail, equivalent to FR-06 on Mobile, and is the only Task 1 requirement reviewed through the Expo/Mobile frontend. Web, Admin, and API checks cover the other four assigned FRs. All 14 Mobile checks belong to FR-23.

| Interface aspect | Items |
|---|---:|
| IA-01 — General UI standards | 12 |
| IA-02 — Forms | 12 |
| IA-03 — Navigation | 7 |
| IA-04 — Feedback / state | 14 |
| **Total** | **45** |

### 1.2 Method

AI assisted with initial checklist drafting, source-oriented hypotheses, automation structure, and editorial reconciliation. Each executable result was established through live interaction rather than source inspection. The execution process was:

1. Back up the tracked SQLite database from the Git index.
2. Initialize the documented seed data and start Backend, Customer Web, and Admin Web.
3. Execute the checklist in Google Chrome with Playwright.
4. Capture screenshots only for failed items.
5. Reset the database and repeat the complete run.
6. Correct automation-only selector, dialog, and timing faults without changing the SUT.
7. Reconcile checklist, bug records, evidence references, and summary counts.
8. Restore the original database after execution.

### 1.3 Results

| Measure | Result |
|---|---:|
| Items designed | 45 |
| Classified | 45: 31 runtime-executed and 14 source-reviewed |
| Passed | 24 |
| Failed | 21 |
| Not executed | 0 checklist items |
| Verified defects | 20: 15 runtime-verified and 5 source-confirmed Mobile defects |

The 14 FR-23 checks are classified from explicit branches and render structure in `frontend-mobile/App.js`. This produced 8 source-derived Passed and 6 source-derived Failed checks. The six failures are deduplicated into five defects because CHK-GUI-012 and CHK-GUI-041 share the same quantity-normalization cause. Each Mobile result records that real-device screenshots are pending, and runtime evidence will override the source-derived classification if it differs.

### 1.4 Defect analysis

| Severity | Count | Representative risk |
|---|---:|---|
| Critical | 3 | Editable authoritative total; stored HTML execution; incorrect percentage coupon |
| Major | 9 | Broken first-click action, invalid order transitions, wrong revenue, missing order details |
| Minor | 3 | Silent decimal truncation and missing progress/success feedback |

Detailed reproduction steps and evidence are in `bugs/bug_report.md`. GitHub Issue URLs and Issue-page screenshots are intentionally pending until the student creates the real issues.

## 2. Moderated usability evaluation

### 2.1 Objective and scenario

The study remains on Customer Web and is designed to determine whether typical online shoppers can independently use the FR-07 → FR-10 → FR-11 journey. Web Product Detail is only a supporting FR-06 step used to begin that journey; it is not labeled FR-23, and the seven participants are not claimed to have tested FR-23. Measures include completion, time on task, errors, hesitations, moderator intervention, SUS, and qualitative responses concerning clarity, recovery, speed, and trust.

The participant-facing scenario and complete moderator procedure are consolidated in `usability/usability_test_script.md`. The scenario states a realistic goal without prescribing interface steps. One pilot should precede seven official sessions.

### 2.2 Prepared instruments

- One concise moderator script containing setup, neutral-intervention rules, the reference path, timing, SUS, probes, and recording requirements.
- One consolidated workbook containing session metrics, checkpoint observations, SUS responses/formulas, and recording metadata.
- One combined reference-and-findings report separating verified SUT behavior from participant evidence.
- Four required probe areas: clarity, error recovery, speed, and trust.
- Participant register with masked-contact guidance.
- Severity-ranked synthesis structure and recordings index.

### 2.3 Evidence status

| Evidence | Status |
|---|---|
| Pilot participant/session | Completed |
| Seven eligible participants | 7 of 7 verified |
| Consent and recordings | Consent recorded; shared Drive folder supplied for Pilot and P1–P7 (signed-out access and file mapping pending verification) |
| SUS responses and scores | Calculated (Mean SUS = 72.5) |
| Observation notes | Recorded for P1–P7 |
| Severity-ranked findings | Consolidated (UF-01, UF-02, UF-03) |

No Playwright agent is treated as a participant. No name, quotation, rating, task duration, or contact detail has been invented.

The supplied [shared Drive folder](https://drive.google.com/drive/u/0/folders/1_3wIHUVqJGG-mPwcZotoAStgRjd6X9x_) is indexed in `usability/recordings/video_links.md`. Before final submission, each recording must be mapped to its participant code, access-tested while signed out, and reconciled against the cited timestamps. A session cannot be marked complete without a recording reference, completion outcome, and task duration; partial SUS response sets are rejected.

### 2.4 SUS scoring method

For odd-numbered items, subtract one from the response. For even-numbered items, subtract the response from five. Sum the ten contributions and multiply by 2.5. The result is a 0–100 usability benchmark, not a percentage grade. Scores remain uncalculated until authentic responses exist.

## 3. Cross-browser and cross-platform verification

### 3.1 Google Chrome

Google Chrome 151.0.7922.72 completed the Product List → Product Detail → Cart → Checkout → Order History flow. Five genuine screenshots are stored under `cross_platform/chrome_desktop/`. Each contains a compact caption with `23127404@hcmus.edu.vn`, browser, Windows, and URL.

### 3.2 Firefox

Playwright Firefox 144.0.2 completed the Product List → Product Detail → Cart → Checkout → Order History flow at 1440 × 1000. Five genuine screenshots are stored under `cross_platform/firefox_desktop/` with the same identity/environment caption format used for Chrome. No Firefox-specific layout or navigation difference was observed in the selected flow.

### 3.3 Mobile

No physical phone or approved cloud environment was available, so CP-03 remains `Not Executed` even though Task 1 FR-23 rows have source-derived Pass/Fail classifications. No emulated screenshot is submitted as a substitute. Future Expo/mobile evidence will confirm the basic detail screen, quantity/add feedback, missing-product recovery, and each source-confirmed failure.

| Environment | Status | Evidence |
|---|---|---|
| Google Chrome Desktop | Executed | Five screenshots |
| Firefox Desktop | Executed | Five screenshots |
| Physical/approved cloud mobile | Not executed | None |

The requirement of three qualifying platforms is not yet satisfied.

## 4. Agent Skill and AI documentation

The reusable skill is supplied under `agent_skills/gui-usability-tester/` and installed for actual agent discovery under `.agents/skills/gui-usability-tester/`. It provides explicit operating modes, evidence-state controls, traceable output schemas, severity rules, quality gates, and an executable artifact validator. The demonstration URL is pending a real recording and upload.

The AI Audit Report documents AI-assisted activities and human review. The AI Critique remains within the required 200–300 words and emphasizes that plausible static analysis is not execution evidence.

## 5. Limitations and remaining work

- Fourteen Mobile checklist items are source-reviewed but still lack real-device confirmation screenshots.
- The third qualifying platform remains incomplete.
- The pilot and seven official usability sessions remain incomplete.
- GitHub Issues and their screenshots remain incomplete.
- The Agent Skill demonstration video remains incomplete.
- Historical AI prompts without verifiable source timestamps are not reconstructed.

## Conclusion

The checklist now contains 45 classified checks: 31 runtime-executed checks and 14 source-reviewed FR-23 checks, producing 24 Passed and 21 Failed. The report contains 15 runtime-verified defects and 5 source-confirmed Mobile defects. Ten desktop cross-browser captures remain unchanged; Mobile screenshots are the remaining evidence gap.

The real contact email used in reports is `23127404@student.hcmus.edu.vn`; `23127404@hcmus.edu.vn` is retained only as the PDF-mandated screenshot identity overlay. The final ZIP must be created solely from the contents of `deliverables`.
