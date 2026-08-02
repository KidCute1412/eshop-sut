# Task 1 — Test Execution Summary

**SUT:** EShop (eshop-clone) — **frontend-web only** (Admin panel and mobile app are out of scope for Task 1, to keep every failing item reproducible and screenshot-able by one person without extra accounts/devices; Admin/mobile remain in scope for Task 3's cross-platform testing where relevant).
**Screens/flows in scope:** Home (product listing/search), Login, Register, Forgot Password (2-step), Profile (+ order history), Product Detail, Cart, Checkout (+ coupon).
**Execution method:** Manual, exploratory execution on the running app — clicking through each screen, filling forms with both valid and deliberately edge-case inputs, and cross-checking on-screen values (OTP length, checkout total, cart contents) against what the app itself displayed elsewhere or against `api_specification.md`. Reviewing the source beforehand (a white-box step) was used only to decide *where* to look and *which* edge-case inputs to try — every finding is stated as an observed behavior, not a source-code citation.

## Numbers

| Metric | Count |
|---|---|
| Screens/flows covered | 8 (all frontend-web) |
| Checklist items designed | 42 |
| — AI-generated (baseline) items | 39 |
| — Human-added items (with rationale for what a generic AI pass would miss) | 3 |
| Items executed | 42 / 42 |
| Passed | 32 |
| Failed | 10 |
| Distinct bugs logged | 10 (BUG-01, BUG-11, BUG-13, BUG-14, BUG-15, BUG-19, BUG-24, BUG-25, BUG-34, BUG-37) |

## Coverage by Interface Aspect (IA)

| IA | Aspect | Items | Failed |
|---|---|---|---|
| IA-01 | General UI standards | 10 | 1 |
| IA-02 | Forms | 12 | 5 |
| IA-03 | Navigation | 7 | 1 |
| IA-04 | Feedback / state | 13 | 3 |

## Severity breakdown of the 10 failed items

| Severity | Count | Bug IDs |
|---|---|---|
| Critical (security) | 2 | BUG-11 (plaintext password field), BUG-19 (reflected XSS via search) |
| Major (misleads/blocks task completion) | 5 | BUG-13, BUG-14, BUG-15, BUG-24, BUG-25 |
| Minor (cosmetic / consistency) | 3 | BUG-01, BUG-34, BUG-37 |

Every failed item is reproducible on **frontend-web alone**, most in 1 screenshot and none needing more than 2 — see `02_bug_reports/Bug_Report.md` for exact repro steps and the GitHub Issues cross-reference.
