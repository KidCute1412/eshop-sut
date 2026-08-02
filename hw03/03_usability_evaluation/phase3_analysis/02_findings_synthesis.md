# Phase 3 — Findings Synthesis

All 4 sessions (P1 Long, P2 Linh, P3 Tiến, P4 Khải) followed the Forgot Password flow (see `../phase1_plan/02_task_scenario.md` for the scope-reduction rationale). Every session's observation table is pulled from `../phase2_sessions/P1.md`–`P4.md`.

## Cluster A: Password-hint / regex mismatch at reset (Blocker, systemic)

- **Hypothesis (from BUG-12, originally scoped for Register):** the hint text and the actual accepted characters diverge. Confirmed here to also affect the **Reset Password** screen, since `ForgotPassword.jsx` reuses the exact same `flawedStrongPasswordRegex` as `Register.jsx` — it requires a whitespace character (`(?=.*\s)`) while the on-screen hint says "...số và ký tự đặc biệt" (special character).
- **Participants who showed this:** P1, P2, P3, P4 — all 4.
- **Isolated or systemic:** Systemic — every single participant failed at this exact step, for the exact same reason, with 2–4 attempts each before giving up. This is the single dominant finding of the study.
- **Supporting quotes:**
  - P1: "Tôi có chữ hoa, chữ thường, số, với dấu chấm than rồi mà, sao vẫn báo yếu?"
  - P2: "Lạ ha, tôi đã có đủ ký tự đặc biệt theo yêu cầu rồi mà nó vẫn kêu yếu."
  - P3: "Kỳ vậy, tôi làm đúng y như nó ghi mà."
  - P4: "Tôi nghĩ là mấy ký hiệu như `!`, `@`, `#`, `-`, `_`. Tôi không nghĩ ra được là phải có dấu cách trong đó."
- **Impact:** 0/4 participants completed the task. This is a hard functional blocker, not a cosmetic annoyance — it fully prevents legitimate password recovery for any user who reads and trusts the hint text.

## Cluster B: Error message gives no actionable path forward (Major, systemic)

- **Hypothesis (new, emerged from observation, not pre-seeded):** the alert "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." repeats the same (misleading) requirement on every failed attempt, giving the user no new information to try something different.
- **Participants who showed this:** P1, P2, P3, P4 — all 4 retried with variations of the same theme (more punctuation, different punctuation, fewer characters) rather than converging on a fix, because the message never changes.
- **Isolated or systemic:** Systemic.
- **Supporting quotes:** P3 tried removing the digit requirement out of desperation ("Chắc phải bỏ chữ số ha..."); P4 explicitly asked the moderator what "ký tự đặc biệt" meant, showing the message alone wasn't sufficient even for an engaged, technically-inclined participant.

## Cluster C: OTP digit-count label (Minor, not observed as an issue in these sessions)

- **Hypothesis (from BUG-13):** OTP field label digit count might mismatch the code shown, causing confusion.
- **Participants who showed this:** None. In all 4 sessions the code displayed matched the "(4 số)" label exactly (confirmed against `backend/server.js`, which generates a 4-digit `resetToken`), so no participant commented on or hesitated over this field.
- **Isolated or systemic:** N/A this round — **refuted** for the current build state. Retained here as a note in case `Bug_Report.md`'s BUG-13 (6-digit code vs. 4-digit label) reflects a different build/commit than the one tested; worth re-checking against the exact commit BUG-13 was filed against.

## Cluster D: Checkout-total trust (not tested this round)

- Out of scope — the narrowed Forgot Password flow never reaches Checkout. See `../phase1_plan/02_task_scenario.md` deviation note. This hypothesis (BUG-14) remains untested by this study and should be evaluated separately if a future round returns to the full Register→Cart→Checkout flow.

## Severity prioritization

| Finding | Cluster | # participants affected | Severity (Blocker/Major/Minor) | Recommended fix |
|---|---|---|---|---|
| Password reset always rejects any hint-compliant password (regex requires whitespace, hint says special character) | A | 4/4 | **Blocker** | Fix `flawedStrongPasswordRegex` in `ForgotPassword.jsx` (and `Register.jsx`, same bug) to require a special character (e.g. `[!@#$%^&*]`) matching what the hint actually says, or fix the hint text to say "khoảng trắng" if whitespace is truly intended. |
| Generic, non-actionable error alert on repeated failure | B | 4/4 | Major | Replace the generic alert with a message that states which specific requirement is unmet (or use inline validation per-character as the user types). |
| OTP label/digit mismatch | C | 0/4 (this round) | Minor | Re-verify against the commit referenced in BUG-13; if already consistent in the current build, close/update that issue. |

## Genuine bugs discovered during sessions

- **Password-reset regex/hint mismatch is confirmed to affect both Register (BUG-12 scope) and Reset Password** — same root cause, same file pattern (`flawedStrongPasswordRegex`), two locations. This is more severe than a cosmetic mismatch: it makes account recovery **fully non-functional** for every user who trusts the visible hint, which is a stronger, user-observed severity claim than the original static-code-review framing in Task 1. Recommend filing a dedicated GitHub Issue (with screenshot/recording excerpt) for the Reset Password instance specifically, separate from BUG-12, since it blocks a different user-facing flow (account recovery vs. new signup) — not yet filed as of this writing.
