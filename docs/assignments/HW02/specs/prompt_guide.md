# HW02 - Step-by-Step Prompting Guide

Use this guide to copy-paste or adapt prompts to guide the agent through completing the homework tasks for the selected features: **FR-06**, **FR-10**, **FR-12**, and **FR-20**.

---

## 🛠️ Step 1: Testing Custom Skill Activation
To initiate the custom skill to design test cases for a specific feature, run the following prompts one feature at a time:

### For FR-06 (Product Detail View)
```text
Apply the custom skill `domain-bva-tester` to generate Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) test cases for "FR-06: Xem chi tiết sản phẩm" as specified in README.md. Write the generated tables directly into docs/assignments/HW02/deliverables/reports/main_report.md.
```

### For FR-10 (Order State Machine)
```text
Apply the custom skill `domain-bva-tester` to generate Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) test cases for "FR-10: Trạng thái Đơn hàng" as specified in README.md. Append the tables into docs/assignments/HW02/deliverables/reports/main_report.md.
```

### For FR-12 (Access Control)
```text
Apply the custom skill `domain-bva-tester` to generate Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) test cases for "FR-12: Kiểm soát truy cập" as specified in README.md. Append the tables into docs/assignments/HW02/deliverables/reports/main_report.md.
```

### For FR-20 (Mobile App)
```text
Apply the custom skill `domain-bva-tester` to generate Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) test cases for "FR-20: Tính năng Mobile" as specified in README.md. Append the tables into docs/assignments/HW02/deliverables/reports/main_report.md.
```

---

## 🐛 Step 2: Documenting Discovered Bugs
After running the tests manually on the EShop application, if you discover bugs, use this prompt to update the bug report:

```text
I have found a bug in [FR-XX]. Here are the details:
- Title: [Bug Title]
- Description: [Bug Description]
- Steps to reproduce: [Steps]
- Expected Result: [Expected behavior]
- Actual Result: [Actual behavior]
Please add this bug to docs/assignments/HW02/deliverables/reports/bug_report.md.
```

---

## 🔍 Step 3: Performing AI Gap Analysis
To write the gap analysis once you have compared your manual testing findings with the AI's suggestions:

```text
Let's do the AI Gap Analysis for [FR-XX]. The AI missed [specify what cases/bugs were missed]. The reason why it missed them is [specify why, e.g., complex state transitions, lack of UI verification]. Document this analysis in the Gap Analysis section of docs/assignments/HW02/deliverables/reports/main_report.md.
```

---

## 🎨 Step 4: Writing the Critique
To generate the final 200–300 words AI critique based on your collaboration experience:

```text
Generate the mandatory 200-300 words AI Critique section in docs/assignments/HW02/deliverables/reports/ai_critique.md. Focus on where the AI made errors or had limitations, why it failed, and what principles were learned about working with AI.
```

---

## 📦 Step 5: Preparing the Final Deliverables Folder
When all testing and reporting are complete, run this prompt to organize the folder for zipping:

```text
All testing tasks are completed. Please:
1. Re-create the `docs/assignments/HW02/deliverables/agent_skills/` folder.
2. Copy the active custom skill from `.agents/skills/domain-bva-tester/` to `docs/assignments/HW02/deliverables/agent_skills/domain-bva-tester/`.
3. Check that all files inside `deliverables/` are correctly formatted.
```
