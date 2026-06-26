---
name: domain-bva-tester
description: A specialized testing skill that guides agents in designing high-quality Domain Testing (Equivalence Partitioning) and Boundary Value Analysis (BVA) test cases from functional requirements.
---

# Skill: Domain & Boundary Value Analysis (BVA) Testing Designer

This skill instructs the agent on how to apply domain testing and boundary value analysis techniques systematically to any software feature specification.

## 🚀 Workflow

### Step 1: Input Variable & Condition Identification
1. Review the target feature's requirements description carefully.
2. List all input variables (e.g., fields, dropdown selections, uploaded files).
3. Identify state variables or environmental conditions (e.g., user authorization roles, database state, order status).

### Step 2: Equivalence Partitioning (Domain Testing)
For each variable identified, split its domain into:
* **Valid Equivalence Classes**: Input values that the system is specified to accept and process normally.
* **Invalid Equivalence Classes**: Input values that the system is specified to reject or handle as errors.
* Assign a unique ID to each class: `EP-VAL-XX` for valid and `EP-INV-XX` for invalid.

### Step 3: Boundary Value Analysis (BVA)
For each ordered/numeric variable:
1. Identify the boundaries (e.g., minimum length, maximum value, exact state limits).
2. Define testing points:
   * **On-points**: Values exactly on the boundary.
   * **Off-points**: Values just outside/inside the boundary (e.g., `Boundary - 1` or `Boundary + 1`).
   * **In-points**: Representative values well inside the valid boundaries.
3. Assign a unique ID to each boundary condition: `BVA-BND-XX`.

### Step 4: Test Case Design & Mapping
Combine the classes and boundaries using test combinations:
* **Normal Cases**: Test with valid classes and `In-points`.
* **Robust Cases**: Test boundary conditions and invalid classes.
* Map each test case back to the specific `EP` and `BVA` class IDs for traceability.

---

## 📋 Standard Output Format
When requested to perform testing on a feature, the agent must output the result using the structures defined in the `templates/` folder:
- **Equivalence Classes Table** (showing Variable, Valid Classes, Invalid Classes)
- **Boundary Conditions Table** (showing Variable, Boundary Condition, On-Point, Off-Point, In-Point)
- **Test Suite Table** (showing Test Case ID, Description, Inputs, Expected Output, and Traceability Mapping)
