# GUI Checklist Schema

The checklist format follows the professor's `Web GUI checklist Template.xlsx` exactly for the
columns it already defines (`No.`, `Checkpoint`, `Yes`, `No`, `Remarks`), with extra columns
appended for what HW03 additionally requires (IA tagging, AI provenance, evidence, bug linking).
One Markdown file per screen (see `assets/checklist-template.md`), indexed by
`assets/gui-list-template.md` (mirrors the xlsx's "GUI list" sheet).

## Per-Screen File Header

Each screen's checklist file starts with three metadata lines, matching the xlsx sheet header
rows `GUI ID` / `GUI name` / `GUI detail`:

```text
- GUI ID: 01
- GUI Name: Trang chủ (Home)
- GUI Detail: <optional extra context>
- Platform: Baseline   (or the platform name for a Task 3 copy)
```

## Table Columns

| Column | Required | Notes |
| --- | --- | --- |
| No. | Always | Dotted hierarchical number matching the professor's taxonomy, e.g. `1`, `1.1`, `1.1.1`, `1.5.1.3`. Stable once reviewed. |
| Type | Always | `Section` (a category/subcategory heading, not independently tested) or `Item` (an actual checkpoint). |
| Checkpoint | Always | The question text. For `Section` rows this is the category name (e.g. `MÀU SẮC (COLORS)`); for `Item` rows this is the actual checkable question. |
| IA | Always | One of `IA-01`, `IA-02`, `IA-03`, `IA-04`, `Task-3` (Section 3 Compatibility rows — re-executed per platform in Task 3, not one of the four interface aspects), or `Mixed` (top-level `2` header only, whose children are individually tagged). |
| Requirement / Heuristic Reference | Required for `Item` rows | `README.md FR-21`, `README.md FR-24`, a named usability heuristic, or `Human observation` with the basis explained in Remarks. `N/A` for `Section` rows. |
| Platform | Always | `Baseline` for the Task 1 file; the platform name (`Chrome`, `Firefox`, `Safari`, `Android Chrome`, `Expo Go`, ...) for a Task 3 copy. |
| Source | Always | `Template-Provided` (from the professor's xlsx, unmodified in substance), `AI-Generated`, or `Human-Added`. |
| AI-Miss Reason | Required if `Source = Human-Added`; `N/A` otherwise | See `references/gui-checklist-method.md`. |
| Yes | Item rows only, after execution | Mark `X` when the checkpoint passes. Leave both `Yes` and `No` empty before execution (`Not Executed`). |
| No | Item rows only, after execution | Mark `X` when the checkpoint fails. Exactly one of `Yes`/`No` is filled after execution; never both. |
| Remarks | Required when `No` is marked | The concrete, observed failure reason (this is the assignment's required "Notes" column, using the professor's own column name). |
| Evidence | Required when `No` is marked; must be empty otherwise | Real path, e.g. `reports/gui-checklist/GUI-01/evidence/1.1.6.png`, or a real URL. |
| Bug ID | Optional | Links to `bug-report.md` / a GitHub Issue when the failure is filed as a bug. |

## Section -> Interface Aspect Mapping

The professor's taxonomy does not use the HW03 IA-01..04 labels directly; this skill maps them so
the required IA coverage can still be validated and reported:

- Section 1 (`GIAO DIỆN NGƯỜI DÙNG` / General UI) -> **IA-01**, except:
  - Section 1.5 (`FORM`) and its subsections -> **IA-02**.
  - Section 1.6 (`KHẢ NĂNG TIẾP CẬN...`, added by this skill) -> **IA-01**.
- Section 2 (`USABILITY`) is `Mixed` at the top level:
  - Section 2.1 (`TÍNH ĐIỀU HƯỚNG` / Navigation) -> **IA-03**.
  - Section 2.2 (`TÍNH TIỆN DỤNG`) -> **IA-01**, except item `2.2.12` (progress notification) ->
    **IA-04**.
  - Section 2.3 (`PHẢN HỒI / TRẠNG THÁI`, added by this skill) -> **IA-04**.
- Section 3 (`TÍNH TƯƠNG THÍCH` / Compatibility) -> **Task-3**. These rows are not counted against
  the IA-01..04 coverage requirement; they are the literal content of Task 3 and are meant to be
  re-executed per platform.

Sections 1.6 and 2.3 do not exist in the professor's xlsx. They are added because the base
template covers IA-04 (Feedback/State) only through item 2.2.12, and does not cover accessibility,
dark mode, or RTL at all — gaps the HW03 PDF explicitly calls out as commonly AI-missed. Generate
their items with AI per `references/gui-checklist-method.md`, then critique/extend by hand.

## ID/Numbering Convention

Keep `No.` values stable once human-reviewed. When adding a new `Item` under an existing
`Section`, append the next sub-number (e.g. adding to `1.2` produces `1.2.12`). When adding an
entirely new `Section`, use the next top-level or sub-level number consistent with the existing
hierarchy (e.g. a new subsection under `1` would be `1.7`, not a renumbering of `1.6`).

## Validation

Run `scripts/validate_checklist.py <checklist-file-1> [<checklist-file-2> ...]` before requesting
human review and again after execution. **Pass every screen's `checklist.md` together in one
invocation** when you want the combined `>40` check to run — the assignment's ">40 items" minimum
is a total for the checklist you design, which may (and often should) span several screens; it is
not a per-screen minimum. A screen with 20 well-justified, non-repetitive items is fine as long as
the combined total across all screens you validate together exceeds 40. Pass
`--no-min-items-check` to validate a single screen in isolation while you are still iterating on
the others.

The script enforces:

- Combined `Item`-type row count strictly greater than 40 across every file passed in the same
  invocation (skippable with `--no-min-items-check`).
- All four IA categories (`IA-01`..`IA-04`) present among `Item` rows **within each individual
  file**, with at least one item each.
- Every `Human-Added` item has a non-empty, non-placeholder `AI-Miss Reason`.
- No `Item` row's `Checkpoint` is still a placeholder (`TODO`/`TBD`).
- Exactly one of `Yes`/`No` is marked for an executed item; neither marked means `Not Executed`.
- Every item with `No` marked has non-empty `Remarks` and an existing evidence file (or a valid
  URL); items with `Yes` marked or unexecuted must not carry an `Evidence` value.
- No duplicate `No.` within a file.
