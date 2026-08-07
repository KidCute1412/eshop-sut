# AI Gap Analysis - FR-07 Shopping Cart

## Human-Reviewed Fixes

| Area | AI / first-pass issue | Human correction | Why AI missed it |
| --- | --- | --- | --- |
| SPA state preservation | The first pass used `page.goto("/cart")` after clicking Add to Cart. That reloads the React app and loses cart context, causing false empty-cart failures. | Navigation was changed to click the header cart link (`a[href='/cart']`) so the SPA context is preserved. | The model reasoned in URL/page terms and missed that this SUT stores cart state only in React memory, not local storage or backend persistence. |
| Strict selectors | `a[href='/']` matched both the EShop logo and the Continue Shopping link. | The final test scopes the locator to `main a[href='/']`. | The first pass did not run in strict mode and did not account for duplicate anchors. |
| Unsupported quantity editing | Some HW02 cart concepts imply quantity controls, but the actual Cart page displays quantity only. | Selected and automated `quantity_display_one`; documented cart-page quantity edit as not automated. | The model inferred standard ecommerce behavior instead of checking the actual page structure. |
| Assertion strength | A simple "cart page loaded" assertion would not catch row/quantity/total regressions. | Added count, URL, text, and visibility assertions across the suite. | AI-generated UI tests often stop at navigation checks unless explicitly pushed toward assertion diversity. |

## Review Result

- Approved: Yes.
- Final FR-07 result: 36/36 browser executions passed.
