# Requirement Analysis - FR-07 Shopping Cart

## Feature Intake

| Field               | Value                                                                     |
| ------------------- | ------------------------------------------------------------------------- |
| Feature ID          | FR-07                                                                     |
| Feature name        | Shopping Cart / Giỏ hàng                                                  |
| Pool                | B - Shopping Cart and Checkout                                            |
| Actor               | Authenticated shopper / customer using EShop User Web and public cart API |
| Application surface | EShop User Web cart/product pages and public cart API                     |
| UI locations        | Product listing/detail add-to-cart flow; `/cart` shopping cart page       |
| API endpoints       | `GET /api/cart`, `POST /api/cart`                                         |
| Output root         | `reports/FR-07`                                                           |

## Approved Black-box Test Bases

- `2026.HW02.Domain Testing_En.pdf` - Pool B identifies FR-07 as Shopping Cart.
- `README.md` - FR-07 Shopping Cart.
- `README.md` - FR-06 Product Detail add-to-cart quantity rule, used only as setup support for adding products into the cart.
- `README.md` - FR-23 Navigation Requirements that apply to the cart page, cart badge, logout label, and breadcrumb.
- `README.md` - FR-24 Feedback & State Requirements that apply to add-to-cart feedback, delete confirmation, and empty state.
- `api_specification.md` - Cart & Orders, `GET /api/cart`, `POST /api/cart`, and `Authorization: Bearer <token>` header requirement.
- `setup_guide.md` - public startup guidance only.
- Public UI/API observations captured only during execution are evidence, not implementation-derived expected results.

## Requirement Rules

