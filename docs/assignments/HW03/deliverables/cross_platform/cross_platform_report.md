# Cross-Browser and Cross-Platform Verification Report

## Execution summary

| ID | Environment | Execution date | SUT URL | Status |
|---|---|---|---|---|
| CP-01 | Google Chrome 151.0.7922.72, Windows NT 10.0.26200 | 2 August 2026 | `http://127.0.0.1:5173` | Executed |
| CP-02 | Playwright Firefox 144.0.2, Windows NT 10.0.26200 | 2 August 2026 | `http://127.0.0.1:5173` | Blocked by browser environment |
| CP-03 | Physical phone / approved cloud device | — | — | Not executed |

The planned customer flow was executed successfully on Google Chrome. Firefox launched, but Playwright failed at `browserContext.newPage` and the Firefox command-line screenshot process also stalled; no Firefox result or image is claimed. A qualifying physical or cloud mobile environment remains pending.

## Chrome execution matrix

| Check | Result | Evidence |
|---|---|---|
| Product list and product media render | Passed | `chrome_desktop/01_product_list.png` |
| Product Detail is visible and readable | Passed | `chrome_desktop/02_product_detail.png` |
| Cart layout, controls, and totals render | Passed, with known functional defects documented separately | `chrome_desktop/03_cart.png` |
| Checkout form and feedback render | Passed, with known total/coupon defects documented separately | `chrome_desktop/04_checkout.png` |
| Order History can be located and interpreted | Passed, with no item-details control | `chrome_desktop/05_order_history.png` |

Each Chrome screenshot contains the required `23127404@hcmus.edu.vn` identity caption together with browser, operating system, and URL context. The caption is part of the captured page and does not simulate browser chrome.

## Observed platform constraints

| Difference ID | Platforms affected | Observation | Impact | Classification |
|---|---|---|---|---|
| CP-DIFF-01 | Firefox | Browser launched, but page creation failed in Playwright; CLI capture also stalled | The Firefox flow could not be evaluated reliably | Test-environment blocker |
| CP-DIFF-02 | Mobile | No physical or approved cloud device was available during this execution | Mobile layout and behavior remain unverified | Evidence gap |

## Conclusion

Chrome Desktop provides five authentic cross-platform captures for the selected flow. The assignment's requirement of three qualifying platforms is not yet satisfied: Firefox must be rerun in a working environment and CP-03 requires a physical device or approved cloud platform. Neither missing platform is represented by emulation or generated evidence.
