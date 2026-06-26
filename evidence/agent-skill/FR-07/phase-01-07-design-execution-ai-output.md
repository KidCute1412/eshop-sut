# FR-07 Phase 1-7 Design and Execution - Complete AI Output

- Feature: FR-07 Shopping Cart
- Generated/compiled: 2026-06-26
- Purpose: Preserve all AI-produced phase outputs for FR-07 in one audit artifact.
- Integrity note: This file is a compiled copy of the outputs listed below; source reports remain in `reports/FR-07/`.

## Included Outputs

- Prompt: `evidence/agent-skill/FR-07/phase-01-07-design-execution-prompt.md`
- Phase 1-2: `reports/FR-07/requirement-analysis.md`
- Phase 3: `reports/FR-07/domain-testing.md`
- Phase 4: `reports/FR-07/boundary-value-analysis.md`
- Phase 5-7: `reports/FR-07/test-cases.md`
- Phase 6-7: `reports/FR-07/execution-summary.md`
- Phase 7: `reports/FR-07/bug-report.md`
- Phase 7: `reports/FR-07/evidence/evidence-index.md`
- Traceability: `reports/FR-07/traceability-matrix.md`
- Phase 8 Placeholder: `reports/FR-07/ai-gap-analysis.md`

---

## Prompt Used

Source: `evidence/agent-skill/FR-07/phase-01-07-design-execution-prompt.md`

# FR-07 Design and Execution Prompt

User request:

> Bây giờ hãy làm tương tự cho FR07 shopping cart như FR02 và FR01. Tuy nhiên, sau khi xong từ phase 1 đến phase 5 hãy thực thi và chụp kết quả lại trong test-cases.md và đưa ra là pass hay fail

Interpreted scope:

- Use the `domain-testing-bva` skill.
- Complete FR-07 Phase 1 through Phase 5 from approved black-box bases.
- Execute the derived FR-07 test cases through public UI/API only.
- Capture real evidence screenshots.
- Update `reports/FR-07/test-cases.md` with actual result, status, and evidence for each case.
- Do not inspect implementation source, database schema, internal tests, controllers, services, routes, middleware, or models.

---

## Phase 1-2 Output - Requirement Analysis

Source: `reports/FR-07/requirement-analysis.md`

# Requirement Analysis - FR-07 Shopping Cart

## Feature Intake

| Field | Value |
| ----- | ----- |
| Feature ID | FR-07 |
| Feature name | Shopping Cart / Giỏ hàng |
| Pool | B - Shopping Cart and Checkout |
| Actor | Authenticated shopper / customer using EShop User Web and public cart API |
| Application surface | EShop User Web cart/product pages and public cart API |
| UI locations | Product listing/detail add-to-cart flow; `/cart` shopping cart page |
| API endpoints | `GET /api/cart`, `POST /api/cart` |
| Output root | `reports/FR-07` |

## Approved Black-box Test Bases

- `2026.HW02.Domain Testing_En.pdf` - Pool B identifies FR-07 as Shopping Cart.
- `README.md` - FR-07 Shopping Cart.
- `README.md` - FR-06 Product Detail add-to-cart quantity rule where relevant to adding products to cart.
- `README.md` - FR-23 Navigation Requirements that apply to the cart page and cart badge.
- `README.md` - FR-24 Feedback & State Requirements that apply to add-to-cart feedback, delete confirmation, and empty state.
- `api_specification.md` - Cart & Orders, `GET /api/cart`, `POST /api/cart`, and `Authorization: Bearer <token>` header requirement.
- `setup_guide.md` - public startup guidance only.
- Public UI/API observations captured only during execution are evidence, not implementation-derived expected results.

## Requirement Rules

