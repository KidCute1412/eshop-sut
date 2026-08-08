# AI Gap Analysis - FR-07 Shopping Cart

## Human-Reviewed Fixes

| Area | AI / first-pass issue | Human correction | Why AI missed it |
| --- | --- | --- | --- |
| SPA state preservation | The first pass used `page.goto("/cart")` after clicking Add to Cart. That reloads the React app and loses cart context, causing false empty-cart failures. | Navigation was changed to click the header cart link (`a[href='/cart']`) so the SPA context is preserved. | The model reasoned in URL/page terms and missed that this SUT stores cart state only in React memory, not local storage or backend persistence. |
| Strict selectors | `a[href='/']` matched both the EShop logo and the Continue Shopping link. | The final test scopes the locator to `main a[href='/']`. | The first pass did not run in strict mode and did not account for duplicate anchors. |
| Duplicate-product oracle | The first FR-07 automation treated adding the same product twice as `2` cart rows because that matched the current implementation. | `FR07-DT-004` was corrected to require `1` row with quantity `2`, matching the HW02/FR07 requirement oracle. | The model overfit to observed implementation behavior instead of preserving the reviewed requirement expectation. |
| Delete confirmation | The first pass clicked `Xóa` and immediately asserted the final row count. | `FR07-DT-005` and `FR07-DT-006` now wait for a confirmation dialog and accept it before checking cart state. | The model tested the end state only and missed the required intermediate confirmation step. |
| Header precision | `FR07-DT-010` only asserted that five table headers existed. | The test now compares the exact required header sequence: `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, `Thao tác`. | The model used a weak count assertion and did not verify the requirement-specific labels. |
| Total-label precision | `FR07-DT-011` only checked that the total amount area was visible. | The test now requires the label `Tổng cộng` and rejects the current `Tổng tạm tính` label. | Visibility alone could not catch copy that violates the documented oracle. |
| Quantity controls | The first pass kept only `FR07-BVA-001` for quantity display `1` and documented cart quantity editing as not automated. | `FR07-BVA-001` was kept, and `FR07-BVA-002`/`FR07-BVA-003` were added for the `+` and `-` quantity controls. | The model accepted the current page limitation instead of adding requirement-based failing automation for missing controls. |
| Assertion strength | A simple "cart page loaded" assertion would not catch row/quantity/total regressions. | Added count, URL, text, visibility, dialog, and exact-array assertions across the suite. | AI-generated UI tests often stop at navigation checks unless explicitly pushed toward assertion diversity. |

## Review Result

- Approved: Yes.
- Latest FR-07 multi-browser run: 42 browser executions, 21 passed, 21 failed.
- Failing cases on Chromium, Firefox, and WebKit: `FR07-DT-004`, `FR07-DT-005`, `FR07-DT-006`, `FR07-DT-010`, `FR07-DT-011`, `FR07-BVA-002`, and `FR07-BVA-003`.
