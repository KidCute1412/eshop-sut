---
name: gui-checklist-runner
description: Design and execute a code-grounded GUI checklist (General UI, Forms, Navigation, Feedback/state) against a given web/mobile screen or flow, in two disciplined passes (AI baseline + human/code-grounded review), then log failures as ready-to-file bug reports. Use when asked to "run a GUI checklist", "test this screen's UI", or "find usability/GUI bugs" in a specific codebase.
---

# GUI Checklist Runner

This skill reproduces the disciplined, two-pass GUI checklist process used in HW03 (GUI & Usability Testing), so it can be reapplied to any new screen or flow without re-deriving the method from scratch.

## When to use this skill

Invoke it whenever the user wants a GUI/usability checklist built and executed against a real codebase — not a generic "list some UI best practices" request. It assumes you have read access to the target source code (React/React Native or similar) and, ideally, an API/spec document to cross-check UI copy against.

## Process (follow every step — do not collapse into one prompt)

### Step 1 — Scope
Ask (or infer from context) which screens/flows are in scope. A single screen rarely yields 40+ non-repetitive items; prefer 3+ related screens/flows unless the user explicitly wants a narrow scope.

### Step 2 — AI baseline pass
Generate an initial checklist covering four fixed categories:
- **General UI standards** (visual consistency, color semantics, hover/focus states, responsive layout, branding)
- **Forms** (validation, required-field cues, error messaging, input types/masking)
- **Navigation** (wayfinding, breadcrumbs, back/redirect behavior, active-state indication)
- **Feedback / state** (loading, empty states, confirmations, error recovery, data-integrity of what's shown vs. what's submitted)

Write each item as a specific, testable statement ("X should do Y"), tagged to a screen. Do not stop at generic industry heuristics only — but expect this pass to be biased toward *shape*, not runtime behavior.

### Step 3 — Human/code-grounded review (the step that matters most)
Actually read the source of every in-scope screen/component, and the API spec if one exists. For each file, deliberately look for the three failure classes a generic pass tends to miss:
1. **Accessibility, dark mode, RTL** — check `alt` attributes, keyboard operability of non-native interactive elements (`<div onClick>`, `<li onClick>`), presence of `dark:` variants or `prefers-color-scheme` handling, and whether spacing/alignment uses physical vs. logical properties.
2. **UI copy vs. actual logic mismatches** — diff every user-facing string (hints, labels, error messages) against the code that enforces it (regex, length checks) and against any API/spec documentation of expected formats.
3. **State/security bugs inside event handlers** — trace `onClick`/`onChange`/submit handlers for: dangerous HTML injection (`dangerouslySetInnerHTML`, `innerHTML`), silently-swallowed first actions, array/object mutations that leak to unrelated rows, and any client-editable value that should be server-computed/read-only.

For every item added in this step, write down *why the AI baseline pass would have missed it* — this is a required deliverable, not decoration; it demonstrates the AI was used as a disciplined assistant, not a black box.

### Step 4 — Execute
Walk every checklist item against the actual behavior (live app if you have browser/device access; otherwise rigorous code-trace, clearly disclosed as a limitation). Mark Passed/Failed with a Notes column explaining *why* for every Failed item, citing file:line.

### Step 5 — Log bugs
For every Failed item, produce a GitHub-issue-ready bug write-up: Title, Labels, Screen/file:line, Steps to reproduce, Expected, Actual, Fix suggestion, Evidence placeholder. Sort by severity (Critical: security/data-integrity > Major: blocks/misleads task completion > Minor: cosmetic).

## Output format

Produce:
1. A checklist table/CSV with columns: No, IA category, Screen, Item, Origin (AI/Human), Why-AI-missed-it (if Human), Expected result, Status, Notes, Bug ID.
2. A short test-summary (counts by category, pass/fail, severity breakdown).
3. A bug report file with full GitHub-issue-ready entries.

## Known limitations to always disclose

- If no browser/screenshot tool is available, state explicitly that execution was via code review, not a live session, and list what must be re-verified live before real submission/use.
- Never fabricate screenshots, live test results, or claim a live browser session occurred if one didn't.
