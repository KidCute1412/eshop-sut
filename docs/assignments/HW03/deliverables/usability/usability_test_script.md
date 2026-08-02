# EShop Usability Test — Execution Script and Result Record

**Scope note:** This study runs on Customer Web and evaluates FR-07 → FR-10 → FR-11. Web Product Detail is a supporting FR-06 step only; it is not FR-23, and participants are not claimed to test Mobile FR-23.

## 1. Test definition

| Field | Value |
|---|---|
| Test case | UT-01 — Purchase an iPhone and verify the new order status |
| Moderator/observer | Lê Tuấn Lộc — 23127404 |
| Participant role | Customer with previous online-shopping experience |
| Official sessions | P1–P7; one independent session per participant |
| SUT | EShop Customer Web and Backend |
| Default environment | Google Chrome Desktop, Windows 11, 1440 × 1000 |
| Start condition | Signed in; Product List open; cart empty; prior orders documented |
| Test data | iPhone 15 Pro Max; quantity 1; no coupon; 30,000,000 VND |
| Timer start | Immediately after the task statement is read |
| Timer stop | Participant identifies the newest order and states its visible status |
| Time limit | 10 minutes |
| Success | Order created and newest status identified without procedural assistance |

The moderator manages the setup, reads the scripts, observes, times, and records. Each participant independently operates the SUT. The step table is a moderator reference and must not be shown or read as navigation instructions to the participant.

## 2. Session assignment

All seven participants perform the same UT-01 flow so results remain comparable.

| Session | Participant | Profile | Assigned work | Evidence/result status |
|---|---|---|---|---|
| P1 | Đặng Đăng Khoa | IT student | Execute UT-01 independently | Completed |
| P2 | Nguyễn Thanh Gia Bảo | IT developer | Execute UT-01 independently | Completed |
| P3 | Đặng Trường Nguyên | IT student | Execute UT-01 independently | Completed |
| P4 | Lâm Đỗ Hoàng Long | Teacher | Execute UT-01 independently | Completed |
| P5 | Lê Minh Sơn | Graphic designer | Execute UT-01 independently | Completed |
| P6 | Nguyễn Hải Đăng | IT student | Execute UT-01 independently | Completed |
| P7 | Võ Lê Bảo Ngọc | Non-IT student | Execute UT-01 independently | Completed |

Masked contacts and consent status are maintained in `participant_list.md`.

## 3. Before each recording

The moderator completes the following preparation:

1. Start Backend and Customer Web; verify `http://127.0.0.1:3000/api/products` and `http://127.0.0.1:5173`.
2. Confirm the five-product catalog and iPhone 15 Pro Max price of 30,000,000 VND.
3. Sign in using a clean customer test account, empty its cart, and document existing orders.
4. Close notifications and hide passwords, contact details, and unrelated personal information.
5. Start screen/audio recording and prepare a visible timer.
6. State the session code, date, browser, operating system, and viewport on the recording.

## 4. Opening and task statement

The moderator reads:

> Thank you for participating. We are evaluating the EShop interface, not you. Please work as you normally would and say aloud what you are looking for, expecting, and deciding. I will usually remain silent. You may stop at any time. Do you consent to participate and to this screen-and-audio recording?

Continue only after affirmative consent. Then read the task and start the timer:

> You want to purchase one iPhone 15 Pro Max from EShop. Find the product, review its details, add one unit to your cart, check the order carefully, complete checkout without a discount code, and then use your account to confirm that the new order was created and identify its status. Please work as you normally would and think aloud.

## 5. Step-by-step execution and reference results

The “verified SUT result” column documents the behavior already established through source review and desktop execution. It is the comparison oracle, not a claim that every participant has produced that result.

