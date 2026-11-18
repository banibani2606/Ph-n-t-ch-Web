# Threads × CIT Farm — AI Skills & n8n Workflow Generator

Bộ **Agent Skills** (Markdown `SKILL.md`) cho AI coding assistant thiết kế và sinh các workflow n8n của hệ thống Threads/Hanpeak. Gồm **3 workflow JSON tham khảo có thể import** và **Python generator + validator**. Đây là **scaffold**, KHÔNG phải tích hợp production đã được kết nối: các adapter endpoint, Google Sheets, Gemini, Telegram, Farm và Apify phải cấu hình/kiểm thử theo hệ thống thật.

## Từ ảnh hiện có → kiến trúc

1. **Pha 1 — Generate & review**: Schedule 07:00/11:00/19:00, Manual/Webhook → Batch config → Gemini generate draft + Google Sheets (`Chờ duyệt`) → Telegram báo duyệt.
2. **Pha 3 — Publish**: Schedule 08:00/12:00/20:00 hoặc webhook duyệt → lấy post `Đã duyệt`, reserve/lock theo tài khoản + slot → CIT Farm chạy thiết bị Android thật → nhận post URL → Google Sheets cập nhật `Đã đăng` → Telegram thông báo.
3. **Pha 4 — Analytics**: Schedule hàng ngày hoặc webhook → lấy URL của post đã đăng → Apify scrape → ghi metrics + timestamp vào Sheets → Telegram báo cáo.

> Ảnh workflow thực tế đang dùng `HTTP Request` tới `host.docker.internal`, kết nối Farm/Apify qua API trung gian. Vì **chưa có hợp đồng API chính xác**, ví dụ dưới đây dùng **adapter API** được mô tả tại `contracts/gateway-api.md`. Không giả định endpoint thật hay tự nhận có thể chạy ngay.

## Cấu trúc

```text
.agents/skills/               # bộ skill agent-neutral cho Claude Code / Cursor / AI coding tools
  threads-farm-orchestrator/  # điều phối, design → generate → validate
  workflow-architect/        # spec, node topology, triggers
  persona-content-generator/  # giọng 8 tài khoản, chống giả danh lời chứng
  google-sheets-approval/    # trạng thái, duyệt, khoá và audit
  farm-android-publisher/    # batch, thiết bị, idempotency
  apify-metrics-collector/   # scrape và upsert metrics
  telegram-approval-reports/ # duyệt / thông báo / báo lỗi
  n8n-qa-security/           # test và security gate
scripts/generate_workflows.py # tạo 3 workflow importable từ đặc tả
scripts/validate_workflows.py # kiểm tra cấu trúc + logic scaffold
examples/project-config.json # dự án mẫu, không chứa secrets
contracts/                    # interface, data model, event schema
 generated/                   # workflow JSON được sinh sẵn
```

## Dùng ngay

1. Giải nén repository rồi mở toàn bộ thư mục trong Claude Code / Cursor / công cụ AI hỗ trợ Agent Skills.
2. Yêu cầu: **“Dùng skill threads-farm-orchestrator, đọc `examples/project-config.json` rồi generate n8n workflows cho 8 tài khoản Threads: 3 bài/ngày, duyệt trước khi đăng, tracking hàng ngày. Kiểm tra JSON và liệt kê việc cần cấu hình trước activation.”**
3. Hoặc chạy ngay bằng Python 3 (không cần pip):

```bash
python3 scripts/generate_workflows.py --config examples/project-config.json --out generated
python3 scripts/validate_workflows.py generated
python3 -m unittest discover -s tests -v
```

4. Trong n8n: Workflows → Import from File → chọn từng file `generated/*.json`.
5. Điền **endpoint thật** thay cho `https://REPLACE_WITH_YOUR_GATEWAY_HOST`, cấu hình authentication qua **n8n Credentials**, chỉnh lịch theo timezone `Asia/Ho_Chi_Minh`, mapping Sheets/Farm/Apify, thử thủ công trên một tài khoản test trước.
6. **Không activate workflow** khi còn placeholder hoặc khi gate QA chưa đạt.

## Ranh giới dữ liệu

- **Đã thấy trong ảnh**: 3 flow, node Cron/Manual/Webhook/Code/HTTP/Telegram, Gemini, Google Sheets, Farm Android, Apify, duyệt thủ công, batch 5 tài khoản, 3 slot (08/12/20h là ví dụ).
- **Theo nhu cầu bạn đã nêu**: 5–10 Threads accounts, từng persona, AI tạo draft và bạn duyệt, 3 post/ngày/account, tracking mỗi ngày.
- **Chưa xác minh**: cấu trúc API Farm, quyền Threads OAuth/API, Google Sheet ID và columns thực tế, Gemini/Apify endpoint, Telegram bot/chat ID, device mapping, method đọc URL và metric của từng post. Đều là tham số hoặc adapter cần triển khai.
- Nên ưu tiên **API chính thức/được phép** khi khả dụng; tương tác qua thiết bị phải tuân thủ điều khoản nền tảng và minh bạch nội dung quảng bá.

## Điều kiện đầu ra được coi là xong

- Có 3 file workflow `.json`, parse thành công, các node link không bị đứt, schedule/webhook có đường xử lý hợp lệ.
- Có khóa idempotency (mỗi post/account/slot chỉ gửi một lần), retry có giới hạn, đường lỗi và audit trail.
- Duyệt là **hard gate**; không đăng bài chỉ vì Gemini đã soạn xong.
- Có metrics timestamp + record ID và upsert tránh nhân bản.
- Secrets chỉ nằm trong Credentials/Vault; không trong git history, code, JSON.

## Tài liệu

Đọc `docs/implementation-guide.md` để triển khai end-to-end, `contracts/gateway-api.md` để viết adapter, `docs/acceptance-tests.md` để test.
