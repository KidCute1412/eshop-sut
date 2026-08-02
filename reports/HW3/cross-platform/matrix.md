# Cross-Platform Execution Matrix — Task 3

Task 1's checklist (`reports/HW3/gui-checklist/checklist.md`, 41 items, IA-01..04, Register + Login)
re-run across 3 platforms per the assignment. Platform 1 reuses the Task 1 execution verbatim (the
assignment explicitly allows this). Platform 2 (Firefox) is a fresh, fully executed run. Platform 3
(Safari/BrowserStack) is scaffolded but not yet executed.

| Platform | Tool | Browser/OS/Device | SUT URL Used | Local Tunnel Used | Checklist File | Passed | Failed | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Coc Coc | Real browser, this machine | Coc Coc Browser, Windows 11 | http://localhost:5173 | N/A | [coc-coc/GUI-RL/checklist.md](coc-coc/GUI-RL/checklist.md) | 10 | 31 | Platform 1 — this is the Task 1 baseline reused verbatim, not re-executed (waived by lecturer clarification — Task 1's own platform counts as one of the 3). Coc Coc is Chromium-based; if strict compliance with the "Chrome, Firefox, Safari-or-Android-Chrome" wording is required, note it here rather than mislabel it as Chrome. |
| Firefox | Real browser, this machine | Firefox Browser, Windows 11 | http://localhost:5173 | N/A | [firefox/GUI-RL/checklist.md](firefox/GUI-RL/checklist.md) | 10 | 31 | Platform 2 — fully executed, all 41 items. Results match Coc Coc exactly (10 Passed / 31 Failed); no new Firefox-specific bugs found — every failure reproduces the same underlying defects already filed under Task 1. |
| Safari (BrowserStack) | BrowserStack trial | TODO (e.g. Safari 17, macOS Sonoma, via BrowserStack) | TODO (localhost via BrowserStack Local) | Yes — BrowserStack Local required to reach localhost:5173 | [safari-browserstack/GUI-RL/checklist.md](safari-browserstack/GUI-RL/checklist.md) | TODO | TODO | Not yet executed. Requires a BrowserStack (or LambdaTest) trial signup and enabling Local/Tunnel before the remote Safari session can reach this machine's localhost. |