| Step | Actor | Exact action/checkpoint | Expected product result | Verified SUT result | Participant evidence to record |
|---:|---|---|---|---|---|
| 1 | Participant | Inspect Product List and locate iPhone 15 Pro Max | Product is discoverable with correct name and price | Five products appear; iPhone price is 30,000,000 VND | Time to locate, scanning, search use, hesitation |
| 2 | Participant | Open the iPhone product details | Detail page presents enough information to make a purchase decision | Image, name, price, description, quantity 1, and Add to Cart appear | Route chosen, comprehension, comments |
| 3 | Participant | Attempt to add one unit to the cart | One click adds one item and gives visible confirmation | First click produces no addition or confirmation — BUG-001 | Expectation, repeated action, confusion, intervention |
| 4 | Participant | Continue attempting the add-to-cart goal | The interface supports recovery without assistance | Second click adds one unit and displays temporary success feedback | Whether recovery is independent and its timestamp |
| 5 | Participant | Open and review the cart | Cart shows the selected product, quantity 1, and correct subtotal | One iPhone, quantity 1, subtotal 30,000,000 ₫, Remove, Continue Shopping, and Checkout appear | Verification behavior, errors, confidence |
| 6 | Participant | Continue from Cart to Checkout | Checkout clearly presents the selected item and authoritative total | One item and total 30,000,000 ₫ appear; total remains editable — BUG-006 | Navigation clarity, delay, whether editable total is noticed |
| 7 | Participant | Submit the order without a coupon | Exactly one pending order is created and confirmation is clear | API creates a pending order and success state appears | Hesitation, repeated clicks, confidence statement |
| 8 | Participant | Leave confirmation and access the account/profile | Purchased cart contents should be cleared | Purchased item remains in the in-memory cart — BUG-007 | Whether retained cart is noticed and interpreted |
| 9 | Participant | Find the newest order in Order History and state its status | New order is identifiable with status and useful details | New row shows 30,000,000 ₫ and “Chờ xác nhận”; no item-detail view — BUG-016 | Time to find, stated status, desire for details |

Do not tell the participant which control to use or that Add to Cart requires a second click. If no progress occurs for approximately 30 seconds, use the next neutral prompt only:

1. “What are you trying to do now?”
2. “What options do you see?”
3. “Please continue in the way that seems most appropriate.”

Any stronger guidance is recorded verbatim as an intervention, and the affected result becomes `Assisted`.

## 6. Per-session final result

After reviewing each genuine recording, complete the corresponding row in `usability_results.xlsx`.

| Session | Completion | Duration | Errors | Hesitations | Interventions | Final visible order status | Overall result | Video reference |
|---|---|---:|---:|---:|---:|---|---|---|
| P1 | Independent | 135s | 2 | 1 | 0 | Chờ xác nhận | Pass | `recordings/video_links.md` |
| P2 | Independent | 120s | 2 | 1 | 0 | Chờ xác nhận | Pass | `recordings/video_links.md` |
| P3 | Independent | 150s | 2 | 2 | 0 | Chờ xác nhận | Pass | `recordings/video_links.md` |
| P4 | Independent | 180s | 3 | 2 | 0 | Chờ xác nhận | Pass | `recordings/video_links.md` |
| P5 | Independent | 140s | 1 | 1 | 0 | Chờ xác nhận | Pass | `recordings/video_links.md` |
| P6 | Independent | 130s | 2 | 1 | 0 | Chờ xác nhận | Pass | `recordings/video_links.md` |
| P7 | Independent | 175s | 2 | 1 | 0 | Chờ xác nhận | Pass | `recordings/video_links.md` |

Allowed completion values are `Independent`, `Assisted`, `Incomplete`, and `Abandoned`. A final result is not assigned until the recording proves the actions, timing, and outcome.

## 7. Post-task questionnaire

After stopping the task timer, the moderator keeps recording and obtains a 1–5 response for each standard SUS statement:

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need technical support to use this system.
5. I found the functions in this system well integrated.
6. I thought there was too much inconsistency in this system.
7. I imagine most people would learn to use this system quickly.
8. I found the system cumbersome to use.
9. I felt confident using this system.
10. I needed to learn many things before I could use this system.

Then ask the four required probes:

1. Which parts were clear or unclear?
2. If you encountered a problem, how easy was it to understand and recover?
3. Did the flow feel appropriately fast? What caused any delay?
4. How confident are you that the order was submitted correctly, and why?

SUS is calculated only from the participant’s ten genuine answers:

`SUS = (sum of each odd response − 1 + sum of 5 − each even response) × 2.5`

## 8. Recording and analysis completion

Use `p1_session.mp4` through `p7_session.mp4`, or enter access-tested cloud URLs in `recordings/video_links.md`. Each recording must show consent, the uninterrupted task, participant interaction, moderator prompts, final status, SUS answers, and four probes. After verifying the video, enter timestamps and observations in `usability_results.xlsx`, then synthesize evidence-backed results in `usability_findings.md`.
