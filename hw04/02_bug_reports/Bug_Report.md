# Bug Report — HW04 Automation (FR-03, FR-09, FR-13)

All bugs below were found by **failing assertions** in the Playwright suite (`tests/fr03-forgot-password.spec.js`, `tests/fr09-coupon.spec.js`, `tests/fr13-dashboard.spec.js`) that assert the behavior documented in `README.md`, run identically across Chromium, Firefox, and WebKit (same 8 failures in all three runs — see `../03_html_reports/`). Screenshots are in `screenshots/`.

New GitHub Issues were filed for HW04 per the assignment's requirement even where a bug had already been reported in an earlier homework (HW02 manual test design), so each entry below also references the earlier issue for traceability.

| Bug ID | Feature | Title | Severity | Test | HW04 GitHub Issue | Earlier Issue (HW02) |
|---|---|---|---|---|---|---|
| BUG-FR09-001 | FR-09 | Coupon rejected when `total_amount` exactly equals `min_order_amount` (`>` used instead of `>=`) | High | `FR09-TC02` | [#135](https://github.com/KidCute1412/eshop-sut/issues/135) | [#29](https://github.com/KidCute1412/eshop-sut/issues/29) |
| BUG-FR09-002 | FR-09 | Percent coupon formula wrong — produces a huge/negative discount instead of a percentage | High | `FR09-TC01` | [#136](https://github.com/KidCute1412/eshop-sut/issues/136) | [#30](https://github.com/KidCute1412/eshop-sut/issues/30) |
| BUG-FR09-003 | FR-09 | `apply-coupon` succeeds without a logged-in user (spec condition C4 not enforced) | High | `FR09-TC08` | [#137](https://github.com/KidCute1412/eshop-sut/issues/137) | [#31](https://github.com/KidCute1412/eshop-sut/issues/31) |
| BUG-FR09-006 | FR-08/FR-09 | Checkout does not clear the cart after a successful order | Medium | `FR09-TC13` | [#138](https://github.com/KidCute1412/eshop-sut/issues/138) | — (new, found during HW04 automation) |
| BUG-FR13-001 | FR-13 | Admin dashboard revenue is exactly double the correct value (`total_amount * 2`) | High | `FR13-TC01`/`TC02` | [#139](https://github.com/KidCute1412/eshop-sut/issues/139) | [#34](https://github.com/KidCute1412/eshop-sut/issues/34) |
| BUG-FR13-002 | FR-12/FR-13 | `/api/admin/orders` and `/api/admin/users` accept any valid JWT, not just `role='admin'` | High | `FR13-TC03`, `FR13-TC05` | [#140](https://github.com/KidCute1412/eshop-sut/issues/140) | [#35](https://github.com/KidCute1412/eshop-sut/issues/35) |

## Not filed as a GitHub issue

- **BUG-FR09-007** (checkout trusts a client-supplied `total_amount` instead of recomputing it server-side — spec FR-08) was found by *reading* `backend/server.js` while writing the E2E test, not by a failing automated assertion. Documented in `../00_report/Review_And_GapAnalysis.md` §2 for the record, but not filed as a formal bug here since HW04's "wherever a failing assertion reveals a genuine defect" criterion is about automation-detected defects specifically.

## Bugs known from HW02/HW03 but out of scope for HW04

- FR-03 bugs (weak-password regex accepting/rejecting the wrong things, 4-digit vs 6-digit OTP, missing confirm-password field) are exercised by the FR-03 spec (`tests/fr03-forgot-password.spec.js`) and documented in the test case design (`../01_test_design/FR03_ForgotPassword_TestCases.md`), but were **not** re-filed as new issues in this pass because the automated assertions for those specific defects are informational (`FR03-TC12`, `FR03-TC14`/`TC14b`) rather than hard failures that block a `test()` — see the spec file for how each is verified. If you want these re-filed alongside #25–#28 as separate HW04 issues too, that's a quick follow-up; flag it and it can be done the same way as the six above.
