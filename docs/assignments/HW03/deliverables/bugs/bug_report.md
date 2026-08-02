# HW03 Verified Defect Report

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc (23127404) |
| System under test | EShop |
| Runtime environment | Google Chrome 151.0.7922.72 on Windows |
| Final execution | 2 August 2026 |
| Verified defects | 15 |
| Unverified Mobile hypotheses | 4; excluded from the defect total |
| GitHub Issue status | URLs and Issue-page screenshots pending creation by the student |

## Evidence policy

Every defect counted below was reproduced in two independent Chromium runs against a freshly seeded database. Static source inspection was used only after reproduction to explain a likely cause. The screenshots are genuine captures of the running SUT. A GitHub Issue is not claimed until the student creates it and supplies the URL.

## Verified defect summary

| Bug ID | Related check | Severity | Title | Evidence |
|---|---|---|---|---|
| BUG-001 | CHK-GUI-002 | Major | Product Detail requires a second click to add an item | `evidence_images/bug_001_first_click_cart_empty.png` |
| BUG-002 | CHK-GUI-003 | Major | Negative product quantity produces a negative cart subtotal | `evidence_images/bug_002_negative_quantity.png` |
| BUG-003 | CHK-GUI-004 | Minor | Decimal quantity is silently truncated | `evidence_images/bug_003_decimal_quantity_truncated.png` |
| BUG-006 | CHK-GUI-005 | Critical | Checkout total is client-editable and trusted | `evidence_images/bug_006_editable_checkout_total.png` |
| BUG-007 | CHK-GUI-009 | Major | Cart remains populated after checkout | `evidence_images/bug_007_cart_retained_after_checkout.png` |
| BUG-010 | CHK-GUI-016 | Major | Customer can cancel an order in shipping state | `evidence_images/bug_010_shipping_order_canceled.png` |
| BUG-011 | CHK-GUI-017 | Major | Canceled order can transition to delivered | `evidence_images/bug_011_canceled_order_delivered.png` |
| BUG-012 | CHK-GUI-024 | Major | Valid Vietnamese phone number is rejected | `evidence_images/bug_012_valid_phone_rejected.png` |
| BUG-013 | CHK-GUI-032 | Critical | Stored shipping-address HTML is executed in Admin | `evidence_images/bug_013_stored_html_injection.png` |
| BUG-014 | CHK-GUI-031 | Major | Admin dashboard doubles delivered revenue | `evidence_images/bug_014_admin_revenue_doubled.png` |
| BUG-015 | CHK-GUI-018 | Critical | Percentage coupon calculation produces invalid negative savings | `evidence_images/bug_015_percent_coupon_calculation.png` |
| BUG-016 | CHK-GUI-026 | Major | Order History provides no order-details view | `evidence_images/bug_016_order_history_has_no_details.png` |
| BUG-017 | CHK-GUI-036 | Major | Editing one product changes every visible product name | `evidence_images/bug_017_admin_product_edit_corrupts_list.png` |
| BUG-018 | CHK-GUI-037 | Minor | Admin data loading has no progress feedback | `evidence_images/bug_018_admin_missing_loading_indicator.png` |
| BUG-019 | CHK-GUI-035 | Minor | Admin order transition has no explicit success feedback | `evidence_images/bug_019_admin_status_no_success_feedback.png` |

## Detailed defect records

### BUG-001 — Product Detail requires a second click to add an item

**Severity:** Major
**Related check:** CHK-GUI-002
**Precondition:** Product 1 is available and the cart is empty.

**Steps to reproduce:**

1. Open `/product/1`.
2. Select **Thêm vào giỏ hàng** once.
3. Open **Giỏ hàng**.

**Expected:** The cart contains one unit after the first click.
**Actual:** The cart remains empty; a second click is required.
**Likely cause:** `handleAddToCart` consumes the first click by updating `clickCount` and returns before `addToCart`.
**Evidence:** `evidence_images/bug_001_first_click_cart_empty.png`
**GitHub Issue:** Pending student-created URL.

### BUG-002 — Negative quantity produces a negative cart subtotal

