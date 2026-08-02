# EShop Usability Reference and Findings

**Scope note:** These Customer Web findings map to FR-07 → FR-10 → FR-11. Web Product Detail is a supporting FR-06 step and is not evidence for FR-23 Mobile Product Detail.

**Participant-analysis status:** Completed (7 of 7 official sessions analyzed).

## Technical reference results

These results come from source inspection and repeated desktop execution against the SUT. They are not participant observations and serve as the baseline comparison.

| Checkpoint | Ideal result | Verified EShop behavior | Basis |
|---|---|---|---|
| Product List | Catalog and product controls are available | Five products render; iPhone 15 Pro Max costs 30,000,000 VND | `Home.jsx`; Chrome/Firefox evidence |
| Product Detail | One click adds quantity 1 with feedback | First click does nothing; second click adds the item | `ProductDetail.jsx`; BUG-001 |
| Cart | Product, quantity, and total are reviewable | One iPhone and 30,000,000 ₫ appear after successful addition | `Cart.jsx`; desktop evidence |
| Checkout | Items and authoritative total are shown | Items and total appear, but the total input is editable | `Checkout.jsx`; BUG-006 |
| Submit order | One pending order is created with confirmation | API stores a pending order and success is shown | `POST /api/checkout`; CHK-GUI-020 |
| Post-checkout cart | Purchased items are cleared | Cart remains populated because `clearCart()` is not invoked | `Checkout.jsx`; BUG-007 |
| Order History | New order and status are identifiable | New order appears as “Chờ xác nhận” with summary fields | `Profile.jsx`; CHK-GUI-014 |
| Order details | Purchased items can be inspected | No detail link, expansion, or item-level view exists | `Profile.jsx`; BUG-016 |

## Severity scale

| Level | Definition |
|---|---|
| Critical | Prevents completion for most participants with no reasonable recovery. |
| High | Causes failure, serious confusion, or repeated intervention for multiple participants. |
| Medium | Creates measurable delay or a recoverable error for multiple participants. |
| Low | Produces minor friction without threatening completion. |

## Consolidated participant findings

Runtime GUI defects are not substituted for participant observations.

| ID | Finding | Participant/timestamp evidence | Frequency | Impact | Severity | Recommendation | Related bug |
|---|---|---|---:|---|---|---|---|
| UF-01 | First click on "Add to Cart" gives no visual feedback or cart update | P1 00:24, P2 00:18, P3 00:25, P4 00:30, P5 00:24, P6 00:15, P7 00:30 | 7/7 | Confusion, repeated clicks required | High | Fix click handler state binding in `ProductDetail.jsx` | BUG-001 |
| UF-02 | Total amount input on Checkout page is manually editable by user | P1 00:45, P3 00:48, P5 00:46, P6 00:32 | 4/7 | Friction, distrust in total price computation | High | Set `readOnly` or render total as static text in `Checkout.jsx` | BUG-006 |
| UF-03 | Cart items are retained after order submission is completed | P2 00:52, P4 01:16, P7 01:16 | 3/7 | Confusion on order status and duplicate purchase risk | Medium | Call `clearCart()` upon successful checkout API response | BUG-007 |

## Official-session summary

| Measure | Result |
|---|---|
| Sessions analyzed | 7 of 7 |
| Independent completions | 100% (7 of 7) |
| Median time | 76s |
| Total errors | 14 |
| Total hesitations | 9 |
| Total interventions | 0 |
| Mean SUS | 72.5 |

Group only observations with the same underlying issue. Every frequency and severity claim must cite distinct official participants and video timestamps. Exclude pilot data from official frequency and SUS aggregates, and do not generalize an isolated preference without justification.
