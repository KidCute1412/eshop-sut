# Task 1 — GUI Checklist: Design, Execution, and Bug Report

**Student ID:** 23127296
**SUT:** EShop (`eshop-clone`) — frontend-web, frontend-admin, frontend-mobile, backed by `backend/server.js` per `api_specification.md`.
**Scope selected (§5):** Multiple screens across all four SUT modules — Home/Search, Login, Register, Forgot Password, Profile + Order History, Product Detail, Cart, Checkout+Coupon (Pool A/B), the full Admin panel — Dashboard, Categories, Products+CSV import, Coupons, Orders, Users (Pool C), and the mobile app's equivalent screens (Pool D). A single screen was judged too shallow to reach 40 non-repetitive items, per the assignment's own guidance, so coverage was deliberately broadened.

## 1. Process

### Step 1 — AI-generated baseline (31 items)
An initial checklist pass was produced by prompting the AI with the four required interface aspects (IA-01 General UI, IA-02 Forms, IA-03 Navigation, IA-04 Feedback/state) and the list of in-scope screens, asking it to generate concrete, screen-specific checklist items rather than one generic "find usability problems" prompt. This produced 31 items covering standard heuristics: visual consistency, color semantics, hover/focus states, breadcrumbs, empty-state handling, confirmation dialogs, field hints, etc. — see rows marked `Origin=AI` in `01_gui_checklist/GUI_Checklist.csv`.

### Step 2 — Critical human review (21 added items)
The AI-generated set was then reviewed against the actual source code (`frontend-web/src`, `frontend-admin/src`, `frontend-mobile/App.js`) and the API contract (`api_specification.md`). This surfaced 21 additional items the baseline pass missed, each annotated in the CSV's `Why_AI_Missed_This` column. The pattern across all 21: **the AI baseline pass reasons about UI *shape and standard heuristics*, not about the specific runtime behavior of this codebase.** Concretely, the misses fall into three buckets:

1. **Accessibility / dark mode / RTL** (BUG-04 through BUG-10) — exactly the categories the assignment calls out as typically overlooked. These require either rendering the app under specific conditions (dark OS theme, RTL locale) or inspecting concrete attribute values (`alt=""`, missing `tabIndex`/`role`) — a prompt that only asks "generate a GUI checklist" has no signal to go looking for them unless told to per-category.
2. **Semantic/data mismatches between UI copy and actual logic** (BUG-12, BUG-13, BUG-27, BUG-28, BUG-29) — e.g., the password-strength *message* claims a special character is required, but the regex actually checks for whitespace; the OTP field says "4 digits" but the backend issues 6. These are invisible to a black-box visual review; they only appear by diffing what the code *says* against what it *does*, or against the API spec.
3. **State/security bugs buried in event handlers** (BUG-16, BUG-19–21, BUG-25, BUG-26) — `dangerouslySetInnerHTML` usage, an add-to-cart handler that no-ops on the first click, a mass-update side effect in local state — all require tracing a specific function body, which is qualitatively different from "does this screen look/feel right."

This is consistent with what the assignment expects: the AI is a fast generator of standard-heuristic coverage, but the *code-grounded* review is what a human (or an AI explicitly directed to read source) contributes on top.

### Step 3 — Execution
All 52 items were executed against the SUT by reading the corresponding component's logic (and, for the Admin dashboard/order state-machine bugs, tracing the actual reducer/handler code) and cross-checking against `api_specification.md` where relevant. Results, Pass/Fail, and per-failure notes are recorded in `01_gui_checklist/GUI_Checklist.csv`. **Important limitation:** this execution pass was performed by static code review, not by clicking through a running browser session (no browser/screenshot tool was available in this environment) — see `../06_ai_audit/AI_Critique.md`. Before final submission, each Failed item should be re-confirmed live and a real screenshot captured, per `../02_bug_reports/HOWTO_create_github_issues.md`.

### Step 4 — Bug logging
All 38 failed items were written up as GitHub-issue-ready bug reports in `../02_bug_reports/Bug_Report.md`, with severity, repro steps, expected/actual, and a fix suggestion each. Screenshots and the actual GitHub Issues must still be created by the student against a live instance (instructions provided).

## 2. Results

See `01_gui_checklist/Test_Summary.md` for the full numeric breakdown:

- 52 items designed, 52 executed, **14 Passed / 38 Failed**.
- Failures span all four IA categories, with the highest concentration in IA-04 (Feedback/state, 14/17 failed) and IA-02 (Forms, 10/13 failed).
- 7 of the 38 failures are security/data-integrity **Critical** issues (2 stored XSS, 1 reflected XSS, 1 plaintext password field, revenue-doubling bug, order-state-machine bypass, dropped cart item on checkout) — these should be prioritized above the cosmetic/consistency failures.
