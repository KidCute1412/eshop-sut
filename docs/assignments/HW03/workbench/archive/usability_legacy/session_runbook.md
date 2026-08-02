# Moderated Usability Session Runbook

## Purpose

This runbook provides the exact preparation, moderator script, reference path, timing rules, and evidence fields for the Pilot and P1–P7 sessions. The moderator may consult the procedural detail below; the participant receives only the goal-oriented scenario in `task_scenario.md`.

## 1. Pre-session setup

Complete and record every check before admitting the participant.

- Start Backend and Customer Web; verify `http://127.0.0.1:3000/api/products` and `http://127.0.0.1:5173` respond.
- Use the standard seeded catalog. Confirm that iPhone 15 Pro Max is visible at 30,000,000 VND.
- Prepare a clean customer account whose cart is empty and whose pre-existing order history is documented.
- Use Google Chrome Desktop at 1440 × 1000 unless the session record states another genuine environment.
- Close unrelated applications, notifications, credentials, and personal information.
- Confirm screen and microphone capture, available storage, system clock, and timer.
- Prepare the participant code (`Pilot`, `P1`, …, `P7`), consent record, observation form, and SUS form.
- Do not reveal known defects or the reference path to the participant.

## 2. Opening script

Read the following consistently:

> Thank you for participating. We are evaluating the EShop interface, not you. There are no right or wrong personal reactions. Please work as you normally would and say aloud what you are looking for, expecting, and deciding. I will usually remain silent. If you become unable to continue, I may give a neutral prompt. With your permission, this session will record the screen and audio for coursework analysis. You may stop at any time. Do you consent to continue and to the recording?

Record the verbal response. Do not start the task if consent is not affirmative.

After recording begins, state the participant code, date, browser/device, and session type. Do not state unmasked personal contact information in the recording.

## 3. Participant task

Start the timer immediately after reading this text:

> You want to purchase one iPhone 15 Pro Max from EShop. Find the product, review its details, add one unit to your cart, check the order carefully, complete checkout without a discount code, and then use your account to confirm that the new order was created and identify its status. Please work as you normally would and think aloud.

Do not name buttons, pages, or the known need for a second Add to Cart click.

## 4. Moderator reference path

This is an observation reference, not a script to read to the participant.

| Step | Reference action | Verified SUT result | Observe and record |
|---:|---|---|---|
| 1 | Begin on Product List while signed in | Five seeded products are shown; iPhone 15 Pro Max is priced at 30,000,000 VND | Initial orientation, scanning, search use |
| 2 | Open “Xem chi tiết” for iPhone 15 Pro Max | Product Detail shows image, name, price, description, quantity 1, and Add to Cart | Whether details are found and understood |
| 3 | Leave quantity at 1 and click “Thêm vào giỏ hàng” once | Known defect: the first click produces no cart addition or confirmation | Expectation, repeated click, navigation, confusion |
| 4 | Click “Thêm vào giỏ hàng” a second time | One unit is added and the button temporarily reports success | Whether the participant discovers recovery independently |
| 5 | Open “Giỏ hàng” | Cart shows product, price, quantity 1, subtotal 30,000,000 ₫, Remove, Continue Shopping, and Checkout | Verification behavior and confidence |
| 6 | Select “Tiến hành thanh toán” | Checkout shows one item and total 30,000,000 ₫ | Navigation clarity and total verification |
| 7 | Do not edit total and do not enter a coupon; select “Xác Nhận Thanh Toán” | A pending order is created and the success state is displayed | Trust, hesitation, duplicate-click behavior |
| 8 | Navigate back, then open the account/profile through the signed-in user name | Known defect: purchased item remains in the in-memory cart | Whether the participant notices or comments on retained cart state |
| 9 | Locate the newest Order History row | New order shows 30,000,000 ₫ and “Chờ xác nhận”; only summary columns are available | Ability to identify the order/status and desire for details |

## 5. Timing and event rules

- Start: immediately after the task statement is fully read.
- Stop—success: participant correctly identifies the new order and states its visible status.
- Stop—abandonment: participant explicitly gives up.
- Stop—timeout: 10 minutes, recorded as incomplete unless the task already succeeded.
- Record timestamps relative to task start as `mm:ss`.
- Count an error when an action creates an unintended state, validation failure, or recovery attempt.
- Count a hesitation when scanning or inactivity indicating uncertainty lasts at least five seconds, or when the participant verbalizes uncertainty.
- Record every moderator intervention verbatim.

## 6. Intervention ladder

Wait through ordinary exploration. If the participant is unable to progress for approximately 30 seconds, use only the next neutral prompt:

1. “What are you trying to do now?”
2. “What options do you see?”
3. “Please continue in the way that seems most appropriate.”

Only when continued progress is impossible may the moderator identify the next goal, such as “Please try to reach the cart.” Any such assistance makes the affected checkpoint `Assisted`; never disclose the exact control unless necessary to prevent abandonment, and record it verbatim.

## 7. Closing script

Stop the task timer but keep recording. Administer all ten SUS items from the participant response form without explaining or reframing them. Then ask:

1. Which parts of the flow were clear or unclear?
2. If you encountered a problem, how easy was it to understand and recover from it?
3. Did the flow feel appropriately fast? What caused any delay?
4. How confident are you that the order was submitted correctly, and why?
5. What single change would most improve this experience?

Thank the participant, stop the recording, verify that the file opens, and update the recording index.

## 8. Post-session completion

- Complete checkpoint outcomes using only the recording and contemporaneous notes.
- Transcribe quotations accurately; distinguish quotations from interpretation.
- Enter SUS responses, calculate the score, and update the canonical CSV/XLSX.
- Record duration, filename/URL, file size or SHA-256, and access verification.
- Do not copy the verified SUT behavior into participant observations unless the video shows that participant encountering it.