| Rule ID | Rule | Test Basis Type | Test Basis Reference | Observable Expected Behaviour | Ambiguity | Assumption |
| ------- | ---- | --------------- | -------------------- | ----------------------------- | --------- | ---------- |
| FR07-R01 | The cart displays a product list with columns: `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, `Thao tác`. | Official requirement | `README.md` - FR-07 | A non-empty cart page visibly presents those columns or equivalent labels. | Exact table structure and responsive layout are unspecified. | Visible column/header text is sufficient observable evidence. |
| FR07-R02 | Adding the same product to the cart increases quantity instead of creating a new line. | Official requirement | `README.md` - FR-07 | After adding the same product twice, the cart shows one line for that product with increased quantity. | Whether quantity increases by 1 or by the entered add quantity depends on input quantity. | For one-unit add actions, expected quantity increases from 1 to 2. |
| FR07-R03 | The remove product button must show a confirmation dialog before removal. | Official requirement | `README.md` - FR-07; `README.md` - FR-24 | Attempting to remove a cart item displays a confirmation dialog before the item is removed. | Exact dialog text and browser-native vs custom modal are unspecified. | Any observable confirmation requiring user choice satisfies the dialog requirement. |
| FR07-R04 | The cart has a `Tiếp tục mua sắm` button to return to the home page. | Official requirement | `README.md` - FR-07 | The cart page provides a visible continue-shopping action and activates navigation back to home. | Exact home URL is unspecified. | Navigating away from `/cart` to the public home/product area is acceptable. |
| FR07-R05 | The total label must be exactly `Tổng cộng`, not `Tổng tạm tính`. | Official requirement | `README.md` - FR-07 | The cart total area uses the exact label `Tổng cộng`; it does not use `Tổng tạm tính`. | Capitalization/diacritics are expected exactly as documented. | The visible label is the oracle; amount formatting is separate unless obviously inconsistent. |
| FR07-R06 | Empty cart must have an illustration and a clear message. | Official requirement | `README.md` - FR-07; `README.md` - FR-24 | An empty cart page shows an icon/illustration and a friendly/clear empty-state message. | Exact icon, image, and message text are unspecified. | A visible graphic/icon plus human-readable empty-state text satisfies the rule. |
| FR07-R07 | The product detail quantity input accepts only positive integers with minimum 1. | Official requirement | `README.md` - FR-06 | Add-to-cart quantity input rejects 0, negative, decimal, non-numeric, and empty values; quantity 1 or more is valid. | Maximum quantity and stock handling are unspecified. | This applies to adding products into the cart from product detail because FR-06 explicitly covers the add-to-cart quantity control. |
| FR07-R08 | After clicking `Thêm vào giỏ`, there must be visual feedback such as toast or badge update. | Official requirement | `README.md` - FR-06; `README.md` - FR-24 | Add-to-cart action causes a visible toast/notification or cart badge update. | Exact text, duration, and animation are unspecified. | Cart badge count increase is acceptable visual feedback. |
| FR07-R09 | The navigation link `Giỏ hàng` must display a badge showing the number of products in the cart. | Official requirement | `README.md` - FR-23 | Navbar/cart link visibly displays a numeric cart badge. | Whether badge counts distinct lines or total quantity is unspecified. | It must be numeric and visibly change when cart content changes. |
| FR07-R10 | Breadcrumb is mandatory on child pages including the cart page. | Official requirement | `README.md` - FR-23 | Cart page displays breadcrumb/navigation path context. | Exact breadcrumb labels are unspecified. | A visible breadcrumb/path indicator including cart context satisfies the rule. |
| FR07-R11 | Cart quantity can be adjusted with `+` and `-` buttons. | Official requirement | `README.md` - FR-07 | Non-empty cart item has visible plus and minus controls that increase/decrease quantity. | Behaviour at quantity 1 is unspecified: decrement may be disabled, ignored, or require remove confirmation. | For quantity greater than 1, minus should decrease by one without making quantity invalid. |
| FR07-R12 | Cart line total (`Thành tiền`) is based on unit price and quantity. | Official requirement | `README.md` - FR-07 | For a cart line, displayed line total equals unit price multiplied by quantity. | Currency formatting and rounding rules are unspecified. | Numeric comparison may normalize punctuation/currency formatting. |

## API Specification Rules

| Rule ID | Rule | Test Basis Type | Test Basis Reference | Observable Expected Behaviour | Ambiguity | Assumption |
| ------- | ---- | --------------- | -------------------- | ----------------------------- | --------- | ---------- |
| FR07-API01 | Cart API requires `Authorization: Bearer <token>`. | API specification | `api_specification.md` - Cart & Orders header requirement | Authenticated cart requests include bearer token; unauthenticated requests are rejected or do not expose a cart. | Exact unauthorized status/body is unspecified. | Any non-successful/no-cart response without token is acceptable rejection. |
| FR07-API02 | `GET /api/cart` retrieves the cart. | API specification | `api_specification.md` - 4.1 `GET /api/cart` | Authenticated GET returns the user's cart data. | Exact status code and response schema are unspecified. | A successful JSON response representing cart content satisfies the contract. |
| FR07-API03 | `POST /api/cart` adds an item to cart. | API specification | `api_specification.md` - 4.2 `POST /api/cart` | Authenticated POST with `id`, `name`, `price`, and `quantity` adds the item to the cart or returns updated cart data. | Exact status code, response body, duplicate merge semantics, and validation errors are unspecified. | The POST body properties in the API contract are required for the nominal request. |
| FR07-API04 | `POST /api/cart` request body contains `id`, `name`, `price`, and `quantity`. | API specification | `api_specification.md` - 4.2 `POST /api/cart` body JSON | Request body with all documented properties is a valid contract shape. | Required-vs-optional status is not explicitly stated, but body contract lists all properties. | Missing documented properties are invalid contract input, though exact error is unspecified. |

## Shared Form / Navigation / Feedback Rules

| Rule ID | Rule | Test Basis Type | Test Basis Reference | Observable Expected Behaviour | Ambiguity | Assumption |
| ------- | ---- | --------------- | -------------------- | ----------------------------- | --------- | ---------- |
| FR07-SH01 | Navbar highlights the selected page. | Official requirement | `README.md` - FR-23 | On `/cart`, the cart navigation item is visibly selected/highlighted. | Exact highlight style is unspecified. | Active CSS/visual distinction is observable. |
| FR07-SH02 | Cart badge displays product count. | Official requirement | `README.md` - FR-23 | Navbar cart link displays a visible numeric badge. | Distinct-product count vs total quantity is unspecified. | Numeric badge should increase when a product is added. |
| FR07-SH03 | Add-to-cart feedback is visual. | Official requirement | `README.md` - FR-24 | A toast or badge update appears after add-to-cart. | Exact toast text is unspecified. | Badge update is enough if no toast appears. |
| FR07-SH04 | Delete item requires confirmation. | Official requirement | `README.md` - FR-24 | Delete action prompts for confirmation before actual removal. | Dialog implementation is unspecified. | Browser confirm or modal both qualify. |
| FR07-SH05 | Empty state has icon/illustration and friendly message. | Official requirement | `README.md` - FR-24 | Empty cart displays both a visual and message. | Exact content is unspecified. | Emoji/icon/image counts as an illustration if visibly present. |

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

## Assumptions

- FR-07 is tested on EShop User Web plus the public cart API.
- A known authenticated user can be obtained through public login.
- Public product add-to-cart controls are acceptable setup for UI cart tests.
- The same product added twice with quantity 1 should result in one cart line with quantity 2.
- Numeric price checks normalize currency symbols, thousands separators, and whitespace.
- For BVA, the documented product quantity minimum of 1 from FR-06 applies to add-to-cart setup for cart behaviour.

## Coverage Gaps

- No maximum cart quantity boundary is tested because no maximum is specified.
- No stock availability boundary is tested because no stock rule is specified.
- No exact cart API response schema is asserted beyond public success/cart observability because the API spec omits details.
- No exact unauthorized API status/message is asserted because the API spec only states the bearer-token header requirement.
- Checkout effects on cart clearing belong to FR-08 and are excluded from FR-07.

## Human Review

- Reviewer: User request authorized execution after Phase 1-5
- Review Date and Time: 2026-06-26
- Status: Completed for AI-assisted execution
- Approved for Domain Modeling: Yes
- Approved for BVA: Yes
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes

---

## Phase 3 Output - Domain Testing

Source: `reports/FR-07/domain-testing.md`

# Domain Testing - FR-07 Shopping Cart

## Black-box Test Basis Summary

This domain model is based only on `reports/FR-07/requirement-analysis.md`, which records approved black-box bases from the assignment PDF, README requirements, API specification, setup guidance, and later public UI/API execution evidence. No application implementation source, database schema, internal tests, controllers, services, routes, middleware, or models are used as expected-result oracles.

## Step 1. Identify Input & Output Variables

| Type | Variable or Output | Description | Related Rule IDs | Applies To |
| ---- | ------------------ | ----------- | ---------------- | ---------- |
| State / Condition | Authenticated user state | User has a valid bearer token/session for cart API and UI cart actions. | FR07-API01 | UI/API |
| State / Condition | Empty cart state | Cart contains no items. | FR07-R06, FR07-SH05 | UI/API |
| State / Condition | Non-empty cart state | Cart contains at least one item. | FR07-R01, FR07-R11, FR07-R12 | UI/API |
| Input | Product identity | Product selected for add-to-cart. | FR07-R02, FR07-API03, FR07-API04 | UI/API |
| Input | Product name | Name property in API body and visible cart product name. | FR07-R01, FR07-API04 | UI/API |
| Input | Unit price | Price property used for unit price and line total. | FR07-R01, FR07-R12, FR07-API04 | UI/API |
| Input | Add quantity | Quantity entered or sent when adding item to cart. | FR07-R07, FR07-API04 | UI/API |
| Input | Duplicate add action | Same product added more than once. | FR07-R02 | UI/API |
| Input | Plus control action | User increments item quantity. | FR07-R11 | UI |
| Input | Minus control action | User decrements item quantity. | FR07-R11 | UI |
| Input | Delete action | User requests item removal. | FR07-R03, FR07-SH04 | UI |
| Input | Delete confirmation decision | User confirms or cancels deletion. | FR07-R03, FR07-SH04 | UI |
| Output | Cart table/list columns | Product, unit price, quantity, line total, action columns. | FR07-R01 | UI |
| Output | Duplicate-merge result | One cart row with increased quantity, not duplicate rows. | FR07-R02 | UI/API |
| Output | Continue shopping navigation | Button returns user to home/public shopping area. | FR07-R04 | UI |
| Output | Total label | Total label text exactly `Tổng cộng`. | FR07-R05 | UI |
| Output | Empty-state message/illustration | Empty cart visual and clear message. | FR07-R06, FR07-SH05 | UI |
| Output | Add-to-cart feedback | Toast or badge update. | FR07-R08, FR07-SH03 | UI |
| Output | Navbar cart badge | Numeric badge on `Giỏ hàng` link. | FR07-R09, FR07-SH02 | UI |
| Output | Breadcrumb | Breadcrumb/path on cart child page. | FR07-R10 | UI |
| Output | Navbar active highlight | Cart navigation item highlighted on cart page. | FR07-SH01 | UI |
| API Contract | GET cart response | Public authenticated cart retrieval. | FR07-API02 | API |
| API Contract | POST cart request/response | Public authenticated add-to-cart request. | FR07-API03, FR07-API04 | API |
| Output | Unauthorized API rejection | Cart API without bearer token is rejected or does not expose a cart. | FR07-API01 | API |

## Step 2. Identify Equivalence Classes

| Partition ID | Type | Variable or Condition | Equivalence Class Description | Validity | Representative Value | Dependencies | Rule IDs | Test Basis Reference | Assumptions |
| ------------ | ---- | --------------------- | ----------------------------- | -------- | -------------------- | ------------ | -------- | -------------------- | ----------- |
| AUTH-V01 | State / Condition | Authenticated state | User has valid token/session. | Valid | `test@eshop.com` login token | User exists and login works. | FR07-API01 | `api_specification.md` Cart header requirement | Existing test account available. |
| AUTH-I01 | State / Condition | Authenticated state | No bearer token for cart API. | Invalid | Omit Authorization header | API reachable. | FR07-API01 | `api_specification.md` Cart header requirement | Exact status unspecified. |
| CART-EMPTY-V01 | State / Condition | Empty cart | Cart has no items. | Valid | Fresh/cleared cart | Cart can be emptied via UI setup. | FR07-R06 | `README.md` - FR-07 | Empty state observable through UI. |
| CART-NONEMPTY-V01 | State / Condition | Non-empty cart | Cart has one or more items. | Valid | One product in cart | Add-to-cart available. | FR07-R01 | `README.md` - FR-07 | Product data exists publicly. |
| CART-COLUMNS-V01 | Output | Cart list columns | Required columns are visible. | Valid | `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, `Thao tác` | Non-empty cart. | FR07-R01 | `README.md` - FR-07 | Equivalent visible labels accepted. |
| PRODUCT-ID-V01 | Input | Product identity | Existing public product. | Valid | Product id `1` / first visible product | Product exists. | FR07-API03 | `api_specification.md` - POST `/api/cart` | Exact product catalog may vary. |
| PRODUCT-ID-I01 | Input | Product identity | Missing product id in API body. | Invalid | Body without `id` | Auth token. | FR07-API04 | `api_specification.md` - POST body | Exact error unspecified. |
| QUANTITY-V01 | Input | Add quantity | Positive integer quantity. | Valid | `1` | Product selected. | FR07-R07, FR07-API04 | `README.md` - FR-06; API body | Minimum 1 applies to add-to-cart. |
| QUANTITY-I01 | Input | Add quantity | Quantity less than 1. | Invalid | `0` | Product selected. | FR07-R07 | `README.md` - FR-06 | Exact browser validation text unspecified. |
| QUANTITY-I02 | Input | Add quantity | Non-integer quantity. | Invalid | `1.5` | Product selected. | FR07-R07 | `README.md` - FR-06 | Number precision behaviour unspecified. |
| DUPLICATE-ADD-V01 | State / Condition | Duplicate add | Same product added twice merges into one line with increased quantity. | Valid | Add product A twice | Cart starts empty or known. | FR07-R02 | `README.md` - FR-07 | Two one-unit adds yield quantity 2. |
| PLUS-V01 | Input | Plus action | Plus increases quantity. | Valid | Click `+` on quantity 1 | Non-empty cart. | FR07-R11 | `README.md` - FR-07 | Plus increments by one. |
| MINUS-V01 | Input | Minus action | Minus decreases quantity above minimum. | Valid | Click `-` on quantity 2 | Non-empty cart quantity > 1. | FR07-R11 | `README.md` - FR-07 | Quantity should remain positive. |
| DELETE-CANCEL-V01 | Input | Delete confirmation | Canceling confirmation preserves item. | Valid | Click delete, cancel dialog | Delete dialog appears. | FR07-R03 | `README.md` - FR-07 | Cancel option is available. |
| DELETE-CONFIRM-V01 | Input | Delete confirmation | Confirming deletion removes item. | Valid | Click delete, confirm dialog | Delete dialog appears. | FR07-R03 | `README.md` - FR-07 | Item removal observable. |
| CONTINUE-V01 | Output | Continue shopping | Continue-shopping button navigates home/shopping area. | Valid | Click `Tiếp tục mua sắm` | Cart page open. | FR07-R04 | `README.md` - FR-07 | Exact home URL unspecified. |
| TOTAL-LABEL-V01 | Output | Total label | Label is exactly `Tổng cộng`. | Valid | Visible text `Tổng cộng` | Cart page open. | FR07-R05 | `README.md` - FR-07 | Diacritics required. |
| TOTAL-LABEL-I01 | Output | Total label | Label incorrectly says `Tổng tạm tính`. | Invalid | Visible text `Tổng tạm tính` | Cart page open. | FR07-R05 | `README.md` - FR-07 | Other wrong labels also invalid. |
| EMPTY-STATE-V01 | Output | Empty state | Empty cart has illustration/icon and clear message. | Valid | Empty cart page | Cart empty. | FR07-R06, FR07-SH05 | `README.md` - FR-07/FR-24 | Exact message unspecified. |
| FEEDBACK-V01 | Output | Add-to-cart feedback | Toast or badge update appears. | Valid | Badge count changes | Add action succeeds. | FR07-R08, FR07-SH03 | `README.md` - FR-06/FR-24 | Badge update enough. |
| BADGE-V01 | Output | Navbar badge | Cart link displays numeric badge count. | Valid | Badge `1` or higher | Cart state known. | FR07-R09, FR07-SH02 | `README.md` - FR-23 | Count semantics ambiguous. |
| BREADCRUMB-V01 | Output | Breadcrumb | Cart page has breadcrumb/path. | Valid | Breadcrumb includes cart context | Cart page open. | FR07-R10 | `README.md` - FR-23 | Exact labels unspecified. |
| NAV-HIGHLIGHT-V01 | Output | Navbar highlight | Cart nav item visibly active on cart page. | Valid | Active/highlight class or style | Cart page open. | FR07-SH01 | `README.md` - FR-23 | Exact style unspecified. |
| API-GET-V01 | API Contract | GET cart | Authenticated GET returns cart data. | Valid | `GET /api/cart` with token | Auth token. | FR07-API02 | `api_specification.md` - GET `/api/cart` | Schema unspecified. |
| API-POST-V01 | API Contract | POST cart | Authenticated POST with documented body adds item. | Valid | `{id:1,name:"Sản phẩm A",price:100000,quantity:2}` | Auth token. | FR07-API03/04 | `api_specification.md` - POST `/api/cart` | Exact response unspecified. |
| API-POST-I01 | API Contract | POST cart | Missing documented request property. | Invalid | Body without `quantity` | Auth token. | FR07-API04 | `api_specification.md` - POST body | Exact error unspecified. |

