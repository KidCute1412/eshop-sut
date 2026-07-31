# 23127404 — PostgreSQL Database Testing Mini Lab

Bundle này độc lập với backend SQLite ở thư mục gốc. Node.js, PostgreSQL, Jest
và MCP server đều chạy trong Docker.

## Yêu cầu duy nhất

- Docker Desktop (Windows/macOS) hoặc Docker Engine + Compose (Linux).
- Internet ở lần chạy đầu để tải image và npm packages.
- Codex chỉ cần thiết khi thực hiện phần nhật ký MCP.

Không cần cài Node.js hoặc PostgreSQL trên máy host.

## Chạy trên Windows

1. Mở Docker Desktop và chờ Docker Engine sẵn sàng.
2. Chạy `run.bat`.
3. Xem kết quả trong `evidence/`.

## Chạy trên Linux/macOS

```sh
chmod +x run.sh clean.sh package.sh
./run.sh
```

Test suite sử dụng yêu cầu đúng làm expected result, do đó các defect có chủ
đích tạo assertion fail. Lệnh chạy chỉ báo `LAB RESULT: PASS` khi đúng bốn
defect `FN-01`, `SP-01`, `API-STATE-01`, `SQLI-01` được phát hiện và không có
failure ngoài dự kiến.

## Nhật ký MCP

Sau khi `run` hoàn tất, PostgreSQL được giữ chạy:

1. Mở/trust folder này trong Codex.
2. Tạo thread mới để `.codex/config.toml` được nạp.
3. Dùng prompt trong `MCP_PROMPT.md`.
4. Ghi phản hồi và cách kiểm chứng vào `../REPORT.md`.

MCP dùng role `mcp_reader` chỉ có quyền đọc. PostgreSQL không publish port ra
máy host.

## Reset và đóng gói

- `clean.bat` hoặc `./clean.sh`: xóa container và volume riêng của lab.
- `package.bat` hoặc `./package.sh`: tạo
  `../../23127404_MINILAB_POSTGRES.zip`, không kèm cache dependency.

Thư mục cha chứa đúng ba deliverable được yêu cầu:

```text
23127404_MINILAB_POSTGRES/
├── db-tests.test.js
├── performance.sql
├── REPORT.md
└── portable/
```

Các mật khẩu xuất hiện trong Compose/SQL chỉ là credential cố định, cô lập
trong mạng Docker của lab và không phải credential thật.
