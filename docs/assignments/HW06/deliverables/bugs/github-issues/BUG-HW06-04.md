# [BUG-HW06-04] Checkout bypasses cart-derived business rules

**Severity:** Critical  
**Endpoint:** `POST /api/checkout`  
**Requirement:** FR-08

## Steps to reproduce

1. Authenticate as a customer.
2. Send checkout with an empty cart, or send a client-controlled `total_amount` that differs from cart contents.
3. Inspect the created order and cart state.

## Expected result

Checkout validates a non-empty cart, computes the order total on the server, and clears the cart only after a valid successful order.

## Actual result

The endpoint does not read or validate the cart. It accepts the client amount, creates an empty-cart order, and does not clear cart state.

## Evidence

- Newman cases: `EXT-CHK-01` through `EXT-CHK-03`
- Raw result: `docs/assignments/HW06/deliverables/newman-reports/pool-b/report.json`
