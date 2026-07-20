---
name: use-case-testing
description: "Use when: testing functional requirements by deriving test cases from user scenarios, involving actors, primary flows, and alternative/exception branches."
---

# Use Case Testing

## Purpose
Design black-box test cases by modeling user-system interactions. Identify actors, preconditions, postconditions, and diverse interaction flows (happy path, alternatives, and exceptions) to ensure functional requirements are met from a user perspective.

## Automatic file access
- Read from [setup/info](../../../setup/info) for requirements and constraints.
- Read from [setup/templates](../../../setup/templates) for documentation templates.
- Write/Read from [setup/plans](../../../setup/plans) for analysis and test design.
- Write/Read from [setup/tests](../../../setup/tests) for individual test case files.
- Write to [setup/logs](../../../setup/logs) for the session log.

## Workflow

### Phase 1: Test Case Design Analysis & Plan
1. **Scope Assessment**: Determine if the requirement (e.g., FR-XX) can be modeled via user interactions. If not, state why the skill is inapplicable.
2. **Model Identification**: 
   - Define the **Actor(s)** involved.
   - Outline the **Primary Use Case** (Happy Path).
   - Identify **Branching Use Cases** (Alternative flows, exception handling, and error branches).
3. **Plan Formulation**: 
   - Map out the relationships between the primary use case and its branches.
   - Estimate the number of test cases required to cover all identified flows.
4. **Output**: Save as `[RequirementID]-UCT.md` in `[setup/plans]`.

### Phase 2: Test Case Creation
1. **Scenario Generation**: Convert the reviewed plan into detailed test cases covering all identified flows (Preconditions -> Steps -> Expected Results -> Postconditions).
2. **Documentation**: Each test case must be saved as a dedicated file `[RequirementID]-TC[Number]-UCT.md` in `[setup/tests]`, using the standardized template.
3. **Traceability**: Ensure each identified use case (primary and branches) is covered by at least one test case.

## Use Case Testing Core Principles
- **Scenario-Based**: Focus on the user's goal and the system's reaction.
- **Branch Coverage**: Ensure all alternative and exception flows are tested, not just the happy path.
- **Pre/Post-Conditions**: Explicitly define the state required to start the use case and the state expected upon completion.
- **Negative Testing**: Specifically model exception flows (e.g., invalid input, permission denied, system errors) as use case branches.

## Execution and Logging
- All activities must be recorded in `[setup/logs/logs.md]`.
- Always append to logs; never overwrite.
- Include the AI tool name, timestamp, prompt, and file references.
- End every log entry with: `------`

## Completion Checklist
- [ ] Phase 1 plan created and saved to `[setup/plans]`.
- [ ] User review completed.
- [ ] Phase 2 test cases created and saved to `[setup/tests]`.
- [ ] Primary, alternative, and exception flows mapped and tested.
- [ ] Session log updated.