## Step 3. Best Representatives

| Partition ID | Representative Value | Why This Representative Was Chosen | Required Nominal Values for Other Variables | Applies To |
| ------------ | -------------------- | ---------------------------------- | ------------------------------------------- | ---------- |
| AUTH-V01 | Login as `test@eshop.com` / `Test1234!` | Existing public test user used in prior feature execution. | API and UI reachable. | UI/API |
| AUTH-I01 | No Authorization header | Isolates missing bearer-token condition. | No body validation target. | API |
| CART-EMPTY-V01 | `/cart` after deleting all visible items | Creates observable empty state. | Auth/session valid if required. | UI |
| CART-NONEMPTY-V01 | One first public product in cart | Minimal non-empty state for list/columns. | Product and cart available. | UI/API |
| CART-COLUMNS-V01 | One visible cart row | Columns become observable only with non-empty cart. | Cart has item. | UI |
| PRODUCT-ID-V01 | First visible product / API id `1` | Nominal documented product id example. | Name, price, quantity valid. | UI/API |
| PRODUCT-ID-I01 | API body missing `id` | Isolates missing id property. | Other body fields valid. | API |
| QUANTITY-V01 | `1` | Minimum valid positive integer. | Product selected. | UI/API |
| QUANTITY-I01 | `0` | Immediately below minimum. | Product selected. | UI |
| QUANTITY-I02 | `1.5` | Representative non-integer. | Product selected. | UI |
| DUPLICATE-ADD-V01 | Add same product twice with quantity 1 | Directly exercises duplicate merge rule. | Cart starts empty/known. | UI/API |
| PLUS-V01 | Click `+` from quantity 1 | Minimal increment state. | One item in cart. | UI |
| MINUS-V01 | Click `-` from quantity 2 | Avoids ambiguous minimum-at-1 behaviour. | Quantity starts at 2. | UI |
| DELETE-CANCEL-V01 | Click remove then Cancel | Confirms dialog exists and cancel preserves item. | One item in cart. | UI |
| DELETE-CONFIRM-V01 | Click remove then OK/Confirm | Confirms actual removal path. | One item in cart. | UI |
| CONTINUE-V01 | Click `Tiếp tục mua sắm` | Directly maps to rule label. | Cart page open. | UI |
| TOTAL-LABEL-V01 | Visible `Tổng cộng` | Exact required label. | Cart page open. | UI |
| TOTAL-LABEL-I01 | Visible `Tổng tạm tính` | Explicit forbidden label. | Cart page open. | UI |
| EMPTY-STATE-V01 | Empty cart page text + icon/image | Directly observable empty-state rule. | Cart empty. | UI |
| FEEDBACK-V01 | Badge count changes after add | Allowed visual feedback type. | Navbar badge visible. | UI |
| BADGE-V01 | Numeric badge on `Giỏ hàng` | Direct navigation rule. | Cart state known. | UI |
| BREADCRUMB-V01 | Breadcrumb text/path on `/cart` | Direct child-page rule. | Cart page open. | UI |
| NAV-HIGHLIGHT-V01 | Highlighted cart nav item | Direct navigation rule. | Cart page open. | UI |
| API-GET-V01 | Authenticated `GET /api/cart` | Nominal cart retrieval. | Token valid. | API |
| API-POST-V01 | Authenticated `POST /api/cart` with all documented fields | Nominal add item contract. | Token valid. | API |
| API-POST-I01 | Authenticated `POST /api/cart` without `quantity` | Isolates missing property. | Token valid, other fields valid. | API |

