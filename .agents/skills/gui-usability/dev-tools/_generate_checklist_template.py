#!/usr/bin/env python3
"""One-off generator for assets/checklist-template.md from the professor's
'Web GUI checklist Template.xlsx' taxonomy (sheets 'GUI (1)'/'GUI (2)'/'GUI (3)'
were identical, confirming this is the shared base template). Not part of the
skill's runtime; kept only so the transcription can be regenerated/audited.

Writes directly to ../assets/checklist-template.md (avoids Windows console
codepage issues with the Vietnamese diacritics).

Run: python _generate_checklist_template.py
"""
from __future__ import annotations

from pathlib import Path

HEADER = [
    "No.", "Type", "Checkpoint", "IA", "Requirement / Heuristic Reference",
    "Platform", "Source", "AI-Miss Reason", "Yes", "No", "Remarks", "Evidence", "Bug ID",
]

# (No., Type, Checkpoint text, IA) -- Vietnamese text transcribed verbatim from
# the professor's xlsx (sheets GUI (1)/(2)/(3) share the same base taxonomy).
ROWS: list[tuple[str, str, str, str]] = [
    ("1", "Section", "GIAO DIỆN NGƯỜI DÙNG (GENERAL UI)", "IA-01"),
    ("1.1", "Section", "LIÊN KẾT (LINKS)", "IA-01"),
    ("1.1.1", "Item", "Kiểm tra xem liên kết có đưa bạn đến trang mà nó đã nói không?", "IA-01"),
    ("1.1.2", "Item", "Đảm bảo không có trang mồ côi (trang không có liên kết đến trang đó)", "IA-01"),
    ("1.1.3", "Item", "Đảm bảo không có trang Dead-End (trang không có chứa liên kết đến trang web khác)", "IA-01"),
    ("1.1.4", "Item", "Kiểm tra tất cả các liên kết của bạn đến các trang web khác có còn hoạt động và được mở trong cửa sổ mới không?", "IA-01"),
    ("1.1.5", "Item", "Tất cả các trang web hoặc địa chỉ email được tham chiếu có được siêu liên kết không?", "IA-01"),
    ("1.1.6", "Item", "Nếu xóa một số trang khỏi website, kiểm tra website có thiết lập trang 404 tùy chỉnh chuyển hướng khách truy cập đến trang chủ (hoặc trang tìm kiếm) khi người dùng cố truy cập trang không còn tồn tại nữa không?", "IA-01"),
    ("1.1.7", "Item", "Kiểm tra tất cả các liên kết mailto và liệu nó có đạt đúng hay không?", "IA-01"),
    ("1.2", "Section", "MÀU SẮC (COLORS)", "IA-01"),
    ("1.2.1", "Item", "Màu nền của website là màu tối ?", "IA-01"),
    ("1.2.2", "Item", "Màu nền của website có làm rối người dùng không?", "IA-01"),
    ("1.2.3", "Item", "Màu giữa các phần trong website có sự khác biệt rõ ràng và đồng nhất ?", "IA-01"),
    ("1.2.4", "Item", "Màu chữ phần nội dung bình thường đồng nhất hay không?", "IA-01"),
    ("1.2.5", "Item", "Màu chữ phần nội dung in đậm, in nghiêng, liên kết khác nhau và nổi bật so với màu của phần nội dung bình thường ?", "IA-01"),
    ("1.2.6", "Item", "Màu chữ khi visit vào liên kết có đổi màu hay không ?", "IA-01"),
    ("1.2.7", "Item", "Màu chữ khi hover vào phần nội dung liên kết có đổi màu ?", "IA-01"),
    ("1.2.8", "Item", "Màu chữ khi nhập liệu trong textbox có đồng nhất hay không ?", "IA-01"),
    ("1.2.9", "Item", "Màu nền của các nhóm button đồng nhất với nhau hay không?", "IA-01"),
    ("1.2.10", "Item", "Màu chữ phần nội dung trên button có đồng nhất hay không?", "IA-01"),
    ("1.2.11", "Item", "Màu các vùng nhập liệu disable có đồng nhất và khác với các vùng nhập liệu khác hay không?", "IA-01"),
    ("1.3", "Section", "NỘI DUNG (CONTENT)", "IA-01"),
    ("1.3.1", "Item", "Font sử dụng trong website có nhất quán theo từng thành phần (button, textbox, nội dung, tiêu đề, liên kết…) không?", "IA-01"),
    ("1.3.2", "Item", "Kích thước font chữ phần nội dung đúng theo chuẩn cơ bản không?", "IA-01"),
    ("1.3.3", "Item", "Kích thước font chữ phần button và textbox hiển thị hợp lý hay không?", "IA-01"),
    ("1.3.4", "Item", "Kích thước font tiêu đề có làm nổi bật hơn so với phần nội dung không?", "IA-01"),
    ("1.3.5", "Item", "Logo website có để góc trên trái ?", "IA-01"),
    ("1.3.6", "Item", "Tất cả nội dung chữ có được canh lề đúng không?", "IA-01"),
    ("1.3.7", "Item", "Tất cả các tiêu đề đều được canh lề đúng không?", "IA-01"),
    ("1.3.8", "Item", "Website có bố cục rõ ràng, hợp lý ?", "IA-01"),
    ("1.3.9", "Item", "Mỗi trang web có tiêu đề rõ ràng không?", "IA-01"),
    ("1.3.10", "Item", "Phần tìm kiếm được hiển thị nổi bật và rõ ràng?", "IA-01"),
    ("1.3.11", "Item", "Phần thông tin, địa chỉ công ty được cung cấp đầy đủ trong website?", "IA-01"),
    ("1.3.12", "Item", "Phần nội dung danh sách các sản phẩm hiển thị thống nhất và hợp lý hay không ?", "IA-01"),
    ("1.3.13", "Item", "Các sản phẩm cùng loại được chia theo nhóm và thể hiện hợp lý hay không?", "IA-01"),
    ("1.3.14", "Item", "Chính sách bảo mật có được xác định rõ ràng và có sẵn để người dùng truy cập không?", "IA-01"),
    ("1.3.15", "Item", "Kiểm tra xem điều gì xảy ra nếu người dùng xóa cookie trong khi ở trong trang web", "IA-01"),
    ("1.3.16", "Item", "Kiểm tra xem điều gì sẽ xảy ra nếu người dùng xóa cookie sau khi truy cập trang web", "IA-01"),
    ("1.3.17", "Item", "Tất cả nội dung thông báo lỗi có được viết đúng chính tả trên màn hình này không?", "IA-01"),
    ("1.3.18", "Item", "Tất cả nội dung trợ giúp (tooltip) có được viết đúng chính tả trên màn hình này không?", "IA-01"),
    ("1.3.19", "Item", "Nội dung trợ giúp (tooltip) cho mọi trường nhập liệu & button có được bật không?", "IA-01"),
    ("1.4", "Section", "HÌNH ẢNH (IMAGES)", "IA-01"),
    ("1.4.1", "Item", "Tất cả các hình ảnh đều được canh lề đúng không?", "IA-01"),
    ("1.4.2", "Item", "Hình ảnh có sử dụng kích thước tập tin hiệu quả nhất không?", "IA-01"),
    ("1.4.3", "Item", "Hình ảnh có được tối ưu hóa để tải xuống nhanh không?", "IA-01"),
    ("1.4.4", "Item", "Đảm bảo rằng các nút lệnh đều có kích thước và hình dạng tương tự, và cùng cỡ chữ & phông chữ.", "IA-01"),
    ("1.4.5", "Item", "Đảm bảo kích thước biểu ngữ (banner) được hiển thị chính xác giống nhau trên các cửa sổ hiện có", "IA-01"),
    ("1.4.6", "Item", "Nội dung chữ có được bao quanh đúng hình ảnh không?", "IA-01"),
    ("1.4.7", "Item", "Liệu website có phù hợp với thị giác ngay cả khi không có đồ họa? (không download được hình, hoặc hình bị mất)", "IA-01"),
    ("1.5", "Section", "FORM", "IA-02"),
    ("1.5.1", "Section", "HÌNH THỨC (FORMAT)", "IA-02"),
    ("1.5.1.1", "Item", "Đảm bảo có thông báo cho biết các trường nhập liệu bắt buộc và tuỳ chọn", "IA-02"),
    ("1.5.1.2", "Item", "Kiểm tra có hiển thị hướng dẫn nhập liệu (điều kiện ràng buộc) cho các trường nhập liệu phức tạp", "IA-02"),
    ("1.5.1.3", "Item", "Kiểm tra có hiển thị giá trị mặc định cho các trường nhập liệu khi tải / tải lại trang (Cũng phải tắt các điều khoản và điều kiện)", "IA-02"),
    ("1.5.1.4", "Item", "Kiểm tra tất cả các phần của một bảng (table) hoặc biểu mẫu (form) hiển thị đúng không? Bạn có thể xác nhận rằng các nội dung đã chọn nằm trong \"đúng chỗ không?\"", "IA-02"),
    ("1.5.1.5", "Item", "Chỉ được chọn 1 trong 1 nhóm radio button", "IA-02"),
    ("1.5.1.6", "Item", "Người dùng có thể chọn một hoặc nhiều checkbox", "IA-02"),
    ("1.5.1.7", "Item", "Nội dung trong danh sách combo box hoặc list box được sắp xếp theo thứ tự hợp lý", "IA-02"),
    ("1.5.2", "Section", "KIỂM TRA TRƯỜNG DỮ LIỆU SỐ (NUMERIC FIELDS)", "IA-02"),
    ("1.5.2.1", "Item", "Có cho phép nhập kí tự chữ hay không?", "IA-02"),
    ("1.5.2.2", "Item", "Có cho phép nhập kí tự đặc biệt hay không?", "IA-02"),
    ("1.5.2.3", "Item", "Cho phép null hay không?", "IA-02"),
    ("1.5.2.4", "Item", "Có xử lý phép chia cho 0 hay không?", "IA-02"),
    ("1.5.3", "Section", "KIỂM TRA TRƯỜNG DỮ LIỆU CHỮ SỐ (ALPHANUMERIC FIELDS)", "IA-02"),
    ("1.5.3.1", "Item", "Có phân biệt hoa, thường hay không?", "IA-02"),
    ("1.5.3.2", "Item", "Cho phép null hay không?", "IA-02"),
    ("1.5.3.3", "Item", "Có kiểm tra độ dài tối đa hay không?", "IA-02"),
    ("1.5.3.4", "Item", "Có giới hạn độ dài chuỗi nhập hay không?", "IA-02"),
    ("1.5.3.5", "Item", "Có cho phép nhập kí tự đặc biệt hay không?", "IA-02"),
    ("1.5.3.6", "Item", "Có cho phép nhập khoảng trắng ở đầu ký tự không?", "IA-02"),
    ("1.5.3.7", "Item", "Có cho phép nhập khoảng trắng ở cuối ký tự không?", "IA-02"),
    ("1.5.3.8", "Item", "Khi nhập ô email có kiểm tra format của email hay không?", "IA-02"),
    ("1.5.3.9", "Item", "Có cho nhập chữ vào số điện thoại hay không?", "IA-02"),
    ("1.5.3.10", "Item", "Khi nhập vào ô password có ẩn thông tin hay không?", "IA-02"),
    ("1.6", "Section", "KHẢ NĂNG TIẾP CẬN & GIAO DIỆN NÂNG CAO (ACCESSIBILITY / DARK MODE / RTL) -- bổ sung cho HW03, KHÔNG có trong template gốc của GV, xem references/gui-checklist-method.md", "IA-01"),
    ("1.6.1", "Item", "TODO -- generate via AI: mọi ảnh sản phẩm có thuộc tính alt mô tả không rỗng", "IA-01"),
    ("1.6.2", "Item", "TODO -- generate via AI: mọi control tương tác có focus-visible outline rõ ràng khi điều hướng bằng bàn phím", "IA-01"),
    ("1.6.3", "Item", "TODO -- generate via AI: giao diện có hỗ trợ dark mode / prefers-color-scheme không", "IA-01"),
    ("1.6.4", "Item", "TODO -- generate via AI: layout có dùng logical properties (không hard-code margin-left/right) để sẵn sàng cho RTL không", "IA-01"),
    ("2", "Section", "USABILITY", "Mixed"),
    ("2.1", "Section", "TÍNH ĐIỀU HƯỚNG (NAVIGATION)", "IA-03"),
    ("2.1.1", "Item", "Có một liên kết đến trang chủ trên mỗi trang không?", "IA-03"),
    ("2.1.2", "Item", "Người dùng có biết được mình đang ở đâu trong website không?", "IA-03"),
    ("2.1.3", "Item", "Tất cả các trang web/cửa sổ đều có thể truy cập từ menu?", "IA-03"),
    ("2.1.4", "Item", "Chức năng tìm kiếm có được đặt ở đúng vị trí không?", "IA-03"),
    ("2.1.5", "Item", "Thanh cuộn có xuất hiện nếu được yêu cầu không?", "IA-03"),
    ("2.1.6", "Item", "Kiểm tra tất cả các field read-only đều không có thứ tự tab hay không?", "IA-03"),
    ("2.1.7", "Item", "Kiểm tra tất cả các field disable đều không có thứ tự tab hay không?", "IA-03"),
    ("2.1.8", "Item", "Thứ tự Tab được chỉ định trên màn hình có theo thứ tự từ trên cùng bên trái đến dưới cùng bên phải không? Đây là mặc định trừ khi được chỉ định khác.", "IA-03"),
    ("2.1.9", "Item", "Khi mở biểu mẫu (form), trường nhập liệu đầu tiên có được focus không?", "IA-03"),
    ("2.1.10", "Item", "Khi thông báo lỗi xảy ra, có focus vào trường nhập liệu bị lỗi đầu tiên không?", "IA-03"),
    ("2.2", "Section", "TÍNH TIỆN DỤNG (USABILITY)", "IA-01"),
    ("2.2.1", "Item", "Trang web có truyền đạt ý nghĩa rõ ràng về đối tượng dự định của nó không?", "IA-01"),
    ("2.2.2", "Item", "Trang web có một \"giao diện\" rõ ràng, dễ nhận biết không?", "IA-01"),
    ("2.2.3", "Item", "Những người dùng thông thường có thể chạy hệ thống mà không cảm thấy thất vọng hay không?", "IA-01"),
    ("2.2.4", "Item", "Tất cả các thuật ngữ có dễ hiểu đối với mỗi dự định sử dụng của trang hay không?", "IA-01"),
    ("2.2.5", "Item", "Hệ thống có cung cấp hoặc hỗ trợ cho khách hàng hay không?", "IA-01"),
    ("2.2.6", "Item", "Phông chữ quá lớn hay quá nhỏ để đọc?", "IA-01"),
    ("2.2.7", "Item", "Tên trong command button và option box có viết tắt hay không?", "IA-01"),
    ("2.2.8", "Item", "Các thành phần cùng loại có được nhóm lại hay không?", "IA-01"),
    ("2.2.9", "Item", "Tất cả các danh sách có được sort hay không?", "IA-01"),
    ("2.2.10", "Item", "Có hỗ trợ gợi ý tìm kiếm hay không?", "IA-01"),
    ("2.2.11", "Item", "Có hỗ trợ tab hay không?", "IA-01"),
    ("2.2.12", "Item", "Có thông báo tiến độ khi xử lý các tác vụ lâu (tải hình, upload hình, tải trang…) không?", "IA-04"),
    ("2.3", "Section", "PHẢN HỒI / TRẠNG THÁI (FEEDBACK / STATE) -- bổ sung cho HW03, template gốc chỉ có 2.2.12, xem references/gui-checklist-method.md", "IA-04"),
    ("2.3.1", "Item", "TODO -- generate via AI: sau khi bấm \"Thêm vào giỏ\" có phản hồi trực quan (toast/badge) không", "IA-04"),
    ("2.3.2", "Item", "TODO -- generate via AI: xóa item khỏi giỏ có dialog xác nhận trước khi thực hiện không", "IA-04"),
    ("2.3.3", "Item", "TODO -- generate via AI: trang trống (empty state) có hình minh họa + thông báo thân thiện không", "IA-04"),
    ("2.3.4", "Item", "TODO -- generate via AI: có hiển thị trạng thái loading khi đang tải dữ liệu không", "IA-04"),
    ("2.3.5", "Item", "TODO -- generate via AI: thông báo lỗi (vd mã giảm giá không hợp lệ) có rõ ràng, đúng chỗ không", "IA-04"),
    ("3", "Section", "TÍNH TƯƠNG THÍCH (COMPATIBILITY) -- các dòng này được thực thi lại ở Task 3 cho từng platform", "Task-3"),
    ("3.1", "Section", "TƯƠNG THÍCH TRÌNH DUYỆT (BROWSER COMPATIBILITY)", "Task-3"),
    ("3.1.1", "Item", "Phiên bản HTML được sử dụng có tương thích với các phiên bản trình duyệt thích hợp không?", "Task-3"),
    ("3.1.2", "Item", "Hình ảnh có hiển thị chính xác với các trình duyệt đang được kiểm tra không?", "Task-3"),
    ("3.1.3", "Item", "Xác minh phông chữ có thể sử dụng được trên bất kỳ trình duyệt nào", "Task-3"),
    ("3.1.4", "Item", "Mã JavaScript có thể sử dụng được bởi các trình duyệt đang được thử nghiệm không?", "Task-3"),
    ("3.1.5", "Item", "Bạn đã thử nghiệm hình GIF động trên các trình duyệt chưa?", "Task-3"),
    ("3.1.6", "Item", "Vị trí, kích thước của các thành phần trong trang web có hiển thị đúng với các trình duyệt đang được kiểm tra không?", "Task-3"),
    ("3.2", "Section", "TƯƠNG THÍCH THIẾT BỊ (DEVICE COMPATIBILITY)", "Task-3"),
    ("3.2.1", "Item", "Độ phân giải màn hình (kiểm tra văn bản và liên kết đồ họa vẫn hoạt động, phông chữ có thể đọc được, v.v.) như 1024x768, 800x600, 640x480 pixel", "Task-3"),
    ("3.2.2", "Item", "Độ sâu màu (256, 16-bit, 32-bit)", "Task-3"),
    ("3.3", "Section", "TƯƠNG THÍCH MÁY IN (PRINTER COMPATIBILITY)", "Task-3"),
    ("3.3.1", "Item", "Căn chỉnh văn bản và hình ảnh", "Task-3"),
    ("3.3.2", "Item", "Màu sắc của văn bản, hình ảnh và nền", "Task-3"),
    ("3.3.3", "Item", "Khả năng mở rộng phù hợp với khổ giấy", "Task-3"),
    ("3.3.4", "Item", "Bảng và đường viền", "Task-3"),
    ("3.3.5", "Item", "Các trang có in rõ ràng không cắt bỏ nội dung không?", "Task-3"),
]


