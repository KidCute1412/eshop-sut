---
name: gui-usability-tester
description: Design, execute, and audit evidence-based GUI, moderated usability, and cross-platform tests for web or mobile interfaces. Use when asked for GUI checklists, UI defect reports, usability scenarios or SUS analysis, browser/device comparisons, or an integrity review of those artifacts.
---

# GUI and Usability Tester

## Operating principle

Produce traceable, reproducible testing artifacts. Separate four evidence states at all times:

- `Planned`: designed but not run.
- `Executed`: directly observed in a qualifying runtime.
- `Participant-reported`: supplied by a real consented participant.
- `Inferred`: derived from source inspection or existing evidence and explicitly labelled.

Never promote one state into another. Static analysis can identify a test target, but it cannot prove a user-visible result.

## Inputs and discovery

Before writing results, locate and read the applicable requirements, source code, existing test artifacts, execution environment, and evidence rules. Establish:

- SUT URL/build, user role, selected screens and end-to-end flow
- in-scope interface aspects and requirement identifiers
- supported browsers, operating systems, devices, and viewport sizes
- available participant evidence, recordings, screenshots, and issue tracker
- privacy, screenshot-overlay, filename, and submission constraints

If an input is unavailable, continue with safe design work and mark the affected empirical field `Not Executed`, `Not Collected`, or `Pending Evidence`. Do not guess.

## Select the work mode

Use only the stages needed by the request:

1. `DESIGN` — requirements-to-checklist and usability-study design.
2. `EXECUTE` — live GUI or cross-platform execution and evidence capture.
3. `ANALYZE` — verified session transcription, SUS calculation, and finding synthesis.
4. `AUDIT` — reconciliation, integrity checks, and readiness reporting.

State the selected mode and scope in the working notes. A request to design does not authorize invented execution results; a request to review does not authorize modifying the SUT.

## Workflow

Read `references/oracles-and-analysis.md` before designing checks or synthesizing findings. Read `references/browser-execution.md` before browser automation or screenshot capture. Read `references/output-contract.md` before creating tabular artifacts. Do not load references unrelated to the selected mode.

### 1. Build the traceability model

Map each requirement or interface aspect to observable screens, controls, states, and risks. Use stable IDs. Prefer one assertion per checklist item. Each item must have a precondition, action, and observable expected result.

Cover at least these GUI dimensions when applicable:

- visual consistency and responsive layout
- labels, content, readability, and accessibility cues
- navigation, focus order, keyboard operation, and state persistence
- validation, error prevention, recovery, loading, empty, success, and failure feedback
- data integrity across list, detail, cart/form, confirmation, and history views

Remove duplicates and vague items such as “UI works correctly.” Mark origin as `AI`, `Human`, or `Hybrid`, and record the human-added context when the assignment requires an AI comparison.

### 2. Execute GUI checks

For every executed item, record exact environment, date/time, test data, actual result, status, and evidence reference. Allowed statuses are `Pass`, `Fail`, `Blocked`, and `Not Executed`.

- `Pass`: the observed result satisfies the stated expectation.
- `Fail`: the observed result contradicts it and maps to a defect.
- `Blocked`: execution began but an external prerequisite prevented observation.
- `Not Executed`: no qualifying run occurred.

Retest failures once when safe to distinguish deterministic behavior from transient behavior. Preserve authentic evidence; do not edit screenshots in a way that changes the tested UI. An informational overlay is allowed only when the evidence policy permits it and the underlying screen remains visible.

### 3. Report defects

Deduplicate failures by root behavior, not merely by screen. Each defect needs:

- stable defect ID and concise title
- environment, build/URL, preconditions, and test data
- minimal numbered reproduction steps
- expected and actual results
- reproducibility and severity with rationale
- affected checklist IDs and evidence references
- issue-tracker link when one exists

Use severity consistently: `Critical` prevents a core journey or causes severe data/security harm; `High` seriously impairs a core journey with no reasonable workaround; `Medium` causes material friction or incorrect feedback with a workaround; `Low` is limited cosmetic or minor consistency impact.

### 4. Prepare moderated usability sessions

Write one realistic, goal-oriented task; do not reveal control names or step-by-step navigation. Define target participant criteria, consent, success criteria, timer start/stop, intervention ladder, neutral probes, and the standard ten SUS questions. Run one pilot to validate wording and logistics before seven official sessions when the assignment requires them.

The moderator may clarify the goal but must not coach the path. Record observed actions, hesitations, errors, recoveries, interventions, completion, time, and timestamped quotations separately from the technical reference path.

### 5. Analyze verified participant evidence

Transcribe only observable or participant-supplied data. Calculate each complete SUS response set as:

`SUS = (sum(odd item - 1) + sum(5 - even item)) * 2.5`

Reject missing or out-of-range responses rather than imputing them. Aggregate findings only after preserving session-level traceability. For each finding, cite participants and timestamps, describe frequency and impact, connect related GUI defects, and recommend a specific change. Distinguish isolated incidents from recurring patterns.

### 6. Verify cross-platform behavior

Execute the same critical flow and checkpoints on every qualifying environment. Record exact browser/version, OS, physical or cloud device, viewport, URL/build, date, result, and screenshot reference. Device emulation does not count as a real mobile device unless the governing requirement explicitly permits it. Report differences observed; never infer an untested platform.

### 7. Audit before finalization

Use `references/output-contract.md` as the artifact schema and run `python scripts/validate_artifacts.py <deliverables-root>` when the output follows that contract. The validator accepts both canonical snake_case headers and the supplied HW03 title-case headers. Then manually reconcile:

- checklist totals against row statuses
- failed checks against defects and evidence
- participant count against raw responses, notes, recordings, and SUS rows
- platform claims against qualifying environment evidence
- issue links, video links, commit hashes, filenames, and privacy masking

Report validation failures precisely. Do not silently rewrite empirical results to make totals pass.

## Quality gates

The work is complete only when:

- every claim has a requirement, source, execution, or participant evidence trail
- every empirical status uses an allowed value and has the required context
- each failure maps to one reproducible defect and authentic evidence
- SUS scores come only from ten valid real responses
- summaries exactly match their source rows
- unavailable evidence is visibly pending, not implied complete
- recommendations are actionable and linked to observed impact

## Safety and integrity

- Do not fabricate participants, consent, responses, quotations, durations, recordings, screenshots, links, issue pages, commits, or test execution.
- Mask participant contact information and avoid unnecessary personal data.
- Do not perform destructive production actions merely to exercise a GUI path.
- Preserve unrelated user changes and distinguish SUT modification from test-artifact creation.

## Demonstration

The demonstration should invoke this installed skill on a bounded feature, show requirement/source discovery, generate traceable checklist items, execute at least one safe check, record authentic evidence, create or update a defect when warranted, and run the audit. Store the access-tested public or unlisted URL in `demo_video_link.txt`.
