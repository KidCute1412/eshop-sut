# Mobile: FR-03 - Forgot Password & Password Reset (Two Steps)

## 1. Thông tin Feature

| Thuộc tính | Giá trị |
|-----------|--------|
| Feature ID | FR-03 |
| Tên | Forgot Password and Password Reset (two steps) |
| Actor | Người dùng (chưa đăng nhập) |
| Interface | Mobile (Expo React Native) |
| URL | Mobile App (Expo Go) |
| Tài khoản test | Email: `gmail` / Password: `Password 1` (user đã đăng ký) |

## 2. Kết quả Code Inspection

### 2.1 Luồng xử lý

**Step 1 - Request OTP**:
- Mobile gửi `POST /api/forgot-password` với body `{ email }`
- Backend tạo resetToken = `Math.floor(1000 + Math.random() * 9000).toString()` (4 chữ số)
- Backend trả về token trong response (server.js)

**Step 2 - Reset Password**:
- Mobile gửi `POST /api/reset-password` với body `{ email, resetToken, newPassword }`
- Backend kiểm tra token, cập nhật password (server.js)

### 2.2 Bugs phát hiện qua code inspection

| # | Bug ID | Mô tả | File | Dòng | Severity |
|---|--------|-------|------|------|----------|
| 1 | FP-BUG-01 | **OTP lộ trong response API**: Backend trả về resetToken trong response json | server.js | ~97-103 | **Cao** |
| 2 | FP-BUG-02 | **OTP hiển thị trên màn hình Web**: Web ForgotPassword hiển thị OTP trực tiếp | ForgotPassword.jsx | ~20 | **Cao** |
| 3 | FP-BUG-03 | **Sai regex password: dùng `\s` thay vì ký tự đặc biệt**: Yêu cầu whitespace, không phải special char | App.js (mobile) | ~268 | **Cao** |
| 4 | FP-BUG-04 | **Không validate OTP 4 số**: Có thể nhập OTP dài hơn 4 số | App.js (mobile) | ~278 | **Trung bình** |
| 5 | FP-BUG-05 | **Không rate-limit reset-password**: Có thể brute-force OTP (chỉ 10000 giá trị) | server.js | ~107-117 | **Cao** |
| 6 | FP-BUG-06 | **Thông báo lộ thông tin email**: Web ForgotPassword cho biết email có tồn tại hay không | server.js | ~95-97 | **Trung bình** |
| 7 | FP-BUG-07 | **Login attempts tăng gấp đôi**: `login_attempts + 2` thay vì `+1` | server.js | ~75 | **Trung bình** |
| 8 | FP-BUG-08 | **Email field không validate định dạng**: Dùng `type="text"` thay vì `type="email"` | App.js (mobile) | ~855 | **Thấp** |
| 9 | FP-BUG-09 | **Sai thông báo lỗi reset password**: Mobile dùng `Alert.alert` nhưng thông báo chung chung | App.js (mobile) | ~280 | **Thấp** |

### 2.3 Chi tiết code bug

#### FP-BUG-01: Backend trả OTP trong response (server.js:97-103)
```javascript
app.post("/api/forgot-password", (req, res) => {
    const { email } = req.body;
    db.get("SELECT * FROM users WHERE email = ?", [email], (err, user) => {
        if (!user) return res.status(404).json({ error: "User not found" });
        const resetToken = Math.floor(1000 + Math.random() * 9000).toString();
        db.run("UPDATE users SET reset_token = ? WHERE id = ?", [resetToken, user.id], (err) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({
                message: "Mã đặt lại mật khẩu đã được tạo",
                resetToken: resetToken,  // <-- BUG: Trả OTP trong response
            });
        });
    });
});
```

#### FP-BUG-03: Sai regex password (mobile App.js:~268)
```javascript
const strongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$/;
// Trong forgot-password lại dùng:
/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/
// BUG: (?=.*\s) yêu cầu whitespace, trong khi (?=.*[^A-Za-z\d]) mới là special char
```

## 3. Domain Testing - Equivalence Partitioning

### 3.1 Biến phân tích - Forgot Password (Step 1)

