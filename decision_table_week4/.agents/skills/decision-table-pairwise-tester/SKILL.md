# Kỹ Năng Kiểm Thử: Decision Table & Pairwise Testing

## 1. Giới thiệu chung
Kỹ năng này hướng dẫn thiết kế các kịch bản kiểm thử (test cases) bằng hai kỹ thuật kết hợp nâng cao:
- **Decision Table Testing (Kiểm thử bảng quyết định)**: Thích hợp để mô tả các quy tắc nghiệp vụ phức tạp có sự kết hợp của nhiều điều kiện đầu vào sinh ra các hành động khác nhau.
- **Pairwise Testing (Kiểm thử phối hợp cặp)**: Giúp tối ưu hóa số lượng ca kiểm thử khi có nhiều biến đầu vào bằng cách đảm bảo mọi cặp giá trị của hai biến bất kỳ được kiểm thử ít nhất một lần.

---

## 2. Quy trình thiết kế Bảng Quyết định (Decision Table)

### Bước 2.1: Xác định Điều kiện (Conditions) và Hành động (Actions)
- **Conditions (Nguyên nhân/Đầu vào/Trạng thái)**: Các biến số, điều kiện môi trường hoặc đầu vào có thể thay đổi (ví dụ: Trạng thái token, Vai trò người dùng, API endpoint).
- **Actions (Kết quả/Hành động/Đầu ra)**: Các phản hồi mong đợi từ hệ thống (ví dụ: Cho phép truy cập 200 OK, Lỗi 401 Unauthorized, Lỗi 403 Forbidden).

### Bước 2.2: Xây dựng Bảng quyết định đầy đủ (Full Decision Table)
- Nếu có $n$ điều kiện dạng Nhị phân (Đúng/Sai), bảng sẽ có $2^n$ cột (quy tắc).
- Đối với điều kiện có nhiều hơn 2 giá trị, số cột sẽ bằng tích số lượng giá trị của mỗi điều kiện.

### Bước 2.3: Rút gọn Bảng quyết định (Reduced Decision Table)
- Áp dụng quy tắc gộp: Nếu hai hoặc nhiều quy tắc có cùng các hành động đầu ra và chỉ khác nhau ở một điều kiện duy nhất, ta có thể gộp chúng lại và đánh dấu điều kiện khác biệt đó là "Don't care" (ký hiệu `-` hoặc `N/A`).
- Việc rút gọn giúp giảm thiểu số lượng test case cần thiết mà không giảm độ bao phủ logic.

---

## 3. Quy trình thiết kế Pairwise (All-Pairs Testing)

### Bước 3.1: Xác định các biến số và miền giá trị của chúng
- Liệt kê toàn bộ các biến đầu vào độc lập và các giá trị tương đương (equivalence partitions) của chúng.

### Bước 3.2: Thực hiện sinh các cặp phối hợp (Pairwise Generation)
- Đảm bảo rằng với mọi cặp biến $(X, Y)$, tất cả các tổ hợp giá trị $(x_i, y_j)$ đều xuất hiện ít nhất một lần trong danh sách kịch bản.
- Có thể sử dụng các công cụ sinh hoặc xây dựng thủ công bằng cách ghép cặp có hệ thống.

---

## 4. Đặc tả mẫu đầu ra (Báo cáo bằng Tiếng Việt)
- **Test Design**:
  - Bảng định nghĩa các biến đầu vào và giá trị.
  - Bảng Quyết định Gốc & Bảng Quyết định Rút gọn (dạng Markdown).
  - Cấu hình và bảng tổ hợp Pairwise.
- **Test Cases**:
  - Mã test case rõ ràng (ví dụ: `FR12-DT-01` cho Decision Table, `FR12-PW-01` cho Pairwise).
  - Có ánh xạ cụ thể đến Quy tắc (Rule) trong bảng quyết định hoặc cặp Pairwise để dễ dàng truy vết (traceability).
