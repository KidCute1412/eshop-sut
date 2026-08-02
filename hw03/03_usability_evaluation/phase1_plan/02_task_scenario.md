# Phase 1 — Task Scenario (participant-facing script)

Read this aloud (or share as text) to every participant, identically, before starting the session.

---

> "Imagine you just heard about **EShop**, an online store, from a friend. You want to try buying something for yourself.
>
> **Your goal:** Create a new account, find a product you like, add it to your cart, and complete the purchase — try to use a discount coupon if you can find one. You can pick any product on the site; there's no specific budget or item you have to choose.
>
> Please think out loud as you go — tell me what you're looking at, what you expect to happen, and if anything confuses you. There are no wrong answers here; we're testing the website, not you. If you get completely stuck, let me know and I'll help, but try to explore on your own first."

---

## Notes for the moderator (not shown to participant)

- Do **not** tell them the coupon code exists or what it is — this deliberately probes discoverability (Objective 3). Have a valid, non-expired coupon pre-seeded in the DB (e.g. via the admin panel) so a successful attempt is possible if they find the field.
- Do **not** explain the checkout-total field is editable/non-editable — just observe whether they notice or touch it (Objective 2).
- Time the session from "create account" click to "order confirmed" screen.
- If a participant is stuck for >60s with no progress, offer a minimal, non-leading nudge (e.g., "What would you try next?") before a direct hint.
- End condition: participant reaches the "Thanh toán thành công!" (Checkout success) screen, or explicitly gives up.
