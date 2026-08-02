# HW03 Report — GUI and Usability Testing

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc (23127404) |
| Email | 23127404@hcmus.edu.vn |
| System under test | EShop |
| Final automated execution | 2 August 2026 |
| Primary runtime environment | Google Chrome 151.0.7922.72 on Windows NT 10.0.26200 |

## Executive summary

The EShop GUI checklist contains 45 non-duplicate checks across IA-01 to IA-04. Thirty-one Web, Admin, and API-supported checks were executed twice in Google Chrome against freshly seeded data; 16 passed and 15 failed. Fourteen checks requiring the Mobile app remain `Not Executed`. The 15 failures map one-to-one to verified defect records and authentic screenshots. The most serious findings concern a client-editable checkout total, stored HTML execution in Admin, and incorrect percentage-coupon arithmetic.

The selected Chrome flow was also captured across five screens for cross-platform evidence. Firefox was attempted with a compatible downloaded browser but failed during page creation and direct CLI capture; it is reported as blocked. A qualifying mobile environment and all real-participant usability sessions remain pending.

## 1. GUI checklist and defect reporting

### 1.1 Scope and coverage

The checklist covers Product Detail, Cart, Checkout, Profile/Order History, Admin Dashboard, Admin Orders, Admin Products, order-state APIs, and selected Mobile behaviors. The Mobile pool has no FR number in the assignment specification; it is identified as Pool D rather than the previously assumed `FR-23`.

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
| Executed | 31 |
| Passed | 16 |
| Failed | 15 |
| Not executed | 14 |
| Verified defects | 15 |

The Mobile-only checks remain `Not Executed` because Playwright viewport emulation is not equivalent to Expo Go, a real phone, or an approved cloud device. Four source-derived Mobile candidates are retained as unverified hypotheses and excluded from the defect count.

### 1.4 Defect analysis

| Severity | Count | Representative risk |
|---|---:|---|
| Critical | 3 | Editable authoritative total; stored HTML execution; incorrect percentage coupon |
| Major | 9 | Broken first-click action, invalid order transitions, wrong revenue, missing order details |
| Minor | 3 | Silent decimal truncation and missing progress/success feedback |

Detailed reproduction steps and evidence are in `bugs/bug_report.md`. GitHub Issue URLs and Issue-page screenshots are intentionally pending until the student creates the real issues.

## 2. Moderated usability evaluation

### 2.1 Objective and scenario

The study is designed to determine whether typical online shoppers can independently select a product, review the cart, complete checkout, and confirm the resulting order status. Measures include completion, time on task, errors, hesitations, moderator intervention, SUS, and qualitative responses concerning clarity, recovery, speed, and trust.

The participant-facing scenario in `usability/task_scenario.md` states a realistic goal and does not prescribe interface steps. One pilot must precede seven official sessions.

### 2.2 Prepared instruments

- Moderator guide and neutral-intervention rules.
- Pilot and P1–P7 structured observation files.
- Standard ten-item SUS response forms and scoring spreadsheet.
- Four required probe areas: clarity, error recovery, speed, and trust.
- Participant register with masked-contact guidance.
- Severity-ranked synthesis structure and recordings index.

### 2.3 Evidence status

| Evidence | Status |
|---|---|
| Pilot participant/session | Not collected |
| Seven eligible participants | 0 of 7 verified |
| Consent and recordings | Not collected |
| SUS responses and scores | Not collected |
| Observation notes | Templates prepared; no observations claimed |
| Severity-ranked findings | Awaiting genuine session data |

No Playwright agent is treated as a participant. No name, quotation, rating, task duration, or contact detail has been invented.

### 2.4 SUS scoring method

For odd-numbered items, subtract one from the response. For even-numbered items, subtract the response from five. Sum the ten contributions and multiply by 2.5. The result is a 0–100 usability benchmark, not a percentage grade. Scores remain uncalculated until authentic responses exist.

## 3. Cross-browser and cross-platform verification

### 3.1 Google Chrome

Google Chrome 151.0.7922.72 completed the Product List → Product Detail → Cart → Checkout → Order History flow. Five genuine screenshots are stored under `cross_platform/chrome_desktop/`. Each contains a compact caption with `23127404@hcmus.edu.vn`, browser, Windows, and URL.

### 3.2 Firefox

Firefox 144.0.2 launched, but Playwright failed while creating the first page with `browserContext.newPage`. A direct headless CLI screenshot attempt also stalled and was terminated. Firefox is therefore `Blocked`, not passed, failed, or completed.

### 3.3 Mobile

No physical phone or approved cloud environment was available. Mobile remains `Not Executed`; no emulated screenshot is submitted as a substitute.

| Environment | Status | Evidence |
|---|---|---|
| Google Chrome Desktop | Executed | Five screenshots |
| Firefox Desktop | Blocked by environment | Diagnostic status only |
| Physical/approved cloud mobile | Not executed | None |

The requirement of three qualifying platforms is not yet satisfied.

## 4. Agent Skill and AI documentation

The reusable skill is supplied under `agent_skills/gui-usability-tester/`. It separates checklist design, runtime evidence, usability safeguards, and final reconciliation. The demonstration URL is pending a real recording and upload.

The AI Audit Report documents AI-assisted activities and human review. The AI Critique remains within the required 200–300 words and emphasizes that plausible static analysis is not execution evidence.

## 5. Limitations and remaining work

- Fourteen Mobile checklist items were not executed.
- Firefox and the third qualifying platform remain incomplete.
- The pilot and seven official usability sessions remain incomplete.
- GitHub Issues and their screenshots remain incomplete.
- The Agent Skill demonstration video remains incomplete.
- Historical AI prompts without verifiable source timestamps are not reconstructed.

## Conclusion

The completed portion provides a traceable and repeatable desktop execution: 45 designed checks, 31 executed checks, 15 reproducible failures, 15 verified defect records, and five Chrome cross-platform captures. The remaining evidence is clearly isolated and can be added without rewriting the completed results. The current evidence supports a conservative self-assessment of 45/100, not a 090 submission claim.
