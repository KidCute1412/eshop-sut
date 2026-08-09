# Bug Report - FR-17


## BUG-HW04-FR17-001 - Coupon creation accepts `discount_value = 0`

- Affected tests: `FR17-BVA-001` on Chromium, Firefox, and WebKit
- Expected: Coupon creation is rejected because `discount_value` must be positive (`> 0`).
- Actual: `POST /api/admin/coupons` returned HTTP `200 OK`.
- Status: Confirmed by automation.

## BUG-HW04-FR17-002 - Coupon creation accepts `min_order_amount = -1`

- Affected tests: `FR17-BVA-002` on Chromium, Firefox, and WebKit
- Expected: Coupon creation is rejected because `min_order_amount` must be `>= 0`.
- Actual: `POST /api/admin/coupons` returned HTTP `200 OK`.
- Status: Confirmed by automation.

## Passing Boundary Control

- `FR17-BVA-003` (`max_uses_per_user = 0`) passed because the Admin UI's native number input validation blocked submission before any create request was sent.
