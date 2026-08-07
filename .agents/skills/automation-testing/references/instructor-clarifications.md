# Instructor Clarifications

1. The assignment header states `Form: Individual Assignment`, but §5 still says "Within each
   group, ensure that your selection is not duplicated among the members of the group." Treat this
   as an unresolved instruction ambiguity carried over from HW02/HW03: record it explicitly in the
   report rather than silently assuming either interpretation, and follow whatever the course's
   actual cohort/grouping practice turns out to be.
2. Feature selection is explicitly tied to HW02: "Automate the same three (3) web features you
   selected in HW02." Do not pick new features for HW04 unless HW02 genuinely was not completed, in
   which case self-declare and state the reason in the report.
3. "At least 12 test cases" per feature may be any mix of positive/negative/edge — there is no
   sub-minimum per category, unlike some other assignments in this course. Do not assume you need
   exactly 4 of each.
4. The 8-commit minimum for the Git Commit Log is scoped narrowly: only commits that change
   `.spec.js`/`.spec.ts` (or the Selenium equivalent) count. A commit that only touches the README,
   the PDF, or other non-test documents does not count, even if it's a real, meaningful commit for
   other purposes — plan the commit cadence accordingly rather than discovering this near the
   deadline.
5. The 8 commits must also span **at least 4 different days** — a burst of 8 same-day commits does
   not satisfy this rule even if each one individually touches a spec file.
6. "Run by: {StudentID}" plus an ISO timestamp in the HTML report is explicitly named as an
   anti-cheat-verified field (§11). Configure it once in the reporter/test setup so every real run
   produces it automatically — do not hand-edit a generated report afterward to add the string,
   since a TA comparing report internals against a hand-edited HTML file is exactly the kind of
   check this rule anticipates.
7. Per §7, the Agent Skill's own demo video is a **separate** requirement from Task 2's demo video,
   though the PDF does not forbid the same recording session from satisfying both if it happens to
   cover a complete feature end-to-end with the skill visibly in use.

When sources conflict, retain the official expectation, label the ambiguity or contradiction
explicitly, and verify only through real, reproducible script runs — never through a hand-edited
report or a description of what a run would show.
