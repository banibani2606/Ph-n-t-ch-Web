<div align="center">

# PHÂN TÍCH WEB — NHÓM 3

### Prompt Engineering · AI Agents · Workflow Automation · Web Design

**Kho lưu trữ bài tập, tài liệu thực hành và sản phẩm của Nhóm 3**  
*Môn học: Phân tích Web | Giảng viên: Thầy Noah*

[![GitHub](https://img.shields.io/badge/GitHub-Project_Repository-181717?logo=github)](https://github.com/banibani2606/Ph-n-t-ch-Web)
![Status](https://img.shields.io/badge/Status-Academic_Project-2563eb)
![Documentation](https://img.shields.io/badge/Documentation-Vietnamese-16a34a)

</div>

---

## 1. Giới thiệu

Repository này tổng hợp các tài liệu, thiết kế và sản phẩm thực hành của **Nhóm 3** trong quá trình học môn **Phân tích Web**.

Nội dung tập trung vào việc ứng dụng **Prompt Engineering** và các công cụ AI để hỗ trợ thiết kế giao diện web, xây dựng luồng AI Agent, tổ chức AI Skills và mô hình hóa quy trình tự động hóa bằng **n8n**. **Hanpeak** được sử dụng làm bối cảnh cho một số bài thực hành về landing page, design system và quy trình ứng dụng AI.

> **Lưu ý:** Đây là kho lưu trữ học tập gồm nhiều hạng mục tương đối độc lập, không phải một ứng dụng duy nhất có thể cài đặt hoặc chạy bằng một lệnh chung.

## 2. Mục tiêu thực hiện

- Vận dụng Prompt Engineering để mô tả yêu cầu, định hướng kết quả và lưu lại quá trình làm việc với AI.
- Khám phá cách tổ chức AI Agent, AI Skills và các workflow tự động hóa.
- Thực hành thiết kế landing page và xây dựng hệ thống thiết kế giao diện.
- Lưu trữ đầu vào, tài liệu đặc tả và sản phẩm đầu ra nhằm thuận tiện cho việc đánh giá, đối chiếu và phát triển tiếp.

## 3. Các hạng mục trong repository

| Hạng mục | Thư mục / tệp tiêu biểu | Nội dung |
|---|---|---|
| **AI Agent & Chatbot** | `Agent Pipiline (Chatbot in app)/` | Tài liệu hoặc thành phần liên quan đến pipeline AI Agent/chatbot trong ứng dụng. |
| **Automation** | `CIT-farm/` | Hạng mục thực hành thuộc nhóm automation. |
| **n8n & AI Skills** | `Skill N8n/` | Tài liệu và thành phần liên quan đến AI Skills và n8n. |
| **Threads Automation** | `threads-farm-ai-skills/` | Bộ tài nguyên AI Skills cho bài toán tự động hóa nội dung Threads. |
| **Hanpeak Landing Page** | `design_handoff_hanpeak_landing/` và các tệp `.html` | Bản thiết kế, handoff và các phiên bản trang web/preview. |
| **Design System** | `Hanpeak Design System.pdf` | Tài liệu thiết kế giao diện Hanpeak. |
| **Prompt Engineering** | `Hanpeak_Prompt_Engineering.docx`, `Prompt.docx` | Hồ sơ prompt và tài liệu phục vụ quy trình thực hành. |
| **Visual Assets** | `assets/`, các tệp PDF về icon | Tài nguyên hình ảnh và bộ icon. |

*Bảng trên mô tả các nhóm nội dung theo tên tệp/thư mục hiện có; khả năng chạy và mức độ hoàn thiện của từng phần cần xem trong chính thư mục tương ứng.*

## 4. Cấu trúc repository

```text
Ph-n-t-ch-Web/
├── Agent Pipiline (Chatbot in app)/
├── CIT-farm/
├── Skill N8n/
├── assets/
├── design_handoff_hanpeak_landing/
├── threads-farm-ai-skills/
├── Hanpeak Design System.pdf
├── Hanpeak Landing Page.html
├── Hanpeak Landing.dc.html
├── Hanpeak Mobile Preview.dc.html
├── Hanpeak Responsive Preview.dc.html
├── Hanpeak Skill Node Icons.pdf
├── Hanpeak skill icon set.pdf
├── Hanpeak-Landing-standalone.html
├── Hanpeak_Prompt_Engineering.docx
├── Prompt.docx
├── support.js
└── README.md
```

## 5. Cách xem và sử dụng tài liệu

**Bước 1 — Tải repository**

```bash
git clone https://github.com/banibani2606/Ph-n-t-ch-Web.git
cd Ph-n-t-ch-Web
```

Hoặc chọn **Code → Download ZIP** trên GitHub.

**Bước 2 — Xem sản phẩm giao diện**

Mở các tệp HTML của Hanpeak bằng trình duyệt để tham khảo giao diện và bản preview. Một số tệp có thể cần tài nguyên đi kèm; hãy giữ nguyên cấu trúc thư mục khi mở.

**Bước 3 — Xem tài liệu Prompt Engineering và Design System**

- Mở `Hanpeak_Prompt_Engineering.docx` và `Prompt.docx` để tham khảo tài liệu prompt.
- Mở `Hanpeak Design System.pdf` để xem tài liệu thiết kế.
- Xem các tệp PDF icon để tham khảo tài nguyên thị giác.

**Bước 4 — Tìm hiểu các hạng mục AI và automation**

Truy cập các thư mục `Agent Pipiline (Chatbot in app)/`, `Skill N8n/`, `CIT-farm/` và `threads-farm-ai-skills/`. Kiểm tra tài liệu và hướng dẫn riêng trong từng thư mục trước khi cài đặt hoặc thực thi workflow.

> **Bảo mật:** Không đưa API key, token bot, thông tin đăng nhập, hoặc file `.env` chứa bí mật lên repository công khai. Chỉ công khai tệp mẫu cấu hình đã loại bỏ thông tin nhạy cảm.

## 6. Phương pháp triển khai

Các bài thực hành được tổ chức theo quy trình tham khảo:

```text
Xác định yêu cầu
       ↓
Xây dựng prompt / đặc tả
       ↓
Tạo bản nháp bằng AI hoặc công cụ liên quan
       ↓
Kiểm tra và điều chỉnh
       ↓
Lưu tài liệu, mã nguồn và kết quả
```

Từng hạng mục có thể sử dụng quy trình và công cụ riêng, tùy theo mục tiêu bài tập.

## 7. Công cụ và định dạng sử dụng

| Nhóm | Công cụ / định dạng |
|---|---|
| Thiết kế web | HTML, JavaScript, tài nguyên giao diện |
| Tự động hóa | n8n và tài liệu workflow liên quan |
| AI | Prompt Engineering, AI Agent, AI Skills |
| Tài liệu | DOCX, PDF |
| Quản lý phiên bản | Git, GitHub |

Danh sách phản ánh các chủ đề và tài nguyên xuất hiện trong repository, không ngụ ý mọi thư mục đều sử dụng tất cả công nghệ trên.

## 8. Thông tin nhóm

- **Nhóm thực hiện:** Nhóm 3
- **Môn học:** Phân tích Web
- **Giảng viên:** Thầy Noah
- **Mục đích:** Lưu trữ, trình bày và nộp các sản phẩm thực hành học phần

## 9. Lưu ý sử dụng

Tài liệu được chia sẻ với mục đích học tập, tham khảo và đánh giá bài thực hành. Những nội dung liên quan đến công cụ, nền tảng và thương hiệu bên thứ ba thuộc về chủ sở hữu tương ứng. Repository hiện chưa công bố giấy phép sử dụng riêng; không mặc định rằng mọi tài nguyên đều được cấp quyền tái sử dụng.

---

<div align="center">

**Made by Nhóm 3 — Phân tích Web**  
*Learn · Build · Experiment · Improve*

</div>
