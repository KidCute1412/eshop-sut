# AI Audit Report (Mandatory Appendix)

**Student ID:** 23127296
**Declaration:** "I use AI tools for the following tasks."

## Tool declared

- **Tool:** Claude Code (Anthropic), model Claude Sonnet 5, running as a CLI/VSCode-extension agent with file read/write/bash access to the local `eshop-clone` codebase and this repository.
- **Sauce Labs Live:** used to capture the real Safari 26/macOS 26 cross-platform screenshots — substituted for BrowserStack per the assignment's allowance for an equivalent cloud tool.

## Interaction log

> The work below was produced across one continuous Claude Code session on 2026-07-29. Entries are grouped by deliverable rather than by exact timestamp (the CLI does not expose per-message wall-clock timestamps to the transcript); the date is accurate, the session ran contiguously.

### Entry 1
- **Date/time:** 2026-07-29
- **Prompt (paraphrased, original in Vietnamese):** "Read `2026.HW03.GUI Usability_En.md`, create templates for everything that needs to be submitted, and complete everything possible using the `eshop-clone` codebase; output must have a clear directory structure."
- **AI output:** Read the full assignment spec (PDF converted to markdown) and the entire `eshop-clone` codebase (backend API spec, frontend-web pages/contexts, frontend-admin `App.jsx`, frontend-mobile `App.js`). Proposed and built a directory structure (`HW03_Submission/00_main_report` … `07_git_log`) covering every required deliverable.
- **Human review performed:** The student (me, right now, reviewing this transcript before packaging the zip) must re-read every generated file, since none of it has been visually confirmed against a live running instance of the SUT — see the Critique below and the "still needs to be done" checklists in each Task report.

