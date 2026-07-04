---
name: cta-blog-checklist-audit
description: Kiểm tra (audit) toàn diện 1 bài blog đã xuất bản hoặc bản nháp theo checklist 26 tiêu chí CTA, bao gồm kỹ thuật SEO, nội dung CTA, vị trí đặt, màu sắc/thiết kế, loại CTA và số lượng CTA theo từng giai đoạn AIDA. Dùng skill này khi người dùng yêu cầu: audit/rà soát 1 bài blog cụ thể xem CTA đã chuẩn chưa, kiểm tra kỹ thuật (tốc độ tải trang, CTR, tracking) liên quan đến CTA, đếm số lượng CTA có phù hợp với giai đoạn AIDA không, hoặc yêu cầu "chấm điểm toàn diện" một bài viết theo checklist chuẩn (không chỉ riêng nội dung CTA mà cả mặt kỹ thuật và thiết kế). Dùng kèm với skill cta-optimization (skill đó lo phần chọn loại CTA/viết nội dung, còn skill này lo việc audit/rà soát sau khi đã có CTA).
---

# Checklist audit CTA cho bài Blog

Skill này dùng để **rà soát/audit** một bài blog theo checklist 26 tiêu chí (dựa theo tài liệu nghiên cứu VMH), chia làm 5 nhóm: Kỹ thuật SEO, Nội dung CTA, Vị trí CTA, Màu sắc & thiết kế, Loại & số lượng CTA. Khác với skill `cta-optimization` (dùng để **tạo mới** CTA), skill này dùng để **kiểm tra CTA đã có sẵn** đạt chuẩn tới đâu.

## Khi nào dùng skill này

- Người dùng đưa 1 URL hoặc nội dung bài blog đã có CTA, muốn "audit", "rà soát", "chấm điểm toàn diện"
- Người dùng hỏi về mặt kỹ thuật: tốc độ tải trang, CTR, tracking, internal link liên quan đến CTA
- Người dùng muốn biết số lượng CTA trong bài đã hợp lý theo giai đoạn AIDA chưa
- Người dùng cần checklist dạng bảng để tự tay rà soát hàng loạt bài

## Cách audit — quy trình 5 bước

1. Rà soát **Nhóm 1: Kỹ thuật SEO** (mục A) — đây là điều kiện nền tảng, nếu sai thì CTA hay đến mấy cũng không hiệu quả
2. Rà soát **Nhóm 2: Nội dung CTA** (mục B)
3. Rà soát **Nhóm 3: Vị trí CTA** (mục C)
4. Rà soát **Nhóm 4: Màu sắc & thiết kế CTA** (mục D)
5. Rà soát **Nhóm 5: Loại & số lượng CTA** (mục E) — đối chiếu với giai đoạn AIDA của bài (dùng skill `cta-optimization` để xác định giai đoạn nếu chưa rõ)

Sau khi rà soát xong cả 5 nhóm, xuất kết quả theo định dạng ở mục **Output**.

---

## A. Kỹ thuật SEO (7 tiêu chí)

| # | Tiêu chí | Chuẩn cần đạt | Ghi chú/căn cứ |
|---|---|---|---|
| 1 | Luồng vận hành thu thập Lead | CTA phải hoạt động bình thường, ghi nhận đúng thông tin khách hàng trước khi vào bài | Kiểm tra bằng cách test thử điền form/click CTA |
| 2 | Văn bản thay thế (alt text) cho CTA dạng ảnh | Phải có alt text dự phòng khi ảnh CTA không hiển thị được trên trình duyệt người dùng | Phòng trường hợp lỗi hiển thị hình ảnh |
| 3 | Tốc độ tải trang (Page Load Speed) | Tối thiểu đạt **62.63** (điểm số theo thang đo tốc độ) | Amazon: cứ chậm thêm 100ms → doanh số giảm 1%. 64% người không mua vì web quá chậm |
| 4 | CTR | CTR trung bình tìm kiếm > **5.17%**; CTR trung bình hiển thị > **0.46%** | Khi CTR tìm kiếm ~5.31%, CTA dạng nút hoạt động tốt nhất (Leighton Interactive) |
| 5 | Internal link | Có link nội bộ trong cùng giai đoạn AIDA và sang giai đoạn tiếp theo | Giúp dẫn dắt khách hàng đi đúng hành trình phễu |
| 6 | Cài đặt đo lường | Đã cài GA4, Tag Manager, UTM cho các CTA | Bắt buộc để đo lường CR sau này (xem skill `cta-optimization` mục 6) |
| 7 | Thứ hạng từ khóa | Từ khóa chính của bài càng lên top trang 1 càng tốt | Ảnh hưởng trực tiếp đến traffic vào CTA |

