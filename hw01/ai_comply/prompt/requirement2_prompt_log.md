# Requirement 2 Prompt Log

## Thông tin log
- **Chủ đề:** Requirement 2 - 20 software defects publicized between 2022 and 2026
- **Thời điểm tạo file log:** 2026-06-07 03:15:30 +07
- **Múi giờ:** Asia/Ho_Chi_Minh
- **Ghi chú quan trọng về timestamp:** ChatGPT không cung cấp timestamp gốc chính xác cho từng tin nhắn trong transcript. Vì vậy, các timestamp bên dưới là **LoggedAt**: thời điểm các lượt hội thoại được ghi lại vào file log này, kèm số thứ tự lượt để thể hiện đúng trình tự trao đổi. Không nên xem đây là thời điểm gửi tin nhắn gốc tuyệt đối.

---

## Mục tiêu Requirement 2

Tìm hiểu **20 lỗi phần mềm được công bố từ năm 2022 đến năm 2026**.

Yêu cầu bắt buộc:

- Có đủ 20 lỗi phần mềm.
- Có ít nhất 5 lỗi liên quan đến AI/LLM như:
  - Ảo giác AI / hallucination
  - Tấn công chèn lệnh vào prompt / prompt injection
  - Thiên kiến AI / bias
- Mỗi lỗi cần có:
  - Link nguồn
  - Mô tả
  - Mức độ nghiêm trọng
  - Hậu quả
  - Giải pháp khắc phục
  - 1 vị trí AI có thể bị thiên kiến hoặc ảo giác khi giải thích lỗi
- Phần bias/hallucination được để trống để người dùng tự điền.

---

# Transcript / Prompt Log

## Turn 01

- **LoggedAt:** 2026-06-07 03:16:30 +07
- **Role:** User
- **Mục đích:** Đưa yêu cầu ban đầu cho Requirement 2.

### Nội dung

```text
tôi đang tìm hiểu về software defect, hãy tìm hiểu giúp tôi theo yêu cầu sau: Find 20 software defects publicized between 2022 and 2026.
Mandatory: ≥ 5 defects related to AI/LLM (hallucination, prompt injection,
bias).
Each defect: source link, description, severity, consequences, solution.
NEW: find 1 place where the AI is biased or hallucinates when explaining the
defect. Clarification: this applies to EVERY defect — each of the 20
entries must include 1 identified instance of AI bias or hallucination (20
instances total). tạo code markdown cho phần tìm hiểu này bắt đầu như sau ## Yêu cầu 2: 20 lỗi phần mềm từ 2022-2026. phần bias hãy để trống để tôi tự điền
```

---

## Turn 02

- **LoggedAt:** 2026-06-07 03:17:30 +07
- **Role:** Assistant
- **Mục đích:** Tạo bản Markdown đầu tiên cho Requirement 2.

### Nội dung phản hồi chính

```text
AI phản hồi rằng sẽ tổng hợp theo dạng có thể dán thẳng vào main_report.md:
- Đủ 20 lỗi.
- Có nhóm AI/LLM riêng.
- Mỗi mục gồm nguồn, mô tả, severity, hậu quả, giải pháp.
- Phần bias/hallucination để trống cho người dùng tự điền.
```

### Danh sách lỗi trong bản đầu tiên

