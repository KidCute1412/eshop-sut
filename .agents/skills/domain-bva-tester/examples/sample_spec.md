# Example: Applying Domain Testing & BVA to OTP Verification

## Specification Detail
* **Description**: The user must input a 6-digit OTP code to verify password reset.
* **Constraints**: 
  - Code must be exactly 6 characters.
  - Code must contain only numeric digits (0-9).

---

## 1. Equivalence Partitioning (Domain Testing)

| Variable / Condition | Valid Equivalence Classes | Invalid Equivalence Classes |
| :--- | :--- | :--- |
| **OTP Code Length** | **EP-VAL-01**: Exactly 6 characters | **EP-INV-01**: Less than 6 characters<br>**EP-INV-02**: More than 6 characters |
| **OTP Character Types** | **EP-VAL-02**: Numeric digits only (0-9) | **EP-INV-03**: Contains alphabetic letters (a-z, A-Z)<br>**EP-INV-04**: Contains special characters (e.g. `@`, `#`) |

---

## 2. Boundary Value Analysis (BVA)

| Variable | Boundary Condition | In-Point | On-Point | Off-Point | ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **OTP Length** | Length = 6 characters | 6 | 6 | 5 (too short), 7 (too long) | BVA-BND-01 |

---

## 3. Test Cases Designed

| Test Case ID | Description | Inputs | Expected Outcome | Traceability Mapping |
| :--- | :--- | :--- | :--- | :--- |
| TC-OTP-01 | Normal verification with valid OTP | `"123456"` | Success, proceed to step 2 | EP-VAL-01, EP-VAL-02, BVA-BND-01 |
| TC-OTP-02 | OTP length too short (5 digits) | `"12345"` | Error: Length must be 6 | EP-INV-01, BVA-BND-01 |
| TC-OTP-03 | OTP length too long (7 digits) | `"1234567"` | Error: Length must be 6 | EP-INV-02, BVA-BND-01 |
| TC-OTP-04 | OTP contains non-numeric characters | `"12a456"` | Error: Numeric digits only | EP-INV-03 |
