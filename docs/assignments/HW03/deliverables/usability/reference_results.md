# Usability Flow Reference Results

## Evidence status

These are technical reference results established from the EShop source and repeated desktop execution. They are not participant observations and must not be used to pre-fill participant behavior, quotations, time, completion, or SUS responses.

| Checkpoint | Ideal expected result | Verified EShop behavior | Source/runtime basis |
|---|---|---|---|
| Product List | Catalog and product controls are available | Five seeded products render; iPhone 15 Pro Max is 30,000,000 VND | `Home.jsx`; Chrome/Firefox Product List captures |
| Product Detail | One click adds quantity 1 and provides feedback | First click intentionally returns without adding; second click adds the item | `ProductDetail.jsx`; BUG-001 |
| Cart | Selected product and correct total are reviewable | Five-column cart shows one iPhone and total 30,000,000 ₫ after successful addition | `Cart.jsx`; desktop Cart captures |
| Checkout entry | Selected items and authoritative total are shown | Items and 30,000,000 ₫ render, but the total input is editable | `Checkout.jsx`; BUG-006 |
| Coupon-free checkout | One pending order is created and success is confirmed | API stores a pending order; success screen is shown | `Checkout.jsx`, `POST /api/checkout`; CHK-GUI-020 |
| Post-checkout cart | Purchased items should be cleared | Cart remains populated because `clearCart()` is not invoked | `Checkout.jsx`; BUG-007 |
| Order History | New order and status can be verified | New order appears as “Chờ xác nhận” with summary fields | `Profile.jsx`, `GET /api/orders/my-orders`; CHK-GUI-014 |
| Order details | Participant should be able to inspect purchased items | No details link, expansion control, or item-level view is provided | `Profile.jsx`; BUG-016 |

## Controlled happy-path data

- Product: iPhone 15 Pro Max
- Quantity: 1
- Displayed price and subtotal: 30,000,000 VND / 30,000,000 ₫
- Coupon: none
- Expected initial order status: `pending` / “Chờ xác nhận”
- Task success: participant locates the newly created order and correctly identifies the visible status

## Excluded branches

`SAVE10`, manual total editing, invalid quantities, order cancellation, and Admin functions are excluded from the participant task. They are already covered by GUI testing and would introduce avoidable data-integrity or task-comparability problems into the moderated study.
