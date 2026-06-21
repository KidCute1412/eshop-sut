# Demo Video Script

1. Show the project root with `backend/`, `frontend-web/`, `frontend-admin/`, `frontend-mobile/`, the PDF, `README.md`, `api_specification.md`, and `setup_guide.md`.
2. Open the official HW02 PDF and point out feature selection, Domain Testing, BVA, AI audit, and Agent Skill requirements.
3. Show `.agents/skills/domain-testing-bva/` with `SKILL.md`, `references/`, `assets/`, and `scripts/`.
4. Explain skill discovery: the folder name and `name` in `SKILL.md` both equal `domain-testing-bva`.
5. Activate the skill by asking: "Use domain-testing-bva for FR-01 Account registration."
6. Provide FR-01 input: feature ID `FR-01`, name `Account registration`, Pool `A`, user web module, backend route `POST /api/register`.
7. Show requirement and source inspection: `README.md`, `api_specification.md`, `frontend-web/src/pages/Register.jsx`, `backend/server.js`, and `backend/database.js`.
8. Show the FR-01 requirement analysis report and explain documented requirements versus implementation evidence.
9. Show the domain table: name, email, password, confirm password, duplicate email, and successful registration redirect.
10. Show the BVA table: password length 7, 8, 9 and email uniqueness/format notes where BVA does or does not apply.
11. Show representative test cases in `agent-skill-demo/FR-01/test-cases.md`.
12. Run `python .agents/skills/domain-testing-bva/scripts/validate_test_cases.py agent-skill-demo/FR-01`.
13. Show human review checklist and explain that all results are still `Not Executed` because the app tests were not run.
14. Show `ai-gap-analysis.md`, including validator weakness and improvement.
15. Show generated reports and the `evidence/` directory.
16. Run `python .agents/skills/domain-testing-bva/scripts/append_ai_audit.py ...` or show the already-created audit entry in `ai-audit/agent-skill-creation.md`.
17. Close with next steps: execute selected tests, capture screenshots for verified bugs, create GitHub Issues, add YouTube link to docs, and export Markdown/PDF submission files.
