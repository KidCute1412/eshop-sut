# Usability Evaluation Task Scenario

## Evaluation objective

Evaluate whether a typical EShop customer can independently select a product, review the cart, place an order, and confirm the resulting order status. The study focuses on navigation clarity, feedback, error recovery, efficiency, and trust.

## Target participant profile

Participants should have prior experience purchasing products online. People outside the HW03 class are eligible; non-IT and non-testing participants are preferred. Seven official participants are required in addition to one pilot participant.

## Preconditions

- The EShop services are running in a stable test environment.
- A customer test account and suitable product data are available.
- The participant has consented to screen and audio recording.
- The moderator has verified that the flow is operational without revealing its procedure.

## Participant-facing scenario

> You want to purchase one iPhone 15 Pro Max from EShop. Find the product, review its details, add one unit to your cart, check the order carefully, complete checkout without a discount code, and then use your account to confirm that the new order was created and identify its status. Please work as you normally would and think aloud.

The moderator must not provide step-by-step instructions or identify the controls required to complete the scenario.

The exact moderator procedure, verified reference path, timing rules, and intervention ladder are defined in `session_runbook.md`. Technical outcomes are documented separately in `reference_results.md` so they cannot be confused with participant evidence.

## Success criteria

| Measure | Definition |
|---|---|
| Task completion | The participant places an order and locates its resulting status without procedural assistance. |
| Time on task | Measured from presentation of the scenario to successful completion or abandonment. |
| Errors | Incorrect actions that cause an unintended state, validation failure, or recovery attempt. |
| Hesitations | Observable pauses or repeated scanning that indicate uncertainty. |
| Moderator intervention | Any assistance required after the participant can no longer make progress. |
| Post-task perception | SUS score and responses to the four qualitative probes. |

The default time limit is ten minutes. A successful task ends when the participant identifies the newly created order and correctly states the visible status. Completion with any procedural assistance is recorded separately as `Assisted`, not independent success.

## Post-task probes

1. Which parts of the flow were clear or unclear?
2. If you encountered a problem, how easy was it to understand and recover from it?
3. Did the flow feel appropriately fast? What caused any delay?
4. How confident are you that the order was submitted correctly, and why?

## Pilot and official sessions

The pilot is used to validate the scenario wording, test setup, timing method, and recording procedure. Any refinement must be documented before the seven official sessions. The participant-facing goal and moderator intervention rule must then remain consistent across P1–P7.
