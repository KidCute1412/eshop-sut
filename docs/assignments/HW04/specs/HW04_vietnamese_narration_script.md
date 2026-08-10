# Kịch bản thuyết minh tiếng Việt — Video demo HW04

> Trạng thái: kịch bản chuẩn bị ghi hình, **không phải bằng chứng video đã tồn tại**. Chỉ đọc các câu khẳng định kết quả sau khi đã chạy thật và điền đúng dữ liệu trong ngoặc vuông. Thời lượng mục tiêu: 6–8 phút.

## 0:00–0:45 — Giới thiệu và chứng minh tác giả

“Xin chào thầy cô, em là **Lê Tuấn Lộc**, mã số sinh viên **23127404**. Đây là video demo bài HW04 về kiểm thử tự động cho hệ thống EShop. Repository của em là `https://github.com/KidCute1412/eshop-sut`. Trong HW04 em giữ nguyên ba tính năng web đã chọn từ HW02: FR-06 Xem chi tiết sản phẩm, FR-10 Trạng thái đơn hàng và FR-12 Kiểm soát truy cập.”

“Trước khi demo, em chạy hai lệnh `whoami` và `hostname` để chứng minh phiên làm việc này do em trực tiếp thực hiện.”

[MỞ TERMINAL, CHẠY `whoami`, SAU ĐÓ `hostname`; KHÔNG ĐỌC HOẶC HIỂN THỊ THÔNG TIN NHẠY CẢM KHÁC.]

## 0:45–1:35 — Giới thiệu ca kiểm thử và dữ liệu

“Trong video này em chọn demo tính năng **[ĐIỀN FR-06 / FR-10 / FR-12]**, với các mã ca kiểm thử **[ĐIỀN DANH SÁCH ID THỰC TẾ]**. Đặc tả mong đợi được truy vết từ yêu cầu **[ĐIỀN MÃ YÊU CẦU]** trong README của SUT.”

“Dữ liệu kiểm thử không được khai báo thành mảng hard-code trong file spec. File **[ĐIỀN ĐƯỜNG DẪN JSON/CSV]** chứa các dòng dữ liệu, còn file **[ĐIỀN ĐƯỜNG DẪN SPEC]** đọc dữ liệu này khi chạy. Mỗi tên test có mã case để em truy ngược từ báo cáo HTML về ma trận thiết kế.”

[MỞ FILE DATA VÀ FILE SPEC; CHỈ VÀO ĐOẠN ĐỌC FILE VÀ TÊN TEST.]

## 1:35–2:25 — Assertion, locator và tính ổn định

“Bộ test sử dụng ít nhất ba kiểu assertion. Cụ thể trong phần đang hiển thị có **[VÍ DỤ THẬT: kiểm tra URL]**, **[VÍ DỤ THẬT: kiểm tra hiển thị hoặc số lượng]**, và **[VÍ DỤ THẬT: kiểm tra text, giá trị, thuộc tính hoặc response]**.”

“Locator ưu tiên role, label hoặc test ID có ý nghĩa. Em không dùng thời gian chờ cố định để ép test chạy; Playwright chờ theo điều kiện của locator và assertion. Phần setup **[MÔ TẢ CÁCH TẠO/RESET DATA THỰC TẾ]** giúp các ca không phụ thuộc thứ tự chạy.”

## 2:25–3:15 — Một chỉnh sửa do con người thực hiện

“Một điểm em phải sửa sau khi review output AI là **[ĐIỀN CHỈNH SỬA THỰC TẾ VÀ CÓ BẰNG CHỨNG]**. AI ban đầu **[MÔ TẢ ĐỀ XUẤT THẬT]**, nhưng đề xuất đó chưa đủ vì **[ĐỐI CHIẾU VỚI YÊU CẦU/RỦI RO]**. Em đã sửa thành **[MÔ TẢ CODE CUỐI]**, nhờ đó test kiểm tra đúng hành vi thay vì chỉ tạo kết quả xanh.”

