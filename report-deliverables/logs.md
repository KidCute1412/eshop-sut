- Name of the AI tool: GitHub Copilot
- Date and time: 27/06/2026 11:14
- Full text of given prompt: I want to create an agent skill for domain testing, this skill will be used to apply the methods of domain testing and equivalence partitioning whenever appropriate for making tests, this skill will also record and write down any session of test making to logs.md following the rules of logs editing. This agent skill will be purely black-box, meaning it cannot access nor have a clear grasp on the source code, however, it can gain access to the program's info and setup, as well as the requirements. The process will be as follows:
  - The agent will be given (or is already given) info about the program and how it is run
  - The agent will be assigned a functional requirement to create test-cases.
  - Following the methods of black-box testing, domain testing and equivalence partitioning with boundary values, a list of equivalence classes will be identified and similarly, a list of test cases from those classes.
  - Using the templates, the agent will first create tables (if not yet existed) and add tests and equivalence classes, while updating the 3 types of traceability matrices about functional requirements, equivalence classes and test cases.
  - The agent will then write down in a file in step-by-step details about how techniques of domain testing and boundary value analysis are used for test cases creation. This part must be written with clear, precise concepts, maintaining truths and avoiding hallucinations.
  - If possible, the agent can use scripts to view and execute some test cases, otherwise this will be done manually by the user.
  - The bug screenshots and documentation will be done primarily by the user.
  - After any session of the agent, a log must be recorded within logs.md following the format.
  Note that after this session also, a log should also be written in logs.md
- Attached file names: setup/skills/domain-testing.md; setup/skills/equivalence-partitioning.md; setup/skills/logs-editing.md; setup/logs/logs.md; setup/templates/traceability_matrix.md; setup/templates/bug_table.md; setup/templates/equivalence_class_table.md; setup/templates/test_table.md; setup/info/functional_requirements.md
- Text Output: I’m creating the requested skill from the workflow you described and will also add the required session log entry in the project logs.

The workspace does not already contain a skill definition, so I’m checking the repository’s conventions before placing the new one.

I’ve drafted the skill structure and am saving it in the workspace so it can be used directly for future test-design sessions.

The skill file is in place, and I’m appending the required session log entry to the project log now.

Edited
logs.md+17-1
✅ Skill created and logged
The new skill is now available at .github/skills/domain-testing/SKILL.md, and the required session entry was added to setup/logs/logs.md.

What the skill covers
Black-box domain testing
Equivalence partitioning
Boundary value analysis
Test artifact creation from the provided templates
Traceability matrix updates
A step-by-step reasoning note
Session logging in the project log format
Next step
You can invoke it in future sessions by referencing the skill name: domain-testing.
- File Outputs: .github/skills/domain-testing/SKILL.md
------
- Name of the AI tool: GitHub Copilot
- Date and time: 27/06/2026 11:24
- Full text of given prompt: can i modify it to automatically access the info folder, the skills folder and the templates folder for instructions, while also automatically access the logs folder and the tables folder to write down the outputs?
- Attached file names: .github/skills/domain-testing/SKILL.md; setup/tables
- Text Output: I’m adjusting the skill so it explicitly points at the relevant folders and makes the workflow more automatic for reading and writing.

I’m making the workflow explicit so the skill will look in the required folders by default and write its outputs to the designated locations.

Yes — that can be made explicit in the skill.

I updated the skill so it now:

reads from the info, skills, and templates folders by default
writes outputs to the logs folder and a dedicated tables folder
uses those locations as the expected workflow for test artifacts and session logging
The relevant change is in .github/skills/domain-testing/SKILL.md, and I also created setup/tables for generated table outputs.
- File Outputs: .github/skills/domain-testing/SKILL.md; setup/tables
------
- Name of the AI tool: GitHub Copilot
- Date and time: 27/06/2026 11:25
- Full text of given prompt: i've added the tables file while also added this file, the agent should have access to this file to write the explanation of explaining how the equivalence classes and boundary values are used
- Attached file names: .github/skills/domain-testing/SKILL.md; report-deliverables/domain_bva_raw.txt
- Text Output: I’m updating the workflow so it explicitly includes the new explanation file and then I’ll record this session in the project log.