**Biến 1: email**
- Kiểu: string (email address)
- Format: local-part@domain

**Biến 2: sự tồn tại của email trong hệ thống**
- Boolean: exists / not exists

### 3.2 Biến phân tích - Reset Password (Step 2)

**Biến 3: resetToken (OTP)**
- Kiểu: string (4 chữ số)
- Range: 1000-9999

**Biến 4: newPassword**
- Kiểu: string
- Length: >= 8
- Phải có: chữ hoa, chữ thường, số, ký tự đặc biệt (theo requirement)

### 3.3 Variable and Condition Table

| Variable ID | Input/Output | Condition ID | Exact condition | Source |
|------------|-------------|-------------|----------------|--------|
| V1 | Input | C1 | email có format hợp lệ (có @) | API spec |
| V2 | Input | C2 | email tồn tại trong hệ thống | Server logic |
| V3 | Input | C3 | resetToken là 4 chữ số (1000-9999) | server.js |
| V4 | Input | C4 | resetToken khớp với DB | Server logic |
| V5 | Input | C5 | newPassword >= 8 ký tự | Frontend validation |
| V6 | Input | C6 | newPassword có chữ hoa | Regex |
| V7 | Input | C7 | newPassword có chữ thường | Regex |
| V8 | Input | C8 | newPassword có số | Regex |
| V9 | Input | C9 | newPassword có ký tự đặc biệt | Regex |

### 3.4 Raw Equivalence Class Table

| EC ID | Variable ID | Condition ID | Validity | Precise class |
|-------|------------|-------------|---------|--------------|
| EC1 | V1 | C1 | Valid | Email hợp lệ (có @domain) |
| EC2 | V1 | C1 | Invalid | Email không có @ |
| EC3 | V1 | C1 | Invalid | Email rỗng |
| EC4 | V2 | C2 | Valid | Email tồn tại trong DB |
| EC5 | V2 | C2 | Invalid | Email không tồn tại trong DB |
| EC6 | V3 | C3 | Valid | resetToken = 4 chữ số (1000-9999) |
| EC7 | V3 | C3 | Invalid | resetToken < 4 chữ số |
| EC8 | V3 | C3 | Invalid | resetToken > 4 chữ số |
| EC9 | V3 | C3 | Invalid | resetToken không phải số |
| EC10 | V4 | C4 | Valid | resetToken khớp với DB |
| EC11 | V4 | C4 | Invalid | resetToken không khớp |
| EC12 | V4 | C4 | Invalid | resetToken đã hết hạn (không có trong DB) |
| EC13 | V5 | C5 | Valid | newPassword >= 8 ký tự |
| EC14 | V5 | C5 | Invalid | newPassword < 8 ký tự |
| EC15 | V6 | C6 | Valid | Có chữ hoa |
| EC16 | V6 | C6 | Invalid | Không có chữ hoa |
| EC17 | V7 | C7 | Valid | Có chữ thường |
| EC18 | V7 | C7 | Invalid | Không có chữ thường |
| EC19 | V8 | C8 | Valid | Có số |
| EC20 | V8 | C8 | Invalid | Không có số |
| EC21 | V9 | C9 | Valid | Có ký tự đặc biệt |
| EC22 | V9 | C9 | Invalid | Không có ký tự đặc biệt |

### 3.5 Combined Equivalence Class Table - Step 1 (Request OTP)

| Combined EC ID | Covered raw EC IDs | Validity | Combined condition | Expected behavior | Bug |
|---------------|-------------------|---------|-------------------|------------------|-----|
| CEC-FP1 | EC1, EC4 | Valid | Email hợp lệ + tồn tại | Gửi OTP (thành công) | FP-BUG-01 (OTP lộ) |
| CEC-FP2 | EC1, EC5 | Valid | Email hợp lệ + không tồn tại | Thông báo lỗi chung chung | FP-BUG-06 (lộ thông tin) |
| CEC-FP3 | EC2 | Invalid | Email không có @ | Báo lỗi format email | - |
| CEC-FP4 | EC3 | Invalid | Email rỗng | Báo lỗi không được để trống | - |

