# Browser execution playbook

## Prepare

- Confirm the authorized environment and whether actions mutate shared data.
- Record browser/version, OS, viewport/device, locale, build/URL, test account role, and seed data.
- Start from a known state and preserve the user's unrelated state.
- Prefer accessible role, label, and visible-name locators; use test IDs when the UI lacks stable semantics.

## Execute reliably

- Navigate through the same path a user takes; avoid direct URL shortcuts when state is held in the client.
- Wait for observable UI or network completion conditions, not arbitrary sleeps.
- Assert preconditions before each action and checkpoint state after it.
- For timing-sensitive behavior, capture a trace or video and record the timer rule.
- On failure, capture the visible state, URL, and relevant console/network diagnostics before cleanup.
- Retry only to classify reproducibility; never overwrite the first failure evidence.

## Capture evidence

Use deterministic names such as `<check-id>_<short-result>.<ext>`. Capture the smallest viewport or full-page image that proves the claim. When required, place identity, browser, OS/device, URL, timestamp, and check ID in a non-obscuring overlay or adjacent evidence record. Never fabricate browser chrome or device identity.

## Cross-browser discipline

Reuse the same test data, task checkpoints, and assertions across engines. Create an independent browser context for each run. Record engine-specific blockers exactly and retry outside a restricted sandbox only when authorized. A successful engine launch is not a completed platform run; the full critical flow and evidence checkpoints must execute.

## Source-assisted diagnosis

After observing a failure, inspect source to narrow the likely cause and propose focused retests. Keep observed behavior, diagnostic inference, and confirmed root cause in separate fields. Do not edit the SUT unless the request includes fixing it.