I’m making the skill explicitly aware of the explanation file location so future runs will use it as part of the workflow.

I’m appending this latest session to the log so the workflow update is documented as requested.

Edited
logs.md+7-0
The latest session has been added to setup/logs/logs.md, and the skill now points to report-deliverables/domain_bva_raw.txt for the explanation output.
- File Outputs: .github/skills/domain-testing/SKILL.md
------
- Name of the AI tool: GitHub Copilot
- Date and time: 27/06/2026 13:40
- Full text of given prompt: run the domain-testing skill for FR-05
- Attached file names: setup/info/functional_requirements.md; setup/info/README.md; setup/tables/equivalence_class_table.md; setup/tables/test_table.md; setup/tables/test_requirement_matrix.md; setup/tables/test_class_matrix.md; report-deliverables/domain_bva_raw.txt
- Text Output: I’m applying the skill to FR-05 by gathering the relevant requirements and then drafting the equivalence classes, test cases, and supporting notes in the project artifacts.

I’m collecting the required artifacts and then I’ll write the FR-05 test design into the project’s test tables and reasoning note.

I’ve gathered the FR-05 requirements and I’m writing the derived equivalence classes, test cases, matrix links, and the explanatory note into the deliverables folder.

The FR-05 artifacts are now drafted; I’m updating the session log with this run so the workflow is fully recorded.

FR-05 has been processed with the domain-testing workflow.

Outputs created
Equivalence classes: setup/tables/equivalence_class_table.md
Test cases: setup/tables/test_table.md
Requirement traceability: setup/tables/test_requirement_matrix.md
Equivalence-class traceability: setup/tables/test_class_matrix.md
Explanation note: report-deliverables/domain_bva_raw.txt
Session log
The run was also appended to setup/logs/logs.md.
- File Outputs: setup/tables/equivalence_class_table.md; setup/tables/test_table.md; setup/tables/test_requirement_matrix.md; setup/tables/test_class_matrix.md; report-deliverables/domain_bva_raw.txt
------
- Name of the AI tool: GitHub Copilot
- Date and time: 28/06/2026 21:48
- Full text of given prompt: run the domain-testing skill on FR-14
- Attached file names: setup/info/functional_requirements.md; setup/info/README.md; setup/tables/equivalence_class_table.md; setup/tables/test_table.md; setup/tables/test_requirement_matrix.md; setup/tables/test_class_matrix.md; report-deliverables/domain_bva_raw.txt
- Text Output: I’m gathering the relevant requirements and templates for FR-14 so I can produce the requested domain-testing artifacts and update the logs.

The relevant API surface for admin category and product management is clear, and I’m now translating that into equivalence classes, boundary-aware tests, and the requested table updates.

I’ve narrowed this to the category-management rule set and I’m aligning the new cases with the repository’s existing table format before writing them into the project artifacts.

The requirement is specific enough to derive a compact set of classes, and I’m adding the new cases in the same artifact style as the earlier FR-05 work so the matrices stay consistent.

I’m writing the FR-14 equivalence classes and test cases into the project tables now, along with the supporting reasoning note and the session log entry.

The main artifact updates are in place; I’m resolving the remaining matrix and log formatting so the append operation is fully consistent with the repository’s existing structure.

The remaining step is a small formatting pass to add the FR-14 coverage into the class traceability matrix and append the new log entry at the end of the session log.

The FR-14 artifacts have been appended and I’m doing a quick verification pass over the updated tables and notes before I hand back the result.
- File Outputs: setup/tables/equivalence_class_table.md; setup/tables/test_table.md; setup/tables/test_requirement_matrix.md; setup/tables/test_class_matrix.md; report-deliverables/domain_bva_raw.txt
------
