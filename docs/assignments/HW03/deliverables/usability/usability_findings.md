# EShop Customer-Web Usability Results

## Study scope and evidence basis

This moderated study evaluates the Customer Web journey **FR-07 → FR-10 → FR-11**. Web Product Detail is used only as a supporting FR-06 step. The study does not evaluate Mobile Product Detail (FR-23).

Seven official sessions (P1–P7) are included in the aggregate results. The pilot is documented separately and excluded from participant frequencies, task metrics, and SUS calculations. Participant profiles and consent status are maintained in `participant_list.md`; recording metadata and the shared Drive location are maintained in `recordings/video_links.md`.

The quantitative results below are calculated from the structured entries in `usability_results.xlsx`. Video timestamps are retained as session-record references in the workbook but were not independently recoded during the final formatting pass. Runtime GUI defects are not substituted for participant observations.

## Evaluation measures

| Measure | Operational definition |
|---|---|
| Completion | `Independent`, `Assisted`, `Incomplete`, or `Abandoned`, using the success criterion in `usability_test_script.md` |
| Task duration | Recorded time from the task statement to identification of the newest order status |
| Error | An action that moves away from the task goal or requires corrective action |
| Hesitation | A visible pause, repeated scan, or uncertainty before the next action |
| Intervention | Moderator guidance beyond the approved neutral prompts |
| SUS | Standard ten-item System Usability Scale, scored from 0 to 100 |

## Official-session results

| Measure | Result |
|---|---:|
| Official sessions included | 7 of 7 |
| Independent completions | 7 of 7 (100%) |
| Median recorded task duration | 75 seconds |
| Total recorded errors | 14 |
| Total recorded hesitations | 14 |
| Total moderator interventions | 0 |
| Mean SUS | 73.6 / 100 |

Individual SUS scores are P1 75.0, P2 82.5, P3 67.5, P4 67.5, P5 77.5, P6 75.0, and P7 70.0. The unrounded mean is 73.5714. The workbook applies the standard odd/even-item SUS formula and excludes the pilot.

## Consolidated findings

| ID | Evidence in `usability_results.xlsx` | Finding | Frequency | User impact | Severity | Recommendation | Related defect |
|---|---|---|---:|---|---|---|---|
| UF-01 | `Observations`, Add to Cart rows for P1–P7 | Participants encountered absent first-action feedback and repeated the add-to-cart action. | 7/7 | Creates uncertainty and unnecessary repetition at a purchase-critical step. | High | Ensure the first valid click updates cart state and presents immediate, accessible confirmation. | BUG-001 |
| UF-02 | `Observations`, Checkout rows for P1, P3, P5, and P6 | Four participants interacted with or explicitly noticed that the displayed total could be edited. | 4/7 | Reduces confidence that the payable amount is authoritative. | High | Render the calculated total as read-only text or a non-editable output. | BUG-006 |
| UF-03 | `Observations`, Post-checkout Cart rows for P2, P4, and P7 | Three participants showed or expressed uncertainty after purchased items remained in the cart. | 3/7 | Makes order completion ambiguous and increases perceived duplicate-purchase risk. | Medium | Clear purchased items after a confirmed checkout and show a persistent order-confirmation path. | BUG-007 |

Frequency represents distinct official participants, not the number of repeated actions. Severity combines frequency, task criticality, recoverability, and effect on confidence.

## Technical reference results

The table below is a product-behavior oracle established through SUT inspection and desktop execution. Technical reference results are not participant observations and are not counted in participant frequencies.

| Checkpoint | Expected product result | Verified EShop behavior | Reference |
|---|---|---|---|
| Product List | Catalog and product controls are available | Five products render; iPhone 15 Pro Max is listed at 30,000,000 VND. | `Home.jsx`; desktop evidence |
| Product Detail | One valid click adds quantity 1 with feedback | The first click does not add the item; a repeated click adds it. | BUG-001 |
| Cart | Product, quantity, and subtotal are reviewable | One iPhone, quantity 1, and a 30,000,000 ₫ subtotal are displayed after addition. | `Cart.jsx`; desktop evidence |
| Checkout | Items and an authoritative total are displayed | The selected item appears, but the total is presented in an editable input. | BUG-006 |
| Submit order | One pending order is created with confirmation | The checkout API creates a pending order and a success state is shown. | CHK-GUI-020 |
| Post-checkout cart | Purchased items are cleared | Purchased items remain because cart state is not cleared after success. | BUG-007 |
| Order History | The newest order and status are identifiable | The new order appears with the status “Chờ xác nhận”. | CHK-GUI-014 |
| Order details | Purchased items can be inspected | No item-level order-detail view is available. | BUG-016 |

## Severity scale

| Severity | Decision rule |
|---|---|
| Critical | Prevents task completion for most participants with no reasonable recovery. |
| High | Affects a purchase-critical decision or causes serious/repeated confusion for multiple participants. |
| Medium | Causes measurable, recoverable friction for multiple participants. |
| Low | Creates minor friction without threatening completion or confidence. |

## Interpretation

All seven official participants reached the stated success criterion without moderator intervention, while the findings show recurring friction at add-to-cart feedback, checkout-total presentation, and post-checkout state. A mean SUS score of 73.6 indicates generally usable interaction, but it does not override the task-level evidence above. The highest-priority improvements are immediate add-to-cart feedback and an authoritative, non-editable checkout total.
