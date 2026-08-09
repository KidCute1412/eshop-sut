# Bug Report - FR-07

## BUG-HW04-FR07-001 - Duplicate product creates separate cart rows

- Affected tests: `FR07-DT-004` on Chromium, Firefox, and WebKit
- Expected: Adding the same product twice shows one cart row with quantity `2`.
- Actual: The cart shows two separate rows, each with quantity `1`.
- Status: Confirmed by automation.

## BUG-HW04-FR07-002 - Delete does not show confirmation before removal

- Affected tests: `FR07-DT-005`, `FR07-DT-006` on Chromium, Firefox, and WebKit
- Expected: Clicking `Xóa` opens a confirmation dialog; only after Confirm is the item removed.
- Actual: No confirmation dialog appears before deletion.
- Status: Confirmed by automation.

## BUG-HW04-FR07-003 - Cart header uses `Giá` instead of `Đơn giá`

- Affected tests: `FR07-DT-010` on Chromium, Firefox, and WebKit
- Expected headers: `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, `Thao tác`.
- Actual headers: `Sản phẩm`, `Giá`, `Số lượng`, `Thành tiền`, `Thao tác`.
- Status: Confirmed by automation.

## BUG-HW04-FR07-004 - Total label is not `Tổng cộng`

- Affected tests: `FR07-DT-011` on Chromium, Firefox, and WebKit
- Expected: Total label is `Tổng cộng`.
- Actual: Total label is `Tổng tạm tính`.
- Status: Confirmed by automation.

## BUG-HW04-FR07-005 - Cart page has no `+` / `-` quantity controls

- Affected tests: `FR07-BVA-002`, `FR07-BVA-003` on Chromium, Firefox, and WebKit
- Expected: Each cart item exposes `+` and `-` controls for quantity adjustment.
- Actual: Quantity is displayed as plain text; no `+` or `-` button is available.
- Status: Confirmed by automation.
