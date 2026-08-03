# EShop Customer-Web Usability Test Protocol

## 1. Study definition

| Field | Value |
|---|---|
| Study ID | UT-01 |
| Task | Purchase one iPhone and identify the new order status |
| Scope | Customer Web, FR-07 → FR-10 → FR-11 |
| Supporting step | Web Product Detail under FR-06; not Mobile FR-23 |
| Moderator/observer | Lê Tuấn Lộc — 23127404 |
| Target participant | Customer with previous online-shopping experience |
| Official sessions | P1–P7; one session per participant |
| SUT | EShop Customer Web and Backend |
| Default environment | Google Chrome Desktop; Windows 11; 1440 × 1000 |
| Start condition | Signed in; Product List open; cart empty; prior orders documented |
| Test data | iPhone 15 Pro Max; quantity 1; no coupon; 30,000,000 VND |
| Timer start | Immediately after the task statement is read |
| Timer stop | Participant identifies the newest order and states its visible status |
| Time limit | 10 minutes |
| Success criterion | Order created and newest status identified without procedural assistance |

The moderator prepares the environment, reads the approved scripts, observes, times, and records. The participant operates the SUT independently. The moderator-reference steps below are not shown or read as navigation instructions.

## 2. Participants and assignment

All seven official participants perform the same task to support comparable measurements. Masked contact and consent records are provided in `participant_list.md`.

| Session | Participant | Profile | Assignment | Recorded result |
|---|---|---|---|---|
| P1 | Đặng Đăng Khoa | IT student | Execute UT-01 independently | Completed |
| P2 | Nguyễn Thanh Gia Bảo | IT developer | Execute UT-01 independently | Completed |
| P3 | Đặng Trường Nguyên | IT student | Execute UT-01 independently | Completed |
| P4 | Lâm Đỗ Hoàng Long | Teacher | Execute UT-01 independently | Completed |
| P5 | Lê Minh Sơn | Graphic designer | Execute UT-01 independently | Completed |
| P6 | Nguyễn Hải Đăng | IT student | Execute UT-01 independently | Completed |
| P7 | Võ Lê Bảo Ngọc | Non-IT student | Execute UT-01 independently | Completed |

## 3. Pre-session checklist

1. Start the Backend and Customer Web; verify the product API and Web application are reachable.
2. Confirm the product catalog and the displayed iPhone 15 Pro Max price.
3. Sign in with a clean customer test account, empty the cart, and document existing orders.
4. Hide passwords, personal contact details, notifications, and unrelated windows.
5. Start screen-and-audio recording and prepare the timer.
6. State the session code, date, browser, operating system, and viewport.
7. Obtain affirmative consent before continuing.

## 4. Opening and task statement

Read the following consent statement:

> Thank you for participating. We are evaluating the EShop interface, not you. Please work as you normally would and say aloud what you are looking for, expecting, and deciding. I will usually remain silent. You may stop at any time. Do you consent to participate and to this screen-and-audio recording?

After affirmative consent, read the task and start the timer:

> You want to purchase one iPhone 15 Pro Max from EShop. Find the product, review its details, add one unit to your cart, check the order carefully, complete checkout without a discount code, and then use your account to confirm that the new order was created and identify its status. Please work as you normally would and think aloud.

## 5. Step-by-step execution and moderator reference

| Step | Participant checkpoint | Expected product result | Evidence to record |
|---:|---|---|---|
| 1 | Locate iPhone 15 Pro Max in Product List | Product is discoverable with correct name and price. | Search path, scan behavior, hesitation |
| 2 | Review Product Detail | Details provide sufficient information for a purchase decision. | Comprehension, comments, uncertainty |
| 3 | Add one unit to Cart | One valid action adds one unit and provides feedback. | Actions, feedback noticed, repetition, recovery |
| 4 | Review Cart | Product, quantity 1, and subtotal are correct. | Verification behavior, errors, confidence |
| 5 | Continue to Checkout | Selected item and authoritative total are clear. | Navigation, delay, interaction with total |
| 6 | Submit without a coupon | Exactly one pending order is created with confirmation. | Repeated action, hesitation, confidence |
| 7 | Review post-checkout state | Purchased cart content is cleared. | Retained content noticed and interpreted |
| 8 | Find newest order | New order and visible status are identifiable. | Time to find, stated status, desire for details |

Do not identify controls or disclose known defects. If no progress occurs for approximately 30 seconds, use only these neutral prompts, in order:

1. “What are you trying to do now?”
2. “What options do you see?”
3. “Please continue in the way that seems most appropriate.”

Any stronger guidance is recorded verbatim as an intervention and changes completion from `Independent` to `Assisted`.

## 6. Coding rules

| Field | Coding rule |
|---|---|
| Independent | Success criterion met without procedural guidance |
| Assisted | Success criterion met after guidance beyond approved neutral prompts |
| Incomplete | Session ends without meeting the success criterion |
| Abandoned | Participant chooses to stop |
| Error | Action moves away from the goal or requires corrective action |
| Hesitation | Visible pause, repeated scan, or stated uncertainty before the next action |
| Intervention | Moderator supplies procedural guidance beyond the approved prompts |

## 7. Recorded official results

These values reproduce the structured session entries in `usability_results.xlsx`. Durations are task-duration entries, not full video lengths.

| Session | Completion | Task duration | Errors | Hesitations | Interventions | Final visible status | Result | Recording |
|---|---|---:|---:|---:|---:|---|---|---|
| P1 | Independent | 75s | 2 | 2 | 0 | Chờ xác nhận | Pass | `P1.mp4` |
| P2 | Independent | 75s | 2 | 1 | 0 | Chờ xác nhận | Pass | `P2.mp4` |
| P3 | Independent | 65s | 2 | 2 | 0 | Chờ xác nhận | Pass | `P3.mp4` |
| P4 | Independent | 80s | 2 | 2 | 0 | Chờ xác nhận | Pass | `P4.mp4` |
| P5 | Independent | 90s | 2 | 2 | 0 | Chờ xác nhận | Pass | `P5.mp4` |
| P6 | Independent | 78s | 2 | 1 | 0 | Chờ xác nhận | Pass | `P6.mp4` |
| P7 | Independent | 62s | 2 | 4 | 0 | Chờ xác nhận | Pass | `P7.mp4` |

The pilot is excluded from this table and all official aggregates. Recording metadata and the shared Drive location are indexed in `recordings/video_links.md`.

## 8. Post-task questionnaire

After stopping the task timer, obtain a 1–5 response to each standard SUS statement:

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

Ask these four follow-up probes:

1. Which parts were clear or unclear?
2. If you encountered a problem, how easy was it to understand and recover?
3. Did the flow feel appropriately fast? What caused any delay?
4. How confident are you that the order was submitted correctly, and why?

SUS scoring uses the standard formula:

`SUS = (sum of each odd response − 1 + sum of 5 − each even response) × 2.5`

## 9. Evidence index

- Participant identity and consent: `participant_list.md`
- Structured session, observation, SUS, and recording data: `usability_results.xlsx`
- Findings and aggregates: `usability_findings.md`
- Recording manifest and Drive folder: `recordings/video_links.md`
- Actual recording names: `Pilot.mp4`, `P1.mp4` through `P7.mp4`
