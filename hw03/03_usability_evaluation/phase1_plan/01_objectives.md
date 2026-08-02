# Phase 1 — Objectives

**Chosen end-to-end flow (per §5):** Forgot Password → enter email → receive OTP → enter OTP + new password → submit reset.
This flow was chosen because it exercises two concrete code-level findings from Task 1: the OTP field's digit-count labeling (BUG-13) and, most importantly, the password-strength regex shared between Register and Reset-Password (`ForgotPassword.jsx`), which requires a whitespace character (`(?=.*\s)`) while its own on-screen hint tells the user a **special character** is required. Reset Password was picked over the original Register→Cart→Checkout flow because with only 4 participants available (see `04_participants.md`), a short, single-screen-pair flow lets every session complete inside ~2 minutes and still surfaces a genuine, high-severity comprehension bug.

## What we want to learn

1. **Comprehension of the password policy at password reset** — do users understand what "strong password" requires from the hint text alone ("Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt")? Since the underlying regex actually requires a whitespace character instead of a special character, no input matching the hint literally can ever pass — how many attempts do users make, and do they ever recover?
2. **OTP field clarity** — is the digit count shown to the user consistent with the field's own label, and does any mismatch cause hesitation or copy/paste errors?
3. **Error message usefulness** — when the reset fails, does the alert ("Mật khẩu quá yếu!...") give the user any actionable path forward, or does it send them in circles retrying variations of the same (hint-compliant) password?
4. **Task completion confidence and speed** — do users complete the reset flow unaided, and how confident/frustrated do they feel afterward (captured via SUS + probe questions)?
5. **Give-up behavior** — at what point (how many attempts, how much elapsed time) do users abandon the flow, and what do they say they would do next in real life (e.g., "I'd just contact support")?

## Success criteria for the study (not for the SUT)

- 4 completed/attempted sessions (no separate pilot run — P1's session is also used to confirm the scenario script works; no script changes were needed after it).
- SUS completed by all 4 participants.
- At least one observed instance (or explicit absence) of friction around each of the 5 questions above, documented in Phase 3 synthesis.