## Partition Derivation

Each partition above is derived from a documented FR-07 cart rule, related FR-06 add-to-cart quantity rule, shared navigation/feedback rules, or the public cart API contract. Valid partitions describe behaviour the requirements explicitly require. Invalid partitions are limited to documented exclusions such as missing bearer token, missing contract property, invalid quantity below the positive integer minimum, non-integer quantity, or forbidden total label text. Ambiguous behaviours such as maximum quantity, stock limits, exact message text, exact unauthorized status, and exact badge-count semantics are excluded from normative coverage.

## Coverage Decisions

- Normative UI coverage includes cart list columns, duplicate add merge, plus/minus adjustment, delete confirmation, continue shopping, total label, empty state, add feedback, badge, breadcrumb, and nav highlight.
- Normative API coverage includes authenticated `GET /api/cart`, authenticated `POST /api/cart`, missing token rejection, and missing documented body property rejection.
- Quantity BVA is included for the documented minimum `1` from the add-to-cart quantity rule.
- Maximum quantity, stock limits, persistence, exact API schemas/statuses, and checkout cart clearing are excluded because they are unsupported or belong to other features.

## Human Review - Phase 3

- Reviewer: User request authorized end-to-end execution
- Review Date and Time: 2026-06-26
- Corrections Made: None before execution
- Missing Partitions Added: None
- Duplicate Partitions Removed: None
- Status: Completed
- Approved for BVA: Yes
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes

---

## Phase 4 Output - Boundary Value Analysis

Source: `reports/FR-07/boundary-value-analysis.md`

# Boundary Value Analysis - FR-07 Shopping Cart

## Scope

BVA is applied only to the ordered/bounded add-to-cart quantity domain. The documented lower bound is a positive integer with minimum `1` from the product detail add-to-cart quantity rule that feeds the shopping cart. No maximum quantity, stock limit, cart capacity, or price precision boundary is specified, so no upper-bound BVA is created.

## Boundary Values

| Boundary ID | Variable | Rule | Test Basis | Test Basis Reference | Boundary Type | On Point | Off Point | In Point | Selected Value | Expected Classification | Justification |
| ----------- | -------- | ---- | ---------- | -------------------- | ------------- | -------- | --------- | -------- | -------------- | ----------------------- | ------------- |
| FR07-QTY-MIN-B01 | Add-to-cart quantity | Quantity must be a positive integer, minimum 1. | Official requirement | `README.md` - FR-06 | Lower-only inclusive minimum | 1 | 0 | 2 | 0 | Invalid | `0` is immediately below the minimum positive integer. |
| FR07-QTY-MIN-B02 | Add-to-cart quantity | Quantity must be a positive integer, minimum 1. | Official requirement | `README.md` - FR-06 | Lower-only inclusive minimum | 1 | 0 | 2 | 1 | Valid | `1` is the inclusive on-point minimum. |
| FR07-QTY-MIN-B03 | Add-to-cart quantity | Quantity must be a positive integer, minimum 1. | Official requirement | `README.md` - FR-06 | Lower-only inclusive minimum | 1 | 0 | 2 | 2 | Valid | `2` is the adjacent valid in-point above the minimum. |

## Non-BVA Domains

- Product identity, delete confirmation, badge visibility, breadcrumbs, labels, and API authorization are categorical, not numeric/ordered boundaries.
- Duplicate add is a count/state relationship, but the requirement only distinguishes same-product duplicate merge; it does not define a broader numeric range.
- Cart line count, maximum cart quantity, stock, and API response status ranges are unspecified.

## Coverage Decisions

- Quantity boundary tests are executed through the public UI add-to-cart flow where the quantity control is observable.
- API quantity BVA is not normative because `api_specification.md` provides a sample quantity in the POST body but does not define min/max/validation behaviour for API quantity.

## Human Review - Phase 4

- Reviewer: User request authorized end-to-end execution
- Review Date and Time: 2026-06-26
- Corrections Made: None before execution
- Missing Boundaries Added: None
- Duplicate Boundaries Removed: None
- Status: Completed
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes

---

## Phase 5 and Executed Test Case Output

Source: `reports/FR-07/test-cases.md`

# Test Cases - FR-07 Shopping Cart

## Domain Testing Test Cases

## FR07-DT-001

- Test Case ID: FR07-DT-001
- Technique: Domain Testing
- Objective: Verify empty cart UI displays a clear empty state with illustration/icon and message.
- Requirement or Rule Reference: FR07-R06, FR07-SH05
- Preconditions: EShop User Web is available; cart is empty or all visible cart items can be removed through public UI.
- Test Data: Empty cart state.
- Steps:
  1. Open `/cart`.
  2. Ensure no products remain in the cart.
  3. Observe the empty cart content.
- Expected Result: Empty cart displays an illustration/icon and a clear user-facing empty-state message. Exact message and image are unspecified.
- Actual Result: Cart page showed empty message text. Visible text included: "EShop
Giỏ hàng
Đăng nhập
Đăng ký
Giỏ hàng của bạn đang trống
Tiếp tục mua sắm
© 2026 EShop SUT. Dành cho mục đích kiểm thử.". Image/icon element count observed: 0.
- Status: Fail
- Evidence: [FR07-DT-001](./evidence/FR07-DT-001.png)
- Partition or Boundary Covered: CART-EMPTY-V01, EMPTY-STATE-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R06, FR07-SH05; `domain-testing.md` - CART-EMPTY-V01, EMPTY-STATE-V01
- Notes and Assumptions: Emoji/icon/image is acceptable as illustration if visibly present.

