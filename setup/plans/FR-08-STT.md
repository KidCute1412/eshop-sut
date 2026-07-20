# FR-08-STT: State-Transition Testing Plan — FR-08 (Thanh toán / Checkout)

## 1. Scope Assessment
- Requirement involves state-dependent behavior: yes. Checkout behavior depends on authentication state, cart contents, and payment outcomes, and includes sequences (open checkout → submit → payment result). The state-transition testing skill is applicable.

## 2. Model Identification

### States
- `LoggedOut` — user unauthenticated.
- `LoggedInEmptyCart` — authenticated user with empty cart.
- `LoggedInHasItems` — authenticated user with ≥1 cart item.
- `CheckoutInitiated` — checkout UI opened; client-visible read-only total shown.
- `PaymentSubmitting` — client submitted payment request.
- `PaymentProcessing` — backend recalculating totals and processing payment/gateway.
- `PaymentSucceeded` — backend accepted payment; order created.
- `PaymentFailed` — payment rejected or error returned.
- `OrderCompleted` — post-success final state with empty cart.

### Events / Inputs (triggers)
- `login` / `logout` — authentication events.
- `addItem` / `removeItem` / `changeQty` — cart modification events.
- `openCheckout` — user navigates to checkout page.
- `submitPayment` — client submits payment payload (may include `total_amount`).
- `gatewaySuccess` / `gatewayFailure` — external payment gateway result.
- `concurrentCartChange` — cart mutated between `openCheckout` and `submitPayment`.
- `maliciousClientTotal` — client tampers `total_amount` in payload.

### Actions / Outputs (resulting behaviors)
- UI: show product list, read-only client total, error or success messages.
- Backend: validate auth, recompute authoritative total from cart/prices, validate inventory, call payment gateway, create order, clear cart on success, preserve cart on failure, ignore client `total_amount`.
- HTTP/API: return appropriate status codes (401 for unauthenticated, 400/409 for invalid submissions, 200/201 for success, 4xx/5xx for failures).

## 3. Plan Formulation

### State Transition Matrix (rows: current state; columns: input/event).
(Cells: resulting state or "no transition / error")

- From `LoggedOut`:
  - `login` → `LoggedInEmptyCart` or `LoggedInHasItems` (depending on cart persisted)
  - `openCheckout` → blocked (401 / redirect)
  - `submitPayment` → blocked (401)

- From `LoggedInEmptyCart`:
  - `addItem` → `LoggedInHasItems`
  - `openCheckout` → blocked / show empty-cart message
  - `submitPayment` → blocked / show empty-cart message

- From `LoggedInHasItems`:
  - `openCheckout` → `CheckoutInitiated` (UI displays items + read-only total)
  - `removeItem`/`changeQty` → `LoggedInHasItems` (cart updated)
  - `logout` → `LoggedOut`

- From `CheckoutInitiated`:
  - `submitPayment` → `PaymentSubmitting` → server begins `PaymentProcessing`
  - `concurrentCartChange` → stay `CheckoutInitiated` (client view stale) but server will use updated cart on submit
  - `logout` → `LoggedOut` (session invalidated)

- From `PaymentProcessing`:
  - `gatewaySuccess` → `PaymentSucceeded` → `OrderCompleted` (cart cleared)
  - `gatewayFailure` → `PaymentFailed` (cart preserved)
  - server inventory validation fail → `PaymentFailed` (with reason)

- From `PaymentFailed`:
  - `submitPayment` → retry to `PaymentProcessing` (if still authenticated and items available)
  - `cancel` → `LoggedInHasItems` (return to cart)

- From `OrderCompleted`:
  - `openCheckout` → blocked (cart empty)
  - further actions create new cart state when adding items

### Coverage goals & test-case estimates
- Coverage criteria:
  - All-States: visit each state at least once.
  - All-Transitions: traverse each defined transition at least once.
  - Negative tests: invalid transitions (e.g., `submitPayment` while `LoggedOut`, `submitPayment` with empty cart) and malicious inputs.

- Estimated number of test cases:
  - All-States baseline: 9 tests (one per state verification).
  - All-Transitions baseline: ~14 core transitions (listed above) → 14 tests.
  - Add negative tests & edge/concurrent cases: +6 tests.
  - Total estimated tests for reasonable coverage: ~25 test cases.

## 4. Notes / Next steps
- Save this file as `setup/plans/FR-08-STT.md` (this file).
- Next: generate explicit sequential test cases (Phase 2) from the transitions, saving each as `FR-08-TC[NN]-STT.md` in `setup/tests` and ensure traceability.


Saved-by: GitHub Copilot
