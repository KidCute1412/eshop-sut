# Output contract

Use UTF-8 CSV or an equivalent spreadsheet with these minimum columns.

## GUI checklist

`check_id, requirement_id, interface_aspect, screen, precondition, action, expected_result, actual_result, status, environment, evidence_ref, defect_id, origin, notes`

Allowed status values: `Pass`/`Passed`, `Fail`/`Failed`, `Blocked`, and `Not Executed`. Select one naming convention and use it consistently within a project.

## Defects

`defect_id, title, severity, environment, preconditions, steps, test_data, expected_result, actual_result, reproducibility, checklist_ids, evidence_refs, issue_url`

Allowed severity values: `Critical`, `High`, `Medium`, `Low`.

## Usability sessions

`session_id, participant_id, consent, completion, duration_seconds, errors, hesitations, interventions, sus_score, notes_ref, recording_ref, evidence_status`

Keep participant identity/contact details in a separate access-controlled register. A session result must not be marked verified without source notes or a recording allowed by the evidence policy.

## Cross-platform runs

`run_id, browser_version, os, device, viewport, sut_url, executed_at, flow, result, evidence_refs, notes`

## Summary rules

- Counts are derived from rows, never typed independently without reconciliation.
- A `Fail` references a defect; a defect references at least one failed check.
- Evidence paths are relative to the deliverables root when possible.
- Pending fields use an explicit marker; they are never left ambiguous.