## FR07-DT-002

- Test Case ID: FR07-DT-002
- Technique: Domain Testing
- Objective: Verify non-empty cart displays required product list columns.
- Requirement or Rule Reference: FR07-R01
- Preconditions: EShop User Web is available; at least one product can be added to cart through public UI.
- Test Data: First visible public product with quantity 1.
- Steps:
  1. Add one product to the cart.
  2. Open `/cart`.
  3. Observe the cart product list headers/columns.
- Expected Result: Cart displays product list with columns or visible labels for `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, and `Thao tác`.
- Actual Result: After authenticated public API setup added an item, UI cart still displayed: "EShop
Giỏ hàng
Chào, Test User
Thoát
Giỏ hàng của bạn đang trống
Tiếp tục mua sắm
© 2026 EShop SUT. Dành cho mục đích kiểm thử.". Required columns observed: None.
- Status: Fail
- Evidence: [FR07-DT-002](./evidence/FR07-DT-002.png)
- Partition or Boundary Covered: CART-NONEMPTY-V01, CART-COLUMNS-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R01; `domain-testing.md` - CART-COLUMNS-V01
- Notes and Assumptions: Equivalent visible labels are accepted only if they clearly represent the documented columns.

## FR07-DT-003

- Test Case ID: FR07-DT-003
- Technique: Domain Testing
- Objective: Verify add-to-cart action gives visual feedback through toast or cart badge update.
- Requirement or Rule Reference: FR07-R08, FR07-SH03
- Preconditions: EShop User Web is available; a public product can be added to cart.
- Test Data: First visible public product; quantity 1.
- Steps:
  1. Observe current cart badge count if visible.
  2. Click `Thêm vào giỏ hàng` for a product.
  3. Observe toast/notification or cart badge update.
- Expected Result: A visual feedback is displayed after add-to-cart, such as toast notification or updated cart badge.
- Actual Result: After authenticated user clicked the first public add-to-cart button, no toast/notification was visible and no numeric cart badge appeared beside `Gi? h?ng`. The cart page remained empty after the action.
- Status: Fail
- Evidence: [FR07-DT-003](./evidence/FR07-DT-003.png)
- Partition or Boundary Covered: FEEDBACK-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R08, FR07-SH03; `domain-testing.md` - FEEDBACK-V01
- Notes and Assumptions: Badge update is accepted as visual feedback if no toast appears.

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
- Actual Result: After two add-to-cart clicks for the same product, UI cart displayed: "EShop
Giỏ hàng
Chào, Test User
Thoát
Giỏ hàng của bạn đang trống
Tiếp tục mua sắm
© 2026 EShop SUT. Dành cho mục đích kiểm thử.". No single product row with quantity 2 was visible.
- Status: Fail
- Evidence: [FR07-DT-004](./evidence/FR07-DT-004.png)
- Partition or Boundary Covered: DUPLICATE-ADD-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R02; `domain-testing.md` - DUPLICATE-ADD-V01
- Notes and Assumptions: Two one-unit add actions should result in quantity 2.

## FR07-DT-005

- Test Case ID: FR07-DT-005
- Technique: Domain Testing
- Objective: Verify plus control increases cart item quantity.
- Requirement or Rule Reference: FR07-R11
- Preconditions: Cart contains one item with quantity 1 and visible `+` control.
- Test Data: One cart item with quantity 1.
- Steps:
  1. Open `/cart` with one item.
  2. Click the item `+` quantity control.
  3. Observe the item quantity.
- Expected Result: The item quantity increases by one.
- Actual Result: After public setup with cart quantity, UI cart text was "EShop
Giỏ hàng
Chào, Test User
Thoát
Giỏ hàng của bạn đang trống
Tiếp tục mua sắm
© 2026 EShop SUT. Dành cho mục đích kiểm thử.". Visible controls were ["EShop","Giỏ hàng","Chào, Test User","Thoát","Tiếp tục mua sắm"]; no item '+' quantity control was observable.
- Status: Fail
- Evidence: [FR07-DT-005](./evidence/FR07-DT-005.png)
- Partition or Boundary Covered: PLUS-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R11; `domain-testing.md` - PLUS-V01
- Notes and Assumptions: Quantity increase by one is expected for a single plus click.

## FR07-DT-006

- Test Case ID: FR07-DT-006
- Technique: Domain Testing
- Objective: Verify minus control decreases cart item quantity when quantity is greater than 1.
- Requirement or Rule Reference: FR07-R11
- Preconditions: Cart contains one item with quantity 2 and visible `-` control.
- Test Data: One cart item with quantity 2.
- Steps:
  1. Open `/cart` with one item quantity 2.
  2. Click the item `-` quantity control.
  3. Observe the item quantity.
- Expected Result: The item quantity decreases from 2 to 1 and remains a positive quantity.
- Actual Result: After public setup with cart quantity 2, UI cart still did not display an item row or '-' quantity control. Visible text: "EShop
Giỏ hàng
Chào, Test User
Thoát
Giỏ hàng của bạn đang trống
Tiếp tục mua sắm
© 2026 EShop SUT. Dành cho mục đích kiểm thử.".
- Status: Fail
- Evidence: [FR07-DT-006](./evidence/FR07-DT-006.png)
- Partition or Boundary Covered: MINUS-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R11; `domain-testing.md` - MINUS-V01
- Notes and Assumptions: Quantity at exactly 1 is not tested here because decrement-at-minimum behaviour is ambiguous.

## FR07-DT-007

- Test Case ID: FR07-DT-007
- Technique: Domain Testing
- Objective: Verify delete action shows confirmation and canceling preserves the item.
- Requirement or Rule Reference: FR07-R03, FR07-SH04
- Preconditions: Cart contains one item and delete action is visible.
- Test Data: One visible cart item; cancel confirmation.
- Steps:
  1. Open `/cart` with one item.
  2. Click the remove/delete action.
  3. Cancel the confirmation dialog.
  4. Observe whether the item remains.
- Expected Result: A confirmation dialog appears before deletion; when canceled, the item remains in the cart.
- Actual Result: After public setup with one cart item, UI cart displayed no delete/remove action and no confirmation dialog could be triggered. Visible controls: ["EShop","Giỏ hàng","Chào, Test User","Thoát","Tiếp tục mua sắm"].
- Status: Fail
- Evidence: [FR07-DT-007](./evidence/FR07-DT-007.png)
- Partition or Boundary Covered: DELETE-CANCEL-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R03, FR07-SH04; `domain-testing.md` - DELETE-CANCEL-V01
- Notes and Assumptions: Browser-native confirm or custom dialog is acceptable.

## FR07-DT-008

- Test Case ID: FR07-DT-008
- Technique: Domain Testing
- Objective: Verify confirming delete removes the item from cart.
- Requirement or Rule Reference: FR07-R03, FR07-SH04
- Preconditions: Cart contains one item and delete action is visible.
- Test Data: One visible cart item; confirm deletion.
- Steps:
  1. Open `/cart` with one item.
  2. Click the remove/delete action.
  3. Confirm the dialog.
  4. Observe cart contents.
- Expected Result: A confirmation dialog appears before deletion; after confirmation, the item is removed from the cart.
- Actual Result: After public setup with one cart item, UI cart displayed no delete/remove action, so confirmed deletion could not remove the item through UI. Visible text: "EShop
Giỏ hàng
Chào, Test User
Thoát
Giỏ hàng của bạn đang trống
Tiếp tục mua sắm
© 2026 EShop SUT. Dành cho mục đích kiểm thử.".
- Status: Fail
- Evidence: [FR07-DT-008](./evidence/FR07-DT-008.png)
- Partition or Boundary Covered: DELETE-CONFIRM-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R03, FR07-SH04; `domain-testing.md` - DELETE-CONFIRM-V01
- Notes and Assumptions: Removal may lead to empty-cart state if it was the only item.

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
- Actual Result: Clicking `Ti?p t?c mua s?m` on `/cart` navigated to `http://localhost:5173/`. The home/product listing was visible with `Danh s?ch s?n ph?m` and public product cards.
- Status: Pass
- Evidence: [FR07-DT-009](./evidence/FR07-DT-009.png)
- Partition or Boundary Covered: CONTINUE-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R04; `domain-testing.md` - CONTINUE-V01
- Notes and Assumptions: Leaving `/cart` for home/product browsing satisfies this requirement.

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
- Actual Result: Cart page text after public item setup still showed the empty-cart message. Label `T?ng c?ng` was not visible; forbidden label `T?ng t?m t?nh` was also not visible.
- Status: Fail
- Evidence: [FR07-DT-010](./evidence/FR07-DT-010.png)
- Partition or Boundary Covered: TOTAL-LABEL-V01, TOTAL-LABEL-I01
- Test Basis Reference: `requirement-analysis.md` - FR07-R05; `domain-testing.md` - TOTAL-LABEL-V01/TOTAL-LABEL-I01
- Notes and Assumptions: Diacritics and wording are checked as visible text.

