# EShop GUI/Usability Analysis Guide

## Approved Test Bases

- Official assignment PDF: `2026.HW03.GUI Usability_En.pdf`.
- Requirements: `README.md`, especially §8 (FR-21..FR-24: General UI, Forms, Navigation,
  Feedback/State) and the feature FRs relevant to the chosen screen/flow (FR-01..FR-20).
- Public API contract: `api_specification.md` (useful for Task 2 error/latency/trust probes, e.g.
  what a real backend error response looks like).
- Setup guidance: `setup_guide.md`, `run_servers.sh`.
- Observable UI: labels, controls, colors, messages, navigation state, loading/empty states, focus
  order, contrast, responsive behaviour.
- General usability heuristics for anything the SRS does not enumerate: Nielsen's 10 heuristics,
  WCAG 2.1 basics (alt text, contrast ratio, keyboard operability, focus visibility, form labeling),
  platform conventions (RTL layout, dark mode / prefers-color-scheme, locale-aware number/currency
  formatting).
- Real execution evidence (screenshots, session recordings, session notes) captured during actual
  use of the running SUT.

Do not use frontend/backend implementation source, database schema, or internal tests as the oracle
for what the UI "should" do — the oracle is the documented requirement, the observable behaviour of
a real user interacting with it, and general usability principles.

## Screens Available for the Checklist (Task 1 / Task 3)

Pick from, or combine, the following (choose per Phase 0 of `SKILL.md`):

- Frontend Web (`frontend-web/src/pages/`): Home, ProductDetail, Cart, Checkout, Login, Register,
  ForgotPassword, Profile.
- Web Admin (`frontend-admin/`): Dashboard, Category/Product/Coupon/Order/User management screens.
- Mobile (`frontend-mobile/`): equivalent screens via Expo Go.

Assign each selected screen a two-digit `GUI ID` (`01`, `02`, ...) as you register it in
`reports/gui-checklist/gui-list.md` via `scripts/create_checklist_workspace.py --gui-id`, matching
the professor's `Web GUI checklist Template.xlsx` "GUI list" sheet convention.

## Flows Available for Usability Evaluation (Task 2)

Pick exactly one end-to-end flow, e.g.:

- Register → Login → Product search → Add to cart → Checkout with a coupon.
- Login → Forgot/Reset password (2-step OTP flow) → Login again.
- Browse → Product detail → Add to cart → Cart quantity edit → Checkout → Order history.

## Startup Safety

`run_servers.sh` may be inspected only to understand safe startup (process-killing commands,
hard-coded paths, prerequisites, ports). Prefer the documented manual startup in `setup_guide.md`
when the script looks unsafe. Backend must be running (`localhost:3000`) before any frontend
checklist item that depends on live data (product listing, cart, checkout, coupon application) can
be meaningfully executed — otherwise mark the item `Blocked`, not `Failed`.

## Cross-Platform / Localhost Note

BrowserStack and LambdaTest run browsers in the cloud; they cannot reach `http://localhost:5173` or
`:5174` directly. Before Task 3 execution, enable one of:

- **BrowserStack Local** (the `BrowserStackLocal` binary) or **LambdaTest Tunnel** (`LT`), so the
  cloud browser can resolve and reach your machine's localhost.
- A temporary reverse tunnel (e.g. `ngrok http 5173`) if no BrowserStack/LambdaTest Local binary is
  available, provided the resulting public URL is disclosed in the report as a substitute for
  localhost access (the assignment's "localhost URL in the screenshot" rule still applies: prefer
  showing the actual localhost URL via the Local/tunnel feature over a raw ngrok URL when possible).
- A real physical device on the same network as the dev machine (LAN IP instead of `localhost`),
  which is the simplest option for Expo Go and for a spare phone's Chrome/Safari.

Never claim a cloud-platform screenshot is real if the browser could not actually reach the running
SUT — that would be fabricated evidence.

## Observation Rules

- A UI observation made while exploring the SUT is `Observable UI behaviour`; it may justify a
  checklist item's existence or an "AI missed this because it can only be seen by using the real
  interface" explanation, but it is not itself a Pass/Fail result until the item is formally
  executed.
- A recorded Pass/Fail from formally executing a checklist item, or a note/response actually
  collected during a usability session, is `Execution evidence`.
- If a documented requirement conflicts with what the running SUT actually does, record it as an
  `Observed contradiction` (this is very likely a bug) — do not silently rewrite the requirement to
  match the implementation.
