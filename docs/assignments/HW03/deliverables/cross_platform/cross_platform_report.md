# Cross-Browser and Cross-Platform Verification Report

## Execution summary

| ID | Environment | Execution date | SUT URL | Status |
|---|---|---|---|---|
| CP-01 | Google Chrome 151.0.7922.72, Windows NT 10.0.26200 | 2 August 2026 | `http://127.0.0.1:5173` | Executed |
| CP-02 | Playwright Firefox 144.0.2, Windows NT 10.0.26200 | 2 August 2026 | `http://127.0.0.1:5173` | Executed |
| CP-03 | Physical phone / approved cloud device | — | — | Not executed |

The planned customer flow was executed successfully on Google Chrome and Firefox. Both desktop runs produced five authentic screenshots. A qualifying physical or cloud mobile environment remains pending.

## Chrome execution matrix

| Check | Result | Evidence |
|---|---|---|
| Product list and product media render | Passed | `chrome_desktop/01_product_list.png` |
| Product Detail is visible and readable | Passed | `chrome_desktop/02_product_detail.png` |
| Cart layout, controls, and totals render | Passed, with known functional defects documented separately | `chrome_desktop/03_cart.png` |
| Checkout form and feedback render | Passed, with known total/coupon defects documented separately | `chrome_desktop/04_checkout.png` |
| Order History can be located and interpreted | Passed, with no item-details control | `chrome_desktop/05_order_history.png` |

Each Chrome screenshot contains the required `23127404@hcmus.edu.vn` identity caption together with browser, operating system, and URL context. The caption is part of the captured page and does not simulate browser chrome.

## Firefox execution matrix

| Check | Result | Evidence |
|---|---|---|
| Product list and product media render | Passed | `firefox_desktop/01_product_list.png` |
| Product Detail is visible and readable | Passed | `firefox_desktop/02_product_detail.png` |
| Cart layout, controls, and totals render | Passed, with known functional defects documented separately | `firefox_desktop/03_cart.png` |
| Checkout form and feedback render | Passed, with known total/coupon defects documented separately | `firefox_desktop/04_checkout.png` |
| Order History can be located and interpreted | Passed, with no item-details control | `firefox_desktop/05_order_history.png` |

The Firefox flow matched the Chrome flow at the tested desktop viewport; no Firefox-specific visual or navigation difference was observed. Each image contains the same required identity/environment caption format.

## Observed platform constraints

| Difference ID | Platforms affected | Observation | Impact | Classification |
|---|---|---|---|---|
| CP-DIFF-01 | Mobile | No physical or approved cloud device was available during this execution | Mobile layout and behavior remain unverified | Evidence gap |

## Conclusion

Chrome Desktop and Firefox Desktop each provide five authentic captures for the selected flow. The assignment's requirement of three qualifying platforms is not yet satisfied because CP-03 still requires a physical device or approved cloud platform. The missing mobile platform is not represented by emulation or generated evidence.
