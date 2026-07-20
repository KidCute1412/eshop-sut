---
name: state-transition-testing
description: "Use when: testing systems with finite state machines where output depends on the current state and the input. Focuses on sequences of actions to transition between states."
---

# State Transition Testing

## Purpose
Design black-box test cases by modeling the system as a finite state machine. Identify states, transitions, events, and actions to ensure the system behaves correctly across life cycles.

## Automatic file access
- Read from [setup/info](../../../setup/info) for requirements and constraints.
- Read from [setup/templates](../../../setup/templates) for documentation templates.
- Write/Read from [setup/plans](../../../setup/plans) for analysis and test design.
- Write/Read from [setup/tests](../../../setup/tests) for individual test case files.
- Write to [setup/logs](../../../setup/logs) for the session log.

## Workflow

### Phase 1: Test Case Design Analysis & Plan
1. **Scope Assessment**: Determine if the requirement (e.g., FR-XX) involves state-dependent behavior. If not, state why the skill is inapplicable.
2. **Model Identification**: 
   - Define all possible **States** (e.g., Idle, Processing, Error).
   - Identify **Events/Inputs** that trigger transitions.
   - Define **Actions/Outputs** resulting from transitions.
3. **Plan Formulation**: 
   - Draft a State Transition Matrix (States vs. Inputs).
   - Estimate the number of test cases required for path coverage (e.g., All-States, All-Transitions).
4. **Output**: Save as `[RequirementID]-STT.md` in `[setup/plans]`.

### Phase 2: Test Case Creation
1. **Sequence Generation**: Convert the reviewed plan into sequential test cases (State -> Event -> Expected State -> Expected Action).
2. **Documentation**: Each test case must be saved as a dedicated file `[RequirementID]-TC[Number]-STT.md` in `[setup/tests]`, using the standardized template.
3. **Traceability**: Ensure each transition is covered by at least one test case.

## State Transition Testing Core Principles
- **State Identification**: A state is a condition where the system waits for an event.
- **Transition Rules**: A transition is triggered by an event and may result in an action.
- **Coverage Criteria**:
  - **All-States**: Each state is visited at least once.
  - **All-Transitions**: Each transition is traversed at least once.
- **Negative Testing**: Include "invalid" transitions (events occurring in states where they are not allowed) to verify error handling.

## Execution and Logging
- All activities must be recorded in `[setup/logs/logs.md]`.
- Always append to logs; never overwrite.
- Include the AI tool name, timestamp, prompt, and file references.
- End every log entry with: `------`

## Completion Checklist
- [ ] Phase 1 plan created and saved to `[setup/plans]`.
- [ ] User review completed.
- [ ] Phase 2 test cases created and saved to `[setup/tests]`.
- [ ] All transitions mapped and tested.
- [ ] Session log updated.