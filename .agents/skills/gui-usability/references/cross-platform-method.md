# Cross-Browser / Cross-Platform Method (Task 3)

Re-run the Task 1 checklist — same items, same schema — on at least 3 platforms.

## Platform Selection

- Required web coverage: Chrome, Firefox, and Safari (Android Chrome may substitute for Safari when
  Safari is unavailable).
- Expo Go on a real phone is a valid platform and may replace one of the three required browsers —
  it is not bonus-only, it satisfies a required slot.
- Preferred tooling: BrowserStack or LambdaTest trial (student obtains their own access). Fallback,
  only if the trial has expired: Sauce Labs, CrossBrowserTesting, or a real physical device —
  acceptable as long as the screenshot requirements below are still met.

## Reaching a Localhost SUT from a Cloud Browser

Cloud device farms cannot resolve `localhost` on your machine. Before running Task 3:

1. Start the SUT locally per `setup_guide.md` (backend + the relevant frontend).
2. Enable **BrowserStack Local** or **LambdaTest Tunnel** so the remote browser session can reach
   your machine's `localhost:5173` / `:5174` directly — this preserves the assignment's requirement
   that the localhost URL be visible in the screenshot.
3. If neither Local/Tunnel feature is available and you fall back to a real device, connect it to
   the same LAN as the dev machine and use the machine's LAN IP instead of `localhost` (e.g.
   `http://192.168.x.x:5173`) — record this substitution explicitly in `matrix.md`.
4. For Expo Go, the mobile app already targets the dev machine's LAN IP per `setup_guide.md`; no
   tunnel is required as long as both devices share Wi-Fi.

## Screenshot Requirements

Every Task 3 screenshot must, in a single frame, show:

1. The actual SUT page/state relevant to the checklist item (or the failure being evidenced).
2. The browser/OS/device name (e.g. "Chrome 124 / Windows 11" or "Safari / iOS 17 / iPhone 14" as
   shown by the cloud tool's session chrome, or manually overlaid if using a real device).
3. The SUT's localhost (or LAN-IP substitute) URL, visible in the address bar or overlaid.
4. An overlay of the student's identity: the assignment states two overlapping requirements — the
   general screenshot rule (§6) asks for the username in the form of the **student email**, and the
   anti-cheat rule (§11) asks for the **student ID and full name**. Satisfy both at once with a
   single overlay text such as: `23127539 - Nguyen Thanh Tien - nttien232@clc.fitus.edu.vn` (student ID -
   full name - student email), positioned so it does not obscure the UI element under test.

Do not crop or stage a screenshot that could not have come from an actual cloud/real-device session
— the anti-cheat rule explicitly makes this evidence class TA-verifiable.

## Execution

1. Use `scripts/create_checklist_workspace.py --gui-id <ID> --gui-name <name> --platform <name>
   --seed-from reports/gui-checklist/GUI-<ID>/checklist.md` to produce a fresh
   `reports/cross-platform/<platform>/GUI-<ID>/checklist.md` pre-seeded from the human-approved
   Task 1 checklist (same `No.`/`Type`/`Checkpoint`/`IA` rows, `Yes`/`No`/`Remarks`/`Evidence`/
   `Bug ID` cleared, `Platform` set to `<name>`).
2. Execute every `Item` row exactly as in Task 1 — pay particular attention to Section 3
   (`Compatibility`), which exists specifically to be re-checked per platform. This frequently
   surfaces platform-specific bugs (CSS inconsistencies, Safari-specific form quirks, Android
   Chrome viewport issues) that did not appear on the baseline platform. These are genuine new
   findings, not re-labelled Task 1 bugs.
3. Update `reports/cross-platform/matrix.md` with one row per platform: tool used, browser/OS/
   device, pass/fail counts, and a link to that platform's `checklist.md`.
4. File any new platform-specific bug the same way as Task 1 (Markdown + GitHub Issue +
   screenshot), noting the platform in the bug title/body.