def render_row(no: str, type_: str, checkpoint: str, ia: str) -> str:
    if type_ == "Section":
        cells = [no, type_, checkpoint, ia, "N/A", "N/A", "Template-Provided", "N/A", "", "", "", "", ""]
    else:
        cells = [no, type_, checkpoint, ia, "TODO", "Baseline", "Template-Provided", "N/A", "", "", "", "", ""]
    return "| " + " | ".join(cells) + " |"


def build() -> str:
    lines: list[str] = []
    lines.append("# GUI Checklist - {{GUI_ID}} {{GUI_NAME}}")
    lines.append("")
    lines.append("- GUI ID: {{GUI_ID}}")
    lines.append("- GUI Name: {{GUI_NAME}}")
    lines.append("- GUI Detail: {{GUI_DETAIL}}")
    lines.append("- Platform: {{PLATFORM}}")
    lines.append("")
    lines.append(
        "Base taxonomy transcribed from the professor's `Web GUI checklist Template.xlsx` "
        "(`Source: Template-Provided`). Section 1 = General UI (IA-01), Section 1.5 = Forms "
        "(IA-02), Section 2.1 = Navigation (IA-03), Section 2.2 = general usability (IA-01, "
        "except 2.2.12 which is Feedback/State -> IA-04), Section 3 = Compatibility (re-executed "
        "per platform in Task 3, not one of the four IA categories). Sections 1.6 and 2.3 are "
        "placeholders this skill adds because the professor's template does not cover "
        "accessibility/dark-mode/RTL or IA-04 Feedback/State beyond item 2.2.12 -- see "
        "`references/gui-checklist-method.md`. Replace every `TODO -- generate via AI` "
        "Checkpoint with a real AI-generated item, then critique and extend per `SKILL.md` "
        "Phase 2 before execution."
    )
    lines.append("")
    lines.append("See `references/checklist-item-schema.md` for column definitions.")
    lines.append("")
    lines.append("| " + " | ".join(HEADER) + " |")
    lines.append("| " + " | ".join("---" for _ in HEADER) + " |")
    for no, type_, checkpoint, ia in ROWS:
        lines.append(render_row(no, type_, checkpoint, ia))
    lines.append("")
    lines.append("## Coverage Summary")
    lines.append("")
    lines.append("| IA | Item Count | Template-Provided | AI-Generated | Human-Added |")
    lines.append("| --- | --- | --- | --- | --- |")
    lines.append("| IA-01 | TODO | TODO | TODO | TODO |")
    lines.append("| IA-02 | TODO | TODO | TODO | TODO |")
    lines.append("| IA-03 | TODO | TODO | TODO | TODO |")
    lines.append("| IA-04 | TODO | TODO | TODO | TODO |")
    lines.append("| Task-3 (Compatibility) | TODO | TODO | TODO | TODO |")
    lines.append("| Total | TODO | TODO | TODO | TODO |")
    lines.append("")
    lines.append("## Human Review")
    lines.append("")
    lines.append("- Reviewer: TODO")
    lines.append("- Review Date and Time: TODO")
    lines.append("- Review Scope: GUI Checklist Design for {{GUI_ID}} {{GUI_NAME}}")
    lines.append("- Corrections Made: TODO")
    lines.append("- Missing Items Added: TODO")
    lines.append("- Duplicate/Unjustified Items Removed: TODO")
    lines.append("- Status: Pending")
    lines.append("- Approved for Test Execution: No")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    output = Path(__file__).resolve().parents[1] / "assets" / "checklist-template.md"
    output.write_text(build(), encoding="utf-8")
    print(f"Wrote {len(ROWS)} rows to {output}")


if __name__ == "__main__":
    main()
