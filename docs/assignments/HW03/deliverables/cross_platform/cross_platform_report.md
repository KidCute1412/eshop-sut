# Cross-Browser and Cross-Platform Verification Report

## Execution summary

| ID | Environment | Execution date | SUT URL | Status |
|---|---|---|---|---|
| CP-01 | Google Chrome 151.0.7922.72, Windows NT 10.0.26200 | 2 August 2026 | `http://127.0.0.1:5173` | Executed |
| CP-02 | Playwright Firefox 144.0.2, Windows NT 10.0.26200 | 2 August 2026 | `http://127.0.0.1:5173` | Executed |
| CP-03 | iPhone / Expo Go capture; exact model, iOS version, SUT location pending | 3 August 2026 | Pending student metadata | Evidence supplied; qualification pending |

The planned Customer Web flow was executed successfully on Google Chrome and Firefox. Both desktop runs produced five authentic screenshots, which are preserved unchanged. Four Mobile captures were also supplied and reviewed, but CP-03 remains incomplete until exact environment metadata and the required identity overlay are present.

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
| CP-DIFF-01 | Mobile | Four iPhone/Expo captures show the FR-23 detail and quantity flow, but exact device/OS/SUT metadata and the required overlay are absent | Visible checkpoints are reviewable, but platform qualification is incomplete | Evidence-compliance gap |

CP-03 uses FR-23 Mobile Product Detail as its Mobile checkpoint. The supplied captures cover the basic detail screen, default quantity, successful add result, and invalid quantity feedback. Before final submission, recapture or otherwise supply authentic images containing the required `23127404@hcmus.edu.vn` overlay and record the exact device model, iOS version, Expo environment, SUT location, and execution date.

## Conclusion

Chrome Desktop and Firefox Desktop each provide five authentic captures for the selected flow. Four authentic Mobile captures provide useful FR-23 runtime evidence, but the assignment's third-platform requirement is not yet fully satisfied because CP-03 lacks exact environment metadata and the mandatory identity overlay.
