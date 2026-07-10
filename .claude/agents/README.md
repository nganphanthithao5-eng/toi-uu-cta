# Buổi 4 — Sub agents

Ghi chú + tài liệu cho sub agent được xây trong buổi này.

## Sub agent là gì

Một "sub agent" trong Claude Code là 1 agent con được định nghĩa riêng bằng file `.claude/agents/<ten>.md`, gồm:
- **Frontmatter**: `name`, `description` (mô tả để hệ thống biết khi nào nên dùng agent này), `tools` (danh sách công cụ được phép dùng), `model`
- **Body**: system prompt / quy trình làm việc riêng cho agent đó

Khi được gọi qua Agent tool (`subagent_type: "<name>"`), sub agent chạy như 1 phiên làm việc độc lập, có ngữ cảnh riêng, và mặc định **chạy nền** — cho phép làm việc khác song song trong lúc chờ kết quả.

## Agent đã xây: `agent-cta`

File: [`agent-cta.md`](./agent-cta.md)

**Nhiệm vụ**: Viết đề xuất CTA (Call-to-Action) cho các bài blog TMA Solutions (tmasolutions.com/insights).

**Skill sử dụng** (tại `.claude/skills/`):
- `cta-optimization-skill` — nguồn phương pháp luận chính: xác định giai đoạn AIDA, chọn nhóm CTA, viết nội dung theo công thức 3S, gợi ý vị trí đặt CTA
- `cta-blog-checklist-audit` — dùng làm bước self-check nhanh (phần B – Nội dung CTA, phần C – Vị trí CTA) sau khi đã viết xong CTA

**Quy trình agent chạy khi nhận 1 bài viết (link hoặc dàn ý)**:
1. Xác định giai đoạn AIDA (A1/I/D/A2) + persona mục tiêu (Outsourcing / Healthcare / Manufacturing / Fintech-Ecommerce / Custom Software-AI)
2. Chọn nhóm mục tiêu CTA phù hợp (tạo lead / củng cố thông tin / chuyển đổi) — tuân thủ quy tắc riêng của TMA: không CTA download/newsletter, CTA chuyển đổi cuối luôn là form liên hệ `tmasolutions.com/contact-us`
3. Viết 2-3 phương án CTA theo công thức 3S (Simple – Specific – Strong), kèm giải thích vì sao phù hợp AIDA/persona
4. Gợi ý vị trí đặt CTA trong bài (đầu/giữa/cuối)
5. Self-check nhanh bằng checklist audit

**Input**: link bài viết (agent tự fetch bằng WebFetch) hoặc nội dung/dàn ý dán trực tiếp.

## Agent đã xây: `agent-cta-design`

File: [`agent-cta-design.md`](./agent-cta-design.md)

**Nhiệm vụ**: Đề xuất và thiết kế **hình thức hiển thị** CTA (button, banner, popup/exit-intent, sticky bar, inline text-link) + dựng mockup trực quan — không viết nội dung câu CTA (đó là việc của `agent-cta`).

**Skill sử dụng** (tại `.claude/skills/`):
- `cta-optimization-skill` — dùng để xác định giai đoạn AIDA, persona, vị trí đặt CTA trong bài
- `cta-mockup-design-standards` — chuẩn thiết kế trực quan: màu sắc/kích thước/khoảng trống theo CRO, chống thiết kế rập khuôn ("AI slop"), kỹ thuật render mockup (iframe/srcdoc, strip code fence)

**Quy trình agent chạy khi nhận 1 câu CTA hoặc 1 bài viết cần chèn CTA**:
1. Xác định giai đoạn AIDA + persona mục tiêu
2. Đề xuất hình thức hiển thị phù hợp theo giai đoạn AIDA + vị trí đặt (đầu/giữa/cuối/thoát trang) — có bảng mapping button/banner/popup/sticky bar/inline text-link ngay trong agent
3. Dựng mockup (HTML/CSS hoặc mô tả layout): vị trí, màu sắc (bám bộ nhận diện TMA), kích thước, text
4. Giải thích lý do chọn hình thức đó dựa trên hiệu ứng tâm lý thuyết phục + mục tiêu kinh doanh

**Tools riêng**: có thêm `Write` (lưu file mockup) và `Artifact` (xem mockup trực quan dạng web) so với `agent-cta`.

## Cách gọi agent

```
Nhờ tôi: "giao bài [link hoặc dàn ý] cho Agent CTA"
```

Tôi sẽ gọi Agent tool với `subagent_type: "agent-cta"` (hoặc `"agent-cta-design"`), chạy nền để có thể làm việc khác song song trong lúc chờ.

### ⚠️ Lưu ý đã phát hiện trong buổi này

Sub agent định nghĩa ở project-level (`.claude/agents/`) chỉ được registry của Claude Code nhận diện khi **phiên làm việc mở với working directory nằm trong chính repo** (`D:\Claude code\thaongan-toi-uu-cta`), không phải thư mục cha (`D:\Claude code`).

- Nếu mở phiên từ `D:\Claude code` → gọi `subagent_type: "agent-cta"` hoặc `"agent-cta-design"` sẽ báo lỗi *"Agent type not found"* → phải chạy tay (không chạy nền được).
- Muốn chạy nền thật sự: mở terminal mới, `cd` vào `D:\Claude code\thaongan-toi-uu-cta`, khởi động Claude Code từ đó, rồi giao bài.

**Cách lách tạm thời đã dùng trong buổi này** khi cần chạy đa agent song song mà đang ở sai thư mục: gọi `subagent_type: "general-purpose"` nhưng yêu cầu agent đó **đọc file định nghĩa tương ứng** (`agent-cta.md` hoặc `agent-cta-design.md`) bằng Read tool trước, rồi thực thi đúng như agent đó — vẫn là 2 tiến trình con tách biệt xử lý đúng chuyên môn, chỉ khác là không gắn được nhãn tên tùy chỉnh.

## Đã test

1. Test riêng `agent-cta` với dàn ý "AI scribes for doctors: how they work, benefits, and features" (persona Healthcare, giai đoạn Interest) — agent chạy đúng quy trình 5 bước, đề xuất 3 CTA ở 3 vị trí khác nhau trong bài, có self-check theo checklist.
2. Test phối hợp cả 2 agent trên cùng bài viết đầy đủ (lấy nội dung từ Google Doc) — `agent-cta` viết câu chữ, `agent-cta-design` đề xuất hình thức + dựng mockup, sau đó tổng hợp thành 1 báo cáo hoàn chỉnh. Kết quả: [`outputs/ai-scribes-cta-report.md`](../../outputs/ai-scribes-cta-report.md).