## B. Nội dung CTA (6 tiêu chí)

| # | Tiêu chí | Chuẩn cần đạt | Ghi chú/căn cứ |
|---|---|---|---|
| 8 | Đề xuất giá trị rõ ràng | Người đọc biết ngay họ nhận được gì (ebook, dùng thử, bản tin...) khi vừa nhìn CTA, không phải đoán | Tránh để CTA mơ hồ kiểu "Xem thêm" không rõ nội dung |
| 9 | Tính cấp thiết về thời gian | Có từ ngữ tạo cảm giác khẩn cấp: "ngay bây giờ", "hôm nay" | Giúp CTA nổi bật giữa các yếu tố gây xao nhãng khác trên trang |
| 10 | Hướng tới hành động cụ thể | Dùng động từ hành động rõ ràng: "tải xuống", "tham gia", "đặt lịch", "xem demo" | Không dùng động từ mơ hồ |
| 11 | Nhất quán CTA và trang đích | Tiêu đề, động từ hành động, hình ảnh giữa CTA và trang đích phải khớp nhau | Tránh gây hụt hẫng/nghi ngờ khi khách click vào |
| 12 | Diễn đạt ngôi thứ nhất | Dùng "của tôi" thay vì "của bạn" trong CTA | CTR có thể tăng đến 90% (VD: "Bắt đầu dùng thử miễn phí 30 ngày **của tôi**") |
| 13 | Hạn chế câu hỏi cá nhân trong form/trang đích | Form càng ít trường thông tin cá nhân, tỷ lệ chuyển đổi càng cao | Theo nghiên cứu GMP |
| 14 | Độ dài nội dung CTA | Chọn 1 trong 5 kiểu: (a) ngắn 100-200 ký tự đánh vào lợi ích/điểm đau, (b) không tách heading, in đậm màu cam, ~1500 ký tự, (c) tách heading riêng ~1600 ký tự giới thiệu sản phẩm, (d) toàn bộ nội dung dạng ảnh không có text, (e) chỉ 1 câu text duy nhất | Chọn theo bối cảnh bài viết và ngành hàng |

## C. Vị trí CTA (3 tiêu chí)

| # | Tiêu chí | Chuẩn cần đạt | Ghi chú/căn cứ |
|---|---|---|---|
| 15 | CTA ở màn hình đầu tiên (cho bài giai đoạn D) | Dùng dạng popup hoặc CTA nhỏ gọn, không chiếm quá nhiều % màn hình | Nielsen Norman Group: khách dành 80% sự chú ý ở phần trên cùng màn hình, không cần cuộn |
| 16 | CTA ở vị trí nổi bật | Quy trình: (B1) xây vị trí theo lý thuyết → (B2) đo bằng site map/heatmap → (B3) chỉnh sửa theo hành vi thực tế | Tỷ lệ chuyển đổi tham khảo theo vị trí (Grow & Convert): Sidebar 0.5-1.5%, cuối bài 0.5-1.5%, Pop-up 1-8%, Slider/bar 1-5%, Welcome gate 10-25%, Feature box 3-9% |
| 17 | CTA sau cuộn chuột (mọi giai đoạn) | Tối ưu nhất ở 1/3 cuối trang hoặc cuối hẳn bài | CTA dưới nếp gấp (below the fold) tạo tăng chuyển đổi cao hơn tới **304%** so với trên nếp gấp (ContentVerve) |

## D. Màu sắc & thiết kế CTA (7 tiêu chí)