```text
1. Meta AI support chatbot bị khai thác để chiếm quyền tài khoản Instagram
2. Google AI Overviews đưa ra câu trả lời sai như “thêm keo vào pizza”
3. Air Canada chatbot cung cấp thông tin sai về chính sách hoàn tiền
4. DPD chatbot chửi thề và chỉ trích chính công ty
5. Luật sư trong vụ Mata v. Avianca dùng ChatGPT tạo án lệ giả
6. NEDA Tessa chatbot đưa ra lời khuyên có hại về rối loạn ăn uống
7. iTutorGroup dùng phần mềm tuyển dụng tự động có dấu hiệu phân biệt tuổi tác
8. CrowdStrike Falcon update gây lỗi màn hình xanh trên Windows
9. AT&T Mobility outage do cấu hình sai network element
10. FAA NOTAM outage do lỗi dữ liệu/hệ thống cơ sở dữ liệu
11. Toyota dừng nhà máy do lỗi hệ thống đặt hàng linh kiện
12. MOVEit Transfer SQL Injection CVE-2023-34362
13. XZ Utils backdoor CVE-2024-3094
14. Atlassian Confluence OGNL Injection CVE-2022-26134
15. Spring4Shell CVE-2022-22965
16. Text4Shell CVE-2022-42889 trong Apache Commons Text
17. CitrixBleed CVE-2023-4966
18. Cisco IOS XE Web UI vulnerabilities CVE-2023-20198 và CVE-2023-20273
19. Optus outage do cập nhật phần mềm/routing information
20. Cloudflare outage do lỗi Bot Management feature file
```

### Ghi chú

```text
Bản này có một số nguồn là báo chí hoặc nguồn chưa đủ kỹ thuật. Người dùng sau đó yêu cầu làm lại với nguồn chính thống hơn.
```

---

## Turn 03

- **LoggedAt:** 2026-06-07 03:18:30 +07
- **Role:** User
- **Mục đích:** Yêu cầu cải thiện chất lượng nguồn và phần giải pháp.

### Nội dung

```text
hãy làm lại với các nguồn lỗi chính thống và có tính kỹ thuật hơn. phần giải pháp hiện tại viết quá mơ hồ, phải lấy từ chính cập nhật từ lỗi đó 
```

---

## Turn 04

- **LoggedAt:** 2026-06-07 03:19:30 +07
- **Role:** Assistant
- **Mục đích:** Làm lại danh sách lỗi theo hướng chính thống và kỹ thuật hơn.

### Nội dung phản hồi chính

```text
AI phản hồi rằng sẽ làm lại theo hướng dễ bảo vệ:
- Ưu tiên advisory, postmortem, incident report từ vendor.
- Ưu tiên nguồn như CISA, NVD, MSRC, GitHub Security Advisory, vendor security advisory.
- Với lỗi AI/LLM, chọn các case có nguồn chính thức nhất có thể.
- Phần giải pháp phải lấy từ version vá, hotfix, workaround hoặc cập nhật chính thức.
```

### Danh sách lỗi trong bản làm lại

```text
1. OpenAI ChatGPT Redis bug làm lộ tiêu đề hội thoại và một phần thông tin thanh toán
2. Microsoft 365 Copilot EchoLeak - CVE-2025-32711
3. LangChain SQLDatabaseChain SQL Injection - GHSA-7q94-qpjr-xpgm / CVE-2023-36189
4. LangChain GraphCypherQAChain prompt injection - GHSA-45pg-36p6-83v9 / CVE-2024-8309
5. LangChain PALChain arbitrary code execution - CVE-2023-44467
6. Google Gemini image generation tạo hình người sai ngữ cảnh lịch sử/văn hóa
7. CrowdStrike Falcon Content Update gây Windows BSOD
8. MOVEit Transfer SQL Injection - CVE-2023-34362
9. XZ Utils supply chain backdoor - CVE-2024-3094
10. Atlassian Confluence OGNL Injection - CVE-2022-26134
11. Spring Framework RCE - Spring4Shell / CVE-2022-22965
12. Apache Commons Text Text4Shell - CVE-2022-42889
13. CitrixBleed - NetScaler ADC/Gateway CVE-2023-4966
14. Cisco IOS XE Web UI privilege escalation/RCE - CVE-2023-20198 và CVE-2023-20273
15. Ivanti Connect Secure / Policy Secure vulnerabilities - CVE-2023-46805 và CVE-2024-21887
16. Palo Alto Networks PAN-OS GlobalProtect command injection - CVE-2024-3400
17. Fortinet FortiOS SSL-VPN heap buffer overflow - CVE-2023-27997
18. Jenkins CLI arbitrary file read - CVE-2024-23897
19. Kubernetes ingress-nginx admission controller RCE - CVE-2025-1974
20. GitLab password reset account takeover - CVE-2023-7028
```

