# TODO — Những việc cần Review và Thêm vào

Danh sách các mục cần hoàn thành trước khi nộp bài.

---

## Task 1 — Cần làm

### Test Plans
- [ ] **Thay `25127001` bằng Student ID thực** trong tên file `.jmx` (Load, Stress, Spike)
- [ ] **Review lại CSV data**: Thêm/điền email, password, product data thực tế vào `test_data_users.csv`, `test_data_products.csv`, `test_data_checkout.csv`
- [ ] **Chạy từng test plan** trong JMeter và kiểm tra kết quả
- [ ] **Điều chỉnh tham số** nếu cần (VUsers, ramp-up, duration) dựa trên phần cứng thực tế
- [ ] **Verify assertions** hoạt động đúng trên từng endpoint

### Review Notes
- [ ] **Điền chi tiết AI prompts** đã sử dụng vào `test_plan_review_notes.md`
- [ ] **Ghi lại các vấn đề AI tạo ra** và cách bạn đã sửa chúng
- [ ] **Document account lockout reset steps** khi chạy Stress/Spike test

### Endurance Threshold
- [ ] **Chạy soak test** 10-15 phút và ghi lại số liệu thực tế
- [ ] **Điền các giá trị** vào bảng endurance threshold trong `test_plan_review_notes.md`

### Screenshots & Evidence
- [ ] **Chụp screenshot** JMeter đang chạy + Task Manager cho từng test
- [ ] **Chụp hardware spec** (dxdiag hoặc screenfetch)
- [ ] **Lưu .jtl files** (3 file) vào thư mục submit
- [ ] **Tạo HTML reports** (3 folder) từ JMeter
- [ ] **Record demo video** >= 6 phút với tiếng Việt, upload YouTube (unlisted)

### Bugs
- [ ] **Log GitHub Issues** cho các bug/performance issues tìm thấy
- [ ] **Chụp screenshot** GitHub Issues page

---

## Task 2 — Cần làm

### AI Analysis
- [ ] **Chạy AI analysis** trên `.jtl` logs (dùng ChatGPT/Claude/Gemini)
- [ ] **Điền prompt** và **AI output** vào `ai_analysis_and_review.md`
- [ ] **Tìm và ghi lại các misinterpretation** của AI (ít nhất 3 ví dụ)
- [ ] **Cite giá trị đúng từ .jtl** cho mỗi misinterpretation
- [ ] **Đánh giá feasibility** cho từng optimization recommendation

### Thresholds
- [ ] **Điền AI-suggested thresholds** và **validated thresholds** vào bảng so sánh

---

## Task 3 — Cần làm

### Continuous Testing Proposal
- [ ] **Review flow chart** — đảm bảo mô tả đúng pipeline
- [ ] **Điền baseline thresholds** cụ thể từ kết quả test thực tế
- [ ] **Thêm chi tiết implementation** nếu cần (tùy chọn tools, config)
- [ ] **Verify trade-off discussion** đầy đủ và thực tế

---

## Files chung — Cần làm

### AI Audit Report
- [ ] **Điền đầy đủ 5+ interactions** với AI tool vào `ai_audit_report.md`
- [ ] **Ghi rõ ngày giờ, prompt, output, và hành động sửa** cho mỗi interaction

### AI Critique
- [ ] **Viết 200-300 words** critique vào `ai_critique.md`
- [ ] **Đảm bảo trả lời** đủ 3 câu hỏi: where wrong, why failed, lesson learned

### README
- [ ] **Điền Student ID, Name, Self-Assessed Grade**
- [ ] **Điền các giá trị** vào bảng self-assessment
- [ ] **Điền endurance threshold** và bug/performance issue count
- [ ] **Thêm YouTube link** và Git commit log

### Git
- [ ] **Tạo Git repo** cho bài nộp
- [ ] **Commit từng bước** (mỗi test plan, AI analysis, proposal)
- [ ] **Export Git commit log** thành text file

---

## Checklist cuối cùng

- [ ] Tên file test plan đúng format `{StudentID}_{ScenarioType}_{YYYYMMDD}`
- [ ] 3 file `.jtl` raw logs đầy đủ
- [ ] 3 HTML report folders
- [ ] Screenshots resource monitor + hardware spec
- [ ] Demo video >= 6 phút (tiếng Việt)
- [ ] AI Audit Report đầy đủ
- [ ] AI Critique 200-300 words
- [ ] Git commit log
- [ ] README.md với self-assessment table
- [ ] Zip file đúng format: `{StudentID}_HW05_AI_Performance_{SelfAssessedGrade}.zip`
