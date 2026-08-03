# Kịch bản quay demo Agent Skill — HW03

| Thông tin | Giá trị |
|---|---|
| Sinh viên | Lê Tuấn Lộc — 23127404 |
| Skill cần được Agent tự nhận diện | `gui-usability-tester` |
| Thời lượng mục tiêu | 2–5 phút |
| Phạm vi demo | FR-23 Mobile Product Detail |
| Evidence sử dụng | Bốn ảnh thật trong `deliverables/cross_platform/mobile_real_device` |
| Nguyên tắc | Không sửa SUT, không tạo evidence mới, không suy diễn hành vi không xuất hiện trong ảnh |

## 1. Mục tiêu video

Video cần chứng minh được năm khả năng:

1. Agent tự nhận diện đúng skill từ yêu cầu kiểm thử GUI, dù prompt không nêu tên skill.
2. Agent đọc yêu cầu, source và artifact liên quan trước khi kết luận.
3. Agent tạo mô hình traceability ngắn cho một feature có phạm vi rõ ràng.
4. Agent phân biệt assertion nhìn thấy trực tiếp với hành vi chưa có evidence.
5. Agent chạy validator thật và báo cáo đúng kết quả.

Không cần tạo hơn 40 checklist item trong video. Checklist 45 mục đã có sẵn; demo chỉ cần chọn một feature nhỏ để thể hiện chất lượng và cách vận hành của skill.

## 2. Chuẩn bị trước khi bấm quay

- Mở repository tại thư mục gốc `eshop-sut` trong Codex hoặc agent interface đang sử dụng.
- Mở sẵn cửa sổ Explorer/IDE tại `.agents/skills/gui-usability-tester`.
- Bảo đảm bốn ảnh sau tồn tại:
  - `mobile_01_product_detail.png`
  - `mobile_02_valid_quantity_add.png`
  - `mobile_03_invalid_quantity_before.png`
  - `mobile_04_invalid_quantity_after.png`
- Bảo đảm Python chạy được trong terminal.
- Đóng thông báo, mật khẩu, token và nội dung cá nhân không liên quan.
- Chưa cần có link YouTube trước khi quay. Link chỉ được điền sau khi video đã upload.

## 3. Kịch bản quay chi tiết

### Phân đoạn A — Giới thiệu ngắn, 0:00–0:25

**Thao tác trên màn hình**

Mở thư mục `.agents/skills/gui-usability-tester` và lướt nhanh qua:

- `SKILL.md`
- `references/`
- `scripts/validate_artifacts.py`

**Lời nói đề xuất**

> Đây là Agent Skill `gui-usability-tester` được cài trong repository. Skill hỗ trợ thiết kế, thực thi, phân tích và audit GUI/usability theo evidence. Trong demo này tôi không gọi tên skill trong prompt; Agent sẽ tự nhận diện skill phù hợp từ nội dung công việc.

### Phân đoạn B — Gửi prompt tự nhận diện skill, 0:25–0:50

Dán nguyên prompt sau vào Agent:

> Hãy audit riêng FR-23 Mobile Product Detail của HW03 trong `docs/assignments/HW03/deliverables`. Đọc yêu cầu/phạm vi liên quan, source Mobile, checklist, bug report và bốn ảnh trong `cross_platform/mobile_real_device`. Không sửa SUT và không thay đổi kết quả thực nghiệm. Hãy trình bày một bảng traceability ngắn gồm 3–5 assertion tiêu biểu, chỉ xác nhận Pass/Fail khi ảnh cho thấy trực tiếp; hành vi không xuất hiện trong evidence phải được ghi rõ là chưa thể xác nhận. Đối chiếu Bug ID và evidence path, sau đó chạy artifact validator với deliverables root và kết luận mức sẵn sàng của riêng phần FR-23.

**Lời nói đề xuất sau khi gửi prompt**

> Prompt mô tả công việc tự nhiên, không bắt người dùng phải biết tên skill hay mode nội bộ. Theo trigger rule, yêu cầu audit GUI, checklist, defect và cross-platform sẽ tự kích hoạt skill phù hợp.

### Phân đoạn C — Quan sát Agent làm việc, 0:50–3:30

Trong lúc Agent chạy, chỉ cần quay các checkpoint sau; không cần đọc toàn bộ output:

