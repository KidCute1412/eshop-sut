---
name: decision-table-pairwise-testing
description: "Use when: creating black-box test cases for complex logic requirements using decision tables and optimizing test coverage with pairwise testing."
---

# Decision Table and Pairwise Testing

## Purpose
Use this skill to design black-box test cases for requirements involving complex business logic, interdependent conditions, and large input combinations. The workflow focuses on logical completeness via decision tables and efficiency via pairwise combinatorial testing.

## Automatic file access
When this skill is used, it should automatically consult these workspace folders:
- Read from [setup/info](../../../setup/info) for business rules, requirement logic, and system constraints.
- Read from [setup/skills](../../../setup/skills) for decision table logic and pairwise strategy guidance.
- Read from [setup/templates](../../../setup/templates) for the required Markdown templates.
- Read from [report-deliverables/logic_coverage_raw.txt](../../../report-deliverables/logic_coverage_raw.txt) for documenting logic derivation.
- Write outputs to [setup/logs](../../../setup/logs) for the session log.
- Write outputs to [setup/tables](../../../setup/tables) for generated decision tables, pairwise matrices, and test sets.

## Core principles
- **Black-Box Strategy**: Focus on observable system outputs based on defined input combinations.
- **Logic Mapping**: Use decision tables to ensure all combinations of conditions are identified and handled.
- **Combinatorial Efficiency**: Use pairwise testing (all-pairs) when the number of input combinations is too high to test exhaustively, ensuring every pair of input values is tested at least once.
- **Minimalism**: Avoid redundant tests; focus on high-impact logic paths.
- **Never Overwrite**: Always append new content to existing files in `[setup/logs]`, `[setup/tables]`, or similar, never overwrite.

## Workflow
1. Gather context
   - Analyze requirements to identify all conditions (inputs) and effects (outputs).
   - Identify dependencies or mutually exclusive conditions.

2. Build the Decision Table
   - List all conditions as rows and define possible states (e.g., True/False, or specific values).
   - Create rules (columns) representing combinations of conditions.
   - Map each rule to the expected system action.
   - Simplify the table by removing impossible combinations and merging redundant rules.

3. Toggle Pairwise Strategy (Optional)
   - If the number of combinations is unmanageable (typically > 15-20 scenarios), toggle to pairwise testing.
   - Create an interaction matrix of input parameters.
   - Generate a test set where every pair of input parameter values appears at least once in the test suite.

4. Create test cases
   - Derive test cases directly from the columns of the final decision table (or the pairwise suite).
   - Include the specific combination of inputs and the expected outcome.

5. Maintain test artifacts
   - Update `[setup/tables]` with the final decision table and/or pairwise test suite.
   - Maintain traceability between business requirements, decision rules, and test cases.

6. Write the reasoning note
   - Document the logic used to create the table.
   - Justify the decision to use or omit pairwise testing.
   - Clearly state any assumptions regarding input dependencies.

7. Execution and reporting
   - Mark tests as manual or automated. Note any limitations in the test environment that prevent specific logical scenarios from being verified.

8. Record the session log
   - Append to `[setup/logs/logs.md]`. Include: tool name, timestamp, prompt, and file output summary.
   - Add "------" at the end of the entry.

## Output expectations
- A structured Decision Table (and a Pairwise Matrix, if toggled).
- A corresponding Test Case Suite based on the logical rules.
- Updated Traceability Matrices.
- A concise reasoning note regarding the chosen logic coverage strategy.
- A new log entry.

## Completion checklist
- All logical combinations from the requirements are addressed.
- Decision table rules cover the full breadth of the business requirements.
- (If pairwise) All-pairs coverage is verified.
- The reasoning note clearly explains the logic mapping.
- All files are updated by appending, not overwriting.