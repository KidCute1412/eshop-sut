# AI Gap Analysis - FR-20 Login and Account Lockout (Mobile)

## Scope

This analysis compares the initial AI-generated FR-20 design/execution output with the current reports in `reports/FR-20/`. No implementation source code, database schema, or internal tests were inspected.

## AI Gap Summary

| Category | Count |
| -------- | ----- |
| AI-missed test case | 0 |
| Human improvement | 0 |
| Runtime bug from AI-generated test | 1 |
| Runtime/environment blocker | 1 |
| Unsupported or incomplete AI assumption | 1 |

Because this was completed in one AI-assisted pass without a separate human correction cycle, no human-added or human-rewritten test cases are recorded yet. The runtime bug was discovered by executing an AI-generated BVA case, so it is not classified as an AI-missed bug.

## Gap Details

| Gap ID | Category | Initial AI Output | Human Correction or Runtime Finding | Why AI Missed or Mishandled It | Corrective Action | Related Artifact |
| ------ | -------- | ----------------- | ----------------------------------- | ------------------------------ | ----------------- | ---------------- |
| FR20-GAP-001 | Runtime bug from AI-generated test | FR20-BVA-003 expected valid login after more than 30 seconds. | Execution still returned HTTP `403 Forbidden` after 31 seconds and after retry around 66 seconds. | The bug is knowable only through runtime execution; the requirement itself states 30 seconds. | Record FAIL and create BUG-FR20-001. | FR20-BVA-003; `bug-report.md`; evidence `FR20-BVA-003*.txt` |
| FR20-GAP-002 | Runtime/environment blocker | Mobile UI partitions and cases were generated for screen, required markers, password masking, and error placement. | Mobile UI cases were Blocked because no Expo Go device, emulator, simulator, or observable mobile runtime was available through the current tool interface. | AI cannot observe a mobile UI without a runtime surface. | Mark UI-only cases Blocked with blocker evidence, not Pass/Fail. | FR20-DT-007 through FR20-DT-010; `FR20-DT-UI-BLOCKER.json` |
| FR20-GAP-003 | Unsupported/incomplete assumption | Mobile email input semantics were mapped from web `type="email"` to mobile equivalent semantics. | The exact React Native equivalent is ambiguous in requirements. | Requirements use web-specific language while FR-20 targets mobile. | Keep expectation as mobile equivalent keyboard/content-type semantics and require human/mobile observation later. | FR20-R09, FR20-FORM02, FR20-DT-008 |

## Lessons Learned

- For mobile features, plan a mobile-runtime availability check before UI execution.
- Keep public API coverage separate from mobile UI coverage; API Pass does not prove mobile screen/form conformance.
- Account-lockout duration is a strong BVA target because the requirement states an ordered 30-second bound.
- Runtime bugs found by AI-generated cases should be credited as execution findings, not mislabeled as missed by AI.

## Human Review

- Reviewer: Pending
- Review Date and Time: Pending
- Human Review Status: Pending
- Human Corrections: Pending
