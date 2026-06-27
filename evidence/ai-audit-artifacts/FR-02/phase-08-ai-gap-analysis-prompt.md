Use the `domain-testing-bva` skill to perform only Phase 8: AI Gap Analysis for FR-02 Login and Account Lockout.

Project root: current repository
Feature: FR-02 Login and Account Lockout
Output: reports/FR-02/ai-gap-analysis.md

Read:

- reports/FR-02/requirement-analysis.md
- reports/FR-02/domain-testing.md
- reports/FR-02/boundary-value-analysis.md
- reports/FR-02/test-cases.md
- reports/FR-02/bug-report.md
- reports/FR-02/evidence/
- ai-audit/ai-audit.md
- evidence/agent-skill/FR-02/phase-03-domain-modeling-ai-output.md
- evidence/agent-skill/FR-02/phase-04-bva-ai-output.md
- evidence/agent-skill/FR-02/phase-05-test-case-design-ai-output.md

Perform only these tasks:

1. Compare the preserved initial AI artifacts with the current human-reviewed reports.
2. Identify:
   - partitions or boundaries corrected by the human;
   - test cases added, removed, reclassified, or rewritten by the human;
   - unsupported or incomplete AI assumptions;
   - test cases genuinely missed by AI;
   - runtime behaviours and bugs discovered after execution.
3. For every gap, record:
   - Gap ID
   - Category
   - Initial AI Output
   - Human Correction or Runtime Finding
   - Why AI Missed or Mishandled It
   - Corrective Action
   - Related requirement, partition, boundary, test case, evidence, or bug
4. Verify all counts from the files; do not assume the counts stated in this prompt.
5. Clearly distinguish:
   - an AI-missed test case;
   - a human improvement to an existing test;
   - a runtime bug discovered by executing an AI-generated test.
6. Do not claim AI missed a bug when the AI generated the test that later exposed it.
7. Add an AI Gap Summary and Lessons Learned section.
8. Add a Human Review section with:
   - Reviewer: Pending
   - Review Date and Time: Pending
   - Human Review Status: Pending
   - Human Corrections: Pending

Do not:

- inspect implementation source code;
- execute tests;
- modify test results, statuses, or evidence;
- invent gaps, bugs, evidence, or GitHub Issue links;
- modify files other than ai-gap-analysis.md and the AI audit records.

Save this prompt and the complete initial AI output under evidence/ai-audit-artifacts/FR-02/.
Append this interaction to ai-audit/ai-audit.md.
Report the created and modified files when finished.