| Rule ID  | Rule                                                                                                        | Test Basis Type      | Test Basis Reference                     | Observable Expected Behaviour                                                                                            | Ambiguity                                                                                                   | Assumption                                                                                                        |
| -------- | ----------------------------------------------------------------------------------------------------------- | -------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| FR07-R01 | The cart displays a product list with columns: `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, `Thao tác`. | Official requirement | `README.md` - FR-07                      | A non-empty cart page visibly presents those columns or equivalent Vietnamese labels from the README.                    | Exact table structure and responsive layout are unspecified.                                                | Visible column/header text is sufficient observable evidence.                                                     |
| FR07-R02 | Adding the same product to the cart increases quantity instead of creating a new line.                      | Official requirement | `README.md` - FR-07                      | After adding the same product twice, the cart shows one line for that product with increased quantity.                   | Whether quantity increases by 1 or by the entered add quantity depends on input quantity.                   | For one-unit add actions, expected quantity increases from 1 to 2.                                                |
| FR07-R03 | The remove product button must show a confirmation dialog before removal.                                   | Official requirement | `README.md` - FR-07; `README.md` - FR-24 | Attempting to remove a cart item displays a confirmation dialog before the item is removed.                              | Exact dialog text and browser-native vs custom modal are unspecified.                                       | Any observable confirmation requiring user choice satisfies the dialog requirement.                               |
| FR07-R04 | The cart has a `Tiếp tục mua sắm` button to return to the home page.                                        | Official requirement | `README.md` - FR-07                      | The cart page provides a visible button labeled `Tiếp tục mua sắm`, and activating it returns the user to the home page. | Exact home URL is unspecified.                                                                              | Navigating away from `/cart` to the public home/product area is acceptable after the labeled action is activated. |
| FR07-R05 | The total label must be exactly `Tổng cộng`, not `Tổng tạm tính`.                                           | Official requirement | `README.md` - FR-07                      | The cart total area uses the exact label `Tổng cộng`; it does not use `Tổng tạm tính`.                                   | Capitalization/diacritics are expected as documented in the README.                                         | The visible label is the oracle; amount formatting is separate unless obviously inconsistent.                     |
| FR07-R06 | Empty cart must have an illustration and a clear message.                                                   | Official requirement | `README.md` - FR-07; `README.md` - FR-24 | An empty cart page shows an icon/illustration and a friendly/clear empty-state message.                                  | Exact icon, image, and message text are unspecified.                                                        | A visible graphic/icon plus human-readable empty-state text satisfies the rule.                                   |
| FR07-R07 | After clicking `Thêm vào giỏ`, there must be visual feedback such as toast or badge update.                 | Official requirement | `README.md` - FR-06; `README.md` - FR-24 | Add-to-cart action causes a visible toast/notification or cart badge update.                                             | Exact text, duration, and animation are unspecified.                                                        | Cart badge count increase is acceptable visual feedback.                                                          |
| FR07-R08 | The navigation link `Giỏ hàng` must display a badge showing the number of products in the cart.             | Official requirement | `README.md` - FR-23                      | Navbar/cart link visibly displays a numeric cart badge.                                                                  | Whether badge counts distinct lines or total quantity is unspecified.                                       | It must be numeric and visibly change when cart content changes.                                                  |
| FR07-R09 | Breadcrumb is mandatory on child pages including the cart page.                                             | Official requirement | `README.md` - FR-23                      | Cart page displays breadcrumb/navigation path context.                                                                   | Exact breadcrumb labels are unspecified.                                                                    | A visible breadcrumb/path indicator including cart context satisfies the rule.                                    |
| FR07-R10 | Cart quantity can be adjusted with `+` and `-` buttons.                                                     | Official requirement | `README.md` - FR-07                      | Non-empty cart item has visible plus and minus controls that increase/decrease quantity.                                 | Behaviour at quantity 1 is unspecified: decrement may be disabled, ignored, or require remove confirmation. | For quantity greater than 1, minus should decrease by one without making quantity invalid.                        |
| FR07-R11 | Cart line total (`Thành tiền`) is based on unit price and quantity.                                         | Official requirement | `README.md` - FR-07                      | For a cart line, displayed line total equals unit price multiplied by quantity.                                          | Currency formatting and rounding rules are unspecified.                                                     | Numeric comparison may normalize currency symbols, thousands separators, and whitespace.                          |

## Supporting Setup Rule

| Rule ID      | Rule                                                                               | Test Basis Type              | Test Basis Reference | Observable Expected Behaviour                                                                               | Ambiguity                                            | Assumption                                                                                           |
| ------------ | ---------------------------------------------------------------------------------- | ---------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| FR07-SETUP01 | Product detail add-to-cart quantity accepts only positive integers with minimum 1. | Supporting setup requirement | `README.md` - FR-06  | Add-to-cart setup rejects 0, negative, decimal, non-numeric, and empty values; quantity 1 or more is valid. | Maximum quantity and stock handling are unspecified. | Used only to prepare cart states for FR-07 testing, not as a standalone FR-07 cart-page requirement. |

## API Specification Rules

| Rule ID    | Rule                                                                          | Test Basis Type   | Test Basis Reference                                      | Observable Expected Behaviour                                                                                         | Ambiguity                                                                                           | Assumption                                                                                                                                        |
| ---------- | ----------------------------------------------------------------------------- | ----------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| FR07-API01 | Cart API requires `Authorization: Bearer <token>`.                            | API specification | `api_specification.md` - Cart & Orders header requirement | Authenticated cart requests include bearer token; unauthenticated requests are rejected or do not expose a cart.      | Exact unauthorized status/body is unspecified.                                                      | Any non-successful/no-cart response without token is acceptable rejection.                                                                        |
| FR07-API02 | `GET /api/cart` retrieves the cart.                                           | API specification | `api_specification.md` - 4.1 `GET /api/cart`              | Authenticated GET returns the user's cart data.                                                                       | Exact status code and response schema are unspecified.                                              | A successful JSON response representing cart content satisfies the contract.                                                                      |
| FR07-API03 | `POST /api/cart` adds an item to cart.                                        | API specification | `api_specification.md` - 4.2 `POST /api/cart`             | Authenticated POST with `id`, `name`, `price`, and `quantity` adds the item to the cart or returns updated cart data. | Exact status code, response body, duplicate merge semantics, and validation errors are unspecified. | The POST body properties in the API contract define the nominal successful request shape.                                                         |
| FR07-API04 | `POST /api/cart` request body contains `id`, `name`, `price`, and `quantity`. | API specification | `api_specification.md` - 4.2 `POST /api/cart` body JSON   | Request body with all documented properties is a valid contract shape.                                                | Required-vs-optional status is not explicitly stated, but body contract lists all properties.       | Missing-property requests are treated as outside the documented successful `POST /api/cart` contract; exact rejection status/body is unspecified. |

## Shared Navigation / Feedback Rules

| Rule ID   | Rule                                                 | Test Basis Type      | Test Basis Reference | Observable Expected Behaviour                                         | Ambiguity                                                  | Assumption                                                    |
| --------- | ---------------------------------------------------- | -------------------- | -------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------- |
| FR07-SH01 | Navbar highlights the selected page.                 | Official requirement | `README.md` - FR-23  | On `/cart`, the cart navigation item is visibly selected/highlighted. | Exact highlight style is unspecified.                      | Active CSS/visual distinction is observable.                  |
| FR07-SH02 | Cart badge shared navigation rule supports FR07-R08. | Official requirement | `README.md` - FR-23  | Covered through FR07-R08.                                             | Badge count semantics remain unspecified.                  | No separate test case is created to avoid duplicate coverage. |
| FR07-SH03 | Add-to-cart feedback shared rule supports FR07-R07.  | Official requirement | `README.md` - FR-24  | Covered through FR07-R07.                                             | Exact toast text, duration, and animation are unspecified. | No separate test case is created to avoid duplicate coverage. |
| FR07-SH04 | Delete confirmation shared rule supports FR07-R03.   | Official requirement | `README.md` - FR-24  | Covered through FR07-R03.                                             | Dialog implementation is unspecified.                      | No separate test case is created to avoid duplicate coverage. |
| FR07-SH05 | Empty-state shared rule supports FR07-R06.           | Official requirement | `README.md` - FR-24  | Covered through FR07-R06.                                             | Exact icon, illustration, and message are unspecified.     | No separate test case is created to avoid duplicate coverage. |

## Requirement Ambiguities

- Exact cart URL is not specified; `/cart` is assumed from application navigation and prior project convention.
- Authentication requirement for UI cart is not explicitly stated; API cart explicitly requires bearer token.
- Exact cart API success status and response schema are unspecified.
- Exact invalid API status/body for missing properties or unauthorized requests is unspecified.
- Whether cart badge counts distinct products or total quantities is unspecified.
- Maximum quantity, stock limits, and price precision are unspecified.
- Behaviour of the `-` button at quantity `1` is unspecified.
- Exact empty-state message and required illustration type are unspecified.
- Exact delete confirmation dialog text is unspecified.
- Whether cart contents persist across sessions/devices is unspecified.
- Product-detail quantity validation belongs to FR-06 and is used only as setup support for FR-07 cart-state preparation.

## Assumptions

- FR-07 is tested on EShop User Web plus the public cart API.
- A known authenticated user can be obtained through public login.
- Public product add-to-cart controls are acceptable setup for UI cart tests.
- The same product added twice with quantity 1 should result in one cart line with quantity 2.
- Numeric price checks normalize currency symbols, thousands separators, and whitespace.
- For BVA, the documented product quantity minimum of 1 from FR-06 applies only to add-to-cart setup for cart behaviour.

## Coverage Gaps

- No maximum cart quantity boundary is tested because no maximum is specified.
- No stock availability boundary is tested because no stock rule is specified.
- No exact cart API response schema is asserted beyond public success/cart observability because the API spec omits details.
- No exact unauthorized API status/message is asserted because the API spec only states the bearer-token header requirement.
- Checkout effects on cart clearing belong to FR-08 and are excluded from FR-07.

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-26 15:47 GMT+7
- Review Scope: FR-07 Requirement Analysis and Black-box Test Basis
- Human Review Status: Completed
- Approved for Domain Modeling: Yes
- Approved for BVA: Yes
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes
