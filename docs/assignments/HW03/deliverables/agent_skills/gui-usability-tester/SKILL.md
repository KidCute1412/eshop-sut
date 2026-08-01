---
name: gui-usability-tester
description: Design and review GUI checklists, prepare moderated usability evaluations, synthesize verified evidence, and structure cross-platform GUI reports without fabricating execution results.
---

# GUI and Usability Tester

## Purpose

Use this skill to create traceable GUI and usability-testing artifacts for web or mobile systems. The skill supports test design and evidence synthesis; it must never represent static analysis, simulated participants, or generated images as authentic execution evidence.

## Required inputs

- System-under-test description and relevant requirements
- Selected screens and one end-to-end usability flow
- Interface aspects or quality criteria to cover
- Available runtime environments and evidence policy
- Real execution results, participant responses, and recordings when analysis is requested

## Workflow

### 1. Define scope and traceability

Record the selected screens, flow, user role, requirements, environment, and exclusions. Map every checklist item to an interface aspect and relevant screen or requirement.

### 2. Design and review the GUI checklist

Create specific, independently executable items covering visual standards, forms, navigation, and feedback/state. For each item, define its precondition and observable expected result. Remove duplicates and generic statements. Identify whether an item originated from AI or human review, and explain the context missed by AI for human-added items.

### 3. Record execution and defects

Execute each item against the live system and record the actual result, `Pass`, `Fail`, or `Not Executed`, notes, and evidence reference. A failure must map to a detailed defect record and authentic screenshot. Source inspection may justify a test hypothesis but cannot independently establish a user-visible defect.

### 4. Prepare the moderated usability evaluation

Write a realistic, goal-oriented participant scenario without procedural instructions. Define the target profile, success criteria, timing method, moderator intervention rule, SUS instrument, and probes for clarity, error recovery, speed, and trust. Conduct one pilot before the seven official sessions.

### 5. Analyze verified session data

Calculate SUS using `(odd response - 1)` and `(5 - even response)`, sum the ten contributions, and multiply by 2.5. Group recurring observations, distinguish isolated defects from systemic usability issues, cite participant/session evidence, and rank findings by user impact and frequency.

### 6. Verify cross-platform behavior

Use at least three qualifying environments. Record the exact browser, operating system, device, execution date, SUT URL, result, and evidence reference. Report observed differences without inferring behavior on an untested platform.

### 7. Perform the evidence-integrity review

Before finalization, confirm that participant details, quotations, recordings, screenshots, GitHub references, and Git commits are authentic. Reconcile summary counts with source files and leave unavailable empirical fields explicitly unreported.

## Output contract

Produce:

- A GUI checklist with traceability, execution status, notes, defect mapping, and evidence references
- A defect report with reproducible steps and authentic evidence references
- A goal-oriented task scenario, participant register, response forms, and per-session observation notes
- A SUS results table and severity-ranked findings based on verified data
- A three-environment cross-platform report
- A concise limitations statement distinguishing planned work from completed evidence

## Safety constraints

- Do not fabricate participants, consent, responses, quotations, durations, recordings, screenshots, links, or commits.
- Do not label an item `Pass` or `Fail` unless it was executed using an appropriate test method.
- Do not convert generated illustrations or static code findings into execution evidence.
- Mask participant contact details according to the assignment privacy rule.

## Demonstration

The demonstration video should show one complete example from scoped input through checklist design, execution evidence, review, and final artifact generation. Record the verified public or unlisted URL in `demo_video_link.txt`.

