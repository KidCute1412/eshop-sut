# AI Gap Analysis - {{SOURCE_LABEL}}

## Scope

- Screens covered: see `reports/gui-checklist/gui-list.md`
- Initial AI artifacts: `reports/gui-checklist/GUI-<ID>/ai-initial-output.md` per screen (preserved,
  pre-review)
- Reviewed artifacts: `reports/gui-checklist/GUI-<ID>/checklist.md` per screen
- Execution evidence reviewed: `reports/gui-checklist/GUI-<ID>/evidence/`
- Source-code inspection used: No

## Summary Comparison

| Area | Initial AI Output | Current Reviewed Output | Change Type |
| --- | --- | --- | --- |
| Total Item-row count | TODO | TODO | TODO |
| IA-01 coverage | TODO | TODO | TODO |
| IA-02 coverage | TODO | TODO | TODO |
| IA-03 coverage | TODO | TODO | TODO |
| IA-04 coverage (Section 2.3 + item 2.2.12) | TODO | TODO | TODO |
| Accessibility/Dark-mode/RTL coverage (Section 1.6) | TODO | TODO | TODO |

## Gap Findings

| Gap ID | Category | AI-Generated Item Missing This | Human-Added Item | Why the AI Missed It | Related No. |
| --- | --- | --- | --- | --- | --- |
| GAP-GUI-001 | Accessibility / Dark mode / RTL / Prompt quality / Model limitation / Interface characteristic / No gap identified | TODO | TODO | TODO | TODO |

## Classification Notes

- Sections 1.6 (Accessibility/Dark mode/RTL) and 2.3 (Feedback/State) do not exist in the
  professor's base template — every real item filled into those two subsections is, by
  construction, something the base template missed. The gap analysis here is specifically about
  what the AI *also* missed on top of that, or where the AI's first draft for 1.6/2.3 was still
  incomplete/wrong once a human actually checked the SUT.
- Prompt quality: the initial prompt did not ask about this category at all.
- Model limitation: the prompt did ask broadly, but the model's output still did not generalize to
  this case.
- Interface characteristic: this EShop screen has a specific quirk (e.g. a particular truncation, a
  particular missing state) that only shows up by actually using it.
- Runtime bug discovered by an AI-generated item: this is a successful AI-assisted finding, not an
  "AI-missed" gap — do not conflate the two.

## Lessons Learned

- TODO

## Human Review

- Reviewer: TODO
- Review Date and Time: TODO
- Review Scope: AI Gap Analysis for {{SOURCE_LABEL}}
- Corrections Recorded: TODO
- Approved: No
