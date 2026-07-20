# FR-08-UCT: Use-Case Testing Plan — FR-08 (Thanh toán / Checkout)

## 1. Scope Assessment
- FR-08 describes a user-facing checkout flow with authentication, cart state, UI behavior, backend validation, and post-order cleanup.
- This requirement is well suited for use-case testing because it defines the actor goal, system responses, and alternative conditions that must be validated through scenarios.
- The checklist below is derived from `setup/info/README.md` and `setup/info/api_specification.md`.

## 2. Model Identification

### Actors
- Primary actor: Authenticated User.
- Secondary actor: Unauthenticated User (negative access control).
- Supporting system: Backend Checkout Service.

### Preconditions
- User account exists and can log in.
- Cart contains one or more items with known product prices.
- Backend session is valid and JWT token is available for authenticated requests.
- Checkout endpoint is available at `POST /api/checkout`.

### Postconditions
- Success: Order is created, backend recalculates the authoritative total from the cart, cart is cleared, and checkout confirmation is displayed.
- Failure: No order is created, cart remains unchanged, user receives an error or guidance message.

### Primary Use Case (Happy Path)
1. User logs in successfully.
2. User adds products to the cart.
3. User navigates to the Checkout page.
4. Checkout UI displays the full list of purchased items and a read-only total calculated from the cart.
5. User submits checkout data (e.g. `shipping_address`), while the client may include `total_amount` in the payload.
6. Backend validates the JWT token, recomputes the total from the cart/prices, ignores the client-supplied `total_amount`, and processes payment.
7. Payment succeeds, backend creates an order, clears the cart, and returns success confirmation.

## 3. Branching Use Cases

### A. Authentication and access control
- A1: Unauthenticated user attempts to open Checkout. Expected result: access blocked, redirect to login or HTTP 401 returned.
- A2: Authenticated user loses session before submit. Expected result: submission rejected with 401/403 and cart preserved.

### B. Cart content validation
- B1: Authenticated user opens Checkout with an empty cart. Expected result: UI shows empty-cart message and blocks payment.
- B2: Authenticated user submits checkout while the cart becomes empty between view and submit. Expected result: backend rejects submission and reports empty cart.

### C. UI and client-side behavior
- C1: Checkout UI must show the full product list and a read-only total value.
- C2: User must not be able to edit the displayed checkout total.

### D. Backend total validation and malicious payload handling
- D1: Backend must recompute authoritative total from cart/prices and ignore `total_amount` sent by client.
- D2: Client sends a tampered `total_amount` lower than the server total. Expected result: backend ignores it and proceeds using server total, or rejects if validation fails.

### E. Concurrent update and inventory validation
- E1: Cart changes after checkout page is opened but before payment submit. Expected result: backend uses latest cart state and recalculated total.
- E2: Product quantity or availability changes before submit. Expected result: backend rejects or adjusts depending on business rules, cart preserved until success.

### F. Payment processing outcomes
- F1: Payment succeeds. Expected result: order created and cart cleared.
- F2: Payment fails or gateway error occurs. Expected result: cart preserved, user receives failure message, and retry is possible.

## 4. Plan Formulation

### Use-Case Mapping
- Primary flow: Authenticated checkout success with backend total recalculation and cart clearance.
- Negative branches: unauthenticated access, empty cart, lost authentication, invalid submit payload.
- Validation branches: read-only total, ignore client-supplied `total_amount`, concurrent cart changes, backend inventory/price recalculation.
- Failure flow: payment/gateway failure preserves cart.

### Estimated Test Coverage
- Recommended use case scenarios: 8–10 distinct flows.
  - 1 main happy path.
  - 2 authentication/access-control branches.
  - 2 cart validation branches.
  - 2 backend validation branches.
  - 1 payment failure branch.
- These scenarios should cover the key requirement elements listed in FR-08 and ensure traceability from user interactions to backend behavior.

## 5. Notes / Next Steps
- Save this plan as `setup/plans/FR-08-UCT.md`.
- Next step is to create detailed test cases from these use cases in `setup/tests/FR-08-TC[NN]-UCT.md` files.
- Ensure each branch is covered by at least one test case and include explicit checks for read-only UI totals, backend total recalculation, and cart clearance after success.