### 3.6 Combined Equivalence Class Table - Step 2 (Reset Password)

| Combined EC ID | Covered raw EC IDs | Validity | Combined condition | Expected behavior | Bug |
|---------------|-------------------|---------|-------------------|------------------|-----|
| CEC-RP1 | EC6, EC10, EC13, EC15, EC17, EC19, EC21 | Valid | OTP đúng + password mạnh | Reset thành công | - |
| CEC-RP2 | EC6, EC11 | Invalid | OTP sai | Báo lỗi OTP không đúng | - |
| CEC-RP3 | EC7 | Invalid | OTP 3 số | Báo lỗi | - |
| CEC-RP4 | EC8 | Invalid | OTP 5+ số | Báo lỗi (hoặc cắt) | FP-BUG-04 (không validate) |
| CEC-RP5 | EC9 | Invalid | OTP chứa chữ | Báo lỗi | FP-BUG-04 (chấp nhận) |
| CEC-RP6 | EC13, EC16, EC17, EC19, EC21 | Invalid | password >=8, thiếu chữ hoa | Báo lỗi password yếu | - |
| CEC-RP7 | EC13, EC15, EC18, EC19, EC21 | Invalid | password >=8, thiếu chữ thường | Báo lỗi password yếu | - |
| CEC-RP8 | EC13, EC15, EC17, EC20, EC21 | Invalid | password >=8, thiếu số | Báo lỗi password yếu | - |
| CEC-RP9 | EC13, EC15, EC17, EC19, EC22 | Invalid | password >=8, thiếu special char | **BUG**: Sai regex dùng `\s` (whitespace) | FP-BUG-03 |
| CEC-RP10 | EC14 | Invalid | password < 8 ký tự | Báo lỗi password yếu | - |
| CEC-RP11 | EC6, EC10, EC13, EC15, EC17, EC19, EC21 | **Brute force** | Với mọi OTP 0000-9999 | **BUG**: Có thể brute-force OTP | FP-BUG-05 |

### 3.7 Representative Test Selection

| Selection ID | Target EC IDs | Test inputs | Expected result | Bug phát hiện |
|-------------|--------------|------------|----------------|--------------|
| TC-FP-01 | CEC-FP1 | Email tồn tại: gmail | OTP được tạo (nhưng không lộ) | FP-BUG-01 (OTP lộ trong response) |
| TC-FP-02 | CEC-FP2 | Email không tồn tại: notexist@test.com | "Nếu email tồn tại..." (mobile) | FP-BUG-06 (Web khác biệt) |
| TC-FP-03 | CEC-FP3 | Email không có @: "notanemail" | Lỗi format email | - |
| TC-FP-04 | CEC-FP4 | Email rỗng: "" | Lỗi không được để trống | - |
| TC-RP-01 | CEC-RP1 | OTP đúng + Password mới mạnh | Reset thành công | - |
| TC-RP-02 | CEC-RP2 | OTP sai | Lỗi "OTP không đúng" | - |
| TC-RP-03 | CEC-RP4 | OTP dài 6 số | Lỗi hoặc cắt bớt | FP-BUG-04 (chấp nhận) |
| TC-RP-04 | CEC-RP5 | OTP chứa chữ: "abcd" | Lỗi OTP phải là số | FP-BUG-04 (chấp nhận) |
| TC-RP-05 | CEC-RP9 | Password: "Pass12345" (thiếu special char, có whitespace) | **BUG**: Sai regex chấp nhận | FP-BUG-03 |
| TC-RP-06 | CEC-RP11 | Brute-force OTP: thử 0000-9999 | **Bỏ qua sau vài lần sai** | FP-BUG-05 (không rate-limit) |
| TC-RP-07 | CEC-RP9 | Password đúng: "Pass1234@" (có special char) | Chấp nhận hoặc từ chối | FP-BUG-03 |

## 4. Boundary Value Analysis (BVA)

### 4.1 Biên cho newPassword length