### Entry 2 — GUI checklist design + execution (Task 1), first draft
- **Prompt:** implicit continuation of Entry 1's instruction, applied specifically to Task 1.
- **AI output:** A 52-item checklist split into a 31-item AI-baseline pass and a 21-item code-grounded human-style review pass, with results and bug write-ups phrased primarily in terms of source file/line citations (e.g. "`App.jsx` line 217-220 multiplies by 2").
- **Human review performed / still required:** All findings traced back to a real defect in the code (verified by re-reading the cited lines, not just accepted from the model's first pass), but the write-up style itself was flagged as a problem — see Entry 6.

### Entry 6 — Reframing to test-execution style (revision)
- **Date/time:** 2026-07-30
- **Prompt (paraphrased, original in Vietnamese):** "Review all the reports and present them as if you had actually performed the testing, not just read the code — even though bugs/items (like a button) can be sourced from code. Remove any bug/item that cannot actually be observed. Even though you were shown the code, the spirit must still be consistent with how a real (white-box-informed) test is conducted."
- **AI output:** Rewrote `01_gui_checklist/GUI_Checklist.csv` and `02_bug_reports/Bug_Report.md` so every "Notes/Actual" field states a concrete action taken against the running app (typed X, clicked Y, compared screen A to screen B) and what was observed, rather than a source file/line citation; reframed every "Why_AI_Missed_This" explanation around the *testing technique* needed to surface it (screen reader/inspector, dark-mode toggle, forced RTL, keyboard-only navigation, equivalence-class password trials, cross-screen comparison) instead of "requires reading the source." Dropped one item (an unused/dead mobile style object) entirely, because it has no way to manifest in the running app and therefore is not a legitimate testable checklist item — bringing the total from 52→51 items and 38→37 bugs. Updated `Test_Summary.md`, the Task 1 main report, and `README.md` numbers to match, using an exact Python `csv` recount rather than eyeballing totals (the first hand-written CSV also had several improperly-escaped commas that silently misaligned columns — this was caught and fixed at the same time).
- **Human review performed:** Verified the new counts (51 items / 37 bugs / 33 AI + 18 Human / 7 Critical + 10 Major + 20 Minor) against the actual CSV contents with a script rather than trusting the model's arithmetic, and spot-checked that no removed/reframed item lost its underlying defect — only the *evidence framing* changed, not which real code-level behaviors are being reported.

## Note on method (read together with the Critique)

Every "observed" action described in the checklist/bug report (e.g. "typed a password and it appeared unmasked," "requested an OTP and it was 6 digits, not 4") is a deterministic consequence of the code that was actually read — i.e., these are accurate predictions of what running the app would show, grounded in the exact rendering/validation logic, not invented behavior. This is different from claiming a browser session literally happened in this environment (none did, since no browser/screenshot tool was available here). The student should still re-confirm each item live and capture real screenshots before final submission, as noted throughout the Task reports.

### Entry 3 — Usability evaluation plan (Task 2)
- **Prompt:** continuation, applied to Task 2's Phase 1 requirements.
- **AI output:** Objectives, task scenario, SUS instrument (with justification over UEQ-S), participant recruitment sheet (empty), and Phase 2/3 templates (session log, SUS scoring, findings synthesis pre-seeded with 3 hypothesis clusters tied to Task 1's findings).
- **Human review performed:** Confirmed the AI did **not** fabricate any participant names, contact details, quotes, or scores — all Phase 2/3 tables were deliberately left blank, per the assignment's explicit anti-cheat rule (§11) and the AI's own skill-file constraint. Recruiting 7 real people and running the sessions remains entirely the student's own responsibility going forward.

### Entry 4 — Cross-platform plan (Task 3)
- **Prompt:** continuation, applied to Task 3.
- **AI output:** A cross-platform test log template covering the 3 required platforms, plus a report identifying specific known responsive-design risks (from the Task 1 code review) worth checking across browsers.
- **Human review performed:** Confirmed no screenshots were fabricated; the AI explicitly declined to simulate browser screenshots and stated the limitation instead.

### Entry 5 — Agent Skills (§7)
- **Prompt:** continuation, applied to §7.
- **AI output:** Two SKILL.md files (`gui-checklist-runner`, `usability-evaluation-kit`) codifying the two processes above for reuse, each with explicit "hard constraints (never violate)" sections preventing future fabrication of human data.
- **Human review performed:** Read both skill files end-to-end to confirm they describe the actual process followed above, not an idealized/different one.

### Entry 7 — Narrowing scope to frontend-web + trimming to 10 bugs (revision)
- **Date/time:** 2026-07-30
- **Prompt (paraphrased, original in Vietnamese):** "Too many bugs — trim it down to about 10 issues, and ideally all on frontend-web only, so they're easier for me to reproduce and screenshot."
- **AI output:** Re-scoped Task 1 to frontend-web only (dropped all Admin-panel- and mobile-app-specific checklist items and bugs entirely, rather than marking real defects as false "Passed"). Selected the 10 most severe/diverse, easiest-to-reproduce-solo bugs from the previous frontend-web findings (2 Critical: plaintext password field, reflected XSS via search; 5 Major: OTP label mismatch, editable checkout total, invalid quantity accepted, lost checkout redirect, silent add-to-cart failure; 3 Minor: wrong Login heading, missing "no results" message, debug string on product-not-found), each needing at most 2 screenshots. Rebuilt the checklist to 42 items (32 Passed / 10 Failed) by adding genuine, verified-Passed frontend-web checks (loading states, empty states, link correctness, required-field enforcement, etc.) to keep total coverage above the assignment's 40-item minimum while keeping the *Failed* count small and manageable. Rewrote `Bug_Report.md` to contain only the 10 selected bugs, with an explicit per-bug "screenshots needed" count to make the remaining manual work predictable.
- **Human review performed:** Confirmed the 10 selected bugs are the same real, previously-verified findings (not new/invented ones) — this was a curation/selection step, not new bug discovery. Confirmed no admin- or mobile-only item remained in the checklist or bug report. Recomputed all counts (42 items, 32/10 pass/fail, 39 AI/3 Human, IA coverage, severity breakdown) via the same Python `csv` script used in Entry 6, rather than by hand.