## FR07-DT-011

- Test Case ID: FR07-DT-011
- Technique: Domain Testing
- Objective: Verify navbar cart link displays numeric badge count.
- Requirement or Rule Reference: FR07-R09, FR07-SH02
- Preconditions: EShop User Web is available; cart state can be changed by adding a product.
- Test Data: Add one product to cart.
- Steps:
  1. Observe `Giỏ hàng` navigation link before add.
  2. Add one product to cart.
  3. Observe `Giỏ hàng` navigation link after add.
- Expected Result: The `Giỏ hàng` link displays a numeric badge count and the badge reflects cart content after add.
- Actual Result: After add-to-cart action, the navbar still displayed `Gi? h?ng` without a numeric badge. No visible badge count appeared or changed.
- Status: Fail
- Evidence: [FR07-DT-011](./evidence/FR07-DT-011.png)
- Partition or Boundary Covered: BADGE-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R09, FR07-SH02; `domain-testing.md` - BADGE-V01
- Notes and Assumptions: Distinct-line count vs total quantity is ambiguous; numeric visibility/change is the oracle.

## FR07-DT-012

- Test Case ID: FR07-DT-012
- Technique: Domain Testing
- Objective: Verify cart page displays breadcrumb.
- Requirement or Rule Reference: FR07-R10
- Preconditions: EShop User Web is available.
- Test Data: Open `/cart`.
- Steps:
  1. Open `/cart`.
  2. Observe breadcrumb/path indicator.
- Expected Result: Cart page displays breadcrumb/path context. Exact labels are unspecified.
- Actual Result: Cart page displayed the navbar and empty-cart content, but no breadcrumb/path indicator beyond the navbar was visible.
- Status: Fail
- Evidence: [FR07-DT-012](./evidence/FR07-DT-012.png)
- Partition or Boundary Covered: BREADCRUMB-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-R10; `domain-testing.md` - BREADCRUMB-V01
- Notes and Assumptions: Breadcrumb must be more than only the navbar link.

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
- Actual Result: On `/cart`, the `Gi? h?ng` navigation link was visible, but it used the normal navigation styling and no observable active/selected highlight was present.
- Status: Fail
- Evidence: [FR07-DT-013](./evidence/FR07-DT-013.png)
- Partition or Boundary Covered: NAV-HIGHLIGHT-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-SH01; `domain-testing.md` - NAV-HIGHLIGHT-V01
- Notes and Assumptions: Exact highlight style is unspecified.

## FR07-DT-014

- Test Case ID: FR07-DT-014
- Technique: Domain Testing
- Objective: Verify authenticated `GET /api/cart` retrieves cart data.
- Requirement or Rule Reference: FR07-API01, FR07-API02
- Preconditions: Backend API is available; valid bearer token can be obtained through public login.
- Test Data: Bearer token for `test@eshop.com`.
- Steps:
  1. Log in through public API to obtain a token.
  2. Send `GET /api/cart` with `Authorization: Bearer <token>`.
  3. Observe status and JSON response.
- Expected Result: Authenticated `GET /api/cart` succeeds and returns cart data. Exact response schema is unspecified.
- Actual Result: Authenticated GET /api/cart for fr07.dt014.1782462973956@example.com returned HTTP 200 with JSON body [].
- Status: Pass
- Evidence: [FR07-DT-014](./evidence/FR07-DT-014.png)
- Partition or Boundary Covered: AUTH-V01, API-GET-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-API01, FR07-API02; `domain-testing.md` - API-GET-V01
- Notes and Assumptions: JSON array or object representing cart content is accepted.

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
- Actual Result: GET /api/cart without Authorization returned HTTP 401 and body {"error": "Unauthorized"}.
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
- Actual Result: Authenticated POST /api/cart returned HTTP 200 with body {"message": "Added to cart"}. Follow-up GET returned [{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 2}].
- Status: Pass
- Evidence: [FR07-DT-016](./evidence/FR07-DT-016.png)
- Partition or Boundary Covered: API-POST-V01, PRODUCT-ID-V01
- Test Basis Reference: `requirement-analysis.md` - FR07-API01, FR07-API03, FR07-API04; `domain-testing.md` - API-POST-V01
- Notes and Assumptions: If response body does not include cart, follow-up GET may confirm public cart state.

## FR07-DT-017

- Test Case ID: FR07-DT-017
- Technique: Domain Testing
- Objective: Verify `POST /api/cart` missing a documented body property is rejected or does not add invalid item.
- Requirement or Rule Reference: FR07-API04
- Preconditions: Backend API is available; valid bearer token can be obtained through public login.
- Test Data: `{"id":1,"name":"Sản phẩm A","price":100000}` missing `quantity`.
- Steps:
  1. Log in through public API to obtain a token.
  2. Send `POST /api/cart` with Authorization header and body missing `quantity`.
  3. Observe status and response body.
- Expected Result: The invalid contract-shape request is rejected or does not add an item with missing quantity. Exact status and error message are unspecified.
- Actual Result: POST /api/cart missing quantity returned HTTP 200 with body {"message": "Added to cart"}. Follow-up GET showed [{"id": 2, "name": "Samsung Galaxy S24 Ultra", "price": 28000000}].
- Status: Fail
- Evidence: [FR07-DT-017](./evidence/FR07-DT-017.png)
- Partition or Boundary Covered: API-POST-I01
- Test Basis Reference: `requirement-analysis.md` - FR07-API04; `domain-testing.md` - API-POST-I01
- Notes and Assumptions: This checks documented body property presence, not hidden validation internals.

## Boundary Value Analysis Test Cases

## FR07-BVA-001

- Test Case ID: FR07-BVA-001
- Technique: Boundary Value Analysis
- Objective: Verify add-to-cart quantity below minimum (`0`) is rejected.
- Requirement or Rule Reference: FR07-R07
- Preconditions: Product detail or add-to-cart quantity control is available.
- Test Data: Quantity `0`.
- Steps:
  1. Open a product add-to-cart flow with quantity input.
  2. Enter quantity `0`.
  3. Attempt to add the product to cart.
  4. Observe whether cart quantity changes or validation blocks the action.
