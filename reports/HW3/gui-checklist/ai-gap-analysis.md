# AI Gap Analysis - GUI Checklist (Register + Login, merged)

## Scope


## Gap Findings

| Gap ID | Related No. | Checklist Item | Why the AI Missed It |
| --- | --- | --- | --- |
| GAP-GUI-001 | `4.3` | Does the server independently re-validate password strength, in case the client-side check is bypassed? | Interface characteristic only discoverable by bypassing the client-side check (e.g. via F12 -> Network, replaying the registration request with a weak password) and observing whether the server still accepts it. This is invisible from using the form normally — an AI reading only the requirements and the rendered form has no occasion to consider "what if the client check is skipped entirely," since nothing about the UI itself suggests the client check might not be the only line of defense. |
| GAP-GUI-002 | `4.4` | Is user-entered data (e.g. the Name field) safely escaped everywhere it is later displayed, instead of being rendered as raw HTML? | Cross-screen blind spot: the place this data is later displayed (the site-wide header, after logging in) is a completely different screen from Register. A checklist scoped to "this screen" does not naturally prompt checking where else a value entered here might re-appear — the AI would need to already know to trace a single field's data flow across the entire application, not just the form it was typed into. |
| GAP-GUI-003 | `9.6` | When the account is locked, is the user shown a message distinct from a plain wrong-credentials message? | Model limitation: a straightforward reading of README.md FR-02 only prompts checking the lockout counter and duration numbers themselves. Noticing that the *same generic message* is reused even for the locked-account case requires a human judgment call about UX quality — recognizing that two different failure states being visually indistinguishable is itself a defect — rather than a literal compliance check against a stated number in the requirement. |

## Human Review

- Reviewer: Nguyen Thanh Tien 
- Review Date and Time: 2026-07-28
- Review Scope: The 3 Human-Added items in `checklist.md` and why the AI did not generate them
- Confirmed all 3 items are genuinely Human-Added (not duplicates of an AI-Generated item): Yes
- Approved: Yes