**Severity:** Major
**Related check:** CHK-GUI-003
**Steps:** Enter `-5` on Product Detail, add the item, and open the cart.
**Expected:** Quantity is constrained to a positive integer with validation feedback.
**Actual:** Quantity `-5` is accepted and the cart shows a negative subtotal.
**Likely cause:** No `min` constraint or range validation is applied.
**Evidence:** `evidence_images/bug_002_negative_quantity.png`
**GitHub Issue:** Pending student-created URL.

### BUG-003 — Decimal quantity is silently truncated

**Severity:** Minor
**Related check:** CHK-GUI-004
**Steps:** Enter `2.5` on Product Detail, add the item, and open the cart.
**Expected:** The decimal is rejected or the user is asked for an integer.
**Actual:** The cart silently stores quantity `2`.
**Likely cause:** `parseInt(quantity)` truncates without validation.
**Evidence:** `evidence_images/bug_003_decimal_quantity_truncated.png`
**GitHub Issue:** Pending student-created URL.

### BUG-006 — Checkout total is client-editable and trusted

**Severity:** Critical
**Related check:** CHK-GUI-005
**Steps:** Add a product, authenticate, open Checkout, and edit **Tổng tiền thanh toán**.
**Expected:** The authoritative total is read-only and calculated server-side.
**Actual:** The input is editable and its value is submitted as `total_amount`.
**Likely cause:** Checkout binds an editable input to `editableTotal`; the API stores the supplied total.
**Evidence:** `evidence_images/bug_006_editable_checkout_total.png`
**GitHub Issue:** Pending student-created URL.

### BUG-007 — Cart remains populated after checkout

**Severity:** Major
**Related check:** CHK-GUI-009
**Steps:** Complete checkout, return home, and open the cart.
**Expected:** The purchased cart is cleared.
**Actual:** The purchased item remains present.
**Likely cause:** The success path never calls `clearCart()`.
**Evidence:** `evidence_images/bug_007_cart_retained_after_checkout.png`
**GitHub Issue:** Pending student-created URL.

### BUG-010 — Customer can cancel an order in shipping state

**Severity:** Major
**Related check:** CHK-GUI-016
**Steps:** Move an owned order to `shipping`, then call the customer cancellation action.
**Expected:** The API rejects cancellation.
**Actual:** The API succeeds and changes the order to `canceled`.
**Likely cause:** The endpoint rejects only `delivered` and `canceled`, rather than allowing only `pending` and `confirmed`.
**Evidence:** `evidence_images/bug_010_shipping_order_canceled.png`
**GitHub Issue:** Pending student-created URL.

### BUG-011 — Canceled order can transition to delivered

**Severity:** Major
**Related check:** CHK-GUI-017
**Steps:** Cancel an order, then select **Đánh dấu Đã giao** in Admin.
**Expected:** `canceled` is terminal.
**Actual:** The UI offers the action and the API accepts `canceled → delivered`.
**Likely cause:** The Admin UI and state validation explicitly permit the transition.
**Evidence:** `evidence_images/bug_011_canceled_order_delivered.png`
**GitHub Issue:** Pending student-created URL.

### BUG-012 — Valid Vietnamese phone number is rejected

**Severity:** Major
**Related check:** CHK-GUI-024
**Steps:** Enter `0912345678` in Profile and submit.
**Expected:** The valid ten-digit number is accepted.
**Actual:** An alert reports that it is invalid.
**Likely cause:** The regex starts with `[1-9]` and excludes the required leading zero.
**Evidence:** `evidence_images/bug_012_valid_phone_rejected.png`
**GitHub Issue:** Pending student-created URL.

### BUG-013 — Stored shipping-address HTML is executed in Admin

**Severity:** Critical
**Related check:** CHK-GUI-032
**Steps:** Store HTML in an order's shipping address and open Admin Orders.
**Expected:** The address is rendered as escaped text.
**Actual:** The markup is interpreted and styled content appears; script-capable payloads can execute in the Admin origin.
**Likely cause:** `dangerouslySetInnerHTML` renders untrusted address content.
**Evidence:** `evidence_images/bug_013_stored_html_injection.png`
**GitHub Issue:** Pending student-created URL.

