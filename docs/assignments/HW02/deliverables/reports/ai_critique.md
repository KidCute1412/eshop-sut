# AI Critique & AI Audit Report

---

## 1. AI Critique (Mandatory, 200–300 words)

*Critique the performance and limitations of the AI tools you interacted with. Address: Where did the AI get something wrong, biased, or incomplete? Why did it fail to catch the issue? What principles did you learn about collaborating with AI during this homework?*

---

## 2. AI Audit Report (Mandatory Appendix)

### Option A: Used AI
"I use AI tools for the following tasks,"

#### Nhật ký tương tác (Interaction Log)
1. **Tương tác #1**:
   * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
   * **Date & Time**: 2026-06-26 17:45 (GMT+7)
   * **Yêu cầu (Your Prompt)**:
     ```text
     apply @[.agents/skills/domain-bva-tester] for FR-06 in @[docs/assignments/HW02/deliverables/reports/main_report.md]
     ```
   * **Kết quả (AI Output)**:
     ```text
     Đã áp dụng kỹ thuật Phân hoạch tương đương (Equivalence Partitioning) và Phân tích giá trị biên (Boundary Value Analysis - BVA) cho yêu cầu FR-06 (Product Detail View) trong tài liệu main_report.md bao gồm:
     - Xác định các biến đầu vào: Số lượng (Quantity), Mã sản phẩm (Product ID), và Trạng thái đăng nhập (Authentication State).
     - Thiết lập bảng Phân hoạch tương đương (EP Table) gồm các phân hoạch hợp lệ (EP-VAL-01 đến EP-VAL-04) và không hợp lệ (EP-INV-01 đến EP-INV-06).
     - Thiết lập bảng Phân tích giá trị biên (BVA Table) cho biến Số lượng với các điểm: On-point (1), Off-point (0 và 2), In-point (5).
     - Thiết kế bộ test case chi tiết cho Domain Testing (FR06-DT-01 đến FR06-DT-07) và BVA (FR06-BVA-01 đến FR06-BVA-04), có ánh xạ truy vết (Traceability Mapping) rõ ràng.
     - Mô tả chi tiết các bước thực hiện kỹ thuật kiểm thử.
     ```

