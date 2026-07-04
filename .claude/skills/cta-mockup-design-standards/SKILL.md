---
name: cta-mockup-design-standards
description: Tiêu chuẩn thiết kế trực quan khi tạo mockup/preview CTA (banner, button, popup, form) cho bài blog — bao gồm quy tắc màu sắc, kích thước, khoảng trống theo nghiên cứu CRO, và nguyên tắc chống thiết kế rập khuôn/nhàm chán kiểu AI. Dùng skill này bất cứ khi nào người dùng yêu cầu: tạo mockup/preview trực quan của CTA, thiết kế banner/button/popup CTA, code giao diện HTML/CSS cho CTA hiển thị trong bối cảnh blog, hoặc khi cần đánh giá/cải thiện tính thẩm mỹ của 1 CTA đã có. Dùng kèm skill cta-optimization (quyết định loại/nội dung CTA) và cta-blog-checklist-audit (đánh giá tổng thể) — skill này chỉ tập trung vào phần THIẾT KẾ TRỰC QUAN.
---

# Tiêu chuẩn thiết kế Mockup CTA

Skill này quyết định **chất lượng thẩm mỹ** khi code/tạo mockup CTA — phần mà nội dung hay (từ skill `cta-optimization`) không tự động đảm bảo được. Một CTA có nội dung đúng giai đoạn AIDA nhưng thiết kế xấu/rập khuôn vẫn thất bại trong việc thu hút click.

## Khi nào dùng skill này

- Tạo mockup/preview HTML cho 1 CTA cụ thể
- Code banner, button, popup, form CTA
- Review lại 1 CTA đã có, đánh giá phần hình ảnh/bố cục
- Bất kỳ lúc nào cần quyết định màu sắc, kích thước, vị trí trực quan của CTA

---

## 1. Quy tắc kỹ thuật thiết kế (theo nghiên cứu CRO)

### Màu sắc

- **Độ tương phản cao** giữa CTA và nền xung quanh — đây là yếu tố quan trọng nhất để mắt người đọc dừng lại
- Bộ màu CTA phải bám theo **bộ nhận diện thương hiệu** (không tự sáng tạo màu ngẫu nhiên) — xác định trước thương hiệu thiên về tông nóng hay tông lạnh, áp dụng nhất quán cho box/nút/chữ
- Không dùng quá nhiều cặp màu tương phản trong 1 bài — chỉ nên có **1 màu CTA chủ đạo** xuyên suốt để tạo tính nhận diện

### Kích thước

- Nút/banner phải **đủ lớn để dễ nhấp**, đặc biệt trên mobile (tối thiểu vùng chạm ~44×44px theo chuẩn accessibility)
- Không được lấn át nội dung chính xung quanh — lớn hơn nhưng không áp đảo
- Banner dạng chữ nhật đứng **160×600** cho CTR tốt nhất; **hạn chế dùng 728×90** (CTR thấp nhất theo dữ liệu nghiên cứu)

### Bố cục & khoảng trống

- Luôn có **khoảng trống (white space)** bao quanh CTA để tách biệt khỏi nội dung khác — đừng để CTA bị "chen chúc" giữa văn bản
- Với bài dài, **không đặt quá nhiều CTA nổi bật cùng lúc** — chỉ 1 CTA chính được làm nổi bật mạnh nhất, các CTA phụ dùng định dạng nhẹ hơn (anchor text, box nhỏ)
- Dùng yếu tố định hướng thị giác khi cần (mũi tên, hình ảnh người nhìn hướng vào nút) để dẫn mắt người đọc tới CTA

---

## 2. Nguyên tắc chống thiết kế rập khuôn ("AI slop")

Đây là phần dễ bị bỏ qua nhất khi AI tự sinh mockup — kết quả thường rơi vào 1 trong 3 khuôn mẫu quen thuộc, khiến mockup "nhìn phát biết ngay là AI tạo":

