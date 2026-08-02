# Phase 1 — Objectives

**Chosen end-to-end flow (per §5):** Register a new account → browse/search for a product → add it to cart → checkout applying a discount coupon.
This flow was chosen because it touches all three of Pool A/B's highest-friction surfaces identified during Task 1's code review: the password-policy mismatch (BUG-12), the editable/non-authoritative checkout total (BUG-14), and the coupon apply/error flow — making it likely to surface genuine, observable usability friction rather than only cosmetic issues.

## What we want to learn

1. **Comprehension of the password policy at Register** — do users understand what "strong password" requires from the hint text alone, and how many attempts does it take them to satisfy it? (Directly probes BUG-12: the hint claims a special character is needed, but the regex actually requires whitespace.)
2. **Trust in the checkout total** — when users reach Checkout and see an editable "Tổng tiền thanh toán" field, do they notice/question that it's editable, and does its presence undermine their confidence that the final charge is correct? (Probes BUG-14.)
3. **Coupon discoverability and error recovery** — can users find the coupon field unprompted, and if a coupon fails (expired/invalid/min-order not met), can they recover without help?
4. **Overall task completion confidence and speed** — do users complete the full flow (register → search → add to cart → checkout with coupon) without external help, and how confident do they feel afterward (captured via SUS/UEQ-S + probe questions)?
5. **Navigation bottlenecks** — where in the 4-step flow (Register → Home/Search → Cart → Checkout) do users hesitate, backtrack, or misclick?

## Success criteria for the study (not for the SUT)

- 7 completed sessions + 1 pilot.
- SUS/UEQ-S completed by all 7 participants.
- At least one observed instance (or explicit absence) of friction around each of the 4 questions above, documented in Phase 3 synthesis.
