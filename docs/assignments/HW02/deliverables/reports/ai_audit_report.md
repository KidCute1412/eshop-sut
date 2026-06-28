# AI Audit Report (Mandatory Appendix)

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

7. **Tương tác #7**:
   * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
   * **Date & Time**: 2026-06-28 23:23 (GMT+7)
   * **Yêu cầu (Your Prompt)**:
     ```text
     @[docs/assignments/HW02/deliverables/reports/main_report.md] thì fr-20 là 1 tính năng không có mô tả. Hãy đổi nó thành fr-23 và suggest cho tôi 1 tính năng nên test trong phần mobile  @[frontend-mobile] để làm fr-23
     ```
   * **Kết quả (AI Output)**:
     ```text
     - Đổi mục FR-20: Mobile App thành FR-23: Navigation Requirements trong mục lục và phần nội dung của main_report.md.
     - Đề xuất và xây dựng nội dung phân tích Domain Testing & BVA cho tính năng Yêu cầu Điều hướng (FR-23) dựa trên mã nguồn frontend-mobile (lỗi hiển thị nhãn nút "Thoát" thay vì "Đăng xuất", thiếu highlight trang đang chọn trên Navbar, và thiếu badge số lượng cho giỏ hàng).
     ```

8. **Tương tác #8**:
   * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
   * **Date & Time**: 2026-06-28 23:27 (GMT+7)
   * **Yêu cầu (Your Prompt)**:
     ```text
     trước tiên hãy vào @[start.bat] để cập nhật mở luôn ứng dụng mobile ra
     ```
   * **Kết quả (AI Output)**:
     ```text
     - Cập nhật tệp start.bat để tự động kiểm tra thư mục node_modules, chạy npm install và khởi chạy ứng dụng di động frontend-mobile bằng lệnh npm run start trong một cửa sổ dòng lệnh độc lập.
     ```

9. **Tương tác #9**:
   * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
   * **Date & Time**: 2026-06-28 23:42 (GMT+7)
   * **Yêu cầu (Your Prompt)**:
     ```text
     kiểm tra mobile tại sao mở được bằng expo nhưng đang ko connect dc với backend dù laptop và điện thoại của tôi đang chung 1 mạng
     ```
   * **Kết quả (AI Output)**:
     ```text
     - Kiểm tra địa chỉ IPv4 LAN thực tế của máy tính bằng lệnh ipconfig (phát hiện IP là 172.20.10.2).
     - Cập nhật biến API_URL trong frontend-mobile/App.js từ 192.168.10.13 thành 172.20.10.2 để thiết bị di động có thể kết nối được tới backend server đang chạy.
     ```

10. **Tương tác #10**:
    * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
    * **Date & Time**: 2026-06-28 23:48 (GMT+7)
    * **Yêu cầu (Your Prompt)**:
      ```text
      Apply the custom skill `domain-bva-tester` to generate Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) test cases for "FR-23: Product detail view (mobile)" as specified in README.md. Append the tables into docs/assignments/HW02/deliverables/reports/main_report.md. Everything must strictly based on @[frontend-mobile]
      ```
    * **Kết quả (AI Output)**:
      ```text
      - Cập nhật và thay thế phần nội dung FR-23: Navigation Requirements thành FR-23: Product detail view (mobile) trong main_report.md.
      - Phân tích và xây dựng bảng Phân hoạch tương đương (EP), Phân tích giá trị biên (BVA), và bộ ca kiểm thử tương ứng cho tính năng Xem Chi tiết Sản phẩm trên thiết bị di động dựa trên mã nguồn frontend-mobile/App.js.
      - Chỉ ra các điểm lỗi Gap Analysis như lỗi bất đồng bộ số lượng bằng 0 hoặc số âm, tự động làm tròn số thập phân mà không hiển thị cảnh báo trên UI.
      ```

11. **Tương tác #11**:
    * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
    * **Date & Time**: 2026-06-29 01:07 (GMT+7)
    * **Yêu cầu (Your Prompt)**:
      ```text
      ở fr23 dt03 tôi đã thêm ảnh trong images, cập nhật cho tôi. đồng thời cái này là giao diện nhập 2.5 được nhưng check trong giỏ hàng thì số lượng làm tròn xuống thành 2
      ```
    * **Kết quả (AI Output)**:
      ```text
      - Cập nhật liên kết hình ảnh minh chứng fr23-DT04-fail.png cho kịch bản FR23-DT-04 trong tài liệu báo cáo main_report.md.
      - Tạo mới chi tiết báo cáo BUG-007 cho lỗi tự động làm tròn số lượng thập phân (ví dụ: 2.5 thành 2) không có cảnh báo trên Mobile vào tài liệu bug_report.md và cập nhật bảng tổng hợp lỗi.
      ```

