# Phase 1 — Task Scenario (participant-facing script)

Read this aloud (or share as text) to every participant, identically, before starting the session.

---

> "Imagine you're trying to log into **EShop**, an online store, but you've forgotten your password.
>
> **Your goal:** Use the "Quên mật khẩu" (Forgot password) link on the login page to get back into your account. You'll be given a test account email to use. Enter it, request the reset code, and follow the screen through to setting a new password.
>
> Please think out loud as you go — tell me what you're looking at, what you expect to happen, and if anything confuses you. There are no wrong answers here; we're testing the website, not you. If you get completely stuck, let me know and I'll help, but try to explore on your own first."

---

## Notes for the moderator (not shown to participant)

- Give the participant a pre-existing test account email (already registered) — do not reveal the OTP or the password hint interpretation in advance.
- Do **not** explain what the "strong password" hint actually means beyond what's on screen — the whole point is to observe whether the hint's wording ("ký tự đặc biệt" / special character) leads them to a password that the field will actually accept (it requires a **whitespace** character instead, per the code — this is a genuine bug, not a trick you engineer).
- Time the session from the "Quên mật khẩu" click to either the "Đổi mật khẩu thành công!" screen or the participant's explicit give-up.
- If a participant is stuck for >60s with no progress, offer a minimal, non-leading nudge (e.g., "What would you try next?") before a direct hint. Do not reveal the whitespace requirement during the session — note whether they discover it themselves; explain it only in the post-session debrief once notes/recording are done.
- End condition: participant reaches "Đổi mật khẩu thành công!", or explicitly gives up / says they'd stop trying.

## Deviation note

The original Phase 1 draft scoped a longer Register → Cart → Checkout flow (see git history). With only 4 participants recruited (see `04_participants.md`) and limited session time per person, the scope was narrowed to the Forgot Password flow alone, which still lets us test a real, high-severity comprehension bug (the password-hint/regex mismatch, shared code with Register) inside a 1–2 minute session. The checkout-total-trust probe from `03_instruments.md` does not apply to this narrower flow and was replaced (see that file).
