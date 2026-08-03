|Id| Screen| Category| Checklist item| Expected| Actual| Status|
|-|-|-|-|-|-|-|
|CL-01|Product List|Visual|Product Info|Mỗi Product có ảnh (alt text), tên, giá (đ, phân cách hàng nghìn)|Mỗi Product có tên, giá-VND, phân cách hàng nghìn nhưng không có ảnh|Failed|
|CL-02|Product List|State|Loading State|Trước khi cả page load đầy đủ thông tin, phải có trạng thái Loading State (đánh dấu bởi chữ hoặc vòng tròn quay loading hoặc icon tương ứng)|Màn hình trắng|Failed|
|CL-03|Product List|Element|&lt;h1> card|Trang chủ chỉ có 1 &lt;h1> card|Phát hiện được ít nhất 2 &lt;h1> card trong trang chủ|Failed|
|CL-04|Product List|Element|&lt;h1> card|Mỗi trang Product chỉ có &lt;h1> card|Mỗi trang Product chỉ có &lt;h1> card làm tiêu đề|Passed|
|CL-05|Product List|Visual|Search Bar Identification|Thanh tìm kiếm phải có đấu hiệu để visualize cho người dùng biết là thanh tìm kiếm|Thanh tìm kiếm có chữ "Tìm kiếm..." ở kế bên|Passed|
|CL-06|Product List|Visual|Search Bar Highlight|Khi đang click và sử dụng thanh tìm kiếm, thanh phải được viền đậm hoặc tô đậm và có bar chữ nhấp nháy ở chỗ đang type.|-|Passed|
|CL-07|Product List|Responsive|Bigger Viewport Table (1963.20px x 1390.40px)|Page tự cản chỉnh tương ứng|Page bị thu nhỏ đáng kể|Failed|
|CL-08|Product List|Responsive|Smaller Viewport Table (785.28px x 556.16px)|Page tự cản chỉnh tương ứng|Page bị phóng lớn đánh kể|Failed|
|CL-09|Product List|Compatibility|Kiểm tra trên 2 Browser Google Chrome và Microsoft Edge|Cả 2 Page đều load được|-|Passed|
|CL-10|Product List|Compatibility|Kiểm tra trên Browser Firefox|Cả 2 Page đều load được|-|Passed|
|CL-11|Product List|Compatibility|Kiểm tra trên Browser Safari|Cả 2 Page đều load được|-|Passed|
|CL-12|Product List|Responsive|Query Status|Kết quả tìm kiếm chỉ được update khi thay đổi query và sau khi bấm Tìm|Kết quả tìm kiếm vẫn bị thay đổi khi chỉ thay đổi query tạm thời|Failed|
|CL-13|Product List|Visual|Search Button Indicator|Khi bấm Tìm thì phải có 1 indicator (tô đậm trong 1 khoảng thời gian, highlight hoặc hiệu ứng) để cho thấy nút Tìm đã được bấm|Không có 1 indicator nào xuất hiện khi bấm|Failed|
|CL-14|Product List|Visual|Category Hover Indicator|Khi hover qua các thẻ (Giỏ hành, Đăng nhập, Đăng ký) thì phải có 1 indicator (tô đậm trong 1 khoảng thời gian, highlight hoặc hiệu ứng) để cho thấy nút Tìm đã được bấm|Các thanh được gạch dưới khi hover qua|Passed|
|CL-14|Product List|Visual|Website Name Hover Indicator|Khi hover qua tên shop (Giỏ hành, Đăng nhập, Đăng ký) thì phải có 1 indicator (tô đậm trong 1 khoảng thời gian, highlight hoặc hiệu ứng) để cho thấy nút Tìm đã được bấm|Không có 1 indicator nào xuất hiện khi hover qua|Failed|
