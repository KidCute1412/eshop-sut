---
name: gui-checklist-making
description: "Use when: creating a GUI checklist that covers the SUT's interface aspects for general UI standards, forms, navigation, and feedback/state."
---

# GUI Checklist Making

## Purpose
Use this skill to design a black-box GUI checklist for functional requirements by inspecting the application's visible interface, user-facing forms, navigation behavior, and feedback/state indicators. The checklist should be assembled from the user's provided UI images, the functional requirement context, and the information available in `setup/info`.

## Automatic file access
- Read from `setup/info` for requirements, UI rules, and application behavior.
- Read from `setup/skills` for project guidance and logging conventions.
- Read from `setup/templates` when a checklist template is available or when templates provide structure guidance.
- Read provided UI image references or attachments supplied by the user.
- Write outputs to `setup/checklist` for the generated draft checklist.
- Write session logs to `setup/logs/logs.md` following the existing log format.

## Core principles
- **Black-box GUI evaluation**: Only use observable UI content, screenshots/images, and requirement descriptions.
- **Four interface aspects**: Cover general UI standards, forms, navigation, and feedback/state.
- **Coverage**: Aim for broad coverage across screens and functional requirements, while avoiding redundant or unrelated items.
- **English with Vietnamese content**: Write checklist items and expected results in English, but preserve Vietnamese text exactly as shown in the UI when describing titles, product names, labels, or other direct Vietnamese content.
- **Draft structure**: Use only the allowed categories: `visual`, `state`, `element`, `responsive`, `compatibility`.
- **Draft behavior**: Leave `Actual` and `Status` blank in the generated draft.

## Workflow
1. Gather context
   - Read the specified functional requirement(s) and any supporting information in `setup/info`.
   - Review available UI images or screenshots supplied by the user to identify screens, layouts, and visible text.
   - Identify the relevant screen names, UI elements, and interaction flows that relate to the requirement.

2. Define checklist scope
   - Map the requirement to one or more screens (e.g. Product List, Checkout, Login, Cart).
   - Identify items for each interface aspect:
     - General UI standards: layout consistency, typography, label clarity, element visibility.
     - Forms: input labels, placeholders, validation clues, required field behavior.
     - Navigation: menu items, links, button affordance, focus order.
     - Feedback/state: loading states, error messages, success confirmations, disabled states.

3. Create checklist draft
   - Build a Markdown table in `setup/checklist/checklist-draft-<FRX>.md` using this exact header:
     |Id| Screen| Category| Checklist item| Expected| Actual| Status|
     |-|-|-|-|-|-|-|
   - Add rows for each identified item.
   - Use `visual`, `state`, `element`, `responsive`, or `compatibility` as the category.
   - Leave `Actual` and `Status` blank.
   - Keep checklist items concise and directly tied to observed UI or requirement behavior.

4. Preserve direct Vietnamese UI content
   - When describing UI labels, button text, or product names that appear in Vietnamese, keep the Vietnamese phrases exactly as visible.
   - Use English around those phrases so the checklist remains readable to English reviewers.

5. Maintain traceability and file naming
   - Name the file `checklist-draft-<FRX>.md`, where `<FRX>` is the functional requirement identifier.
   - If multiple requirements are covered in one draft, choose the primary FR identifier for the filename, or create separate draft files per requirement.

6. Logging
   - Append a session entry to `setup/logs/logs.md` after any use of this skill.
   - The log entry must include:
     - Name of the AI tool
     - Date and time (DD/MM/YYYY HH:MM)
     - Full text of the given prompt
     - Attached file names
     - Text Output
     - File Outputs
   - End the entry with `------`.

## Output expectations
- A draft checklist Markdown file in `setup/checklist/checklist-draft-<FRX>.md`.
- The checklist contains the required header line and one or more rows.
- The category values are limited to `visual`, `state`, `element`, `responsive`, and `compatibility`.
- `Actual` and `Status` are blank in the draft.
- A log entry is appended to `setup/logs/logs.md`.

## Completion checklist
- [ ] Checklist draft file created in `setup/checklist`.
- [ ] Checklist covers UI standards, forms, navigation, and feedback/state.
- [ ] Checklist items are based on requirement context and visible UI image content.
- [ ] Vietnamese UI text is preserved where direct content is referenced.
- [ ] `Actual` and `Status` columns are blank.
- [ ] Session log appended to `setup/logs/logs.md`.
