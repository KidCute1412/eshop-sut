# MCP prompt và cách ghi bằng chứng

Sau khi chạy `run.bat`, mở chính folder này trong Codex, trust project và tạo
thread mới để Codex nạp `.codex/config.toml`.

Prompt:

> Dùng MCP server `minilab_postgres` để liệt kê các bảng, khóa ngoại,
> constraints, trigger, function và stored procedure trong schema `public`.
> Với mỗi đối tượng, nêu tên, bảng liên quan và mục đích. Sau đó dùng các truy
> vấn chỉ đọc trên `pg_catalog` hoặc `information_schema` để kiểm chứng kết quả.

Chép phần tóm tắt phản hồi vào mục 5 của `../REPORT.md`. Không ghi nhận
phản hồi AI là kết luận cuối cùng nếu chưa đối chiếu với kết quả truy vấn.