“Nếu demo FR-06 với artifact lịch sử, em có thể chỉ ra rằng yêu cầu bắt buộc hiển thị danh mục. Assertion danh mục phải được giữ lại; bỏ assertion này sẽ tạo false pass. Em chỉ dùng ví dụ này khi code và audit log trên màn hình chứng minh đúng nội dung vừa nêu.”

[HIỂN THỊ AI AUDIT/HUMAN-REVIEW ROW VÀ ĐOẠN CODE CUỐI.]

## 3:15–4:35 — Chạy thật trên ba trình duyệt

“Bây giờ em xác nhận frontend tại **[URL THẬT]**, backend tại **[URL THẬT]**, và SUT revision là **[COMMIT HASH THẬT]**. Lệnh chạy chính xác là **[LỆNH THẬT]**.”

[CHẠY LỆNH; KHÔNG CẮT BỎ OUTPUT QUAN TRỌNG.]

“Playwright đang chạy cùng feature trên Chromium, Firefox và WebKit. **[SAU KHI CHẠY XONG]** tổng số browser execution là **[SỐ THẬT]**, trong đó **[PASS THẬT]** pass, **[FAIL THẬT]** fail và **[BLOCKED THẬT]** blocked.”

> Không đọc câu tổng kết trên nếu chưa có output thật. Nếu có lỗi môi trường, nói rõ đó là lỗi môi trường và không gọi là bug của SUT.

## 4:35–5:45 — Mở và giải thích báo cáo HTML

“Em mở báo cáo HTML vừa sinh tại **[ĐƯỜNG DẪN THẬT]**. Trên báo cáo có dòng `Run by: 23127404`, timestamp ISO **[TIMESTAMP THẬT]**, tên browser **[TÊN/PHIÊN BẢN THẬT]**, danh sách case và trạng thái thực tế.”

[PHÓNG TO PHẦN METADATA, CASE, ASSERTION VÀ SCREENSHOT/TRACE NẾU CÓ.]

“Kết quả âm tính mong đợi mà assertion xác nhận đúng vẫn được tính là test pass. Chỉ một assertion thất bại ngoài mong đợi mới là failed execution. Với failure, em kiểm tra locator, dữ liệu, trạng thái SUT và môi trường trước khi kết luận bug.”

“Trong lần chạy này, **[NÓI MỘT TRONG HAI: ‘không có bug SUT được xác minh’ / ‘bug [ID] đã được tái hiện và Issue công khai là [URL]’]**. Em chỉ hiển thị Issue nếu URL và ảnh đính kèm đã được kiểm tra thật.”

## 5:45–6:30 — Kết luận trung thực

“Tóm lại, phần demo này bao phủ **[FEATURE VÀ SỐ CASE THẬT]** trên ba browser, dùng dữ liệu ngoài, locator ổn định và nhiều kiểu assertion. Các tổng số cuối cùng được lấy từ manifest và báo cáo HTML, không nhập ước lượng.”

“Tại thời điểm ghi hình, tình trạng yêu cầu Git là **[ĐẠT: NÊU 8+ COMMIT/4+ NGÀY VỚI LOG / CHƯA ĐẠT: NÊU ĐÚNG THIẾU HỤT]**. Em không tính commit tài liệu vào số commit test-script.”

“Cảm ơn thầy cô đã theo dõi. Link video unlisted này và toàn bộ đường dẫn evidence được ghi trong README và báo cáo chính.”

## Kiểm tra trước khi tải lên

- [ ] Các phần trong ngoặc vuông đã được thay bằng dữ liệu thật.
- [ ] Không đọc câu khẳng định pass/fail nếu output không hiển thị trên video.
- [ ] Video dài ít nhất 5 phút và có giọng nói thật của sinh viên.
- [ ] Đã hiển thị cả `whoami` và `hostname`, hoặc có face-cam.
- [ ] Metadata `Run by: 23127404` và ISO timestamp nhìn rõ.
- [ ] Không lộ mật khẩu, JWT, secret, email riêng hoặc dữ liệu cá nhân không cần thiết.
- [ ] Video đặt chế độ Unlisted và mở được khi đăng xuất.