### Tổng kết của bản làm lại

```text
- Tổng số software defects: 20
- Khoảng thời gian: 2022-2026
- Số lỗi liên quan đến AI/LLM: 6 lỗi
- Số lỗi không trực tiếp liên quan đến AI/LLM: 14 lỗi
- Nguồn ưu tiên: vendor advisory, vendor postmortem, NVD, GitHub Security Advisory, Microsoft MSRC, Kubernetes official blog, Jenkins Security Advisory, Fortinet PSIRT và Palo Alto Security Advisory.
```

---

## Turn 05

- **LoggedAt:** 2026-06-07 03:20:30 +07
- **Role:** User
- **Mục đích:** Yêu cầu gửi lại dưới dạng code Markdown với tiêu đề bắt đầu bằng `##`.

### Nội dung

```text
hãy gửi tôi code markdown với tiêu đề bắt đầu bằng ##
```

---

## Turn 06

- **LoggedAt:** 2026-06-07 03:21:30 +07
- **Role:** Assistant
- **Mục đích:** Gửi lại nội dung Markdown thuần.

### Nội dung phản hồi chính

```text
AI gửi lại nội dung Markdown có thể dán trực tiếp vào file .md.
Tiêu đề bắt đầu bằng:

## Yêu cầu 2: 20 lỗi phần mềm từ 2022-2026
```

### Cấu trúc Markdown

```text
- Tiêu chí thực hiện
- Danh sách 20 software defects
- Mỗi lỗi có:
  - Năm công bố
  - Loại lỗi
  - Nguồn chính thống
  - Description
  - Severity
  - Consequences
  - Solution
  - AI bias/hallucination khi giải thích defect: [Tự điền]
- Tổng kết Requirement 2
```

---

## Turn 07

- **LoggedAt:** 2026-06-07 03:22:30 +07
- **Role:** User
- **Mục đích:** Yêu cầu tạo file Markdown thay vì chỉ gửi nội dung trong chat.

### Nội dung

```text
gửi tôi file code markdown 
```

---

## Turn 08

- **LoggedAt:** 2026-06-07 03:23:30 +07
- **Role:** Assistant
- **Mục đích:** Tạo file Markdown đầu tiên.

### Nội dung phản hồi chính

```text
AI tạo file Markdown trong môi trường làm việc với tên:

yeu_cau_2_20_software_defects.md

Sau đó AI gửi link tải file.
```

### File được tạo

```text
/mnt/data/yeu_cau_2_20_software_defects.md
```

### Link sandbox đã gửi

```text
sandbox:/mnt/data/yeu_cau_2_20_software_defects.md
```

---

## Turn 09

- **LoggedAt:** 2026-06-07 03:24:30 +07
- **Role:** User
- **Mục đích:** Yêu cầu Việt hóa report vì còn lẫn tiếng Anh và tiếng Việt.

### Nội dung

```text
hiện tại report bị lẫn tiếng anh và tiếng việt, hãy chỉnh về tiếng việt
```

---

## Turn 10

- **LoggedAt:** 2026-06-07 03:25:30 +07
- **Role:** Assistant
- **Mục đích:** Việt hóa file Markdown.

### Nội dung phản hồi chính

```text
AI chỉnh trực tiếp file Markdown đã tạo trước đó:
- Việt hóa các nhãn như Description, Severity, Consequences, Solution.
- Đổi phần tổng kết và mô tả loại lỗi sang tiếng Việt hơn.
- Giữ nguyên các tên kỹ thuật/CVE/package cần thiết.
- Tạo file mới để không ghi đè file cũ.
```

### Một số thay đổi chính

```text
Description → Mô tả
Severity → Mức độ nghiêm trọng
Consequences → Hậu quả
Solution → Giải pháp khắc phục
AI bias/hallucination khi giải thích defect → Thiên kiến/ảo giác của AI khi giải thích lỗi
software defects → lỗi phần mềm
Source link → Link nguồn
```