### BUG-014 — Admin dashboard doubles delivered revenue

**Severity:** Major
**Related check:** CHK-GUI-031
**Steps:** Create delivered orders with known totals and open Dashboard.
**Expected:** Revenue equals `8,234,567 ₫`.
**Actual:** Dashboard displays `16,469,134 ₫`.
**Likely cause:** The reducer adds `o.total_amount * 2`.
**Evidence:** `evidence_images/bug_014_admin_revenue_doubled.png`
**GitHub Issue:** Pending student-created URL.

### BUG-015 — Percentage coupon calculation produces invalid negative savings

**Severity:** Critical
**Related check:** CHK-GUI-018
**Steps:** Add a `30,000,000 ₫` product and apply `SAVE10` at Checkout.
**Expected:** Savings `3,000,000 ₫`; final total `27,000,000 ₫`.
**Actual:** Savings `-270,000,000 ₫`; final total `300,000,000 ₫`.
**Likely cause:** The formula uses `total_amount * (1 - discount_value)` instead of `total_amount * discount_value / 100`.
**Evidence:** `evidence_images/bug_015_percent_coupon_calculation.png`
**GitHub Issue:** Pending student-created URL.

### BUG-016 — Order History provides no order-details view

**Severity:** Major
**Related check:** CHK-GUI-026
**Steps:** Open Profile for a customer with orders.
**Expected:** Each order can be expanded or opened to inspect its items.
**Actual:** Only summary columns are available; there is no details control.
**Evidence:** `evidence_images/bug_016_order_history_has_no_details.png`
**GitHub Issue:** Pending student-created URL.

### BUG-017 — Editing one product changes every visible product name

**Severity:** Major
**Related check:** CHK-GUI-036
**Steps:** In Admin Products, edit one name and save.
**Expected:** Only the selected row changes.
**Actual:** Every visible product row shows the edited name until refresh.
**Likely cause:** The success handler maps the new name onto every product in client state.
**Evidence:** `evidence_images/bug_017_admin_product_edit_corrupts_list.png`
**GitHub Issue:** Pending student-created URL.

### BUG-018 — Admin data loading has no progress feedback

**Severity:** Minor
**Related check:** CHK-GUI-037
**Steps:** Delay Admin API responses and authenticate.
**Expected:** A spinner, skeleton, loading message, or disabled state is shown.
**Actual:** No loading feedback appears while requests are pending.
**Evidence:** `evidence_images/bug_018_admin_missing_loading_indicator.png`
**GitHub Issue:** Pending student-created URL.

### BUG-019 — Admin order transition has no explicit success feedback

**Severity:** Minor
**Related check:** CHK-GUI-035
**Steps:** Confirm a pending order in Admin.
**Expected:** A success toast or confirmation message appears.
**Actual:** Only the badge changes; no explicit success message is presented.
**Evidence:** `evidence_images/bug_019_admin_status_no_success_feedback.png`
**GitHub Issue:** Pending student-created URL.

## Unverified Mobile hypotheses

These source-derived candidates were not executed on Expo Go, a physical phone, or an approved cloud device. They are excluded from the verified defect count.

| Candidate | Hypothesis | Required verification |
|---|---|---|
| BUG-004 | Mobile Product Detail may omit category information | Execute CHK-GUI-039 on a qualifying device |
| BUG-005 | Missing-product handling may expose technical text without recovery navigation | Execute CHK-GUI-044 on a qualifying device |
| BUG-008 | Mobile checkout may omit the final cart item | Execute CHK-GUI-012 and inspect the request payload |
| BUG-009 | Mobile quantity entry may add one to the typed value | Execute CHK-GUI-011 on a qualifying device |

## GitHub Issue handoff

Create one GitHub Issue per verified defect using its detailed record and attach the corresponding PNG. After the URLs are supplied, update each `GitHub Issue` field and store a genuine Issue-page screenshot under `github_issues_screenshots/`.
