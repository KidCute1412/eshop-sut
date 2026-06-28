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

2. **Tương tác #2**:
   * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
   * **Date & Time**: 2026-06-26 18:07 (GMT+7)
   * **Yêu cầu (Your Prompt)**:
     ```text
     Apply the custom skill `domain-bva-tester` to generate Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) test cases for "FR-10: Trạng thái Đơn hàng" as specified in README.md. Append the tables into docs/assignments/HW02/deliverables/reports/main_report.md.
     ```
   * **Kết quả (AI Output)**:
     ```text
     Đã áp dụng thành công kỹ thuật Phân hoạch tương đương (Equivalence Partitioning) và Phân tích giá trị biên (Boundary Value Analysis - BVA) cho yêu cầu "FR-10: Trạng thái Đơn hàng" (Order State Machine) bằng tiếng Việt vào tài liệu main_report.md:
     - Xác định các biến đầu vào & điều kiện: Current Status (Trạng thái hiện tại), Target Status (Trạng thái đích), và Actor Role (Vai trò thực hiện).
     - Thiết lập bảng Phân hoạch tương đương (EP Table) chia các lớp vai trò hợp lệ/không hợp lệ, trạng thái hiện tại hợp lệ/không xác định, và trạng thái đích hợp lệ/không hợp lệ theo nghiệp vụ.
     - Thiết lập bảng Phân tích giá trị biên (BVA Table) tập trung vào các trạng thái kết thúc (delivered, canceled) và giới hạn quyền hạn tại trạng thái shipping.
     - Thiết kế bộ test case chi tiết cho Domain Testing (FR10-DT-01 đến FR10-DT-07) và BVA (FR10-BVA-01 đến FR10-BVA-05), có ánh xạ truy vết (Traceability Mapping) rõ ràng.
     ```

3. **Tương tác #3**:
   * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
   * **Date & Time**: 2026-06-26 18:09 (GMT+7)
   * **Yêu cầu (Your Prompt)**:
     ```text
     Apply the custom skill `domain-bva-tester` to generate Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) test cases for "FR-12: Kiểm soát truy cập" as specified in README.md. Append the tables into docs/assignments/HW02/deliverables/reports/main_report.md.
     ```
   * **Kết quả (AI Output)**:
     ```text
     Đã áp dụng thành công kỹ thuật Phân hoạch tương đương (Equivalence Partitioning) và Phân tích giá trị biên (Boundary Value Analysis - BVA) cho yêu cầu "FR-12: Kiểm soát truy cập" (Access Control) bằng tiếng Việt vào tài liệu main_report.md:
     - Xác định các biến đầu vào & điều kiện: JWT Token (Trạng thái xác thực), User Role (Vai trò người dùng), và Target API Path (Đường dẫn API đích).
     - Thiết lập bảng Phân hoạch tương đương (EP Table) phân loại token JWT hợp lệ/không hợp lệ, vai trò admin/user, và các API yêu cầu quyền admin hoặc API công khai.
     - Thiết lập bảng Phân tích giá trị biên (BVA Table) tập trung vào biên phân quyền (giá trị chuỗi vai trò), biên hiệu lực Token JWT (lệch đúng 1 giây còn hạn hay hết hạn), và biên định dạng header Authorization.
     - Thiết kế bộ test case chi tiết cho Domain Testing (FR12-DT-01 đến FR12-DT-07) và BVA (FR12-BVA-01 đến FR12-BVA-06) với đầy đủ ánh xạ truy vết.
     ```

4. **Tương tác #4**:
   * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
   * **Date & Time**: 2026-06-26 20:38 (GMT+7)
   * **Yêu cầu (Your Prompt)**:
     ```text
     tôi đã thêm 1 hình ảnh fr10-dt05-fail, đó thể hiện bên admin đã ship nhưng bên user vẫn có thể ấn hủy được.
     ```
   * **Kết quả (AI Output)**:
     ```text
     Đã cập nhật chi tiết lỗi FR10-DT-05 và FR10-BVA-05 (User tự hủy đơn hàng đang giao hàng) kèm theo hình ảnh minh chứng fr10-DT05-fail.png vào các tài liệu:
     - main_report.md: Mục 2.3 AI Gap Analysis & Screenshot Proofs (giải thích lỗi ở cả Frontend lẫn Backend).
     - bug_report.md: Cập nhật chi tiết lỗi BUG-001 bao gồm mô tả lỗi, các bước tái hiện, kết quả mong đợi và thực tế.
     ```

5. **Tương tác #5**:
   * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
   * **Date & Time**: 2026-06-27 12:31 (GMT+7)
   * **Yêu cầu (Your Prompt)**:
     ```text
     với fr12 trong @[docs/assignments/HW02/deliverables/reports/main_report.md] thì tôi cần test sao
     ...
     tôi đã thêm fr12-admin-login và fr12-user-login và fr12-DT03-fail trong ảnh, bạn thêm vào trong report cho tôi
     ```
   * **Kết quả (AI Output)**:
     ```text
     - Giải thích và hướng dẫn phương pháp kiểm thử API bằng Postman/cURL đối với tính năng phân quyền (FR-12).
     - Phân tích nguyên nhân lỗi logic phân quyền tại middleware backend (chỉ kiểm tra tính hợp lệ của token mà bỏ sót việc kiểm tra giá trị của trường role).
     - Cập nhật các hình ảnh minh chứng fr12-admin-login.png, fr12-user-login.png, và fr12-DT03-fail.png cùng các mô tả chú thích chi tiết vào báo cáo main_report.md.
     ```

6. **Tương tác #6**:
   * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
   * **Date & Time**: 2026-06-28 23:03 (GMT+7)
   * **Yêu cầu (Your Prompt)**:
     ```text
     các kịch bản BVA ở FR12 chính xác rồi đúng không
     ```
   * **Kết quả (AI Output)**:
     ```text
     - Giải thích tính chính xác của các kịch bản BVA được thiết kế cho FR-12 (Access Control) bao gồm biên chuỗi quyền hạn (role string), biên thời gian sống token (expiry) và biên định dạng header Authorization.
     - Xác nhận các kịch bản đã phản ánh đúng lỗi thực tế của SUT (đối với các trường hợp bị trạng thái thực tế Fail).
     ```
