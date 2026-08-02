# Instructor Clarifications

1. GUI checklist items and usability findings must be grounded in the SUT's actual user-interface
   requirements (`README.md` FR-21..FR-24) and general usability heuristics — not invented rules.
2. AI-First does not mean one generic prompt ("find usability problems in this app"). The AI must
   be guided through each discrete step of the technique: checklist generation by interface aspect,
   scenario drafting, probe-question drafting, note synthesis — each reviewed separately.
3. Human review is mandatory for every AI output. The student is fully responsible for correctness;
   submitting raw AI output is not acceptable.
4. The AI Audit Report must be a complete, appended (never overwritten) log of AI tool, timestamp,
   verbatim prompt, and AI output for every interaction.
5. Reports must explain the complete derivation of checklist items and usability findings, not
   merely summarize them.
6. Task 2 participants, their contact details, and their responses must be genuine. Nothing in the
   participant table or session notes may be AI-generated or fabricated. A TA may call two
   participants to verify identity and participation.
7. Cross-platform screenshots must show the student ID and full name, and per the tooling section
   must also overlay the username in the form of the student email; the browser/OS/device name and
   the SUT's localhost URL must be visible in the same screenshot.
8. Demonstrate work through frequent, per-step Git commits, and provide the commit log as a
   text-based file.
9. Agent Skills are normally individual work and must be demonstrated end-to-end (video, voice-over
   or captions acceptable) on one complete screen or flow.
10. Never fabricate a Passed/Failed status, a bug, a screenshot, a participant, a SUS/UEQ-S
    response, an execution result, or a GitHub Issue link.
11. The assignment header states `Form: Individual Assignment`, but §5 of the PDF also says
    "Within each group, ensure that your selection is not duplicated among the members of the
    group." Treat this as an unresolved instruction ambiguity: record it explicitly in the report
    rather than silently assuming either interpretation, and follow whatever the course's actual
    cohort/grouping practice turns out to be.
12. The lecturer clarified in class (student-reported, not in the written PDF) that Task 2 only
    requires the 7 real participant session `create_usability_workspace.py` and `validate_usability_session.py` still default to
    requiring a pilot (the PDF's Phase 1 step, and the safer general practice for future
    assignments where no such waiver exists) — pass `--no-pilot-required` to
    `validate_usability_session.py` when this specific clarification applies.

When sources conflict, retain the official expectation, label the ambiguity or contradiction
explicitly, and verify only through observable, real execution or real participant sessions.
