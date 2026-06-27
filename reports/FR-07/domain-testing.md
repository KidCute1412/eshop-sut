# Domain Testing - FR-07 Shopping Cart

## Step 1. Identify Input & Output Variables

| Type              | Variable or Output               | Description                                                                  | Related Rule IDs                 | Applies To |
| ----------------- | -------------------------------- | ---------------------------------------------------------------------------- | -------------------------------- | ---------- |
| State / Condition | Authenticated user state         | User has a valid bearer token/session for cart API and UI cart actions.      | FR07-API01                       | UI/API     |
| State / Condition | Empty cart state                 | Cart contains no items and the empty-state UI can be observed.               | FR07-R06                         | UI         |
| State / Condition | Non-empty cart state             | Cart contains at least one item.                                             | FR07-R01, FR07-R10, FR07-R11     | UI/API     |
| Input             | Product identity                 | Product selected for add-to-cart.                                            | FR07-R02, FR07-API03, FR07-API04 | UI/API     |
| Input             | Product name                     | Name property in API body and visible cart product name.                     | FR07-R01, FR07-API04             | UI/API     |
| Input             | Unit price                       | Price property used for unit price and line total.                           | FR07-R01, FR07-R11, FR07-API04   | UI/API     |
| Input             | Add-to-cart setup quantity       | Quantity entered on product detail before adding product into cart.          | FR07-SETUP01, FR07-API04         | UI/API     |
| Input             | Duplicate add action             | Same product added more than once.                                           | FR07-R02                         | UI/API     |
| Input             | Plus control action              | User increments item quantity in the cart.                                   | FR07-R10                         | UI         |
| Input             | Minus control action             | User decrements item quantity in the cart.                                   | FR07-R10                         | UI         |
| Input             | Delete action                    | User requests item removal.                                                  | FR07-R03                         | UI         |
| Input             | Delete confirmation decision     | User confirms or cancels deletion.                                           | FR07-R03                         | UI         |
| Output            | Cart table/list columns          | Product, unit price, quantity, line total, and action columns.               | FR07-R01                         | UI         |
| Output            | Duplicate-merge result           | One cart row with increased quantity, not duplicate rows.                    | FR07-R02                         | UI/API     |
| Output            | Continue shopping navigation     | Button labeled `Tiếp tục mua sắm` returns user to home/public shopping area. | FR07-R04                         | UI         |
| Output            | Total label                      | Total label text exactly `Tổng cộng`.                                        | FR07-R05                         | UI         |
| Output            | Empty-state message/illustration | Empty cart visual and clear message.                                         | FR07-R06                         | UI         |
| Output            | Add-to-cart feedback             | Toast or badge update.                                                       | FR07-R07                         | UI         |
| Output            | Navbar cart badge                | Numeric badge on `Giỏ hàng` link.                                            | FR07-R08                         | UI         |
| Output            | Breadcrumb                       | Breadcrumb/path on cart child page.                                          | FR07-R09                         | UI         |
| Output            | Navbar active highlight          | Cart navigation item highlighted on cart page.                               | FR07-SH01                        | UI         |
| Output            | Logout label                     | Logout action label is `Đăng xuất`, not `Thoát`.                             | FR07-SH06                        | UI         |
| API Contract      | GET cart response                | Public authenticated cart retrieval.                                         | FR07-API02                       | API        |
| API Contract      | POST cart request/response       | Public authenticated add-to-cart request.                                    | FR07-API03, FR07-API04           | API        |
| Output            | Unauthorized API rejection       | Cart API without bearer token is rejected or does not expose a cart.         | FR07-API01                       | API        |

## Step 2. Identify Equivalence Classes

