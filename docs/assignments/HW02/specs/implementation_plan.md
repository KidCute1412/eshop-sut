# HW02 - Domain Testing & BVA Testing Plan

This plan details a structured, step-by-step approach to completing the testing tasks for the selected features:
1. **FR-06: Product Detail View** (Pool A - Frontend Web / Mobile)
2. **FR-10: Order State Machine** (Pool B - Backend / Orders)
3. **FR-12: Access Control** (Pool C - Web Admin / Backend API)
4. **FR-20: Mobile App** (Pool D - Mobile App)

---

## 📅 Roadmap & Milestones

### Phase 1: Preparation & Setup
- **Goal**: Understand the feature requirements and set up the testing workspace.
- **Tasks**:
  1. Review the system specifications in [README.md](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/README.md) for **FR-06**, **FR-10**, **FR-12**, and **FR-20**.
  2. Launch and run the SUT (System Under Test) components (API Backend, Frontend Web, Web Admin, Mobile App) to ensure they are accessible.

### Phase 2: Feature-by-Feature Testing Cycle
For each feature (**FR-06** $\rightarrow$ **FR-10** $\rightarrow$ **FR-12** $\rightarrow$ **FR-20**):

#### Step 2.1: Domain Testing Design
- **Actions**:
  1. Define input parameters, domains, variables, and equivalence classes.
  2. With the guidance of AI (using a structured prompting strategy), generate a domain testing test case suite.
  3. Perform a **Human Review** to correct and refine the test cases.
- **Git Commit**: Commit test designs with a clear message:
  `test(hw02): design domain test cases for FR-XX`

#### Step 2.2: Boundary Value Analysis (BVA) Design
- **Actions**:
  1. Identify boundary values, boundary conditions, and off-points (e.g., product quantity bounds, role permission checks, order state transitions).
  2. With AI assistance, generate BVA test cases.
  3. Perform a **Human Review** to check boundaries for correctness.
- **Git Commit**: Commit BVA test designs:
  `test(hw02): design BVA test cases for FR-XX`

#### Step 2.3: Test Execution & Bug Reporting
- **Actions**:
  1. Execute the designed test cases against the running EShop application.
  2. Document results (Pass/Fail).
  3. For failed test cases (bugs found):
     - Take screenshots of the failure/bug.
     - Report the bug in your markdown report.
     - File the bug as an issue on the group's GitHub repository, attaching screenshots.
- **Git Commit**: Commit test execution results and local bug reports:
  `test(hw02): execute test cases & report bugs for FR-XX`

#### Step 2.4: AI Gap Analysis
- **Actions**:
  1. Compare manually discovered bugs/test cases against those proposed by the AI.
  2. Analyze gaps: *Why did the AI miss these?* (e.g., prompt quality, tool limitations, system complexity).
  3. Document the gap analysis for the feature.
- **Git Commit**: Commit gap analysis:
  `docs(hw02): add AI gap analysis for FR-XX`

---

### Phase 3: Agent Skill Development
- **Goal**: Automate testing techniques using Agent Skills or custom system configurations.
- **Tasks**:
  1. Build/define an Agent Skill or structured rule designed to run Domain Testing / BVA on a specified requirement.
  2. Test the skill on a complete feature to demonstrate its end-to-end usage.
  3. Record a demonstration video showcasing the usage and results, and upload it (e.g., to YouTube).
- **Git Commit**: Commit the agent skill files:
  `feat(hw02): add custom agent skill for test case generation`

---

### Phase 4: Audit, Critique & Self-Assessment
- **Goal**: Prepare all mandatory submission documentation.
- **Tasks**:
  1. Write the **AI Critique** (200–300 words) discussing AI biases, errors, and collaboration lessons.
  2. Compile the **AI Audit Report** detailing tools used, date/times, prompts, and raw/refined outputs.
  3. Extract the **Git Commit Log** into a text file.
  4. Create the final **README.md** summarizing execution metrics and embedding the self-assessment table.
- **Git Commit**: Commit final documentation:
  `docs(hw02): complete AI critique, audit report, and README`

---

### Phase 5: Submission Packaging
- **Goal**: Pack the deliverables cleanly.
- **Tasks**:
  1. Compile reports from Markdown to PDF.
  2. Check file paths and structure of the zip package.
  3. Compress the folder into `<StudentID>_HW02_AI_DomainTesting_<SelfAssessedGrade>.zip`.
