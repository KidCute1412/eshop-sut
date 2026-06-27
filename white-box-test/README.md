# White-Box Domain Testing - EShop SUT

## Tổng quan

Tài liệu này thực hiện **Domain Testing** kết hợp với **White-Box (Code Inspection)** cho hai tính năng được đánh dấu "Yes" trong `requirements-to-test.md`:

| STT | Feature ID | Mô tả | Môi trường | Base URL |
|-----|-----------|-------|-----------|----------|
| 1 | Web: FR-13 | Dashboard (Admin) | Web Admin | http://localhost:5174 |
| 2 | Mobile: FR-03 | Forgot Password & Reset (two steps) | Mobile Web/Expo | http://localhost:5173 (Web) / Mobile App |

## Phương pháp

- **Domain Testing**: Equivalence Partitioning (EP) + Boundary Value Analysis (BVA) theo quy trình môn Kiểm thử Phần mềm (Transcript Domain Testing & EP).
- **White-Box Inspection**: Kết hợp đọc mã nguồn (backend `server.js`, frontend `App.jsx`, mobile `App.js`) để xác định các miền giá trị, điều kiện biên và phát hiện lỗi.

## Danh sách tài liệu

| File | Mô tả |
|------|-------|
| `FR-13-dashboard-test-plan.md` | Test plan cho Admin Dashboard - Domain analysis, EP, BVA, test cases, bugs |
| `FR-03-mobile-forgot-password-test-plan.md` | Test plan cho Mobile Forgot Password - Domain analysis, EP, BVA, test cases, bugs |

## Bug count tìm được qua White-Box + Domain Testing

- **Web: FR-13 Dashboard (Admin)**: 6 bugs
- **Mobile: FR-03 Forgot Password**: 7 bugs
- **Tổng cộng**: 13 bugs

## Cách chạy test

1. Khởi động backend: `cd backend && node server.js`
2. Khởi động frontend-admin: `cd frontend-admin && npm run dev`
3. Khởi động frontend-mobile: `cd frontend-mobile && npx expo start`
4. Thực hiện các test case theo hướng dẫn trong từng file test plan