| Partition ID       | Type              | Variable or Condition      | Equivalence Class Description                                          | Validity | Representative Value                                        | Dependencies                      | Rule IDs                 | Test Basis Reference                           | Assumptions                                                               |
| ------------------ | ----------------- | -------------------------- | ---------------------------------------------------------------------- | -------- | ----------------------------------------------------------- | --------------------------------- | ------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------- |
| AUTH-V01           | State / Condition | Authenticated state        | User has valid token/session.                                          | Valid    | `test@eshop.com` login token/session                        | User exists and login works.      | FR07-API01               | `api_specification.md` Cart header requirement | Existing test account available.                                          |
| AUTH-I01           | State / Condition | Authenticated state        | No bearer token for cart API.                                          | Invalid  | Omit Authorization header                                   | API reachable.                    | FR07-API01               | `api_specification.md` Cart header requirement | Exact status/body unspecified.                                            |
| CART-EMPTY-V01     | State / Condition | Empty cart                 | Cart has no items and empty-state UI is visible.                       | Valid    | Fresh/cleared cart                                          | Cart can be emptied via UI setup. | FR07-R06                 | `README.md` - FR-07/FR-24                      | Empty state observable through UI only.                                   |
| CART-NONEMPTY-V01  | State / Condition | Non-empty cart             | Cart has one or more items.                                            | Valid    | One product in cart                                         | Add-to-cart available.            | FR07-R01                 | `README.md` - FR-07                            | Product data exists publicly.                                             |
| CART-COLUMNS-V01   | Output            | Cart list columns          | Required columns are visible.                                          | Valid    | `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, `Thao tác` | Non-empty cart.                   | FR07-R01                 | `README.md` - FR-07                            | Equivalent visible labels accepted only when they satisfy README wording. |
| PRODUCT-ID-V01     | Input             | Product identity           | Existing public product.                                               | Valid    | Product id `1` / first visible product                      | Product exists.                   | FR07-API03               | `api_specification.md` - POST `/api/cart`      | Exact product catalog may vary.                                           |
| PRODUCT-ID-I01     | Input             | Product identity           | Missing product id in API body.                                        | Invalid  | Body without `id`                                           | Auth token.                       | FR07-API04               | `api_specification.md` - POST body             | Outside documented successful contract; exact error unspecified.          |
| SETUP-QTY-V01      | Input             | Add-to-cart setup quantity | Positive integer setup quantity.                                       | Valid    | `1`                                                         | Product selected.                 | FR07-SETUP01, FR07-API04 | `README.md` - FR-06; API body                  | Minimum 1 applies to add-to-cart setup.                                   |
| SETUP-QTY-I01      | Input             | Add-to-cart setup quantity | Quantity less than 1.                                                  | Invalid  | `0`                                                         | Product selected.                 | FR07-SETUP01             | `README.md` - FR-06                            | Exact browser validation text unspecified.                                |
| SETUP-QTY-I02      | Input             | Add-to-cart setup quantity | Non-integer quantity.                                                  | Invalid  | `1.5`                                                       | Product selected.                 | FR07-SETUP01             | `README.md` - FR-06                            | Decimal handling may be browser/control dependent.                        |
| DUPLICATE-ADD-V01  | State / Condition | Duplicate add              | Same product added twice merges into one line with increased quantity. | Valid    | Add product A twice                                         | Cart starts empty or known.       | FR07-R02                 | `README.md` - FR-07                            | Two one-unit adds yield quantity 2.                                       |
| PLUS-V01           | Input             | Plus action                | Plus increases cart item quantity.                                     | Valid    | Click `+` on quantity 1                                     | Non-empty cart.                   | FR07-R10                 | `README.md` - FR-07                            | Plus increments by one.                                                   |
| MINUS-V01          | Input             | Minus action               | Minus decreases cart item quantity above minimum.                      | Valid    | Click `-` on quantity 2                                     | Non-empty cart quantity > 1.      | FR07-R10                 | `README.md` - FR-07                            | Quantity should remain positive.                                          |
| DELETE-CANCEL-V01  | Input             | Delete confirmation        | Canceling confirmation preserves item.                                 | Valid    | Click delete, cancel dialog                                 | Delete dialog appears.            | FR07-R03                 | `README.md` - FR-07/FR-24                      | Cancel option is available.                                               |
| DELETE-CONFIRM-V01 | Input             | Delete confirmation        | Confirming deletion removes item.                                      | Valid    | Click delete, confirm dialog                                | Delete dialog appears.            | FR07-R03                 | `README.md` - FR-07/FR-24                      | Item removal observable.                                                  |
| CONTINUE-V01       | Output            | Continue shopping          | `Tiếp tục mua sắm` button navigates home/shopping area.                | Valid    | Click `Tiếp tục mua sắm`                                    | Cart page open.                   | FR07-R04                 | `README.md` - FR-07                            | Exact home URL unspecified.                                               |
| TOTAL-LABEL-V01    | Output            | Total label                | Label is exactly `Tổng cộng`.                                          | Valid    | Visible text `Tổng cộng`                                    | Cart page open.                   | FR07-R05                 | `README.md` - FR-07                            | Diacritics required.                                                      |
| TOTAL-LABEL-I01    | Output            | Total label                | Label incorrectly says `Tổng tạm tính`.                                | Invalid  | Visible text `Tổng tạm tính`                                | Cart page open.                   | FR07-R05                 | `README.md` - FR-07                            | Other wrong labels also invalid.                                          |
| EMPTY-STATE-V01    | Output            | Empty state                | Empty cart has illustration/icon and clear message.                    | Valid    | Empty cart page with icon/image and message                 | Cart empty.                       | FR07-R06                 | `README.md` - FR-07/FR-24                      | Exact message unspecified.                                                |
| FEEDBACK-V01       | Output            | Add-to-cart feedback       | Toast or badge update appears.                                         | Valid    | Badge count changes or toast appears                        | Add action succeeds.              | FR07-R07                 | `README.md` - FR-06/FR-24                      | Badge update enough.                                                      |
| BADGE-V01          | Output            | Navbar badge               | Cart link displays numeric badge count.                                | Valid    | Badge `1` or higher                                         | Cart state known.                 | FR07-R08                 | `README.md` - FR-23                            | Count semantics ambiguous.                                                |
| BREADCRUMB-V01     | Output            | Breadcrumb                 | Cart page has breadcrumb/path.                                         | Valid    | Breadcrumb includes cart context                            | Cart page open.                   | FR07-R09                 | `README.md` - FR-23                            | Exact labels unspecified.                                                 |
| NAV-HIGHLIGHT-V01  | Output            | Navbar highlight           | Cart nav item visibly active on cart page.                             | Valid    | Active/highlight class or style                             | Cart page open.                   | FR07-SH01                | `README.md` - FR-23                            | Exact style unspecified.                                                  |
| API-GET-V01        | API Contract      | GET cart                   | Authenticated GET returns cart data.                                   | Valid    | `GET /api/cart` with token                                  | Auth token.                       | FR07-API02               | `api_specification.md` - GET `/api/cart`       | Schema unspecified.                                                       |
| API-POST-V01       | API Contract      | POST cart                  | Authenticated POST with documented body adds item.                     | Valid    | `{id:1,name:"Sản phẩm A",price:100000,quantity:2}`          | Auth token.                       | FR07-API03, FR07-API04   | `api_specification.md` - POST `/api/cart`      | Exact response unspecified.                                               |
| API-POST-I01       | API Contract      | POST cart                  | Missing documented request property.                                   | Invalid  | Body without `quantity`                                     | Auth token, other fields valid.   | FR07-API04               | `api_specification.md` - POST body             | Outside documented successful contract; exact error unspecified.          |

## Step 3. Best Representatives

| Partition ID       | Representative Value                                      | Why This Representative Was Chosen                  | Required Nominal Values for Other Variables | Applies To |
| ------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------- | ---------- |
| AUTH-V01           | Login as `test@eshop.com` / `Test1234!`                   | Existing public test user.                          | API and UI reachable.                       | UI/API     |
| AUTH-I01           | No Authorization header                                   | Isolates missing bearer-token condition.            | No body validation target.                  | API        |
| CART-EMPTY-V01     | `/cart` after deleting all visible items                  | Creates observable empty state.                     | Auth/session valid if required.             | UI         |
| CART-NONEMPTY-V01  | One first public product in cart                          | Minimal non-empty state for list/columns.           | Product and cart available.                 | UI/API     |
| CART-COLUMNS-V01   | One visible cart row                                      | Columns become observable only with non-empty cart. | Cart has item.                              | UI         |
| PRODUCT-ID-V01     | First visible product / API id `1`                        | Nominal documented product id example.              | Name, price, quantity valid.                | UI/API     |
| PRODUCT-ID-I01     | API body missing `id`                                     | Isolates missing id property.                       | Other body fields valid.                    | API        |
| SETUP-QTY-V01      | `1`                                                       | Minimum valid positive integer.                     | Product selected.                           | UI/API     |
| SETUP-QTY-I01      | `0`                                                       | Immediately below minimum.                          | Product selected.                           | UI         |
| SETUP-QTY-I02      | `1.5`                                                     | Representative non-integer.                         | Product selected.                           | UI         |
| DUPLICATE-ADD-V01  | Add same product twice with quantity 1                    | Directly exercises duplicate merge rule.            | Cart starts empty/known.                    | UI/API     |
| PLUS-V01           | Click `+` from quantity 1                                 | Minimal increment state.                            | One item in cart.                           | UI         |
| MINUS-V01          | Click `-` from quantity 2                                 | Avoids ambiguous minimum-at-1 behaviour.            | Quantity starts at 2.                       | UI         |
| DELETE-CANCEL-V01  | Click remove then Cancel                                  | Confirms dialog exists and cancel preserves item.   | One item in cart.                           | UI         |
| DELETE-CONFIRM-V01 | Click remove then OK/Confirm                              | Confirms actual removal path.                       | One item in cart.                           | UI         |
| CONTINUE-V01       | Click `Tiếp tục mua sắm`                                  | Directly maps to rule label.                        | Cart page open.                             | UI         |
| TOTAL-LABEL-V01    | Visible `Tổng cộng`                                       | Exact required label.                               | Cart page open.                             | UI         |
| TOTAL-LABEL-I01    | Visible `Tổng tạm tính`                                   | Explicit forbidden label.                           | Cart page open.                             | UI         |
| EMPTY-STATE-V01    | Empty cart page text + icon/image                         | Directly observable empty-state rule.               | Cart empty.                                 | UI         |
| FEEDBACK-V01       | Badge count changes after add or toast appears            | Allowed visual feedback type.                       | Add action succeeds.                        | UI         |
| BADGE-V01          | Numeric badge on `Giỏ hàng`                               | Direct navigation rule.                             | Cart state known.                           | UI         |
| BREADCRUMB-V01     | Breadcrumb text/path on `/cart`                           | Direct child-page rule.                             | Cart page open.                             | UI         |
| NAV-HIGHLIGHT-V01  | Highlighted cart nav item                                 | Direct navigation rule.                             | Cart page open.                             | UI         |
| API-GET-V01        | Authenticated `GET /api/cart`                             | Nominal cart retrieval.                             | Token valid.                                | API        |
| API-POST-V01       | Authenticated `POST /api/cart` with all documented fields | Nominal add item contract.                          | Token valid.                                | API        |
| API-POST-I01       | Authenticated `POST /api/cart` without `quantity`         | Isolates missing property.                          | Token valid, other fields valid.            | API        |

## Partition Derivation

Each partition above is derived from a documented FR-07 cart rule, the supporting FR-06 add-to-cart quantity setup rule, shared navigation/feedback rules, or the public cart API contract. Valid partitions describe behaviour the requirements explicitly require. Invalid partitions are limited to documented exclusions or non-conforming outputs, such as missing bearer token, missing contract property, invalid setup quantity below the positive integer minimum, non-integer setup quantity, forbidden total label text, or forbidden logout label text.

Ambiguous behaviours such as maximum quantity, stock limits, exact message text, exact unauthorized status, and exact badge-count semantics are excluded from normative coverage.

## Coverage Decisions

- Normative UI coverage includes cart list columns, duplicate add merge, plus/minus adjustment, delete confirmation, continue shopping, total label, empty state, add feedback, badge, breadcrumb, nav highlight, and logout label.
- Normative API coverage includes authenticated `GET /api/cart`, authenticated `POST /api/cart`, missing token rejection, and missing documented body property rejection.
- Quantity Domain Testing covers the supporting setup quantity rule from FR-06 because it prepares FR-07 cart states.
- Quantity BVA is included only for the documented minimum `1` from `FR07-SETUP01`.
- Maximum quantity, stock limits, persistence, exact API schemas/statuses, and checkout cart clearing are excluded because they are unsupported or belong to other features.
- Shared rules `FR07-SH02` through `FR07-SH05` are traced through their corresponding FR-07 rules to avoid duplicate test cases.

## Human Review - Phase 3

- Reviewer: Nguyen Thanh Tien
- Review Time: 2026-06-26 18:50
- Scope: FR-07 Domain Modeling
- Status: Completed
- Approved for BVA, test-case derivation, and test execution.

## Human Corrections

- Synced FR-07 domain model with reviewed `requirement-analysis.md`.
- Moved product-detail quantity rule from `FR07-R07` to setup rule `FR07-SETUP01`; renamed quantity partitions to `SETUP-QTY-*`.
- Updated rule IDs:
  - `FR07-R07`: Add-to-cart feedback
  - `FR07-R08`: Cart badge
  - `FR07-R09`: Breadcrumb
  - `FR07-R10`: Plus/minus quantity adjustment
  - `FR07-R11`: Cart line total

- Marked `CART-EMPTY-V01` as UI-only.
- Softened API missing-property partitions: only assert outside documented successful `POST /api/cart` contract; exact error response unspecified.
- Kept `FR07-SH02`–`FR07-SH05` for traceability only, not duplicate test targets.
