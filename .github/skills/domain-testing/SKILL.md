---
name: domain-testing
description: "Use when: creating black-box test cases with domain testing, equivalence partitioning, and boundary value analysis for functional requirements."
---

# Domain Testing and Equivalence Partitioning

## Purpose
Use this skill to design black-box test cases for functional requirements when the behavior can be described by input domains, valid and invalid ranges, and boundary conditions. The workflow must be grounded in the provided requirements, setup information, API documentation, and observable behavior only.

## Automatic file access
When this skill is used, it should automatically consult these workspace folders for context and artifacts:
- Read from [setup/info](../../../setup/info) for requirements, setup details, and black-box constraints.
- Read from [setup/skills](../../../setup/skills) for the domain-testing, equivalence-partitioning, and logging guidance.
- Read from [setup/templates](../../../setup/templates) for the required Markdown templates.
- Read from [report-deliverables/domain_bva_raw.txt](../../../report-deliverables/domain_bva_raw.txt) as the explanation/output file for documenting how equivalence classes and boundary values are used.
- Write outputs to [setup/logs](../../../setup/logs) for the session log.
- Write outputs to [setup/tables](../../../setup/tables) for generated test tables and related documentation.

## Core principles
- Treat the system as a black box. Do not inspect or infer implementation details from source code.
- Base all work on the provided setup materials, API specification, functional requirements, and runtime information.
- Use domain testing, equivalence partitioning, and boundary value analysis to identify representative inputs.
- Prefer clear, minimal, and non-redundant test cases. Each test should cover at least one unique equivalence class or boundary condition.
- If information is missing or ambiguous, explicitly state the assumption instead of guessing.

## Workflow
1. Gather context
   - Read the relevant functional requirement, API specification, setup notes, and any available runtime instructions.
   - Identify the relevant input and output variables, constraints, and expected behavior.

2. Partition the domain
   - For each input or output condition, identify valid and invalid equivalence classes.
   - Use the rules of equivalence partitioning:
     - Range-based conditions -> one valid class and two invalid classes.
     - Set-based conditions -> one class per allowed value and one invalid class.
     - "Must be" conditions -> one valid and one invalid class.
     - Split a class further if the program is likely to handle its members differently.

3. Apply boundary analysis
   - For ordered domains, choose boundary values and nearby values.
   - Prefer 2-point or 3-point boundary values when appropriate.
   - Include the minimum and maximum valid boundary values as well as adjacent values just inside and just outside the boundary.

4. Create test cases
   - Create test cases that cover each equivalence class at least once.
   - Avoid redundant tests when multiple values belong to the same class.
   - Record the partition tested, representative input values, and expected result.

5. Maintain test artifacts
   - Create or update the equivalence class table and test case table by using the provided templates.
   - Prefer storing generated artifacts in [setup/tables](../../../setup/tables) when a dedicated table file is needed.
   - Update the traceability matrices for:
     - functional requirements to tests
     - equivalence classes to tests
     - bugs to tests when bug data is available
   - Keep the artifacts concise, structured, and evidence-based.

6. Write the reasoning note
   - Create a step-by-step note explaining how the equivalence classes and boundary values were derived.
   - Keep the explanation precise and factual; do not invent unseen behavior.
   - Mention assumptions and unresolved ambiguity clearly.

7. Execution and reporting
   - If scripts or runnable commands are available, use them to execute or validate relevant cases when appropriate.
   - If execution is not possible, mark the test as manual, blocked, or not tested and explain why.
   - Bug screenshots and deeper documentation should be handled by the user unless otherwise instructed.

8. Record the session log
   - Append a session entry to [setup/logs/logs.md](../../../setup/logs/logs.md) following the project's logging rules.
   - Include the AI tool name, timestamp, prompt, attached files, text output, and file outputs.
   - Add the separator line "------" at the end of the new entry.

## Output expectations
- A list of equivalence classes with partitions and representative values.
- A corresponding set of test cases with clear expected results.
- Updated traceability matrices that connect requirements, equivalence classes, and tests.
- A short reasoning note describing the methodology used.
- A new log entry in the project session log.

## Completion checklist
- Every relevant requirement has at least one derived test case.
- Each equivalence class is represented by at least one test case.
- Boundary values are considered for ordered inputs.
- The reasoning note is factual and does not claim implementation details.
- The session log has been updated.