- Expected Result: Quantity `0` is rejected and is not added to the cart.
- Actual Result: Quantity input accepted value 0 with input info {"value":"0","min":"","validationMessage":""}. After add attempt, cart text was "EShop
Giỏ hàng
Chào, Test User
Thoát
Giỏ hàng của bạn đang trống
Tiếp tục mua sắm
© 2026 EShop SUT. Dành cho mục đích kiểm thử.".
- Status: Fail
- Evidence: [FR07-BVA-001](./evidence/FR07-BVA-001.png)
- Partition or Boundary Covered: FR07-QTY-MIN-B01
- Test Basis Reference: `boundary-value-analysis.md` - FR07-QTY-MIN-B01
- Notes and Assumptions: Exact validation message is unspecified.

## FR07-BVA-002

- Test Case ID: FR07-BVA-002
- Technique: Boundary Value Analysis
- Objective: Verify add-to-cart quantity at minimum (`1`) is accepted.
- Requirement or Rule Reference: FR07-R07
- Preconditions: Product detail or add-to-cart quantity control is available.
- Test Data: Quantity `1`.
- Steps:
  1. Open a product add-to-cart flow with quantity input.
  2. Enter quantity `1`.
  3. Add the product to cart.
  4. Open `/cart` and observe item quantity.
- Expected Result: Quantity `1` is accepted and the cart shows the product with quantity 1.
- Actual Result: After entering valid minimum quantity 1 and clicking add-to-cart, cart page displayed "EShop
Giỏ hàng
Chào, Test User
Thoát
Giỏ hàng của bạn đang trống
Tiếp tục mua sắm
© 2026 EShop SUT. Dành cho mục đích kiểm thử."; no product with quantity 1 was visible.
- Status: Fail
- Evidence: [FR07-BVA-002](./evidence/FR07-BVA-002.png)
- Partition or Boundary Covered: FR07-QTY-MIN-B02
- Test Basis Reference: `boundary-value-analysis.md` - FR07-QTY-MIN-B02
- Notes and Assumptions: A single one-unit add is the minimum valid add.

## FR07-BVA-003

- Test Case ID: FR07-BVA-003
- Technique: Boundary Value Analysis
- Objective: Verify add-to-cart quantity immediately above minimum (`2`) is accepted.
- Requirement or Rule Reference: FR07-R07
- Preconditions: Product detail or add-to-cart quantity control is available.
- Test Data: Quantity `2`.
- Steps:
  1. Open a product add-to-cart flow with quantity input.
  2. Enter quantity `2`.
  3. Add the product to cart.
  4. Open `/cart` and observe item quantity.
- Expected Result: Quantity `2` is accepted and the cart shows the product with quantity 2.
- Actual Result: After entering valid adjacent quantity 2 and clicking add-to-cart, cart page displayed "EShop
Giỏ hàng
Chào, Test User
Thoát
Giỏ hàng của bạn đang trống
Tiếp tục mua sắm
© 2026 EShop SUT. Dành cho mục đích kiểm thử."; no product with quantity 2 was visible.
- Status: Fail
- Evidence: [FR07-BVA-003](./evidence/FR07-BVA-003.png)
- Partition or Boundary Covered: FR07-QTY-MIN-B03
- Test Basis Reference: `boundary-value-analysis.md` - FR07-QTY-MIN-B03
- Notes and Assumptions: `2` is the adjacent valid in-point above the minimum.

## Coverage Summary

| Requirement / Rule | Partition or Boundary | Technique | Test Case(s) | Surface | Coverage Status | Notes |
| ------------------ | --------------------- | --------- | ------------ | ------- | --------------- | ----- |
| FR07-R06, SH05 | CART-EMPTY-V01, EMPTY-STATE-V01 | DT | FR07-DT-001 | UI | Covered | Empty-state visual and message. |
| FR07-R01 | CART-NONEMPTY-V01, CART-COLUMNS-V01 | DT | FR07-DT-002 | UI | Covered | Required cart columns. |
| FR07-R08, SH03 | FEEDBACK-V01 | DT | FR07-DT-003 | UI | Covered | Toast or badge update. |
| FR07-R02 | DUPLICATE-ADD-V01 | DT | FR07-DT-004 | UI | Covered | Same product merge behaviour. |
| FR07-R11 | PLUS-V01, MINUS-V01 | DT | FR07-DT-005, FR07-DT-006 | UI | Covered | Quantity controls. |
| FR07-R03, SH04 | DELETE-CANCEL-V01, DELETE-CONFIRM-V01 | DT | FR07-DT-007, FR07-DT-008 | UI | Covered | Confirmation before delete. |
| FR07-R04 | CONTINUE-V01 | DT | FR07-DT-009 | UI | Covered | Continue shopping navigation. |
| FR07-R05 | TOTAL-LABEL-V01/I01 | DT | FR07-DT-010 | UI | Covered | Exact label and forbidden label. |
| FR07-R09, SH02 | BADGE-V01 | DT | FR07-DT-011 | UI | Covered | Navbar badge. |
| FR07-R10 | BREADCRUMB-V01 | DT | FR07-DT-012 | UI | Covered | Cart breadcrumb. |
| FR07-SH01 | NAV-HIGHLIGHT-V01 | DT | FR07-DT-013 | UI | Covered | Active navbar state. |
| FR07-API01, API02 | AUTH-V01, API-GET-V01 | DT | FR07-DT-014 | API | Covered | Authenticated cart retrieval. |
| FR07-API01 | AUTH-I01 | DT | FR07-DT-015 | API | Covered | Missing token rejection. |
| FR07-API03, API04 | API-POST-V01 | DT | FR07-DT-016 | API | Covered | Valid API add contract. |
| FR07-API04 | API-POST-I01 | DT | FR07-DT-017 | API | Covered | Missing documented body property. |
| FR07-R07 | FR07-QTY-MIN-B01/B02/B03 | BVA | FR07-BVA-001 through FR07-BVA-003 | UI | Covered | Quantity lower boundary. |

## Human Review - Phase 5

- Reviewer: User request authorized execution after Phase 1-5
- Review Date and Time: 2026-06-26
- Review Scope: FR-07 Phase 1 through Phase 5 AI-generated black-box DT/BVA reports and test cases.
- Human Corrections: None before execution.
- Human-added Cases: None.
- Removed or Reclassified Cases: None.
- Duplicate-case Decisions: No duplicates removed before execution.
- Status: Completed
- Approved for Validation: Yes
- Approved for Test-Case Quality Review: Yes
- Approved for Test Execution: Yes

---

## Execution Summary Output

Source: `reports/FR-07/execution-summary.md`

# Execution Summary - FR-07 Shopping Cart

## Scope

FR-07 Shopping Cart test cases were executed through public UI and public API surfaces only. No implementation source, database schema, internal tests, controllers, services, routes, middleware, or models were inspected.

## Environment

- Web UI: `http://localhost:5173`
- Backend API: `http://localhost:3000`
- Browser evidence: Chrome headless screenshots captured via Chrome DevTools Protocol
- Execution date: 2026-06-26

## Result Summary

| Metric | Count |
| ------ | ----- |
| Total test cases | 20 |
| Domain Testing cases | 17 |
| Boundary Value Analysis cases | 3 |
| Pass | 4 |
| Fail | 16 |
| Blocked | 0 |
| Not Executed | 0 |
| Evidence screenshots | 20 |