| Boundary ID | Variable ID | EC ID | Boundary type | Valid boundary | Variant |
|------------|------------|-------|--------------|---------------|---------|
| B-FP1 | V5 | EC13 | Valid minimum | 8 | 3-point |
| B-FP2 | V5 | EC13 | Valid maximum | Không giới hạn | 3-point |

### 4.2 Biên cho OTP

| Boundary ID | Variable ID | EC ID | Boundary type | Valid boundary | Variant |
|------------|------------|-------|--------------|---------------|---------|
| B-FP3 | V3 | EC6 | Valid minimum | 1000 | 3-point |
| B-FP4 | V3 | EC6 | Valid maximum | 9999 | 3-point |

### 4.3 Boundary Value Selection

| Selection ID | Boundary ID | Position | Concrete value | Valid/Invalid | Expected behavior |
|-------------|------------|----------|---------------|--------------|------------------|
| BVA-FP-01 | B-FP1 | Below | 7 (Pass123@ = 7) | Invalid | Từ chối, password yếu |
| BVA-FP-02 | B-FP1 | On | 8 (Pass123@) | Valid | Chấp nhận |
| BVA-FP-03 | B-FP1 | Above | 9 (Pass123@a) | Valid | Chấp nhận |
| BVA-FP-04 | B-FP3 | Below | 999 (< 1000) | Invalid | Từ chối |
| BVA-FP-05 | B-FP3 | On | 1000 (OTP hợp lệ) | Valid | Chấp nhận |
| BVA-FP-06 | B-FP3 | Above | 1001 (OTP hợp lệ) | Valid | Chấp nhận |
| BVA-FP-07 | B-FP4 | Below | 9998 (OTP hợp lệ) | Valid | Chấp nhận |
| BVA-FP-08 | B-FP4 | On | 9999 (OTP hợp lệ) | Valid | Chấp nhận |
| BVA-FP-09 | B-FP4 | Above | 10000 (> 9999) | Invalid | Từ chối |

## 5. Test Case - Chi tiết

### TC-FP-01: Request OTP với email tồn tại (Step 1)

**Môi trường**: Mobile App hoặc test API

| Bước | Mô tả | Dữ liệu |
|------|-------|---------|
| 1 | Mở mobile app, chọn "Quên mật khẩu?" | - |
| 2 | Nhập email đã đăng ký | `test@eshop.com` |
| 3 | Nhấn "Lấy mã OTP" | - |
| 4 | **Quan sát response API** | |

**Expected**: API trả về 200, `{ message: "Mã đặt lại mật khẩu đã được tạo" }` (không kèm resetToken)  
**Actual (bug)**: API trả về resetToken trong response  
**Bug**: **FP-BUG-01** - OTP bị lộ

### TC-RP-05: Reset password với whitespace thay vì special char

| Bước | Mô tả | Dữ liệu |
|------|-------|---------|
| 1 | Vào Step 2 của Forgot Password | - |
| 2 | Nhập OTP hợp lệ | `1234` |
| 3 | Nhập password có whitespace (đáp ứng regex sai) | `Pass 1234` (có space, không có special char) |
| 4 | Nhấn "Đặt lại mật khẩu" | - |

**Expected**: Từ chối vì thiếu ký tự đặc biệt  
**Actual (bug)**: Chấp nhận vì regex dùng `(?=.*\s)` thay vì `(?=.*[^A-Za-z\d])`  
**Bug**: **FP-BUG-03** - Sai regex password

### TC-RP-04: OTP chứa chữ

| Bước | Mô tả | Dữ liệu |
|------|-------|---------|
| 1 | Vào Step 2 của Forgot Password | - |
| 2 | Nhập OTP chứa chữ | `abcd` |
| 3 | Nhập password hợp lệ | `Pass1234@` |
| 4 | Nhấn "Đặt lại mật khẩu" | - |

**Expected**: Báo lỗi OTP phải là 4 chữ số  
**Actual**: Mobile gửi request lên backend, backend parse OTP = 0 (NaN), báo "Invalid token"  
**Bug**: **FP-BUG-04** - Không validate OTP là số

### TC-RP-06: Brute-force OTP (rate-limiting)