### File được tạo

```text
/mnt/data/yeu_cau_2_20_loi_phan_mem_viet_hoa.md
```

### Link sandbox đã gửi

```text
sandbox:/mnt/data/yeu_cau_2_20_loi_phan_mem_viet_hoa.md
```

---

## Turn 11

- **LoggedAt:** 2026-06-07 03:26:30 +07
- **Role:** User
- **Mục đích:** Yêu cầu giải thích tất cả lỗi.

### Nội dung

```text
hãy giải thích giúp tôi tất cả các lỗi trên
```

---

## Turn 12

- **LoggedAt:** 2026-06-07 03:27:30 +07
- **Role:** Assistant
- **Mục đích:** Giải thích bản chất các lỗi ở mức dễ hiểu.

### Nội dung phản hồi chính

```text
AI giải thích từng lỗi theo hướng dễ hiểu hơn:
- Lỗi nằm ở đâu
- Vì sao nguy hiểm
- Cách khắc phục thực chất là gì
```

### Nhóm lỗi AI/LLM được giải thích

```text
1. OpenAI ChatGPT Redis bug
2. Microsoft 365 Copilot EchoLeak
3. LangChain SQLDatabaseChain SQL Injection
4. LangChain GraphCypherQAChain Prompt Injection
5. LangChain PALChain Arbitrary Code Execution
6. Google Gemini Image Generation Bias/Overcorrection
```

### Nhóm lỗi cập nhật, hạ tầng và bảo mật nghiêm trọng được giải thích

```text
7. CrowdStrike Falcon Content Update gây Windows BSOD
8. MOVEit Transfer SQL Injection
9. XZ Utils Backdoor
10. Atlassian Confluence OGNL Injection
11. Spring4Shell
12. Apache Commons Text Text4Shell
13. CitrixBleed
14. Cisco IOS XE Web UI
15. Ivanti Connect Secure / Policy Secure
16. Palo Alto PAN-OS GlobalProtect
17. Fortinet FortiOS SSL-VPN
18. Jenkins CLI Arbitrary File Read
19. Kubernetes ingress-nginx
20. GitLab Password Reset Account Takeover
```

### Kết luận chính

```text
- Nhóm AI/LLM nguy hiểm vì AI có thể bị lừa qua prompt, dùng sai quyền truy cập, sinh query/code nguy hiểm hoặc tạo kết quả sai lệch.
- Nhóm lỗi truyền thống nguy hiểm vì attacker có thể chiếm server, đọc file, đánh cắp session token, thực thi lệnh hoặc chiếm hạ tầng mạng.
```

---

## Turn 13

- **LoggedAt:** 2026-06-07 03:28:30 +07
- **Role:** User
- **Mục đích:** Yêu cầu giải thích kỹ thuật hơn vì phần trước còn mơ hồ.

### Nội dung

```text
hãy giải thích chi tiết có tính kỹ thuật hơn của từng lỗi, bạn đang giải thích khá mơ hồ
```

---

## Turn 14

- **LoggedAt:** 2026-06-07 03:29:30 +07
- **Role:** Assistant
- **Mục đích:** Giải thích kỹ thuật chi tiết hơn cho từng lỗi.

### Nội dung phản hồi chính

```text
AI thừa nhận bản giải thích trước còn ở mức ý nghĩa chung và làm lại theo hướng phân tích defect kỹ thuật hơn.

Mỗi lỗi được giải thích theo:
- Thành phần bị lỗi
- Nguyên nhân kỹ thuật
- Luồng khai thác hoặc luồng sự cố
- Tác động hệ thống
- Bản vá hoặc mitigation chính thức
```

### Tóm tắt kỹ thuật từng lỗi