## Passed Test Cases

- FR07-DT-009
- FR07-DT-014
- FR07-DT-015
- FR07-DT-016

## Failed Test Cases

- FR07-DT-001
- FR07-DT-002
- FR07-DT-003
- FR07-DT-004
- FR07-DT-005
- FR07-DT-006
- FR07-DT-007
- FR07-DT-008
- FR07-DT-010
- FR07-DT-011
- FR07-DT-012
- FR07-DT-013
- FR07-DT-017
- FR07-BVA-001
- FR07-BVA-002
- FR07-BVA-003

## Evidence Location

Evidence screenshots are stored under:

```text
reports/FR-07/evidence/
```

## Human Verification

- Human Review Status: Pending
- Human Corrections: None yet

---

## Bug Report Output

Source: `reports/FR-07/bug-report.md`

# Bug Report - FR-07 Shopping Cart

## Scope

This bug report is based on executed FR-07 black-box test cases and evidence screenshots in `reports/FR-07/evidence/`. No implementation source, database schema, internal tests, controllers, services, routes, middleware, or models were inspected.

Human verification is still pending, so GitHub Issue links are not invented.

## Execution Result Basis

| Metric | Count |
| ------ | ----- |
| Executed test cases | 20 |
| Passed | 4 |
| Failed | 16 |
| Candidate bug groups | 8 |

## Candidate Bugs

### BUG-FR07-001 - Empty cart state has no illustration/icon

- Severity: Low
- Status: Pending Human Verification
- Related Test Case: FR07-DT-001
- Expected Result: Empty cart displays both an illustration/icon and a clear message.
- Actual Result: Empty cart displayed a clear message but no image/icon element was observed.
- Evidence: [FR07-DT-001](./evidence/FR07-DT-001.png)
- GitHub Issue Link: Pending

### BUG-FR07-002 - UI cart remains empty after public cart setup and does not show required cart list/controls

- Severity: High
- Status: Pending Human Verification
- Related Test Cases: FR07-DT-002, FR07-DT-005, FR07-DT-006, FR07-DT-007, FR07-DT-008, FR07-DT-010
- Expected Result: Non-empty cart displays required columns, quantity controls, delete action with confirmation, and total label `Tổng cộng`.
- Actual Result: After public authenticated cart setup, UI cart still displayed `Giỏ hàng của bạn đang trống`, with no required columns, quantity controls, delete action, or total label.
- Evidence:
  - [FR07-DT-002](./evidence/FR07-DT-002.png)
  - [FR07-DT-005](./evidence/FR07-DT-005.png)
  - [FR07-DT-006](./evidence/FR07-DT-006.png)
  - [FR07-DT-007](./evidence/FR07-DT-007.png)
  - [FR07-DT-008](./evidence/FR07-DT-008.png)
  - [FR07-DT-010](./evidence/FR07-DT-010.png)
- GitHub Issue Link: Pending

### BUG-FR07-003 - Public UI add-to-cart gives no visible feedback and does not produce visible cart item

- Severity: High
- Status: Pending Human Verification
- Related Test Cases: FR07-DT-003, FR07-DT-004, FR07-BVA-002, FR07-BVA-003
- Expected Result: Add-to-cart action gives visual feedback; duplicate add merges into one row with increased quantity; valid quantities 1 and 2 are accepted.
- Actual Result: Add-to-cart clicks showed no toast/badge update and the cart remained empty, including for valid quantities 1 and 2.
- Evidence:
  - [FR07-DT-003](./evidence/FR07-DT-003.png)
  - [FR07-DT-004](./evidence/FR07-DT-004.png)
  - [FR07-BVA-002](./evidence/FR07-BVA-002.png)
  - [FR07-BVA-003](./evidence/FR07-BVA-003.png)
- GitHub Issue Link: Pending

### BUG-FR07-004 - Navbar cart badge is missing

- Severity: Medium
- Status: Pending Human Verification
- Related Test Case: FR07-DT-011
- Expected Result: `Giỏ hàng` navigation link displays a numeric badge count.
- Actual Result: Navbar displayed `Giỏ hàng` without any numeric badge, and no badge appeared after add-to-cart action.
- Evidence: [FR07-DT-011](./evidence/FR07-DT-011.png)
- GitHub Issue Link: Pending

### BUG-FR07-005 - Cart page breadcrumb is missing

- Severity: Low
- Status: Pending Human Verification
- Related Test Case: FR07-DT-012
- Expected Result: Cart child page displays breadcrumb/path context.
- Actual Result: No breadcrumb/path indicator beyond the navbar was visible.
- Evidence: [FR07-DT-012](./evidence/FR07-DT-012.png)
- GitHub Issue Link: Pending

### BUG-FR07-006 - Cart navigation item is not highlighted on cart page

- Severity: Low
- Status: Pending Human Verification
- Related Test Case: FR07-DT-013
- Expected Result: Navbar highlights the selected cart page.
- Actual Result: `Giỏ hàng` link used normal navigation styling with no observable selected/highlighted state.
- Evidence: [FR07-DT-013](./evidence/FR07-DT-013.png)
- GitHub Issue Link: Pending

### BUG-FR07-007 - Add-to-cart quantity input accepts `0`

- Severity: Medium
- Status: Pending Human Verification
- Related Test Case: FR07-BVA-001
- Expected Result: Quantity `0` is rejected because add-to-cart quantity must be a positive integer with minimum 1.
- Actual Result: Quantity input accepted visible value `0`, had no `min` value, and showed no validation message.
- Evidence: [FR07-BVA-001](./evidence/FR07-BVA-001.png)
- GitHub Issue Link: Pending

### BUG-FR07-008 - `POST /api/cart` accepts request missing documented `quantity`

- Severity: High
- Status: Pending Human Verification
- Related Test Case: FR07-DT-017
- Expected Result: API request missing documented body property `quantity` is rejected or does not add an invalid cart item.
- Actual Result: `POST /api/cart` missing `quantity` returned `200` with `{"message":"Added to cart"}`; follow-up `GET /api/cart` showed an item without `quantity`.
- Evidence: [FR07-DT-017](./evidence/FR07-DT-017.png)
- GitHub Issue Link: Pending

## Human Review

- Reviewer: Pending
- Review Date and Time: Pending
- Human Review Status: Pending
- Human Corrections: Pending

---

## Evidence Index Output

Source: `reports/FR-07/evidence/evidence-index.md`

# Evidence Index - FR-07 Shopping Cart

| Test Case ID | Evidence Path | Evidence Type | Execution Time | Environment | Notes |
| --- | --- | --- | --- | --- | --- |

Evidence must be real and stored as `evidence/<TEST-CASE-ID>.<extension>`.

---

## Traceability Matrix Output

Source: `reports/FR-07/traceability-matrix.md`

# Traceability Matrix - FR-07 Shopping Cart

| Rule ID | Test Basis Reference | Partition IDs | Boundary IDs | Test Case IDs | Execution Status | Evidence | Bug IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Uncovered Items

Record every uncovered rule, partition, or boundary and its justification.

---

## AI Gap Analysis Placeholder Output

Source: `reports/FR-07/ai-gap-analysis.md`

# AI Gap Analysis - FR-07 Shopping Cart

## Comparison

| Initial AI-generated Test / Output | Human Correction | Human-added Test | Behaviour or Bug Missed by AI | Runtime Finding | Reason for Gap |
| --- | --- | --- | --- | --- | --- |

Do not describe a runtime miss before execution. Link preserved initial output and corrected output.

## Human Review

- Reviewer:
- Review time:
- Corrections recorded:
- Approved for execution: No