| Bước | Mô tả |
|------|-------|
| 1 | Có email hợp lệ `test@eshop.com` |
| 2 | Gửi request forgot-password để lấy OTP thật (biết qua FP-BUG-01) |
| 3 | Gửi request reset-password với OTP sai liên tục 10000 lần |
| 4 | **Quan sát**: Có bị chặn sau N lần thử không? |

**Expected**: Chặn sau 5-10 lần thử sai  
**Actual**: Không có rate-limiting, có thể brute-force  
**Bug**: **FP-BUG-05**

## 6. Bug Details

### FP-BUG-01: OTP lộ trong response API (Cao)

**File**: `backend/server.js:100-103`
```javascript
res.json({
    message: "Mã đặt lại mật khẩu đã được tạo",
    resetToken: resetToken,  // Lộ OTP!
});
```

**Impact**: Bất kỳ ai cũng có thể đọc response API để lấy OTP, bỏ qua bước gửi email.

### FP-BUG-02: OTP hiển thị trên màn hình Web (Cao)

**File**: `frontend-web/src/pages/ForgotPassword.jsx:20`
```javascript
setMessage(`Mã OTP của bạn là: ${res.data.resetToken}`);
```

**Impact**: OTP hiển thị trực tiếp cho người dùng, ai nhìn vào màn hình cũng thấy.

### FP-BUG-03: Sai regex password - dùng `\s` thay vì special char (Cao)

**File**: `frontend-mobile/App.js:~268`
```javascript
const strongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/;
// Yêu cầu whitespace, KHÔNG phải special character
```

**Impact**: 
- Password `Pass 1234` (có space, không special char) được chấp nhận
- Password `Pass1234@` (có special char, không space) bị từ chối

### FP-BUG-04: Không validate OTP 4 số (Trung bình)

**File**: `frontend-mobile/App.js:~278`
```javascript
<TextInput
    value={resetToken}
    onChangeText={setResetToken}
    keyboardType="numeric"  // Không giới hạn độ dài
/>
```

**Impact**: Có thể nhập OTP > 4 số hoặc không phải số.

### FP-BUG-05: Không rate-limit reset-password (Cao)

**File**: `backend/server.js:107-117`
```javascript
app.post("/api/reset-password", (req, res) => {
    // Không có rate-limiting, có thể gọi không giới hạn
});
```

**Impact**: OTP 4 số (10000 giá trị) có thể brute-force.

### FP-BUG-06: Lộ thông tin email tồn tại (Trung bình)

**File**: `backend/server.js:95-97`
```javascript
db.get("SELECT * FROM users WHERE email = ?", [email], (err, user) => {
    if (!user) return res.status(404).json({ error: "User not found" });
    // Nếu tồn tại thì tạo OTP
});
```

**Impact**: Attacker có thể kiểm tra email có đăng ký hay không.

### FP-BUG-07: Login attempts tăng gấp đôi (Trung bình)

**File**: `backend/server.js:75`
```javascript
const newAttempts = user.login_attempts + 2;
```

**Impact**: Tài khoản bị khóa sau 2 lần sai thay vì 3 lần.

## 7. BVA Coverage Matrix

| Coverage item | Boundary ID | Required values | Test Case IDs | Covered |
|--------------|------------|----------------|--------------|---------|
| Password length minimum | B-FP1 | Below, On, Above | BVA-FP-01, BVA-FP-02, BVA-FP-03 | Yes |
| OTP minimum | B-FP3 | Below, On, Above | BVA-FP-04, BVA-FP-05, BVA-FP-06 | Yes |
| OTP maximum | B-FP4 | Below, On, Above | BVA-FP-07, BVA-FP-08, BVA-FP-09 | Yes |

## 8. Summary

| Technique | Số test case | Pass | Fail (bug) | Blocked |
|-----------|-------------|------|-----------|---------|
| Equivalence Partitioning (EP) | 11 | 0 | 9 | 2 |
| Boundary Value Analysis (BVA) | 9 | 0 | 4 | 5 |
| **Tổng cộng** | **20** | **0** | **13** | **7** |

**Bugs tìm được**: 9 bugs (FP-BUG-01 đến FP-BUG-09)
