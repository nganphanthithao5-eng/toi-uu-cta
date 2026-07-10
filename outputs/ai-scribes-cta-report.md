# Báo cáo tối ưu CTA — "AI scribes for doctors: how they work, benefits, and features"

Nguồn bài viết: [Google Doc](https://docs.google.com/document/d/e/2PACX-1vQaAIRgOO-PVDy7A_3_5krHqb1EXBp3pLJgk-pPyaiimJELwAxDe-voN0IcPK6dfHiOmjLhH7CL_76D/pub)
Đăng trên: tmasolutions.com/insights

## Giai đoạn AIDA & Persona

Bài là **A1 → I** ở phần thân (mục 1-5: định nghĩa, cơ chế, lợi ích, tính năng, toplist công cụ — DeepScribe, Abridge, Freed, Sunoh.ai, S10.AI, Ambience Healthcare), chuyển sang **D → A2** ở mục 6, nơi TMA tự giới thiệu năng lực làm custom AI scribe.

**Persona: Healthcare** — cụ thể là quản lý kỹ thuật/sản phẩm (CTO, Head of Product, IT Director) tại bệnh viện/phòng khám/healthtech company đang cân nhắc build vs. buy cho bài toán AI scribe, quan tâm tích hợp EHR/EMR và compliance (HIPAA/GDPR).

**Nhận xét về draft CTA cũ** (*"Ready to validate your AI medical scribe use case? Contact TMA Solutions"*): loại bỏ — vi phạm 3S, thiếu Strong (không urgency/giá trị cụ thể) và Specific (không rõ liên hệ thì nhận được gì).

## CTA đề xuất — 3 vị trí

| Vị trí | Hình thức hiển thị | Câu CTA | Lý do lựa chọn |
|---|---|---|---|
| **Sau mục 3 "Key benefits"** (~1/3 bài) | Banner nhẹ inline + button outline | *"Not sure which AI scribe fits your practice's workflow? → Talk to Our Team"* | Giai đoạn A1/I, CTA nhóm 1 (tư vấn nhẹ), giữ mạch đọc, không cạnh tranh với CTA chính ở mục 6 |
| **Mục 6 "Build custom AI scribes with TMA Solutions"** (CTA chính, mạnh nhất bài) | Banner/CTA-box lớn: gradient xanh TMA (#259dd9 → #1c7ba8) + button trắng nổi bật + 3 badge "HIPAA/GDPR compliant · 15+ years healthcare tech · Deep EHR/EMR integration" | *"Not sure an off-the-shelf tool fits your EHR workflow? Get a free technical fit assessment from TMA's healthcare engineering team."* (phương án B để A/B test: *"Start my custom AI scribe assessment today — free, HIPAA-compliant, and built around my clinic's workflow."*) | Section bán hàng thực sự (D→A2) → cần độ tương phản mạnh nhất bài. Badge dùng **Halo Effect**; phương án B dùng ngôi thứ nhất ("my") để tăng CTR |
| **Cuối bài, sau FAQ** | Button card căn giữa, đơn giản, tương phản rõ | *"Ready to stop charting after hours? → Book a Free Consultation"* + micro-copy *"Response within 1 business day"* | Vị trí "an toàn" nhất để chốt hành động khi thông tin còn mới; dùng **Peak-End effect**; CTA dưới nếp gấp có thể tăng chuyển đổi tới 304% (ContentVerve) |

Cả 3 CTA đều dẫn về `https://www.tmasolutions.com/contact-us` — đúng quy tắc CTA chuyển đổi cuối cùng của TMA (không dùng CTA tải tài liệu/newsletter).

## Mockup trực quan

Artifact (mô phỏng cả 3 vị trí trong bối cảnh blog tmasolutions.com/insights, có toggle sáng/tối): https://claude.ai/code/artifact/175c04ed-5332-4f59-b9ed-6cd8fb032291

## Self-check nhanh

- Đúng giai đoạn AIDA: đạt — CTA chính đặt ở mục 6 (D→A2), CTA phụ ở mục 3 giữ đúng mức độ A1/I, không ép nhảy cóc.
- 3S: cả 3 phương án đạt Simple/Specific/Strong.
- Định dạng: CTA mục 6 dùng button/box tương phản màu, không để dạng text thuần.
- Số lượng CTA: 3 CTA cho 1 bài dài, đúng chuẩn khuyến nghị (2-3 CTA cho giai đoạn I/D), không nổi bật quá nhiều CTA cùng lúc.

## Agent nào xử lý phần nào

| Phần việc | Agent xử lý | Skill dùng |
|---|---|---|
| Xác định AIDA/persona, chọn nhóm CTA, viết phương án câu CTA theo 3S, gợi ý vị trí, self-check checklist | **Agent CTA** | `cta-optimization-skill`, `cta-blog-checklist-audit` |
| Xác định hình thức hiển thị, dựng mockup HTML, giải thích lý do theo tâm lý học thuyết phục | **Agent CTA Design** | `cta-optimization-skill`, `cta-mockup-design-standards` |

Ghi chú kỹ thuật: 2 agent chạy như 2 tiến trình con tách biệt, mỗi agent tự đọc đúng file playbook (`agent-cta.md` / `agent-cta-design.md`) và tự load skill tương ứng — do `agent-cta`/`agent-cta-design` chưa được registry của phiên nhận diện làm `subagent_type` riêng (xem `.claude/agents/README.md`), việc dispatch phải đi qua `subagent_type: general-purpose` kèm chỉ định rõ file cần đọc.
