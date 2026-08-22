# FR07 - Shopping cart API Mapping

| Field | Value |
|---|---|
| Feature | FR-07 Shopping cart |
| Pool | B - Shopping Cart and Checkout |
| Primary endpoints | GET /api/cart; POST /api/cart |
| Actor | Authenticated user |
| Authentication | Required JWT token |
| Request body | `id`, `name`, `price`, `quantity` for add-to-cart |
| Source of truth | `README.md` FR-07, SEC-02/SEC-05; `api_specification.md` 4.1, 4.2 |
| Key rules | Cart requires token; adding same product increases quantity instead of adding duplicate row; item data includes product/unit price/quantity; quantity is positive integer by FR-06/FR-07 interaction |
| Documented ambiguity | API spec exposes add and get cart only; UI-only remove/confirmation/total-label requirements are recorded as non-API coverage notes. |