1. Agent thông báo đang sử dụng `gui-usability-tester` và nêu lý do.
2. Agent đọc `SKILL.md` cùng reference cần thiết.
3. Agent đối chiếu FR-23 với checklist, bug report, source và ảnh Mobile.
4. Agent tạo bảng traceability có Item/Assertion, Expected, Evidence, Result và Defect mapping.
5. Agent không đánh dấu một hành vi là Pass chỉ dựa trên source code.
6. Agent chỉ ra các nội dung như loading timing hoặc repeated-add sequence chưa thể xác nhận nếu ảnh không thể hiện chúng.
7. Agent chạy validator thật.

Nếu muốn phóng to terminal để người xem thấy rõ, lệnh đúng là:

```powershell
python .agents/skills/gui-usability-tester/scripts/validate_artifacts.py docs/assignments/HW03/deliverables
```

Output hợp lệ hiện tại phải bắt đầu bằng:

```text
VALIDATION PASSED
```

Validator kiểm tra cấu trúc và tính liên kết của artifact. Nó không thay thế việc đánh giá chất lượng hoặc xác minh evidence bằng con người.

### Phân đoạn D — Tổng kết, 3:30–4:15

Mở phần kết luận của Agent và nói:

> Agent đã tự chọn đúng skill từ yêu cầu tự nhiên, đọc nguồn sự thật liên quan, tạo traceability, phân biệt evidence trực tiếp với inference, đối chiếu defect và chạy validator. Điểm quan trọng là skill không biến source inspection thành kết quả runtime và không tự tạo evidence còn thiếu.

Nếu Agent báo các hạn chế như Mobile overlay hoặc environment metadata còn thiếu, giữ nguyên kết luận đó trong video. Đây là minh chứng cho evidence integrity, không phải lỗi của demo.

## 4. Trường hợp Agent không hiển thị tên skill rõ ràng

Không cần quay lại từ đầu. Gửi câu hỏi tiếp theo:

> Bạn đã tự chọn skill hoặc quy trình chuyên biệt nào cho tác vụ này? Hãy nêu tên skill và hai quy tắc evidence quan trọng nhất bạn đã áp dụng, không chạy lại toàn bộ audit.

Phần này chỉ làm rõ auto-discovery; không yêu cầu Agent thay đổi kết quả.

## 5. Những điều không nên làm trong video

- Không yêu cầu tạo hơn 40 checklist item trong vài phút.
- Không yêu cầu `EXECUTE` nếu không cung cấp runtime hoặc evidence đủ điều kiện.
- Không yêu cầu Agent mặc định kiểm tra dark mode, RTL hoặc accessibility khi chúng không thuộc phạm vi đang demo.
- Không tuyên bố validator chứng minh mọi nội dung đều đúng.
- Không sửa ảnh, thêm evidence giả hoặc thay đổi status chỉ để validator pass.
- Không nói skill “chuẩn hóa 100%” hoặc “đảm bảo chắc chắn đạt điểm tối đa”.
- Không mở participant contact đầy đủ, mật khẩu, token hoặc dữ liệu cá nhân.

## 6. Sau khi quay

1. Cắt phần chờ dài nhưng không cắt mất prompt, auto-discovery, traceability và kết quả validator.
2. Upload video lên YouTube ở chế độ `Unlisted` hoặc `Public`.
3. Mở link trong cửa sổ đăng xuất/ẩn danh để kiểm tra quyền truy cập.
4. Điền URL thật vào:

```text
docs/assignments/HW03/deliverables/agent_skills/gui-usability-tester/demo_video_link.txt
```

5. Không ghi link placeholder hoặc link chưa access-test vào README/main report.

## 7. Checklist trước khi kết thúc video

- [ ] Prompt không nêu tên skill nhưng Agent tự nhận diện đúng `gui-usability-tester`.
- [ ] Video cho thấy Agent đọc `SKILL.md` hoặc thông báo sử dụng skill.
- [ ] Có bảng traceability 3–5 assertion cho FR-23.
- [ ] Có ít nhất một assertion được đối chiếu với ảnh runtime thật.
- [ ] Có ít nhất một giới hạn evidence được ghi rõ thay vì suy diễn.
- [ ] Có Bug ID/evidence path mapping.
- [ ] Validator chạy với đúng `deliverables` root và trả về `VALIDATION PASSED`.
- [ ] Không lộ thông tin nhạy cảm.
- [ ] Video dài trong khoảng 2–5 phút.
- [ ] Link video đã được kiểm tra ở trạng thái đăng xuất trước khi điền vào deliverables.