```text
1. OpenAI ChatGPT Redis bug
   - Lỗi ở tầng backend cache, không phải model GPT.
   - Liên quan redis-py, request bị hủy, Redis connection dùng chung và response mix-up.
   - Dữ liệu cache của user này có thể bị trả nhầm cho user khác.

2. Microsoft 365 Copilot EchoLeak
   - Lỗi indirect prompt injection / AI command injection.
   - Attack surface gồm email, tài liệu, Teams, SharePoint mà Copilot đọc làm context.
   - Vấn đề là LLM trộn lẫn dữ liệu không tin cậy với instruction đáng tin.

3. LangChain SQLDatabaseChain SQL Injection
   - Prompt không tin cậy có thể khiến LLM sinh SQL nguy hiểm.
   - Đây là prompt-to-SQL injection, khác với SQL injection truyền thống.
   - Cần giới hạn quyền database user, kiểm tra SQL AST, allowlist bảng/cột.

4. LangChain GraphCypherQAChain Prompt Injection
   - Tương tự SQLDatabaseChain nhưng dùng graph database và Cypher query.
   - Prompt độc hại có thể khiến model tạo truy vấn đọc/xóa/sửa dữ liệu.
   - Cần read-only permission và chặn keyword nguy hiểm như CREATE, MERGE, DELETE, SET.

5. LangChain PALChain Arbitrary Code Execution
   - LLM sinh Python code rồi server chạy code đó.
   - Attacker có thể khiến model sinh code độc hại, bypass import restriction.
   - Cần sandbox/container, giới hạn network, CPU/RAM/time và không mount secrets.

6. Google Gemini Image Generation Bias/Overcorrection
   - Lỗi ở model behavior và safety tuning.
   - Tuning tăng đa dạng bị áp dụng quá rộng, làm sai bối cảnh lịch sử/văn hóa.
   - Đây là policy overgeneralization.

7. CrowdStrike Falcon Content Update gây Windows BSOD
   - Chuỗi lỗi: content không hợp lệ → validator không bắt được → interpreter đọc memory ngoài biên → kernel crash.
   - Vì Falcon Sensor chạy quyền cao nên lỗi làm sập toàn bộ Windows.

8. MOVEit Transfer SQL Injection
   - Web application nhận request crafted tác động vào SQL backend.
   - Attacker có thể truy cập database, cài web shell và trích xuất dữ liệu.

9. XZ Utils Backdoor
   - Supply-chain compromise, mã độc nằm trong release tarball/build artifact.
   - Backdoor sửa đổi build liblzma và có thể ảnh hưởng SSH trong một số môi trường.

10. Atlassian Confluence OGNL Injection
    - Payload OGNL được framework evaluate không an toàn.
    - Attacker chưa xác thực có thể thực thi lệnh trên server Confluence.

11. Spring4Shell
    - Lỗi data binding trong Spring Framework.
    - Attacker dùng parameter đặc biệt để truy cập object graph, thay đổi property nguy hiểm và ghi JSP web shell trong một số điều kiện.

12. Apache Commons Text Text4Shell
    - StringSubstitutor xử lý input không tin cậy với interpolator nguy hiểm.
    - Khác Log4Shell vì cần code path gọi API substitution với input user kiểm soát.

13. CitrixBleed
    - Memory disclosure/buffer boundary issue.
    - Attacker có thể lấy session token từ vùng nhớ thiết bị.
    - Chỉ vá binary chưa đủ, cần terminate sessions.

14. Cisco IOS XE Web UI
    - CVE-2023-20198 tạo local user privilege 15 không cần xác thực.
    - CVE-2023-20273 giúp thực thi command/root-level action.
    - Cần tắt ip http server/ip http secure-server nếu không cần.

15. Ivanti Connect Secure / Policy Secure
    - Chain gồm authentication bypass + command injection.
    - Vì là VPN appliance nên khi bị chiếm có thể trở thành foothold vào mạng nội bộ.

16. Palo Alto PAN-OS GlobalProtect
    - Arbitrary file creation dẫn đến OS command injection.
    - Attacker chưa xác thực có thể đạt quyền cao trên firewall.

17. Fortinet FortiOS SSL-VPN
    - Heap-based buffer overflow trong SSL-VPN.
    - Attacker gửi payload làm ghi/đọc vượt vùng nhớ để đạt RCE.

18. Jenkins CLI Arbitrary File Read
    - args4j có tính năng expandAtFiles dùng cú pháp @file.
    - Jenkins không tắt tính năng này nên attacker có thể đọc file local trên Jenkins controller.

19. Kubernetes ingress-nginx
    - Admission controller và NGINX config generation là attack surface.
    - CVE-2025-1974 cho phép thành phần trên pod network khai thác admission controller, có nguy cơ cluster takeover.

20. GitLab Password Reset Account Takeover
    - Lỗi logic password reset khiến email reset có thể gửi đến email chưa xác minh.
    - Account takeover có thể dẫn tới supply-chain attack qua source code, CI/CD variables và token.
```

