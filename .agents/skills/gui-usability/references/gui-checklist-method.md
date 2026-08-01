# GUI Checklist Method (Task 1)

The checklist is not written from scratch: it starts from the professor's provided
`Web GUI checklist Template.xlsx`, then is extended with AI-generated items and human-added items.
Every item must still be traceable to that template, a requirement, a general usability heuristic,
or an explicit human observation of the real interface.

## Starting Point: the Professor's Template

`Web GUI checklist Template.xlsx` has a `GUI list` index sheet plus one sheet per screen, each with
the same three-section taxonomy:

- **Section 1 — GIAO DIỆN NGƯỜI DÙNG (General UI)**: 1.1 Links, 1.2 Colors, 1.3 Content, 1.4
  Images, 1.5 Form (1.5.1 Format, 1.5.2 Numeric field validation, 1.5.3 Alphanumeric field
  validation).
- **Section 2 — USABILITY**: 2.1 Navigation, 2.2 General usability.
- **Section 3 — TÍNH TƯƠNG THÍCH (Compatibility)**: 3.1 Browser, 3.2 Device, 3.3 Printer.

`assets/checklist-template.md` already transcribes this taxonomy verbatim (`Source:
Template-Provided`), tagged with the IA mapping in `references/checklist-item-schema.md`. Do not
retype it from the PDF/xlsx by hand — copy the workspace with
`scripts/create_checklist_workspace.py` and adapt the generic wording to the concrete EShop screen
you selected (e.g. "Phần tìm kiếm được hiển thị nổi bật" -> check the actual search bar on
`frontend-web/src/pages/Home.jsx`).

## Where the Template Falls Short (and Why AI Must Fill It)

The professor's template, by itself, does **not** give adequate coverage of two things HW03
explicitly requires:

1. **IA-04 Feedback/State**: the template has exactly one relevant item (`2.2.12`, a generic
   progress-notification check). EShop-specific feedback behaviour — the add-to-cart toast, the
   cart badge, the remove-item confirmation dialog, the empty-cart/empty-search illustration, the
   invalid-coupon error message — is not represented at all.
2. **Accessibility / dark mode / RTL**: entirely absent from the template, and exactly the
   categories the HW03 PDF calls out as commonly missed by both templates and AI.

`assets/checklist-template.md` already reserves two placeholder subsections for this:
`1.6 KHẢ NĂNG TIẾP CẬN & GIAO DIỆN NÂNG CAO` (IA-01, accessibility/dark-mode/RTL) and
`2.3 PHẢN HỒI / TRẠNG THÁI` (IA-04, feedback/state). Their items are literal `TODO -- generate via
AI` placeholders — generate real items for these two subsections first; this is the single
clearest, most auditable place the AI-First workflow does real work.

## AI-Assisted Generation Procedure

1. Give the AI the actual scope: the selected screen, the two gap subsections (1.6 and 2.3) with
   their placeholder rows, and the relevant `README.md` FR text (FR-21..FR-24 plus any feature FR
   touching that screen, e.g. FR-07/FR-08 for Cart/Checkout feedback). A vague prompt ("generate a
   GUI checklist") is explicitly disallowed by the assignment's AI-First principle — prompt once
   per gap subsection so the output stays auditable step by step.
2. Ask the AI to justify each new item with a one-line rationale (requirement reference or
   heuristic name) — this feeds the `Requirement / Heuristic Reference` column and makes the later
   human gap-analysis meaningful instead of a black box.
3. Save the AI's raw, unedited output before any correction
   (`reports/gui-checklist/GUI-<ID>/ai-initial-output.md`).
4. Merge the reviewed AI items into the `1.6.x` / `2.3.x` rows (or new rows appended after them)
   with `Source: AI-Generated`, replacing the `TODO` placeholders.
5. Beyond the two reserved subsections, also prompt the AI to review Sections 1-2 for anything
   EShop-specific the generic template wording doesn't quite capture (e.g. the ₫ currency-format
   rule in `README.md` FR-21, the exact Vietnamese button labels in FR-23) and add those as new
   `AI-Generated` items too.

## Human Critique Procedure

For each screen actually opened in a browser, look specifically for:

- Anything only visible by actually triggering the state (a specific truncated string at a
  particular viewport width, a specific contrast failure, a specific race condition between a
  loading spinner and an empty-state message) — the AI reasoned from requirement text and cannot
  see the rendered page.
- Gaps in the AI's own 1.6/2.3 output — did it cover keyboard-only operability? Screen-reader label
  association? The specific dark-mode toggle (or lack of one) on this exact screen?
- Anything Section 3 (Compatibility) hints at but doesn't fully specify for EShop, e.g. how the
  ₫-formatted price wraps at a narrow viewport.

For every such item, record a specific `AI-Miss Reason` — not a generic "AI doesn't know
accessibility" but why *this* prompt, *this* model turn, or *this* interface characteristic caused
the omission.

## Execution Discipline

- Leave both `Yes` and `No` empty before real testing (`Not Executed`); mark exactly one after
  actually operating the SUT.
- Marking `No` requires a concrete `Remarks` reason and a real screenshot; marking `Yes` requires
  neither.
- `Section`-type rows (category headings) are never marked `Yes`/`No` themselves — only their child
  `Item` rows are.
- Do not infer Yes/No from reading requirement text alone — open the actual page.
- Section 3 (Compatibility) rows get their first pass on the baseline platform like everything
  else, then are re-executed per platform in Task 3 — that repetition is the point of a
  compatibility check.