| # | Tiêu chí | Chuẩn cần đạt | Ghi chú/căn cứ |
|---|---|---|---|
| 18 | Độ tương phản màu cao | Tách CTA khỏi văn bản còn lại bằng in đậm/in nghiêng/box | Giúp CTA nổi bật rõ ràng so với nội dung xung quanh |
| 19 | Kích thước đủ lớn | Banner/nút lớn hơn thành phần xung quanh nhưng không lấn át; dễ nhấp trên mobile | CTA dạng nút tăng CTR 28% so với dạng liên kết (Campaign Monitor) |
| 20 | Khoảng trống xung quanh CTA | Tạo không gian trắng bao quanh để tách biệt CTA | Tăng mức độ nổi bật và tầm quan trọng trong mắt người đọc |
| 21 | Kiểu dáng nhất quán | CTA nổi bật nhưng vẫn phù hợp thẩm mỹ tổng thể thương hiệu | Sự nhất quán tạo dựng lòng tin |
| 22 | Bộ màu gắn với nhận diện thương hiệu | Xác định thương hiệu thiên về màu nóng hay màu lạnh → áp dụng cho box/nút/chữ | Đồng bộ theo brand guideline |
| 23 | Kích thước banner chuẩn | Ưu tiên **160×600** (dọc); hạn chế **728×90** | 160×600 có CTR cao nhất (~0.15%); 728×90 thấp nhất (~0.03%) |

## E. Loại & số lượng CTA (3 tiêu chí)

| # | Tiêu chí | Chuẩn cần đạt |
|---|---|---|
| 24 | Loại CTA trong bài | Mỗi bài nên có **2 loại**: CTA đúng giai đoạn AIDA của bài + CTA giai đoạn cuối (dẫn về nhóm chuyển đổi). Xem chi tiết 10 loại CTA cụ thể (kêu gọi tải xuống, đăng ký bản tin, sự kiện/hội thảo, tìm hiểu thêm, giới thiệu sản phẩm, giới thiệu thương hiệu, nhận tư vấn, chương trình ưu đãi, hướng dẫn mua hàng, dùng thử miễn phí) trong skill `cta-optimization` |
| 25 | Đa dạng hình thức CTA | Kết hợp nhiều hình thức trong cùng 1 bài: popup, box, form trần, banner — không chỉ dùng 1 kiểu duy nhất xuyên suốt |
| 26 | Số lượng CTA theo giai đoạn AIDA | **A1**: 4 CTA · **I**: 2 CTA · **D**: 2-3 CTA (dao động 2,34) · **A2**: theo số liệu thực tế của dự án (tài liệu gốc chưa có con số cụ thể — cần đối chiếu thêm dữ liệu nội bộ dự án) |

---

## Output — Định dạng báo cáo audit

Khi hoàn thành audit, xuất kết quả theo cấu trúc sau:

```
BÁO CÁO AUDIT CTA — [Tên bài/URL]
Giai đoạn AIDA: [A1/I/D/A2]

A. KỸ THUẬT SEO: X/7 đạt
   ⚠️ Chưa đạt: [liệt kê số thứ tự + tên tiêu chí chưa đạt]

B. NỘI DUNG CTA: X/6 đạt
   ⚠️ Chưa đạt: [...]

C. VỊ TRÍ CTA: X/3 đạt
   ⚠️ Chưa đạt: [...]

D. MÀU SẮC & THIẾT KẾ: X/7 đạt
   ⚠️ Chưa đạt: [...]

E. LOẠI & SỐ LƯỢNG CTA: X/3 đạt
   ⚠️ Chưa đạt: [...]

TỔNG ĐIỂM: X/26

TOP 3 ƯU TIÊN SỬA NGAY (ảnh hưởng lớn nhất đến chuyển đổi):
1. [...]
2. [...]
3. [...]
```

**Lưu ý khi audit:** Nếu người dùng chỉ cung cấp nội dung bài viết (text) mà không có URL/khả năng đo tốc độ tải trang thực tế, hãy đánh dấu các tiêu chí kỹ thuật (mục A, tiêu chí 3-6) là "Không thể kiểm tra qua nội dung văn bản — cần công cụ đo riêng (PageSpeed Insights, GA4, GSC)" thay vì đoán bừa kết quả.

## Dùng kèm skill khác

- Nếu bài audit ra kết quả "chưa đạt" ở phần Nội dung/Vị trí/Loại CTA → dùng tiếp skill **`cta-optimization`** để đề xuất phương án sửa cụ thể (loại CTA nào, viết nội dung theo công thức 3S, áp dụng hiệu ứng tâm lý nào)
- Skill này chỉ audit, không tự sinh ra CTA mới