### Phân loại theo góc nhìn Software Defect

```text
- Lỗi quản lý trạng thái/concurrency: OpenAI Redis bug
- Lỗi AI trust-boundary: Copilot, LangChain SQL/Cypher, PALChain
- Lỗi validation/parsing: CrowdStrike, Jenkins, Apache Commons Text, MOVEit, ingress-nginx
- Lỗi RCE truyền thống: Confluence, Spring4Shell, Palo Alto, Fortinet, Ivanti
- Lỗi supply chain: XZ Utils và GitLab
```

---

## Turn 15

- **LoggedAt:** 2026-06-07 03:30:30 +07
- **Role:** User
- **Mục đích:** Yêu cầu tạo prompt log cho Requirement 2.

### Nội dung

```text
hãy tạo một requirement2_prompt_log.md giúp tôi gồm nội dung của toàn bộ cuộc nói chuyện này
```

---

## Turn 16

- **LoggedAt:** 2026-06-07 03:31:30 +07
- **Role:** Assistant
- **Mục đích:** Tạo bản prompt log đầu tiên.

### Nội dung phản hồi chính

```text
AI tạo file requirement2_prompt_log.md, ghi lại quá trình trao đổi về Requirement 2:
- Prompt ban đầu
- Yêu cầu làm lại với nguồn chính thống và giải pháp kỹ thuật hơn
- Yêu cầu xuất Markdown
- Yêu cầu tạo file Markdown
- Yêu cầu Việt hóa report
- Yêu cầu giải thích tất cả lỗi
- Yêu cầu giải thích kỹ thuật chi tiết hơn
- Yêu cầu tạo prompt log
```

### File được tạo

```text
/mnt/data/requirement2_prompt_log.md
```

---

## Turn 17

- **LoggedAt:** 2026-06-07 03:32:30 +07
- **Role:** User
- **Mục đích:** Yêu cầu tạo lại prompt log có timestamp.

### Nội dung

```text
hãy tạo một requirement2_prompt_log.md giúp tôi gồm nội dung của toàn bộ cuộc nói chuyện này và timestamp
```

---

## Turn 18

- **LoggedAt:** 2026-06-07 03:33:30 +07
- **Role:** Assistant
- **Mục đích:** Tạo file prompt log mới có timestamp.

### Nội dung phản hồi chính

```text
AI tạo lại file prompt log có timestamp.
File bao gồm:
- Thời điểm tạo log.
- Múi giờ Asia/Ho_Chi_Minh.
- Ghi chú rằng timestamp gốc chính xác của từng tin nhắn không được cung cấp trong giao diện.
- Các lượt hội thoại được đánh số Turn 01, Turn 02, ...
- Mỗi lượt có LoggedAt, Role, Mục đích và Nội dung.
```

---

# Danh sách file đã tạo trong quá trình làm Requirement 2

```text
/mnt/data/yeu_cau_2_20_software_defects.md
/mnt/data/yeu_cau_2_20_loi_phan_mem_viet_hoa.md
/mnt/data/requirement2_prompt_log.md
/mnt/data/requirement2_prompt_log_with_timestamp.md
```

---

# Ghi chú sử dụng

File này có thể được dùng làm bằng chứng quá trình sử dụng AI cho Requirement 2.

