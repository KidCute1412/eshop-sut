# Bug Report - FR-07 Shopping Cart

## Scope

This bug report is based on the current executed `reports/FR-07/test-cases.md` results and evidence files under `reports/FR-07/evidence/`.

No implementation source code, database schema, controllers, services, routes, middleware, models, or internal tests were inspected. Expected results are taken from the documented FR-07 requirements, supporting setup rule `FR07-SETUP01`, shared navigation/feedback requirements, API specification references, Domain Testing report, BVA report, and executed test cases.

## Execution Summary

| Metric | Count |
| --- | --- |
| Total executed test cases | 20 |
| Domain Testing cases | 17 |
| Boundary Value Analysis cases | 3 |
| Passed cases | 6 |
| Failed cases | 14 |
| Blocked cases | 0 |
| Not Executed cases | 0 |
| Confirmed bug records | 11 |

## Confirmed Bugs

## BUG-FR07-001: Empty Cart State Is Missing Illustration or Icon

- Status: Confirmed
- Severity: Low
- Feature: FR-07 Shopping Cart
- Requirement: FR07-R06
- Related Test Case: [FR07-DT-001](./test-cases.md#fr07-dt-001)
- URL: `http://localhost:5173/cart`

### Description

The empty cart page displays a clear empty-cart message, but it does not display the required illustration, icon, or image.

### Steps to Reproduce

1. Open `http://localhost:5173/cart`.
2. Ensure the cart is empty.
3. Observe the empty cart state.

### Expected Result

The empty cart page displays both an illustration/icon and a clear empty-state message.

### Actual Result

The page displayed `Giỏ hàng của bạn đang trống`, but no visible illustration/icon was observed.

### Evidence

- [FR07-DT-001 screenshot](./evidence/FR07-DT-001.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-002: Cart Product List Uses `Giá` Instead of Required `Đơn giá` Column Label

- Status: Confirmed
- Severity: Low
- Feature: FR-07 Shopping Cart
- Requirement: FR07-R01
- Related Test Case: [FR07-DT-002](./test-cases.md#fr07-dt-002)
- URL: `http://localhost:5173/cart`

### Description

The cart displays a product table, but the unit-price column label does not match the documented requirement.

### Steps to Reproduce

1. Add product `iPhone 15 Pro Max` to the cart.
2. Open `http://localhost:5173/cart`.
3. Observe the cart table headers.

### Expected Result

The cart displays the required columns: `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, and `Thao tác`.

### Actual Result

The cart displayed `Sản phẩm`, `Giá`, `Số lượng`, `Thành tiền`, and `Thao tác`. The required `Đơn giá` label was not displayed.

### Evidence

- [FR07-DT-002 screenshot](./evidence/FR07-DT-002.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-003: Add-to-Cart Feedback and Cart Badge Are Missing

- Status: Confirmed
- Severity: Medium
- Feature: FR-07 Shopping Cart
- Requirements: FR07-R07, FR07-R08
- Related Test Cases: [FR07-DT-003](./test-cases.md#fr07-dt-003), [FR07-DT-011](./test-cases.md#fr07-dt-011)
- URL: `http://localhost:5173`

### Description

After adding a product to the cart, the UI does not show a toast/notification and the `Giỏ hàng` navbar link does not display a numeric cart badge.

### Steps to Reproduce

1. Log in as a public user.
2. Add one product to the cart from the public product flow.
3. Observe whether a toast/notification appears.
4. Observe whether the `Giỏ hàng` navbar link displays a numeric badge.

### Expected Result

After clicking `Thêm vào giỏ`, the UI shows visual feedback, such as a toast notification or a cart badge update. The `Giỏ hàng` link displays a numeric badge showing the number of products in the cart.

### Actual Result

No toast/notification was visible, and no numeric cart badge appeared beside `Giỏ hàng`.

### Evidence

- [FR07-DT-003 screenshot](./evidence/FR07-DT-002.png)
- [FR07-DT-011 screenshot](./evidence/FR07-DT-002.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-004: Adding the Same Product Twice Creates Duplicate Rows Instead of Increasing Quantity

- Status: Confirmed
- Severity: Medium
- Feature: FR-07 Shopping Cart
- Requirement: FR07-R02
- Related Test Case: [FR07-DT-004](./test-cases.md#fr07-dt-004)
- URL: `http://localhost:5173/cart`

### Description

When the same product is added twice, the cart creates two separate rows instead of merging the product into one row with increased quantity.

### Steps to Reproduce

1. Add the same product to the cart once.
2. Add the same product to the cart a second time.
3. Open `http://localhost:5173/cart`.
4. Observe row count and displayed quantity for that product.

### Expected Result

The cart shows one row for the product and increases the quantity to `2`.

### Actual Result

The cart displayed two separate rows for the same product, each with quantity `1`.

### Evidence

- [FR07-DT-004 screenshot](./evidence/FR07-DT-004.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-005: Cart Quantity Cannot Be Adjusted with `+` and `-` Controls

- Status: Confirmed
- Severity: Medium
- Feature: FR-07 Shopping Cart
- Requirement: FR07-R10
- Related Test Cases: [FR07-DT-005](./test-cases.md#fr07-dt-005), [FR07-DT-006](./test-cases.md#fr07-dt-006)
- URL: `http://localhost:5173/cart`

### Description

The cart displays quantity as plain text and does not provide the required `+` or `-` quantity adjustment controls.

### Steps to Reproduce

1. Add one product to the cart.
2. Open `http://localhost:5173/cart`.
3. Observe the quantity area for the cart item.
4. Add the same product twice if needed to prepare quantity greater than 1.
5. Observe whether `+` and `-` controls are available.

### Expected Result

The cart item has visible `+` and `-` controls. `+` increases quantity, and `-` decreases quantity when the quantity is greater than 1.

### Actual Result

The cart displayed item quantity as plain text and no `+` or `-` control was visible.

### Evidence

- [FR07-DT-005 screenshot](./evidence/FR07-DT-002.png)
- [FR07-DT-006 screenshot](./evidence/FR07-DT-002.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-006: Delete Action Does Not Show Confirmation Dialog

- Status: Confirmed
- Severity: Medium
- Feature: FR-07 Shopping Cart
- Requirement: FR07-R03
- Related Test Cases: [FR07-DT-007](./test-cases.md#fr07-dt-007), [FR07-DT-008](./test-cases.md#fr07-dt-008)
- URL: `http://localhost:5173/cart`

### Description

The cart provides a visible `Xóa` action, but clicking it does not show a browser-native confirmation dialog or custom confirmation modal before deletion.

### Steps to Reproduce

1. Add one product to the cart.
2. Open `http://localhost:5173/cart`.
3. Click `Xóa` for the cart item.
4. Observe whether a confirmation dialog appears before deletion.

### Expected Result

A confirmation dialog appears before deletion. Canceling the dialog preserves the item; confirming it removes the item.

### Actual Result

No browser-native confirmation dialog or custom confirmation modal appeared before the delete action. Therefore, the cancel and confirm paths could not be performed as specified.

### Evidence

- [FR07-DT-007 screenshot](./evidence/FR07-DT-007.png)
- [FR07-DT-008 screenshot](./evidence/FR07-DT-002.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-007: Cart Total Label Uses Forbidden `Tổng tạm tính` Instead of Required `Tổng cộng`

- Status: Confirmed
- Severity: Low
- Feature: FR-07 Shopping Cart
- Requirement: FR07-R05
- Related Test Case: [FR07-DT-010](./test-cases.md#fr07-dt-010)
- URL: `http://localhost:5173/cart`

### Description

The cart total area uses the forbidden label `Tổng tạm tính` instead of the required label `Tổng cộng`.

### Steps to Reproduce

1. Add one product to the cart.
2. Open `http://localhost:5173/cart`.
3. Observe the total label.

### Expected Result

The cart total label is exactly `Tổng cộng`. The label `Tổng tạm tính` is not used.

### Actual Result

The cart displayed `Tổng tạm tính: 30.000.000 đ`. The required label `Tổng cộng` was not displayed.

### Evidence

- [FR07-DT-010 screenshot](./evidence/FR07-DT-002.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-008: Cart Page Is Missing Breadcrumb

- Status: Confirmed
- Severity: Low
- Feature: FR-07 Shopping Cart
- Requirement: FR07-R09
- Related Test Case: [FR07-DT-012](./test-cases.md#fr07-dt-012)
- URL: `http://localhost:5173/cart`

### Description

The cart page is a child page, but it does not display a breadcrumb/path indicator.

### Steps to Reproduce

1. Open `http://localhost:5173/cart`.
2. Observe whether a breadcrumb/path indicator is displayed.

### Expected Result

The cart page displays breadcrumb/path context. Exact breadcrumb labels are unspecified.

### Actual Result

No breadcrumb/path indicator beyond the navbar was visible.

### Evidence

- [FR07-DT-012 screenshot](./evidence/FR07-DT-002.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-009: Cart Navigation Item Is Not Highlighted on Cart Page

- Status: Confirmed
- Severity: Low
- Feature: FR-07 Shopping Cart
- Requirement: FR07-SH01
- Related Test Case: [FR07-DT-013](./test-cases.md#fr07-dt-013)
- URL: `http://localhost:5173/cart`

### Description

The `Giỏ hàng` navbar item is visible on the cart page, but it is not visibly highlighted or selected.

### Steps to Reproduce

1. Open `http://localhost:5173/cart`.
2. Observe the `Giỏ hàng` navigation item.

### Expected Result

The cart navigation item is visibly highlighted/selected on the cart page.

### Actual Result

The `Giỏ hàng` navigation link used normal navigation styling and no observable active/selected highlight was present.

### Evidence

- [FR07-DT-013 screenshot](./evidence/FR07-DT-013.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-010: Cart API Accepts Missing `quantity` Property

- Status: Confirmed
- Severity: High
- Feature: FR-07 Shopping Cart
- Requirement: FR07-API04
- Related Test Case: [FR07-DT-017](./test-cases.md#fr07-dt-017)
- Endpoint: `POST http://localhost:3000/api/cart`

### Description

The cart API reports successful add-to-cart when the documented `quantity` property is omitted from the request body.

### Steps to Reproduce

1. Log in through the public API to obtain a bearer token.
2. Send `POST http://localhost:3000/api/cart` with the Authorization header and the following body:

```json
{
  "id": 1,
  "name": "Sản phẩm B",
  "price": 100000
}
```

3. Observe the HTTP status and JSON response.

### Expected Result

The request is outside the documented successful `POST /api/cart` contract and is rejected or does not add an item with missing quantity. Exact status and error message are unspecified.

### Actual Result

The API returned `200 OK` with body `{"message":"Added to cart"}`.

### Evidence

- [FR07-DT-017 screenshot](./evidence/FR07-DT-017.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR07-011: Add-to-Cart Accepts Quantity `0`

- Status: Confirmed
- Severity: High
- Feature: FR-07 Shopping Cart
- Requirement: FR07-SETUP01
- Related Test Case: [FR07-BVA-001](./test-cases.md#fr07-bva-001)
- URL: `http://localhost:5173/product/2`

### Description

The product detail add-to-cart quantity input accepts `0`, reports the add action as successful, and the cart displays the product with quantity `0`.

### Steps to Reproduce

1. Open product detail page for `Samsung Galaxy S24 Ultra`.
2. Enter quantity `0`.
3. Click `Thêm vào giỏ hàng`.
4. Open `http://localhost:5173/cart`.
5. Observe the Samsung cart row.

### Expected Result

Quantity `0` is rejected and the product is not added to the cart with quantity `0`. Exact validation message is unspecified.

### Actual Result

The product detail page accepted quantity `0` and showed `Đã thêm`. The cart then displayed `Samsung Galaxy S24 Ultra` with quantity `0` and line total `0 đ`.

### Evidence

- [FR07-BVA-001 screenshot](./evidence/FR07-BVA-001.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## Failed Test Cases to Bug Mapping

| Failed Test Case | Status | Bug ID |
| --- | --- | --- |
| FR07-DT-001 | Fail | BUG-FR07-001 |
| FR07-DT-002 | Fail | BUG-FR07-002 |
| FR07-DT-003 | Fail | BUG-FR07-003 |
| FR07-DT-004 | Fail | BUG-FR07-004 |
| FR07-DT-005 | Fail | BUG-FR07-005 |
| FR07-DT-006 | Fail | BUG-FR07-005 |
| FR07-DT-007 | Fail | BUG-FR07-006 |
| FR07-DT-008 | Fail | BUG-FR07-006 |
| FR07-DT-010 | Fail | BUG-FR07-007 |
| FR07-DT-011 | Fail | BUG-FR07-003 |
| FR07-DT-012 | Fail | BUG-FR07-008 |
| FR07-DT-013 | Fail | BUG-FR07-009 |
| FR07-DT-017 | Fail | BUG-FR07-010 |
| FR07-BVA-001 | Fail | BUG-FR07-011 |

## Non-Bug Notes

- Passing cases are not listed as bugs.
- `FR07-DT-009`, `FR07-DT-014`, `FR07-DT-015`, `FR07-DT-016`, `FR07-BVA-002`, and `FR07-BVA-003` passed in the current execution.
- No GitHub Issue links are invented; all issue links remain `Pending` until real issues are created.
- Repeated failures with the same likely root cause are grouped into one bug record where appropriate.

## Human Review

- Reviewer: Pending
- Review Date and Time: Pending
- Human Review Status: Pending
- Human Corrections: Pending
