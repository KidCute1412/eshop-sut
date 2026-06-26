# Test Cases - FR-07 Shopping Cart

## Domain Testing Test Cases

## FR07-DT-001

- Test Case ID: FR07-DT-001
- Technique: Domain Testing
- Objective: Verify empty cart UI displays a clear empty state with illustration/icon and message.
- Requirement or Rule Reference: FR07-R06
- Preconditions: EShop User Web is available; cart is empty or all visible cart items can be removed through public UI.
- Test Data: Empty cart state.
- Steps:
  1. Open `/cart`.
  2. Ensure no products remain in the cart.
  3. Observe the empty cart content.
- Expected Result: Empty cart displays an illustration/icon and a clear user-facing empty-state message. Exact message and image are unspecified.
- Actual Result: Cart page showed empty message text: `Giỏ hàng của bạn đang trống`, but no visible illustration/icon was observed. Image/icon element count observed: 0.
- Status: Fail
- Evidence: [FR07-DT-001](./evidence/FR07-DT-001.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R06; `domain-testing.md` - CART-EMPTY-V01, EMPTY-STATE-V01

## FR07-DT-002

- Test Case ID: FR07-DT-002
- Technique: Domain Testing
- Objective: Verify non-empty cart displays required product list columns.
- Requirement or Rule Reference: FR07-R01
- Preconditions: EShop User Web is available; at least one product can be added to cart through public UI or public API setup.
- Test Data: Product `iPhone 15 Pro Max`; quantity `1`.
- Steps:
  1. Add one product to the cart.
  2. Open `/cart`.
  3. Observe the cart product list headers/columns.
- Expected Result: Cart displays product list with columns or visible labels for `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, and `Thao tác`.
- Actual Result: The non-empty cart displayed one product row for `iPhone 15 Pro Max`. Visible headers were `Sản phẩm`, `Giá`, `Số lượng`, `Thành tiền`, and `Thao tác`. The required `Đơn giá` header was not displayed; it was shown as `Giá`.
- Status: Fail
- Evidence: [FR07-DT-002](./evidence/FR07-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R01; `domain-testing.md` - CART-COLUMNS-V01

## FR07-DT-003

- Test Case ID: FR07-DT-003
- Technique: Domain Testing
- Objective: Verify add-to-cart action gives visual feedback through toast or cart badge update.
- Requirement or Rule Reference: FR07-R07
- Preconditions: EShop User Web is available; a public product can be added to cart.
- Test Data: First visible public product; quantity 1.
- Steps:
  1. Observe current cart badge count if visible.
  2. Click `Thêm vào giỏ` or the visible add-to-cart action for a product.
  3. Observe toast/notification or cart badge update.
- Expected Result: A visual feedback is displayed after add-to-cart, such as toast notification or updated cart badge.
- Actual Result: After the add-to-cart action, no toast/notification was visible and no numeric cart badge appeared beside `Giỏ hàng`. The product was added to the cart, but the required visual feedback was not observed.
- Status: Fail
- Evidence: [FR07-DT-003](./evidence/FR07-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R07; `domain-testing.md` - FEEDBACK-V01

## FR07-DT-004

- Test Case ID: FR07-DT-004
- Technique: Domain Testing
- Objective: Verify adding the same product twice increases quantity instead of creating a second row.
- Requirement or Rule Reference: FR07-R02
- Preconditions: Cart is empty or known; same public product can be added twice.
- Test Data: First visible public product; two one-unit add actions.
- Steps:
  1. Add the same product to cart once.
  2. Add the same product to cart a second time.
  3. Open `/cart`.
  4. Observe row count for that product and displayed quantity.
- Expected Result: The cart shows one row for the product and quantity increases to 2 rather than creating a duplicate line.
- Actual Result: After two add-to-cart clicks for the same product, the UI cart still displayed two separate rows for the same product, each with quantity 1.
- Status: Fail
- Evidence: [FR07-DT-004](./evidence/FR07-DT-004.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R02; `domain-testing.md` - DUPLICATE-ADD-V01

## FR07-DT-005

- Test Case ID: FR07-DT-005
- Technique: Domain Testing
- Objective: Verify plus control increases cart item quantity.
- Requirement or Rule Reference: FR07-R10
- Preconditions: Cart contains one item with quantity 1 and visible `+` control.
- Test Data: One cart item with quantity 1.
- Steps:
  1. Open `/cart` with one item.
  2. Click the item `+` quantity control.
  3. Observe the item quantity.
- Expected Result: The item quantity increases by one.
- Actual Result: After public setup with one visible cart item, the cart displayed the quantity as plain text and no `+` quantity control was visible.
- Status: Fail
- Evidence: [FR07-DT-005](./evidence/FR07-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R10; `domain-testing.md` - PLUS-V01

## FR07-DT-006

- Test Case ID: FR07-DT-006
- Technique: Domain Testing
- Objective: Verify minus control decreases cart item quantity when quantity is greater than 1.
- Requirement or Rule Reference: FR07-R10
- Preconditions: Cart contains one item with quantity greater than 1 and visible `-` control.
- Test Data: Same product `iPhone 15 Pro Max` added twice.
- Steps:
  1. Add the same product twice to prepare quantity greater than 1.
  2. Open `/cart`.
  3. Observe whether the cart shows one item row with quantity 2 and a visible `-` quantity control.
  4. If the `-` control is available, click it and observe the item quantity.
- Expected Result: The cart provides a visible `-` control for quantity adjustment. For an item with quantity 2, clicking `-` decreases the quantity from 2 to 1 and keeps the quantity positive.
- Actual Result: After adding the same product twice, the cart displayed two separate `iPhone 15 Pro Max` rows, each with quantity `1`. No `-` quantity control was visible for either row, so quantity decrease could not be performed.
- Status: Fail
- Evidence: [FR07-DT-006](./evidence/FR07-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R10; `domain-testing.md` - MINUS-V01

## FR07-DT-007

- Test Case ID: FR07-DT-007
- Technique: Domain Testing
- Objective: Verify delete action shows confirmation and canceling preserves the item.
- Requirement or Rule Reference: FR07-R03
- Preconditions: Cart contains one visible item and the delete action is visible.
- Test Data: One visible cart item; click `Xóa`.
- Steps:
  1. Open `/cart` with one item.
  2. Click the `Xóa` action for the item.
  3. Observe whether a confirmation dialog appears before deletion.
  4. If a confirmation dialog appears, cancel it and observe whether the item remains.
- Expected Result: A confirmation dialog appears before deletion; when canceled, the item remains in the cart.
- Actual Result: The cart displayed a visible `Xóa` action for the item. After clicking `Xóa`, no browser-native confirmation dialog or custom confirmation modal appeared before the delete action. Therefore, the cancel path could not be performed.
- Status: Fail
- Evidence: [FR07-DT-007](./evidence/FR07-DT-007.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R03; `domain-testing.md` - DELETE-CANCEL-V01

## FR07-DT-008

- Test Case ID: FR07-DT-008
- Technique: Domain Testing
- Objective: Verify confirming delete removes the item from cart.
- Requirement or Rule Reference: FR07-R03
- Preconditions: Cart contains one visible item and the delete action is visible.
- Test Data: One visible cart item; click `Xóa`.
- Steps:
  1. Open `/cart` with one item.
  2. Click the `Xóa` action for the item.
  3. Observe whether a confirmation dialog appears before deletion.
  4. If a confirmation dialog appears, confirm it.
  5. Observe whether the item is removed from the cart.
- Expected Result: A confirmation dialog appears before deletion; after confirmation, the item is removed from the cart.
- Actual Result: The cart displayed a visible `Xóa` action for the item. After clicking `Xóa`, no browser-native confirmation dialog or custom confirmation modal appeared, so there was no confirmation step to perform before deletion.
- Status: Fail
- Evidence: [FR07-DT-008](./evidence/FR07-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R03; `domain-testing.md` - DELETE-CONFIRM-V01

## FR07-DT-009

- Test Case ID: FR07-DT-009
- Technique: Domain Testing
- Objective: Verify `Tiếp tục mua sắm` returns user to home/public shopping area.
- Requirement or Rule Reference: FR07-R04
- Preconditions: Cart page is open and continue-shopping action is visible.
- Test Data: Click `Tiếp tục mua sắm`.
- Steps:
  1. Open `/cart`.
  2. Click `Tiếp tục mua sắm`.
  3. Observe navigation result.
- Expected Result: The user is navigated back to the home/public shopping area. Exact destination URL is unspecified.
- Actual Result: Clicking the continue-shopping action on `/cart` navigated to `http://localhost:5173/`. The home/product listing was visible.
- Status: Pass
- Evidence: [FR07-DT-009](./evidence/FR07-DT-009.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R04; `domain-testing.md` - CONTINUE-V01

## FR07-DT-010

- Test Case ID: FR07-DT-010
- Technique: Domain Testing
- Objective: Verify cart total label is exactly `Tổng cộng` and not `Tổng tạm tính`.
- Requirement or Rule Reference: FR07-R05
- Preconditions: Cart page is open.
- Test Data: Any cart state where total label is visible.
- Steps:
  1. Open `/cart`.
  2. Observe total label text.
  3. Check whether forbidden label `Tổng tạm tính` appears.
- Expected Result: Total label is exactly `Tổng cộng`; `Tổng tạm tính` is not used.
- Actual Result: The cart page displayed the total label as `Tổng tạm tính: 30.000.000 đ`. The required label `Tổng cộng` was not displayed.
- Status: Fail
- Evidence: [FR07-DT-010](./evidence/FR07-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R05; `domain-testing.md` - TOTAL-LABEL-V01, TOTAL-LABEL-I01

## FR07-DT-011

- Test Case ID: FR07-DT-011
- Technique: Domain Testing
- Objective: Verify navbar cart link displays numeric badge count.
- Requirement or Rule Reference: FR07-R08
- Preconditions: EShop User Web is available; cart state can be changed by adding a product.
- Test Data: Add one product to cart.
- Steps:
  1. Observe `Giỏ hàng` navigation link before add.
  2. Add one product to cart.
  3. Observe `Giỏ hàng` navigation link after add.
- Expected Result: The `Giỏ hàng` link displays a numeric badge count and the badge reflects cart content after add.
- Actual Result: After add-to-cart action, the navbar still displayed `Giỏ hàng` without a numeric badge. No visible badge count appeared or changed.
- Status: Fail
- Evidence: [FR07-DT-011](./evidence/FR07-DT-002.png)
- Partition or Boundary Covered: BADGE-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R08; `domain-testing.md` - BADGE-V01
- Notes and Assumptions: Distinct-line count vs total quantity is ambiguous; numeric visibility/change is the oracle.

## FR07-DT-012

- Test Case ID: FR07-DT-012
- Technique: Domain Testing
- Objective: Verify cart page displays breadcrumb.
- Requirement or Rule Reference: FR07-R09
- Preconditions: EShop User Web is available.
- Test Data: Open `/cart`.
- Steps:
  1. Open `/cart`.
  2. Observe breadcrumb/path indicator.
- Expected Result: Cart page displays breadcrumb/path context. Exact labels are unspecified.
- Actual Result: Cart page displayed the navbar and empty-cart content, but no breadcrumb/path indicator beyond the navbar was visible.
- Status: Fail
- Evidence: [FR07-DT-012](./evidence/FR07-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-R09; `domain-testing.md` - BREADCRUMB-V01

## FR07-DT-013

- Test Case ID: FR07-DT-013
- Technique: Domain Testing
- Objective: Verify cart navigation item is highlighted when cart page is selected.
- Requirement or Rule Reference: FR07-SH01
- Preconditions: EShop User Web is available.
- Test Data: Open `/cart`.
- Steps:
  1. Open `/cart`.
  2. Observe navbar active/highlight state.
- Expected Result: Cart navigation item is visibly highlighted/selected on the cart page.
- Actual Result: On `/cart`, the `Giỏ hàng` navigation link was visible, but it used normal navigation styling and no observable active/selected highlight was present.
- Status: Fail
- Evidence: [FR07-DT-013](./evidence/FR07-DT-013.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-SH01; `domain-testing.md` - NAV-HIGHLIGHT-V01

## FR07-DT-014

- Test Case ID: FR07-DT-014
- Technique: Domain Testing
- Objective: Verify authenticated `GET /api/cart` retrieves cart data.
- Requirement or Rule Reference: FR07-API01, FR07-API02
- Preconditions: Backend API is available; valid bearer token can be obtained through public login.
- Test Data: Bearer token for an authenticated public user.
- Steps:
  1. Log in through public API to obtain a token.
  2. Send `GET /api/cart` with `Authorization: Bearer <token>`.
  3. Observe status and JSON response.
- Expected Result: Authenticated `GET /api/cart` succeeds and returns cart data. Exact response schema is unspecified.
- Actual Result: Authenticated `GET /api/cart` returned HTTP 200 with JSON body `[]`.
- Status: Pass
- Evidence: [FR07-DT-014](./evidence/FR07-DT-014.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-API01, FR07-API02; `domain-testing.md` - API-GET-V01

## FR07-DT-015

- Test Case ID: FR07-DT-015
- Technique: Domain Testing
- Objective: Verify unauthenticated `GET /api/cart` is rejected or does not expose cart data.
- Requirement or Rule Reference: FR07-API01
- Preconditions: Backend API is available.
- Test Data: No Authorization header.
- Steps:
  1. Send `GET /api/cart` without Authorization header.
  2. Observe status and response body.
- Expected Result: Request is rejected or does not expose authenticated cart data. Exact status and message are unspecified.
- Actual Result: `GET /api/cart` without Authorization returned HTTP 401 and body `{"error":"Unauthorized"}`.
- Status: Pass
- Evidence: [FR07-DT-015](./evidence/FR07-DT-015.png)
- Partition or Boundary Covered: AUTH-I01
- Test Basis Reference: `requirement-analysis.md` - FR07-API01; `domain-testing.md` - AUTH-I01
- Notes and Assumptions: A 4xx response is acceptable; success exposing user cart would contradict the header requirement.

## FR07-DT-016

- Test Case ID: FR07-DT-016
- Technique: Domain Testing
- Objective: Verify authenticated `POST /api/cart` with documented body adds an item.
- Requirement or Rule Reference: FR07-API01, FR07-API03, FR07-API04
- Preconditions: Backend API is available; valid bearer token can be obtained through public login.
- Test Data: `{"id":1,"name":"Sản phẩm A","price":100000,"quantity":2}`.
- Steps:
  1. Log in through public API to obtain a token.
  2. Send `POST /api/cart` with Authorization header and documented JSON body.
  3. Observe status and response body.
  4. Optionally send authenticated `GET /api/cart` to verify item is observable.
- Expected Result: Authenticated POST succeeds and the item is added to cart or updated cart data is returned. Exact success status/body schema is unspecified.
- Actual Result: Authenticated `POST /api/cart` returned HTTP 200 with body `{"message":"Added to cart"}`. Follow-up GET returned `[{"id":1,"name":"Sản phẩm A","price":100000,"quantity":2}]`.
- Status: Pass
- Evidence: [FR07-DT-016](./evidence/FR07-DT-016.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-API01, FR07-API03, FR07-API04; `domain-testing.md` - API-POST-V01

## FR07-DT-017

- Test Case ID: FR07-DT-017
- Technique: Domain Testing
- Objective: Verify `POST /api/cart` missing a documented body property is rejected or does not add invalid item.
- Requirement or Rule Reference: FR07-API04
- Preconditions: Backend API is available; valid bearer token can be obtained through public login.
- Test Data: `{"id":1,"name":"Sản phẩm B","price":100000}` missing `quantity`.
- Steps:
  1. Log in through public API to obtain a token.
  2. Send `POST /api/cart` with Authorization header and body missing `quantity`.
  3. Observe status and response body.
- Expected Result: The request is outside the documented successful `POST /api/cart` contract and is rejected or does not add an item with missing quantity. Exact status and error message are unspecified.
- Actual Result: `POST /api/cart` missing `quantity` returned HTTP 200 with body `{"message":"Added to cart"}`.
- Status: Fail
- Evidence: [FR07-DT-017](./evidence/FR07-DT-017.png)
- Test Basis Reference: `requirement-analysis.md` - FR07-API04; `domain-testing.md` - API-POST-I01

## Boundary Value Analysis Test Cases

## FR07-BVA-001

- Test Case ID: FR07-BVA-001
- Technique: Boundary Value Analysis
- Objective: Verify add-to-cart setup quantity below minimum (`0`) is rejected.
- Requirement or Rule Reference: FR07-SETUP01
- Preconditions: Product detail add-to-cart quantity control is available.
- Test Data: Product `Samsung Galaxy S24 Ultra`; Quantity `0`.
- Steps:
  1. Open product detail page for `Samsung Galaxy S24 Ultra`.
  2. Enter quantity `0`.
  3. Click `Thêm vào giỏ hàng`.
  4. Open `/cart`.
  5. Observe whether the product is added with quantity `0`.
- Expected Result: Quantity `0` is rejected and the product is not added to the cart with quantity `0`. Exact validation message is unspecified.
- Actual Result: The product detail page accepted quantity `0` and showed the add action state `Đã thêm`. The cart then displayed `Samsung Galaxy S24 Ultra` as a cart row with quantity `0` and line total `0 đ`.
- Status: Fail
- Evidence: [FR07-BVA-001](./evidence/FR07-BVA-001.png)
- Partition or Boundary Covered: FR07-SETUP-QTY-MIN-B01
- Test Basis Reference: `boundary-value-analysis.md` - FR07-SETUP-QTY-MIN-B01
- Notes and Assumptions: The failure is based on the observable cart row with quantity `0`; exact validation message is outside the oracle.

## FR07-BVA-002

- Test Case ID: FR07-BVA-002
- Technique: Boundary Value Analysis
- Objective: Verify add-to-cart setup quantity at minimum (`1`) is accepted.
- Requirement or Rule Reference: FR07-SETUP01
- Preconditions: Product detail add-to-cart quantity control is available.
- Test Data: Product `iPhone 15 Pro Max`; Quantity `1`.
- Steps:
  1. Open a product detail page with an add-to-cart quantity input.
  2. Enter quantity `1`.
  3. Click `Thêm vào giỏ hàng`.
  4. Open `/cart`.
  5. Observe whether the product is shown with quantity `1`.
- Expected Result: Quantity `1` is accepted and the cart shows the product with quantity `1`.
- Actual Result: After entering quantity `1` and clicking `Thêm vào giỏ hàng`, the cart displayed the product `iPhone 15 Pro Max` with quantity `1`.
- Status: Pass
- Evidence: [FR07-BVA-002](./evidence/FR07-DT-002.png)
- Partition or Boundary Covered: FR07-SETUP-QTY-MIN-B02
- Test Basis Reference: `boundary-value-analysis.md` - FR07-SETUP-QTY-MIN-B02
- Notes and Assumptions: Quantity `1` is the inclusive minimum valid value.

## FR07-BVA-003

- Test Case ID: FR07-BVA-003
- Technique: Boundary Value Analysis
- Objective: Verify add-to-cart setup quantity immediately above minimum (`2`) is accepted.
- Requirement or Rule Reference: FR07-SETUP01
- Preconditions: Product detail add-to-cart quantity control is available.
- Test Data: Product `iPhone 15 Pro Max`; Quantity `2`.
- Steps:
  1. Open a product detail page with an add-to-cart quantity input.
  2. Enter quantity `2`.
  3. Click `Thêm vào giỏ hàng`.
  4. Open `/cart`.
  5. Observe whether the product is shown with quantity `2`.
- Expected Result: Quantity `2` is accepted and the cart shows the product with quantity `2`.
- Actual Result: After entering quantity `2` and clicking `Thêm vào giỏ hàng`, the cart displayed the product `iPhone 15 Pro Max` with quantity `2`.
- Status: Pass
- Evidence: [FR07-BVA-003](./evidence/FR07-BVA-003.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR07-SETUP-QTY-MIN-B03

## Coverage Summary

| Requirement / Rule     | Partition or Boundary                 | Technique | Test Case(s)                      | Surface | Coverage Status | Notes                             |
| ---------------------- | ------------------------------------- | --------- | --------------------------------- | ------- | --------------- | --------------------------------- |
| FR07-R06               | CART-EMPTY-V01, EMPTY-STATE-V01       | DT        | FR07-DT-001                       | UI      | Covered         | Empty-state visual and message.   |
| FR07-R01               | CART-NONEMPTY-V01, CART-COLUMNS-V01   | DT        | FR07-DT-002                       | UI      | Covered         | Required cart columns.            |
| FR07-R07               | FEEDBACK-V01                          | DT        | FR07-DT-003                       | UI      | Covered         | Toast or badge update.            |
| FR07-R02               | DUPLICATE-ADD-V01                     | DT        | FR07-DT-004                       | UI      | Covered         | Same product merge behaviour.     |
| FR07-R10               | PLUS-V01, MINUS-V01                   | DT        | FR07-DT-005, FR07-DT-006          | UI      | Covered         | Quantity controls.                |
| FR07-R03               | DELETE-CANCEL-V01, DELETE-CONFIRM-V01 | DT        | FR07-DT-007, FR07-DT-008          | UI      | Covered         | Confirmation before delete.       |
| FR07-R04               | CONTINUE-V01                          | DT        | FR07-DT-009                       | UI      | Covered         | Continue shopping navigation.     |
| FR07-R05               | TOTAL-LABEL-V01/I01                   | DT        | FR07-DT-010                       | UI      | Covered         | Exact label and forbidden label.  |
| FR07-R08               | BADGE-V01                             | DT        | FR07-DT-011                       | UI      | Covered         | Navbar badge.                     |
| FR07-R09               | BREADCRUMB-V01                        | DT        | FR07-DT-012                       | UI      | Covered         | Cart breadcrumb.                  |
| FR07-SH01              | NAV-HIGHLIGHT-V01                     | DT        | FR07-DT-013                       | UI      | Covered         | Active navbar state.              |
| FR07-API01, FR07-API02 | AUTH-V01, API-GET-V01                 | DT        | FR07-DT-014                       | API     | Covered         | Authenticated cart retrieval.     |
| FR07-API01             | AUTH-I01                              | DT        | FR07-DT-015                       | API     | Covered         | Missing token rejection.          |
| FR07-API03, FR07-API04 | API-POST-V01                          | DT        | FR07-DT-016                       | API     | Covered         | Valid API add contract.           |
| FR07-API04             | API-POST-I01                          | DT        | FR07-DT-017                       | API     | Covered         | Missing documented body property. |
|                        |
| FR07-SETUP01           | FR07-SETUP-QTY-MIN-B01/B02/B03        | BVA       | FR07-BVA-001 through FR07-BVA-003 | UI      | Covered         | Setup quantity lower boundary.    |

## Human Review - Phase 5

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-26 15:47 GMT+7
- Review Scope: FR-07 Test-Case Design, Execution Results, Evidence Links, and Coverage Summary
- Human Review Status: Completed
- Approved for Validation: Yes
- Approved for Test-Case Quality Review: Yes
- Approved for Test Execution: Yes

## Human Corrections

- Synchronized test-case rule references with the reviewed `requirement-analysis.md` and `domain-testing.md`.
- Updated add-to-cart feedback from `FR07-R08` to `FR07-R07`.
- Updated navbar badge from `FR07-R09` to `FR07-R08`.
- Updated breadcrumb from `FR07-R10` to `FR07-R09`.
- Updated plus/minus cart quantity controls from `FR07-R11` to `FR07-R10`.
- Updated BVA test cases from `FR07-R07` to supporting setup rule `FR07-SETUP01`.
- Renamed BVA boundary references from `FR07-QTY-MIN-B01/B02/B03` to `FR07-SETUP-QTY-MIN-B01/B02/B03`.
- Kept executed Actual Results, Status values, and evidence links from the current execution evidence.
