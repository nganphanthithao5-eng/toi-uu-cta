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

## Cách gọi agent

```
Nhờ tôi: "giao bài [link hoặc dàn ý] cho Agent CTA"
```

Tôi sẽ gọi Agent tool với `subagent_type: "agent-cta"`, chạy nền để có thể làm việc khác song song trong lúc chờ.

### ⚠️ Lưu ý đã phát hiện trong buổi này

Sub agent định nghĩa ở project-level (`.claude/agents/`) chỉ được registry của Claude Code nhận diện khi **phiên làm việc mở với working directory nằm trong chính repo** (`D:\Claude code\thaongan-toi-uu-cta`), không phải thư mục cha (`D:\Claude code`).

- Nếu mở phiên từ `D:\Claude code` → gọi `subagent_type: "agent-cta"` sẽ báo lỗi *"Agent type not found"* → phải chạy tay (không chạy nền được).
- Muốn chạy nền thật sự: mở terminal mới, `cd` vào `D:\Claude code\thaongan-toi-uu-cta`, khởi động Claude Code từ đó, rồi giao bài.

## Đã test

Test với dàn ý "AI scribes for doctors: how they work, benefits, and features" (persona Healthcare, giai đoạn Interest) — agent chạy đúng quy trình 5 bước, đề xuất 3 CTA ở 3 vị trí khác nhau trong bài, có self-check theo checklist. Xem lại kết quả trong lịch sử hội thoại buổi này.