12. **Tương tác #12**:
    * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
    * **Date & Time**: 2026-06-29 01:10 (GMT+7)
    * **Yêu cầu (Your Prompt)**:
      ```text
      tôi đã thêm fr23-dt05 trong image, cập nhật cho tôi. đồng thời thì khi nhập input rỗng thì vẫn nhập được, còn check trong giỏ hàng thì kết quả là 1
      ```
    * **Kết quả (AI Output)**:
      ```text
      - Cập nhật liên kết hình ảnh minh chứng fr23-DT05-fail.png cho kịch bản FR23-DT-05 trong tài liệu báo cáo main_report.md.
      - Tạo mới chi tiết báo cáo BUG-008 cho lỗi tự động thêm số lượng bằng 1 khi để trống ô nhập liệu trên Mobile vào tài liệu bug_report.md và cập nhật bảng tổng hợp lỗi.
      ```

13. **Tương tác #13**:
    * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
    * **Date & Time**: 2026-06-29 01:16 (GMT+7)
    * **Yêu cầu (Your Prompt)**:
      ```text
      @[docs/assignments/HW02/deliverables/reports/bug_report.md] là viết lại tất cả những test case domain hay bva mà bị fail hay sao
      ```
    * **Kết quả (AI Output)**:
      ```text
      - Giải thích bản chất của tài liệu bug_report.md (Báo cáo lỗi nghiệp vụ chuyên nghiệp) so với việc chỉ chép lại các ca kiểm thử thất bại (failed test cases).
      - Phân tích cách gộp các ca kiểm thử thất bại có cùng nguyên nhân gốc rễ và cấu trúc tiêu chuẩn của một báo cáo lỗi (Bug ID, Description, Steps to Reproduce, Expected/Actual Result, Screenshots).
      ```

14. **Tương tác #14**:
    * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
    * **Date & Time**: 2026-06-29 01:23 (GMT+7)
    * **Yêu cầu (Your Prompt)**:
      ```text
      bây giờ tôi sẽ chỉ điểm từng fr trong @[docs/assignments/HW02/deliverables/reports/main_report.md] . nhiện vụ của bạn là kiểm tra fr đó có syntax error hay sai lỗi chính tả hay không nhất quán ở bố cục, phong cách, định dạng ở đâu không và chỉnh sửa cần thiết. Đồng thời kiểm tra đã hoàn thiện bug phù hợp cho @[docs/assignments/HW02/deliverables/reports/bug_report.md] chưa. Lên kế hoạch để thực hiện theo chỉ dẫn tôi một cách phù hợp. Rà soát FR-06, FR-10, FR-12, FR-23.
      ```
    * **Kết quả (AI Output)**:
      ```text
      Hi sir - Đã rà soát chi tiết cả 4 phân hệ yêu cầu chức năng (FR-06, FR-10, FR-12, FR-23) trong main_report.md:
      - Cập nhật thuật ngữ kỹ thuật tràn số (integer overflow) thay thế từ tràn viền trong FR-06.
      - Đối chiếu các kịch bản kiểm thử trạng thái Fail trong main_report.md với danh sách báo cáo lỗi trong bug_report.md để đảm bảo tính đồng bộ.
      - Phát hiện lỗi thiếu kịch bản kiểm thử biên vai trò token (FR12-BVA-01) chưa được đưa vào báo cáo lỗi.
      - Đã cập nhật và bổ sung mã lỗi mới BUG-014 (Hệ thống chấp nhận JWT token có vai trò chứa khoảng trắng không hợp lệ 'admin ') kèm theo các bước tái hiện, kết quả mong đợi/thực tế và hình ảnh minh chứng vào tệp bug_report.md.
      ```

15. **Tương tác #15**:
    * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
    * **Date & Time**: 2026-06-29 01:45 (GMT+7)
    * **Yêu cầu (Your Prompt)**:
      ```text
      Có chắc chắn 14 bug trong @[docs/assignments/HW02/deliverables/reports/bug_report.md] là đầy đủ theo @[docs/assignments/HW02/deliverables/reports/main_report.md] không
      ```
    * **Kết quả (AI Output)**:
      ```text
      Hi sir - Đã đối chiếu chi tiết 100% các kịch bản kiểm thử có trạng thái Fail trong main_report.md bao gồm 5 kịch bản Fail ở FR-06, 2 kịch bản Fail ở FR-10, 4 kịch bản Fail ở FR-12, và 3 kịch bản Fail ở FR-23. Kết quả xác nhận toàn bộ 14 lỗi thực tế đều được ánh xạ tương ứng không thiếu sót tới 14 Bug ID từ BUG-001 đến BUG-014 trong báo cáo lỗi bug_report.md.
      ```

16. **Tương tác #16**:
    * **AI Tool Name**: Gemini (Antigravity Coding Assistant)
    * **Date & Time**: 2026-06-29 02:50 (GMT+7)
    * **Yêu cầu (Your Prompt)**:
      ```text
      kiểm tra @[docs/assignments/HW02/deliverables/reports/bug_report.md] đã chính xác và đầy đủ rồi đúng không
      ```
    * **Kết quả (AI Output)**:
      ```text
      Hi sir - Xác nhận báo cáo bug_report.md đã hoàn toàn chính xác, đầy đủ 14 bug, có đầy đủ các bước tái hiện, kết quả mong đợi/thực tế và các hình ảnh minh chứng tương ứng được gán chuẩn xác theo từng lỗi trong main_report.md.
      ```