1. **Nền cream/be nhạt (~#F4F1EA) + chữ serif tương phản cao + accent màu cam đất (~#D97757)** — mẫu này đặc biệt cần tránh vì trùng màu accent của chính Claude, dễ bị nhận diện ngay
2. **Nền gần đen + 1 màu accent xanh neon hoặc đỏ tươi chói** — mẫu tối giản "công nghệ" nhưng đã quá quen thuộc
3. **Layout kiểu báo in với đường kẻ hairline, bo góc = 0, cột dày đặc kiểu newspaper** — chỉ phù hợp nếu brief thực sự yêu cầu phong cách editorial

### Cách tránh rập khuôn khi tạo mockup CTA

- **Luôn bám theo bộ màu thương hiệu thật của khách hàng** (TMA Solutions hoặc brand cụ thể đang làm) thay vì mặc định 1 trong 3 kiểu trên — đây là cách tự nhiên nhất để tránh trùng lặp, vì mỗi thương hiệu có màu riêng
- Nếu chưa có bộ màu thương hiệu cụ thể, **hỏi người dùng** trước khi tự chọn màu mặc định, đừng tự ý dùng cam đất hoặc đen-neon
- Chọn **1 yếu tố "signature"** làm điểm nhấn khác biệt cho mockup (ví dụ: hình minh họa gắn với ngành nghề cụ thể của khách hàng, thay vì icon/emoji chung chung) — nhưng giữ phần còn lại đơn giản, không lạm dụng hiệu ứng
- Typography: chọn font phù hợp với tính chất thương hiệu (B2B kỹ thuật vs B2C tiêu dùng sẽ khác nhau), không mặc định dùng đúng 1 cặp font quen thuộc cho mọi mockup

---

## 3. Checklist nhanh trước khi xuất mockup

Trước khi hiển thị/xuất mockup cho người dùng xem, tự kiểm tra:

- [ ] Màu CTA có tương phản rõ với nền không?
- [ ] Màu có bám theo thương hiệu thật (hoặc đã hỏi người dùng nếu chưa rõ) không?
- [ ] Kích thước nút/banner có đủ lớn, dễ nhấp trên mobile không?
- [ ] Có khoảng trống đủ để CTA không bị chen lấn không?
- [ ] Nếu bài dài, có đang nổi bật quá nhiều CTA cùng lúc không (nên chỉ 1 CTA chính)?
- [ ] Mockup có đang rơi vào 1 trong 3 khuôn mẫu rập khuôn ở mục 2 không? Nếu có → sửa lại theo bộ màu/phong cách riêng của thương hiệu
- [ ] Bối cảnh mockup (trình duyệt giả lập, layout blog xung quanh) có phản ánh đúng giao diện thật của trang đích (VD: tmasolutions.com/insights) không?

---

## 4. Kỹ thuật render (áp dụng riêng cho tool web)

Khi tạo mockup bằng cách gọi AI sinh HTML rồi hiển thị lên web:

- Yêu cầu AI trả về **HTML thuần túy**, không kèm markdown code fence (```html), không giải thích thêm
- Hiển thị bằng `<iframe srcdoc="...">` để cô lập CSS, tránh xung đột với giao diện chính của tool
- Luôn có bước làm sạch (sanitize) chuỗi trả về trước khi render, phòng trường hợp AI lỡ kèm code fence
- Nếu render lỗi/rỗng, hiển thị thông báo thân thiện kèm nút "Thử lại", không để hiện khung trống hoặc lỗi kỹ thuật thô

---

## Dùng kèm skill khác

- **`cta-optimization`**: quyết định loại CTA và nội dung text trước khi thiết kế
- **`cta-blog-checklist-audit`**: mục D (Màu sắc & thiết kế) trong checklist đó tham chiếu chi tiết hơn tới đúng các quy tắc CRO ở mục 1 của skill này — dùng để audit sau khi đã có mockup
