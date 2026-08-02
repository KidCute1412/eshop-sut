# HW03 Authoring Workbench

This directory contains authoring utilities and manual completion guidance. It is not part of the submission package and must not be included in the final ZIP archive.

- `generate_derived_files.py`: generates the submission PDFs and consolidated Excel workbooks from Markdown and internal CSV sources.
- `data/`: canonical machine-readable usability data used to regenerate the submission workbook; excluded from the final ZIP.
- `archive/usability_legacy/`: reversible archive of the former multi-file usability templates; excluded from the final ZIP.
- `apply_watermark.py`: applies the required student identity overlay to authentic cross-platform screenshots.
- `finalize_submission.md`: lists the real-world evidence and packaging checks that remain before submission.
- `moderator_guide.md`: provides the moderator protocol for the pilot and seven official usability sessions.
- `calculate_sus.py`: validates genuine 1–5 responses and calculates participant/aggregate SUS scores; it never supplies missing responses.
- `automation/`: contains the deterministic Google Chrome checklist harness, the Firefox cross-browser capture runner, raw results, and checklist reconciliation script.
- `validate_submission.py`: verifies checklist counts, evidence mappings, derived files, and submission consistency.
