# AI Gap Analysis - FR-01 Account Registration

## Human-Reviewed Fixes

| Area | AI / first-pass issue | Human correction | Why AI missed it |
| --- | --- | --- | --- |
| Network wait | The duplicate-email test initially waited for any `/api/register` response and captured a 200 response instead of the real POST outcome. | The wait was restricted to `r.request().method() === "POST"`. | The first pass treated URL matching as enough and did not account for browser/network noise. |
| Duplicate email expectation | The test expected duplicate registration to reject, but the real SUT accepted the duplicate and redirected successfully. | Kept the assertion failing and recorded `BUG-HW04-FR01-001` instead of weakening the test. | AI tends to make tests pass by adapting to actual behavior, but the oracle must come from requirements, not from the implementation's bug. |
| Password oracle | A documented special-character password such as `Aa1!aaaa` failed in the UI, but the earlier automation incorrectly marked it as expected `password_error`. | The oracle was corrected to requirement-based `success`, and additional `@` plus 20-character password cases were added. | The model overfit to current behavior instead of using `README.md` as the oracle for expected behavior. |
| Selector strategy | The first-pass selector idea used labels/accessible names, but the form labels are not associated with inputs. | The final spec scopes to the form and indexes the three input fields while keeping assertions on URL/API/error visibility. | The app has no `id`/`data-testid` and no `for`/`id` label binding, so ideal role/label locators are unavailable. |

## Review Result

- Approved: Yes, with one real SUT failure retained.
- Remaining failures: `FR01-DT-006`, `FR01-DT-011`, `FR01-BVA-009`, and `FR01-BVA-010` on Chromium, Firefox, and WebKit. `FR01-BVA-011` confirms that a 20-character password with whitespace can pass, so the password bug is the incorrect special-character regex rather than a general maximum-length defect.
