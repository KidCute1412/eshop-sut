# TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN - ĐHQG-HCM
## KHOA CÔNG NGHỆ THÔNG TIN
### BỘ MÔN CÔNG NGHỆ PHẦN MỀM

<p align="center">
  <img src="images/logo-hcmus.png" alt="HCMUS Logo" width="150px"/>
</p>

---

# BÁO CÁO BÀI TẬP VỀ NHÀ 2
## MÔN HỌC: KIỂM THỬ PHẦN MỀM (SE310)
### ĐỀ TÀI: KIỂM THỬ PHẦN MỀM VỚI SỰ HỖ TRỢ CỦA AI (HW02 - BVA & DOMAIN TESTING)

**Thông tin sinh viên:**
- **Họ và tên:** Lê Tuấn Lộc
- **Mã số sinh viên:** 23127404
- **Lớp:** 23KTPM3

**Giảng viên hướng dẫn:**
- Cô Trần Thị Bích Hạnh
- Thầy Trương Phước Lộc
- Thầy Hồ Tuấn Thanh

**Điểm tự đánh giá (Self-Assessment Grade):** 100/100

*Thành phố Hồ Chí Minh, Tháng 6 Năm 2026*

---

## MỤC LỤC (TABLE OF CONTENTS)
1. [FR-06: Product Detail View](#1-fr-06-product-detail-view)
   - 1.1. Domain Testing
   - 1.2. Boundary Value Analysis (BVA)
   - 1.3. AI Gap Analysis & Screenshot Proofs
2. [FR-10: Order State Machine](#2-fr-10-order-state-machine)
   - 2.1. Domain Testing
   - 2.2. Boundary Value Analysis (BVA)
   - 2.3. AI Gap Analysis & Screenshot Proofs
3. [FR-12: Access Control](#3-fr-12-access-control)
   - 3.1. Domain Testing
   - 3.2. Boundary Value Analysis (BVA)
   - 3.3. AI Gap Analysis & Screenshot Proofs
4. [FR-20: Mobile App](#4-fr-20-mobile-app)
   - 4.1. Domain Testing
   - 4.2. Boundary Value Analysis (BVA)
   - 4.3. AI Gap Analysis & Screenshot Proofs

---

## 1. FR-06: Product Detail View

### 1.1. Domain Testing
#### 1.1.1. Xác định các biến đầu vào & Điều kiện hệ thống
Chúng tôi xác định các biến và điều kiện hệ thống sau cho tính năng Xem Chi tiết Sản phẩm (FR-06):
1. **Quantity (Số lượng)**: Trường nhập liệu cho phép người dùng chỉ định số lượng mặt hàng muốn thêm vào giỏ hàng. Được đặc tả là chỉ nhận số nguyên dương tối thiểu là 1.
2. **Product ID (Mã sản phẩm)**: Tham số đường dẫn trên URL chỉ định sản phẩm cần hiển thị. Sản phẩm này phải tồn tại trong cơ sở dữ liệu.
3. **User Authentication State (Trạng thái xác thực người dùng)**: Mặc dù khách vãng lai vẫn có thể xem sản phẩm và thêm vào giỏ hàng, trạng thái đăng nhập của người dùng là một điều kiện môi trường.

#### 1.1.2. Bảng Phân hoạch tương đương (Equivalence Partitioning)
| Biến đầu vào / Điều kiện | Lớp tương đương hợp lệ (ID) | Lớp tương đương không hợp lệ (ID) |
| :--- | :--- | :--- |
| **Quantity (Số lượng)**<br>*(Kiểu: Số nguyên)* | **EP-VAL-01**: Số nguyên dương $\ge 1$ (ví dụ: 1, 5, 99) | **EP-INV-01**: Số nguyên $< 1$ (ví dụ: 0, -5)<br>**EP-INV-02**: Số thập phân / số thực (ví dụ: 1.5, 2.7)<br>**EP-INV-03**: Chuỗi không phải số / ký tự đặc biệt / để trống (ví dụ: "abc", "@", "")<br>**EP-INV-04**: Số nguyên cực kỳ lớn gây tràn viền (ví dụ: 99999999999) |
| **Product ID (Mã sản phẩm)**<br>*(Kiểu: Số nguyên)* | **EP-VAL-02**: Mã sản phẩm tồn tại trong cơ sở dữ liệu (ví dụ: ID = 1) | **EP-INV-05**: Mã sản phẩm không tồn tại (ví dụ: ID = 9999)<br>**EP-INV-06**: Định dạng ID không hợp lệ (ví dụ: số âm, chuỗi chữ "abc") |
| **User Authentication State**<br>*(Trạng thái)* | **EP-VAL-03**: Người dùng đã đăng nhập<br>**EP-VAL-04**: Khách vãng lai (chưa đăng nhập) | *Không có* |

#### 1.1.3. Các kịch bản kiểm thử (Domain Testing)
| Mã Kịch bản | Mô tả kiểm thử | Đầu vào | Kết quả mong đợi | Trạng thái | Ánh xạ truy vết |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR06-DT-01 | Xem thông tin chi tiết sản phẩm tồn tại dưới vai trò khách vãng lai. | Product ID = 1, User = Guest | Hiển thị đầy đủ ảnh lớn, tên sản phẩm, giá (định dạng phân cách hàng nghìn với ₫), mô tả và danh mục. | Pass | EP-VAL-02, EP-VAL-04 |
| FR06-DT-02 | Xem thông tin chi tiết sản phẩm tồn tại dưới vai trò người dùng đã đăng nhập. | Product ID = 1, User = Logged in | Hiển thị thông tin chi tiết sản phẩm thành công. | Pass | EP-VAL-02, EP-VAL-03 |
| FR06-DT-03 | Xem trang chi tiết của sản phẩm không tồn tại. | Product ID = 9999 | Hiển thị thông báo lỗi "Sản phẩm không tồn tại" hoặc điều hướng an toàn (không bị trắng trang). | Fail | EP-INV-05 |
| FR06-DT-04 | Thêm vào giỏ hàng với số lượng là số nguyên dương hợp lệ. | Product ID = 1, Quantity = 3 | Sản phẩm được thêm vào giỏ, cập nhật badge giỏ hàng, hiển thị thông báo toast hoặc badge cập nhật trực quan. | Fail | EP-VAL-01, EP-VAL-02 |
| FR06-DT-05 | Thêm vào giỏ hàng với số lượng âm. | Product ID = 1, Quantity = -5 | Từ chối đầu vào, hiển thị thông báo lỗi hoặc reset về giá trị mặc định. | Fail | EP-INV-01, EP-VAL-02 |
| FR06-DT-06 | Thêm vào giỏ hàng với số lượng không phải là số. | Product ID = 1, Quantity = "abc" | Từ chối đầu vào, hiển thị thông báo lỗi hoặc đặt lại về 1. | Fail | EP-INV-03, EP-VAL-02 |
| FR06-DT-07 | Thêm vào giỏ hàng với số lượng là số thập phân. | Product ID = 1, Quantity = 2.5 | Từ chối đầu vào hoặc làm tròn có thông báo cảnh báo cho người dùng. | Fail | EP-INV-02, EP-VAL-02 |

#### 1.1.4. Giải thích áp dụng kỹ thuật
1. **Xác định biến**: Phân tích đặc tả yêu cầu FR-06 để xác định đầu vào trực tiếp (`Số lượng`), tham số đường dẫn (`Mã sản phẩm`), và trạng thái hệ thống (`Trạng thái đăng nhập`).
2. **Xác định các phân hoạch**: Với mỗi biến, thiết lập các khoảng giá trị hợp lệ (ví dụ: số nguyên dương $\ge 1$ cho số lượng) và không hợp lệ (số thập phân, chuỗi ký tự, số âm) dựa trên tài liệu đặc tả.
3. **Thiết kế kịch bản**: Kết hợp các phân hoạch này thành các kịch bản kiểm thử rõ ràng, bao gồm cả luồng thông thường (Normal cases) và luồng lỗi ngoại lệ (Robust cases). Ánh xạ truy vết đảm bảo mọi phân hoạch đều được kiểm thử ít nhất một lần.

---

### 1.2. Phân tích giá trị biên (Boundary Value Analysis)
#### 1.2.1. Bảng Phân tích giá trị biên
| Biến / Thuộc tính | Điều kiện biên (ID) | Điểm biên (On-Point) | Điểm cận biên (Off-Point) | Điểm trong biên (In-Point) |
| :--- | :--- | :--- | :--- | :--- |
| **Quantity (Số lượng)** | Phải $\ge 1$ (BVA-BND-01) | 1 | 0 (không hợp lệ), 2 (hợp lệ) | 5 |

#### 1.2.2. Các kịch bản kiểm thử (BVA)
| Mã Kịch bản | Mô tả kiểm thử | Đầu vào | Kết quả mong đợi | Trạng thái | Ánh xạ truy vết |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR06-BVA-01 | Thêm vào giỏ hàng với số lượng nằm chính xác tại biên dưới. | Product ID = 1, Quantity = 1 | Sản phẩm được thêm vào giỏ hàng thành công, hiển thị thông báo phản hồi trực quan. | Fail | BVA-BND-01 (On-Point) |
| FR06-BVA-02 | Thêm vào giỏ hàng với số lượng nằm ngay dưới biên dưới. | Product ID = 1, Quantity = 0 | Từ chối đầu vào, hiển thị lỗi hoặc vô hiệu hóa nút thêm. | Fail | BVA-BND-01 (Off-Point, không hợp lệ) |
| FR06-BVA-03 | Thêm vào giỏ hàng với số lượng nằm ngay trên biên dưới. | Product ID = 1, Quantity = 2 | Sản phẩm được thêm vào giỏ hàng thành công, hiển thị thông báo. | Fail | BVA-BND-01 (Off-Point, hợp lệ) |
| FR06-BVA-04 | Thêm vào giỏ hàng với số lượng là một giá trị đại diện nằm trong biên. | Product ID = 1, Quantity = 5 | Sản phẩm được thêm thành công. | Fail | BVA-BND-01 (In-Point) |

#### 1.2.3. Giải thích áp dụng kỹ thuật
1. **Xác định biên**: Vì trường số lượng có giới hạn dưới nghiêm ngặt là 1, chúng tôi xác định điểm biên tại giá trị 1.
2. **Lựa chọn các điểm kiểm thử**:
   - **Điểm biên (On-point)** là giá trị biên: `1` (hợp lệ).
   - **Điểm cận biên (Off-points)** là các giá trị liền kề biên: `0` (không hợp lệ, nằm ngoài) và `2` (hợp lệ, nằm trong).
   - **Điểm trong biên (In-point)** là một giá trị đại diện nằm an toàn bên trong khoảng: `5`.
3. **Xây dựng bộ test**: Tạo các kịch bản kiểm thử cho từng điểm đã chọn, ghi nhận trạng thái thực tế phản ánh lỗi hiện có trong hệ thống SUT.

---

### 1.3. AI Gap Analysis & Screenshot Proofs
*Identify missed test cases or bugs by AI tools, and explain why they were missed.*

#### Minh chứng kết quả chạy test / lỗi phát hiện (Screenshots):
*(Dán hình ảnh minh chứng từ thư mục `images/` vào đây)*
```markdown
![FR06 Verification](images/fr06_verification.png)
```

---
---

## 2. FR-10: Order State Machine

### 2.1. Domain Testing
#### 2.1.1. Input Variables & Condition Identification
*List all input variables, state variables, or environmental conditions.*

#### 2.1.2. Equivalence Partitioning Table
| Input Variable / Condition | Valid Equivalence Classes (ID) | Invalid Equivalence Classes (ID) |
| :--- | :--- | :--- |
| | | |

#### 2.1.3. Test Cases Designed (Domain Testing)
| Test Case ID | Test Description | Inputs | Expected Outcome | Status | Traceability Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR10-DT-01 | | | | | |

#### 2.1.4. Application Explanation
*Step-by-step explanation of how the domain testing technique was applied.*

---

### 2.2. Boundary Value Analysis (BVA)
#### 2.2.1. Boundary Analysis Table
| Variable / Property | Boundary Condition (ID) | On-Point | Off-Point | In-Point |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

#### 2.2.2. Test Cases Designed (BVA)
| Test Case ID | Test Description | Inputs | Expected Outcome | Status | Traceability Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR10-BVA-01 | | | | | |

#### 2.2.3. Application Explanation
*Step-by-step explanation of how BVA was applied.*

---

### 2.3. AI Gap Analysis & Screenshot Proofs
*Identify missed test cases or bugs by AI tools, and explain why they were missed.*

#### Minh chứng kết quả chạy test / lỗi phát hiện (Screenshots):
*(Dán hình ảnh minh chứng từ thư mục `images/` vào đây)*
```markdown
![FR10 Verification](images/fr10_verification.png)
```

---
---

## 3. FR-12: Access Control

### 3.1. Domain Testing
#### 3.1.1. Input Variables & Condition Identification
*List all input variables, state variables, or environmental conditions.*

#### 3.1.2. Equivalence Partitioning Table
| Input Variable / Condition | Valid Equivalence Classes (ID) | Invalid Equivalence Classes (ID) |
| :--- | :--- | :--- |
| | | |

#### 3.1.3. Test Cases Designed (Domain Testing)
| Test Case ID | Test Description | Inputs | Expected Outcome | Status | Traceability Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR12-DT-01 | | | | | |

#### 3.1.4. Application Explanation
*Step-by-step explanation of how the domain testing technique was applied.*

---

### 3.2. Boundary Value Analysis (BVA)
#### 3.2.1. Boundary Analysis Table
| Variable / Property | Boundary Condition (ID) | On-Point | Off-Point | In-Point |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

#### 3.2.2. Test Cases Designed (BVA)
| Test Case ID | Test Description | Inputs | Expected Outcome | Status | Traceability Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR12-BVA-01 | | | | | |

#### 3.2.3. Application Explanation
*Step-by-step explanation of how BVA was applied.*

---

### 3.3. AI Gap Analysis & Screenshot Proofs
*Identify missed test cases or bugs by AI tools, and explain why they were missed.*

#### Minh chứng kết quả chạy test / lỗi phát hiện (Screenshots):
*(Dán hình ảnh minh chứng từ thư mục `images/` vào đây)*
```markdown
![FR12 Verification](images/fr12_verification.png)
```

---
---

## 4. FR-20: Mobile App

### 4.1. Domain Testing
#### 4.1.1. Input Variables & Condition Identification
*List all input variables, state variables, or environmental conditions.*

#### 4.1.2. Equivalence Partitioning Table
| Input Variable / Condition | Valid Equivalence Classes (ID) | Invalid Equivalence Classes (ID) |
| :--- | :--- | :--- |
| | | |

#### 4.1.3. Test Cases Designed (Domain Testing)
| Test Case ID | Test Description | Inputs | Expected Outcome | Status | Traceability Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR20-DT-01 | | | | | |

#### 4.1.4. Application Explanation
*Step-by-step explanation of how the domain testing technique was applied.*

---

### 4.2. Boundary Value Analysis (BVA)
#### 4.2.1. Boundary Analysis Table
| Variable / Property | Boundary Condition (ID) | On-Point | Off-Point | In-Point |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

#### 4.2.2. Test Cases Designed (BVA)
| Test Case ID | Test Description | Inputs | Expected Outcome | Status | Traceability Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR20-BVA-01 | | | | | |

#### 4.2.3. Application Explanation
*Step-by-step explanation of how BVA was applied.*

---

### 4.3. AI Gap Analysis & Screenshot Proofs
*Identify missed test cases or bugs by AI tools, and explain why they were missed.*

#### Minh chứng kết quả chạy test / lỗi phát hiện (Screenshots):
*(Dán hình ảnh minh chứng từ thư mục `images/` vào đây)*
```markdown
![FR20 Verification](images/fr20_verification.png)
```
