# Handoff: HanPeak Landing Page

> **Read `BUILD_BRIEF.md` first.** It covers the stack choice, the known defects in this prototype (responsive, a11y, SEO, wiring), what is placeholder content, and the definition of done. This file is the visual specification it refers to.

## Overview
Marketing landing page for **HanPeak**, a Vietnamese-language platform for learning and practising for the **HSK 3.0** Chinese proficiency exam. The page runs top-to-bottom through: hero → problem framing → 4-step solution → feature showcase (tabbed) → audience segments → testimonials (auto-scrolling) → free-assessment CTA → footer with policies and contact.

All copy is in Vietnamese. The single conversion goal is **"Làm bài đánh giá năng lực miễn phí"** (take the free placement assessment).

## About the Design Files
The files in this bundle are **design references authored in HTML** — a working prototype that demonstrates the intended look, motion, and interaction. They are **not production code to copy verbatim**.

The task is to **recreate these designs inside the target codebase's existing environment** (React, Next.js, Vue, etc.) using its established component patterns, styling solution, and routing. If no frontend environment exists yet, pick the framework that best fits the project and implement the design there.

Two things in the prototype are framework-specific scaffolding and should be re-expressed idiomatically, not ported:
- The `.dc.html` file uses a small template runtime (`<x-dc>` / `{{ hole }}` / a `Component extends DCLogic` class). Treat the template as **markup structure** and the logic class as **a plain description of state and effects**.
- All styling is written as **inline `style` attributes**. This was a constraint of the prototyping tool. Move it into the codebase's normal styling layer (CSS modules, Tailwind, styled-components, etc.) — the exact values are listed under **Design Tokens** below.

## Fidelity
**High-fidelity.** Colors, typography, spacing, radii, shadows, motion timings, and copy are final and should be reproduced faithfully. Layout is desktop-first at ~1180–1300px content width; the prototype has **no mobile breakpoints** — responsive behaviour must be designed during implementation (guidance in *Responsive behaviour* below).

---

## Screens / Views

This is a single scrolling page. Sections below are in DOM order. Every section except the header is full-bleed with an inner max-width container.

### 0. Header (sticky)
- **Purpose**: persistent brand + section nav + primary CTA.
- **Layout**: `position: sticky; top: 0; z-index: 100`. Flex row, `justify-content: space-between`, `flex-wrap: wrap`, `row-gap: 10px`, `column-gap: clamp(16px, 2.4vw, 40px)`, padding `14px clamp(20px, 3vw, 44px)`.
- **Background**: `rgba(248,250,252,.85)` + `backdrop-filter: blur(14px)`; bottom border `1px solid #e2e8f0`.
- **Components**:
  - **Brand** (`flex: none`): logo image 44px tall, `object-fit: contain`; wordmark "HanPeak" 18px/800, `letter-spacing: -.02em`, `#0f172a`, `white-space: nowrap`.
  - **Nav** (`flex: 1 1 auto`, wraps, `gap: 10px clamp(18px, 2.4vw, 40px)`, centered): 5 anchor links, 15px/500, `#475569`, `padding: 6px 0`, `white-space: nowrap`, `flex: none`. Hover → `#059669`.
    | Label | Target |
    |---|---|
    | Vấn đề | `#van-de` |
    | Giải pháp | `#giai-phap` |
    | Tính năng nổi bật | `#tinh-nang` |
    | Ai dùng HanPeak | `#doi-tuong` |
    | Đánh giá | `#danh-gia` |
  - **CTA button** (`flex: none`): "Bắt đầu ngay", 14px/600, white on `#10b981`, padding `11px 22px`, `border-radius: 9999px`, shadow `0 6px 16px -6px rgba(16,185,129,.7)`. Hover → background `#059669`, `translateY(-1px)`.
- **Note**: every target section carries `scroll-margin-top: 82px` so headings clear the sticky header.

### 1. Hero
- **Purpose**: state the value proposition and drive to the primary CTA.
- **Layout**: `position: relative; overflow: hidden`, padding `84px 48px 148px`, background `#f8fafc`, `text-align: center`. Inner container `max-width: 1300px; margin: 0 auto`, flex column, `align-items: center`, `gap: 30px`.
- **Decorative layers** (all absolutely positioned, behind content):
  1. Dot grid: `radial-gradient(#a7f3d0 1px, transparent 1px)`, `background-size: 26px 26px`, `opacity: .5`.
  2. Top glow: 900×520px at `top: -140px; left: 50%` translated `-50%`, `radial-gradient(ellipse at center, rgba(16,185,129,.20), rgba(248,250,252,0) 65%)`.
  3. **Pixel-wave canvas** — see *Interactions & Behavior*.
  4. Hanzi 汉 — 340px, `Ma Shan Zheng`, `#10b981`, `opacity: .05`, at `left: -40px; bottom: -90px`.
  5. Hanzi 峰 — 260px, same treatment, at `right: -20px; top: -40px`.
- **Components**:
  - **H1**: "Nền tảng luyện thi HSK 3.0 tích hợp AI - Trúng lỗ hổng, chuẩn lộ trình" — 68px/1.1, weight 800, `letter-spacing: -.035em`, `#0f172a`, `text-wrap: balance`, `width: 100%; max-width: 1260px`.
  - **Subheadline (p)**: "Cá nhân hóa bài tập bằng thuật toán RASCH. Giúp bạn tăng band điểm thần tốc mà không bị học dàn trải" — 26px/1.5, weight 400, `#059669`, `letter-spacing: -0.01em`, `text-wrap: balance`, same 1260px cap.
  - **CTA button**: "Bắt đầu ngay" — `margin-top: 26px`, 19px/700, white on `#10b981`, padding `20px 52px`, pill, shadow `0 18px 40px -14px rgba(16,185,129,.9)`, `transition: all .2s ease`. Hover → `#059669`, `translateY(-2px)`, shadow `0 24px 48px -14px rgba(16,185,129,1)`.
  - **Ascent graphic (inline SVG, `viewBox="0 0 1100 360"`, `max-width: 1100px`)** — the page's signature illustration: a stepped ridge whose steps are the six HSK bands, with a jade curve (the learner's ability) drawn upward across it to a glowing summit marked 峰.
    - Enters with `hp-rise` (`.9s cubic-bezier(.2,.7,.3,1)`, fade + 22px translate).
    - Gradients: `#hpRidge` vertical `#10b981` .26 → 0 alpha; `#hpLine` horizontal `#6ee7b7` → `#10b981` (55%) → `#047857`.
    - Grid: 6 dashed verticals `#cbd5e1`, `stroke-dasharray: 3 7`, plus a `#94a3b8` baseline.
    - Ability curve: 5px stroke, round caps, `stroke-dasharray: 1600`, animated by `hp-draw` (`2.2s cubic-bezier(.4,0,.2,1) .25s both`, dashoffset 1600 → 0).
    - Milestone dots at (360,234) and (660,158): white fill, `#10b981` 3px stroke, r=6.
    - Summit: `#047857` dot r=8 pulsing via `hp-glow` (2.6s, r 7↔10) + `#10b981` halo r=26 expanding via `hp-halo` (2.6s, scale .7→1.9, opacity .55→0), both delayed 1.6s and looping.
    - Axis labels HSK 1…HSK 6 at 15px/600 `#94a3b8`; 峰 at 40px `Ma Shan Zheng` `#047857` above the summit.
    - Caption row below: 26×4px `#10b981` bar + "Đường năng lực của bạn — dựng từ bài đánh giá RASCH, cập nhật theo từng buổi học" (14.5px `#64748b`).

### 2. Vấn đề — `#van-de`
- **Purpose**: name the three reasons study effort fails today.
- **Layout**: padding `76px 48px 120px`, background `#f1f5f9`, top border `1px solid #e2e8f0`. Dot-grid overlay `radial-gradient(#cbd5e1 1px, transparent 1px)` at 30px, `opacity: .55`. Inner `max-width: 1180px`, flex column, `gap: 44px`.
- **H2**: "Tại sao nhiều người học mà vẫn không hiệu quả" — 48px/1.18, 800, `-.03em`, `#0f172a`, `width: 760px`.
- **Cards**: 3-column grid, `gap: 24px`. Each card: flex column, `gap: 18px`, padding `34px 30px 38px`, `border: 1px solid #e2e8f0`, `border-radius: 20px`, background `#ffffff`, shadow `0 12px 30px -26px rgba(15,23,42,.7)`, `min-height: 300px`. Hover → border `#10b981`, `translateY(-3px)`.
  - Index: 13px/700, `letter-spacing: .16em`, `#ef4444` (`01`, `02`, `03`).
  - Title: 23px/700, line-height 1.3, `#0f172a`, **`min-height: 90px`** — this fixed block is what keeps the body copy of all three cards starting on the same baseline. Preserve it (or use a grid/subgrid equivalent).
  - Body: 16px/1.65, `#64748b`.
  | # | Title | Body |
  |---|---|---|
  | 01 | Sai môi trường luyện tập | Luyện mobile, thi máy — bỡ ngỡ khi vào phòng thi thật. |
  | 02 | Luyện đề mù quáng | Làm nhiều đề nhưng không biết lỗ hổng ở đâu. |
  | 03 | Khủng hoảng chuyển đổi HSK 3.0 | Tài liệu cũ trên thị trường sắp lỗi thời. |

### 3. Giải pháp — `#giai-phap`
- **Purpose**: the 4-step method, presented as a connected timeline.
- **Layout**: padding `130px 48px`, background `#ffffff`. Inner `max-width: 1180px`, flex column, `gap: 64px`.
- **H2**: "Tại sao HanPeak có thể giúp bạn" — 48px/1.18, 800, `-.03em`, `#0f172a`, `max-width: 820px`.
- **Steps**: 4-column grid, `gap: 26px`, `position: relative`. A connector line sits behind the numbers: absolutely positioned `top: 34px; left: 6%; right: 6%; height: 2px`, `linear-gradient(90deg,#d1fae5,#10b981,#d1fae5)`.
- Each step: flex column, `gap: 18px`.
  - Number badge: 68×68px circle, `border: 2px solid #10b981`, 24px/800. Steps 1–3 → background `#ecfdf5`, text `#047857`. Step 4 (current/active) → background `#10b981`, text `#ffffff`.
  - Eyebrow: 13px/700, `letter-spacing: .14em` — "BƯỚC 1…4". `#10b981` for 1–3, `#047857` for 4.
  - Title: 22px/700, line-height 1.35, `#0f172a`, `min-height: 60px` (baseline alignment).
  - Body: 16.5px/1.7, `#475569`.
  | Step | Title | Body |
  |---|---|---|
  | 1 | Test đầu vào thông minh | Thuật toán **RASCH** (700 weight, `#047857`) riêng biệt giúp đo lường chính xác năng lực thực tế. |
  | 2 | Quét sạch "lỗ hổng" kiến thức | Hệ thống phân tích và chỉ mặt đặt tên từng điểm yếu của bạn một cách chi tiết nhất. |
  | 3 | Lộ trình cá nhân hóa | Học đúng trọng tâm bạn cần, bỏ qua kiến thức dư thừa. |
  | 4 | Luyện tập thực chiến với AI | Môi trường thi mô phỏng 100% CBT, AI chấm chữa ngay lập tức. |

### 4. Tính năng nổi bật — `#tinh-nang`
- **Purpose**: showcase four product capabilities in a tabbed panel.
- **Layout**: padding `120px 40px`, background `#f8fafc`, top border `1px solid #e2e8f0`. Inner `max-width: 1240px`, flex column, `align-items: center`, `gap: 44px`.
- **H2**: "Các tính năng hỗ trợ học tập mạnh mẽ đang chờ bạn khám phá" — 46px/1.18, 800, `-.03em`, centered, `max-width: 900px`.
- **Tab bar**: flex row, wraps, centered, `gap: 6px`, padding 6px, background `#ffffff`, `border: 1px solid #e2e8f0`, `border-radius: 26px`, shadow `0 4px 14px -8px rgba(15,23,42,.25)`, `max-width: 100%`.
  - Tab button: 15px/600, padding `12px 26px`, pill, `white-space: nowrap`, `transition: all .2s ease`. Active → background `#10b981`, text `#ffffff`. Inactive → transparent, `#475569`.
  - **Visual order**: `Kho đề thi` · `Review & test` · `Kho từ vựng` · `AI chấm Viết & Nói`. **Default open tab = Kho đề thi.**
- **Panel shell**: flex row with a 52px round prev/next button either side (`gap: 22px`; `border: 1px solid #cbd5e1`, white, `#0f172a` chevron, shadow `0 4px 12px -6px rgba(15,23,42,.3)`; hover → border `#10b981`, text `#059669`). The card between them: `flex: 1; min-width: 0`, `border-radius: 28px`, background `#ffffff`, `border: 1px solid #e2e8f0`, shadow `0 24px 60px -34px rgba(15,23,42,.45)`, `overflow: hidden`, `position: relative`. Only the active panel is rendered/`display: flex`; the rest are `display: none`.
  - Panel body: padding `52px 56px 56px`, flex column, `align-items: center`, `gap: 34px`. Intro block centered, `max-width: 760–800px`, `gap: 14px`: title 30px/800 `-.02em` `#0f172a`, description 17px/1.7 `#475569`.
  - Arrows step through the **visual order**, not the internal indices.

**Panel A — Kho đề thi chuẩn hóa HSK 3.0** (default)
> Hàng trăm đề luyện đa dạng cấp độ, liên tục cập nhật theo format mới nhất. Mô phỏng trải nghiệm thi máy (CBT) giúp bạn làm quen thao tác, tối ưu thời gian làm bài.

Two-column grid `1fr 1.2fr`, `gap: 20px`, `max-width: 940px`.
- Left tile (`#f8fafc`, `1px solid #e2e8f0`, radius 18px, padding 26px): eyebrow "KHO ĐỀ THEO CẤP ĐỘ" (12px/700, `.14em`, `#94a3b8`); three rows (radius 12px, padding `14px 16px`) — `HSK 1 – 2 / 64 đề` and `HSK 5 – 6 / 96 đề` on white with `#e2e8f0` border, `HSK 3 – 4 / 128 đề` highlighted `#ecfdf5` on `#a7f3d0`; footer note with an 8px `#10b981` dot: "Cập nhật format mới nhất · tháng này +12 đề" above a dashed top border.
- Right tile — **CBT exam simulator mock**: dark header bar (`#0f172a`, padding `14px 20px`) with "MÔ PHỎNG THI MÁY · CBT" (13px/700, `.1em`, `#94a3b8`) and timer "00:18:42" (14px/700, `#34d399`). Body padding 24px: meta row "阅读 · 第 14 题" / "14 / 40"; the passage 19px, line-height 1.9, with 锻炼身体 marked `background: #ecfdf5; border-bottom: 2px solid #10b981`; three answer rows (26px letter badge + label) — A and C neutral (`#f8fafc`, `#e2e8f0`), B selected (`#ecfdf5`, `1px solid #10b981`, badge filled `#10b981`, label 600 `#065f46`); progress bar at 35% (`#10b981` on `#f1f5f9`) with a "35%" label.

**Panel B — Review & test**
> Mỗi bài kiểm tra trên HanPeak không chỉ chấm điểm mà cho bạn thấy chính xác kỹ năng nào đã vững, kỹ năng nào còn hổng, tới từng điểm kiến thức nhỏ nhất.

Grid `1fr 1.15fr`, `gap: 20px`. Left: "TỔNG QUAN KỸ NĂNG" with four labelled 10px bars on `#e2e8f0` — Nghe 88% `#059669` "Vững", Đọc 79% `#10b981` "Vững", Viết 46% `#f59e0b` "Cần ôn" (`#b45309`), Nói 31% `#ef4444` "Lỗ hổng" (`#b91c1c`). Right: "CHI TIẾT TỚI TỪNG ĐIỂM KIẾN THỨC" — four rows, radius 12px, padding `14px 16px`: 来/去 9/10 and 量词 8/8 in jade (`#ecfdf5`/`#a7f3d0`/`#065f46`), 把 4/9 in amber (`#fffbeb`/`#fde68a`/`#92400e`), 被 2/9 in red (`#fef2f2`/`#fecaca`/`#991b1b`); closing note 14px `#64748b`: "Lộ trình tuần tới đã tự động ưu tiên 2 điểm kiến thức còn hổng."

**Panel C — Kho từ vựng**
> Tra cứu nhanh, học đúng trọng tâm theo từng band HSK — không lan man, không học lẫn lộn trình độ. Từ vựng được sắp xếp để bạn tra đâu nhớ đó, ôn tới đâu chắc tới đó.

Band chips (HSK 1–6, 13px/700, pill, padding `8px 18px`): HSK 1–2 `#ecfdf5`/`#a7f3d0`/`#047857`, **HSK 3 active** `#10b981`/white, HSK 4–6 white/`#e2e8f0`/`#64748b`. Below, a 3-column grid of 6 word cards (radius 16px, padding 20px, white on `#e2e8f0`; hover → border `#10b981`, `translateY(-2px)`): hanzi 30px/700 `#0f172a`, pinyin 14px/600 `#10b981`, gloss 14.5px `#475569` — 经验/jīng yàn/kinh nghiệm, 解决/jiě jué/giải quyết, 环境/huán jìng/môi trường, 影响/yǐng xiǎng/ảnh hưởng, 习惯/xí guàn/thói quen, 安排/ān pái/sắp xếp. Footer strip (`#f8fafc`, radius 16px): "Đã thuộc **612** / 973 từ band HSK 3" + a 280×8px bar at 63%.

**Panel D — AI chấm Viết & Nói**
> Không cần chờ giáo viên, không cần tự đoán mình sai ở đâu. AI chấm bài Viết/Nói theo chuẩn HSK, chỉ ra lỗi cụ thể và gợi ý nâng cấp câu chữ, từ vựng — giúp bạn cải thiện sau từng lần luyện, không phải sau từng học kỳ.

Carries a **"COMING SOON" badge** pinned to the card's top-right: `position: absolute; top: 24px; right: 26px; z-index: 2`; 12px/700, `.1em`, padding `6px 14px`, pill, `#fffbeb` on `1px solid #fde68a`, text `#b45309`, preceded by a 7px `#f59e0b` dot.
Grid `1.25fr 1fr`, `gap: 20px`. Left: "BÀI VIẾT CỦA BẠN" — a 19px/2 sentence with 昨天 flagged red (`#fee2e2`, `2px solid #ef4444`) and 那儿的 flagged amber (`#fef3c7`, `2px solid #f59e0b`); two pill tags ("Lỗi thì · 1", "Gợi ý nâng cấp · 1"); an AI note block (`#ecfdf5`, `1px solid #a7f3d0`, radius 14px) with a 28px `#10b981` "AI" avatar and 14.5px `#065f46` feedback. Right: "ĐIỂM THEO TIÊU CHÍ HSK" — four 8px bars on `#f1f5f9` (Ngữ pháp 78 `#10b981`, Từ vựng 85 `#10b981`, Mạch lạc 64 `#34d399`, Phát âm · thanh điệu 71 `#34d399`), scores in `#059669`; footer above a dashed border: a 7-bar audio waveform (4px wide, heights 40/75/100/55/85/35/65%, colors `#a7f3d0`/`#6ee7b7`/`#10b981`) + "Bản ghi âm 00:42 — đã phân tích 3 lỗi thanh điệu".

### 5. Ai dùng HanPeak — `#doi-tuong`
- **Layout**: padding `130px 48px`, background `#ffffff`, inner `max-width: 1180px`, 3-column grid, `gap: 26px`.
- **Cards**: flex column, `gap: 22px`, `min-height: 380px`, padding `38px 34px`, `border-radius: 24px`, `transition: all .2s ease`. Hover → `translateY(-4px)` + shadow `0 22px 44px -28px rgba(15,23,42,.5)`.
  - Hanzi glyph: 52px `Ma Shan Zheng`, `#10b981` (card 3 uses `#059669`).
  - Title: 26px/800, `-.02em`, line-height 1.25, `#0f172a`.
  - Body: 17px/1.7.
  - Link cue pinned bottom (`margin-top: auto`): 15px/700, `#047857`, "Bắt đầu ngay →".
  | # | Glyph | Title | Body | Card styling |
  |---|---|---|---|---|
  | 1 | 基 | Người mất gốc | Xây nền tảng vững chắc từ con số 0, học đúng lộ trình để không bị bỏ lại phía sau. | `#f8fafc` on `#e2e8f0`, body `#475569` |
  | 2 | 升 | Người muốn tăng band HSK | Ôn tập trúng lỗ hổng kiến thức, tăng band nhanh hơn mà không cần học lan man. | `#ecfdf5` on `#a7f3d0`, body `#065f46` |
  | 3 | 冲 | Người gần ngày thi *(Sprinter)* — the parenthetical in `#059669` | Bứt tốc đúng lúc, luyện trúng điểm yếu trong thời gian ngắn trước ngày thi. | `#f1f5f9` on `#cbd5e1`, body `#475569` |

### 6. Đánh giá — `#danh-gia`
- **Purpose**: social proof via an infinite horizontal marquee.
- **Layout**: padding `110px 0`, background `#f8fafc`, top border `1px solid #e2e8f0`, `overflow: hidden`. Heading block `max-width: 1180px`, `margin: 0 auto 48px`, `padding: 0 48px`: "Người học nói gì về HanPeak" — 44px/1.2, 800, `-.03em`, `#0f172a`.
- **Marquee**: track is `display: flex; width: max-content; gap: 22px; padding: 8px 11px`, animated by `hp-marquee` — `translateX(0) → translateX(-50%)`, **linear, infinite, 80s** (exposed as a tweakable prop, range 20–140s). The 10 cards are rendered **twice**; the second copy is `aria-hidden="true"` so the wrap is seamless and screen readers don't double-read.
- **Edge fades**: two 120px absolutely-positioned gradients (`#f8fafc` → transparent) at left and right, `z-index: 2`.
- **Card** (all 10 identical in styling): `flex: none`, 330×430px, padding `30px 30px 26px`, `border-radius: 22px`, background `#ffffff`, `border: 1px solid #e2e8f0`, flex column, `gap: 10px`, shadow `0 10px 30px -26px rgba(15,23,42,.6)`.
  - Opening quote “: 102px `Ma Shan Zheng`, `line-height: .58`, `#a7f3d0`.
  - Quote text: 16px/1.7, `#334155`.
  - Footer row (`margin-top: auto`, flex, `align-items: flex-end`, `justify-content: space-between`, `gap: 12px`, `padding-top: 2px`): left = name (14px/700 `#047857`) stacked over result (12.5px/600 `#64748b`, `gap: 3px`); right = closing quote ” styled like the opener but with **`margin-top: -46px`** so its optical gap to the text matches the opener's.
  | Name | Result | Quote |
  |---|---|---|
  | Minh Anh | Thi đỗ HSK 3 · 280/300 | Học tiếng Trung chưa bao giờ dễ theo dõi đến vậy! |
  | Thảo Vy | Thi đỗ HSK 4 · 258/300 | Lộ trình học tự điều chỉnh theo năng lực của mình, không còn cảm giác học lan man như trước nữa. |
  | Đức Huy | Thi đỗ HSK 5 · 241/300 | Phần chấm bài Viết và Nói cho phản hồi rất chi tiết, mình biết chính xác lỗi phát âm và ngữ pháp cần sửa. Sau một tháng dùng, kỹ năng nói của mình cải thiện rõ rệt. |
  | Ngọc Trâm | Thi đỗ HSK 3 · 272/300 | App thiết kế gọn gàng, dễ dùng. |
  | Quang Khải | Thi đỗ HSK 4 · 265/300 | Trước đây mình học tiếng Trung qua nhiều nguồn lẻ tẻ nên rất mất phương hướng. HanPeak giúp mình nắm được điểm mạnh, điểm yếu của từng kỹ năng nghe – nói – đọc – viết, từ đó có lộ trình luyện tập phù hợp. |
  | Bảo Trân | Thi đỗ HSK 4 · 269/300 | Tính năng đánh giá năng lực đầu vào rất chính xác, giúp mình biết ngay nên bắt đầu từ đâu. |
  | Hoàng Long | Thi đỗ HSK 5 · 236/300 | Là người vừa đi làm vừa tự học thêm tiếng Trung để phục vụ công việc, mình đánh giá cao việc HanPeak cho phép học linh hoạt mà vẫn bám sát mục tiêu cá nhân. Hệ thống bài tập luyện tập song song với phần kiến thức giúp mình nhớ lâu hơn nhiều so với học chay. |
  | Phương Uyên | Thi đỗ HSK 3 · 261/300 | Giao diện thân thiện, hỗ trợ nhiệt tình. |
  | Trung Kiên | Thi đỗ HSK 4 · 254/300 | Mình từng thi trượt HSK vì không biết mình yếu ở đâu. Từ khi dùng HanPeak, phần báo cáo và thống kê cá nhân hóa cho mình thấy rõ tiến độ theo từng tuần, cộng với ngân hàng câu hỏi luyện tập sát với đề thi thật. Nhờ vậy lần thi gần nhất mình đã đạt điểm cao hơn hẳn. |
  | Yến Nhi | Thi đỗ HSK 5 · 244/300 | Một nền tảng học tiếng Trung đáng đầu tư thời gian, đặc biệt nếu bạn cần lộ trình học được cá nhân hóa thay vì học tràn lan không định hướng. |

  > ⚠️ The score lines are **illustrative placeholders**. Replace with verified results before launch, or drop the line.

### 7. CTA cuối trang
- **Layout**: `position: relative; overflow: hidden`, padding `150px 48px`, background `#ecfdf5`, top border `1px solid #a7f3d0`, centered. Inner `max-width: 880px`, flex column, `gap: 26px`.
- **Decoration**: 30px dot grid `#a7f3d0` at `opacity: .7`; a 1100×620px radial glow at `bottom: -260px`, `rgba(16,185,129,.28)` → transparent, animated by `hp-pulse` (7s ease-in-out infinite, opacity .35↔.7, scale 1↔1.06); a 180px 峰 at `right: 4%; top: 12%`, `#10b981` at `opacity: .14`, animated by `hp-float` (8s, ±10px).
- **Components**:
  - Urgency pill: "HSK 3.0 SẮP CHÍNH THỨC ÁP DỤNG" — 13px/700, `.06em`, padding `8px 18px`, pill, background `#ef4444`, white.
  - H2: "Làm bài đánh giá năng lực miễn phí" — 58px/1.15, 800, `-.035em`, `#0f172a`.
  - Body: "Tài liệu cũ sắp lỗi thời. Chỉ mất vài phút để biết mình đang ở đâu theo chuẩn HSK 3.0 — và bắt đầu lộ trình đúng ngay từ hôm nay." — 19px/1.7, `#475569`, `max-width: 640px`.
  - CTA: same label as the H2 — 19px/700, white on `#10b981`, padding `20px 52px`, pill, shadow `0 18px 44px -14px rgba(16,185,129,.85)`, `margin-top: 10px`. Hover → `#059669`, `translateY(-2px)`.
  - Reassurance: "Miễn phí · Không cần thẻ · Có kết quả ngay" — 14px `#64748b`.

### 8. Footer
- **Layout**: padding `72px clamp(24px,4vw,64px) 40px`, background `linear-gradient(160deg,#10b981,#0fb27c 55%,#0d9f72)`, text white. Inner `max-width: 1180px`, flex column, `gap: 56px`. Top area is a `1.2fr 1fr 1.3fr` grid with `gap: 48px`.
- **Column 1 — brand**: logo 40px + "Hanpeak" 22px/800; blurb 16px/1.7 at `rgba(255,255,255,.86)`, `max-width: 300px`: "Nền tảng học tập và ôn luyện HSK 3.0 cá nhân hóa theo năng lực của bạn."
- **Column 2 — Chính sách** (heading 20px/800): four links, 15.5px, `rgba(255,255,255,.9)`, underlined with `text-underline-offset: 3px`, each preceded by a 17px white stroked icon, `gap: 14px` between rows. Items: **Privacy Policy** (shield), **Term of Use** (document), **Chính sách thanh toán** (card), **Chính sách dùng AI** (sparkle). Hover → full white. *All `href="#"` — wire to real routes.*
- **Column 3 — Contact us** (heading 20px/800):
  - `mailto:hello@hanpeak.vn` and `tel:+84901234567` (displayed "0901 234 567"), 15.5px with 18px stroked icons, `gap: 12px`.
  - Social row (`gap: 12px`, `margin-top: 4px`): four 44×44px white circles with `#0d9f72` glyphs — TikTok, Facebook, Instagram, Threads. Hover → `translateY(-3px)`. *All `href="#"` — wire to real profiles.*
  - > ⚠️ Email and phone are **placeholders**. Confirm before launch.
- **Bottom bar**: `padding-top: 26px`, `border-top: 1px solid rgba(255,255,255,.28)`, flex row, wraps, space-between: "© 2026 Hanpeak. All Rights Reserved." (14px, `rgba(255,255,255,.85)`) and "Học nhanh hiểu gốc, bứt phá thần tốc" (14px/600, white).

---

## Interactions & Behavior

### Feature tabs (§4)
- Single `activeTab` value. Clicking a pill sets it directly; only the active panel mounts/displays.
- **Internal panel ids are 0=AI chấm, 1=Kho từ vựng, 2=Review & test, 3=Kho đề thi**, but the **display order is `[3, 2, 1, 0]`** and the **initial value is 3**. Prev/next walk that display array with wraparound (`(pos ± 1 + 4) % 4`) — not the raw index. In a rewrite, prefer storing tabs in one ordered array so this indirection disappears.
- Pill and panel transitions: `all .2s ease`.

### Hero pixel wave (§1) — the one piece of custom canvas work
A `<canvas>` fills the hero (`position: absolute; inset: 0; pointer-events: none`) and paints an irregular, isometric ridge of square "pixels" sweeping from the top-left to the bottom-right.

Rules, in order of importance:
1. **It plays exactly one sweep on page load**, then clears itself and stops. No idle loop.
2. **It replays one sweep each time the hero re-enters the viewport** after having left it (i.e. the user scrolls down and comes back up). Implemented with an `IntersectionObserver` on the hero: threshold list `[0, 0.05, 0.55, 1]`; mark `away = true` when ratio < 0.05; when ratio > 0.55 and `away`, clear the flag and play. A `playing` guard prevents overlapping sweeps.
3. Exactly **one crest** should be visible at any moment.

Parameters as tuned:
```
COLS = 86, ROWS = 44, SIZE = 4.2      // grid density and base pixel size
SPEED = 2.2                            // phase velocity
K = 1.7                                // spatial frequency — one crest on screen
DUR = (2.6 * K + 2π) / SPEED           // ≈ 4.9s: one full diagonal sweep
DPR = min(devicePixelRatio, 2)         // canvas resized on window resize
```
Per grid cell, with `u = c/COLS`, `v = r/ROWS`:
```
warp  = .26*sin(u*5.1 - v*3.7 + t*.55)
      + .17*sin(v*8.3 + u*2.2 - t*.9)
      + .10*sin((u+v)*13.0 - t*1.7)     // ragged crest edge (not a clean rhombus)
d     = u + v + warp
wave  = sin(d*K - t*SPEED)
grain = .72 + .28*sin(u*21.0 + v*17.0)  // uneven brightness
band  = max(0, wave) * grain
lift  = band² * 62 + band * 14 * sin(v*9.4 - t*1.3)   // 3D pop toward the viewer

stepX = w*1.35/COLS ; stepY = h*1.5/ROWS ; ox = -w*.16 ; oy = -h*.3
x = ox + c*stepX*.5 + r*stepY*.42
y = oy + r*stepY*.55 + c*stepX*.2 - lift
s = SIZE * (.55 + (.35 + band*.65) * .85)
a = (.05 + band² * .46) * fade          // fade ramps 1→0 over the last .9s
fill = band > .8 ? rgba(4,120,87,a) : rgba(16,185,129,a)
```
Squares are drawn with `fillRect(x - s/2, y - s/2, s, s)`; cells outside the canvas ±20px are skipped.

**Implementation notes for the rewrite**: cancel the rAF on unmount and disconnect the observer. Honour `prefers-reduced-motion: reduce` by skipping the animation and leaving the canvas blank (it is purely decorative and `aria-hidden`). The prototype needed a retry loop because its ref attached late — in React this is unnecessary; a normal `useRef` + `useEffect` is enough.

### Other motion
| Name | Used by | Definition |
|---|---|---|
| `hp-marquee` | Testimonial track | `translateX(0)` → `translateX(-50%)`, linear, infinite, 80s |
| `hp-draw` | Hero ability curve | `stroke-dashoffset: 1600 → 0`, `2.2s cubic-bezier(.4,0,.2,1) .25s both` |
| `hp-rise` | Hero SVG entrance | opacity 0→1 + `translateY(22px)→0`, `.9s cubic-bezier(.2,.7,.3,1) both` |
| `hp-glow` | Summit dot | `r: 7↔10`, `opacity: 1↔.75`, 2.6s ease-in-out, 1.6s delay, infinite |
| `hp-halo` | Summit halo | `scale(.7)→scale(1.9)`, `opacity .55→0`, 2.6s ease-out, 1.6s delay, infinite |
| `hp-pulse` | Final-CTA glow | `opacity .35↔.7`, `scale 1↔1.06`, 7s ease-in-out infinite |
| `hp-float` | Final-CTA 峰 | `translateY(0 ↔ -10px)`, 8s ease-in-out infinite |

Hover states are consolidated per component above; the common pattern is a jade border swap plus a 1–4px lift.

### Navigation
Anchor links scroll to section ids. Sections carry `scroll-margin-top: 82px`. **Do not use `scrollIntoView` inside the prototyping host**; in a real app, `scroll-behavior: smooth` on the root is fine.

### CTAs
"Bắt đầu ngay" (header, hero) and "Làm bài đánh giá năng lực miễn phí" (final CTA) are **not wired** — no handlers, no routes. Point all of them at the free-assessment entry point.

### Responsive behaviour
The prototype is desktop-only. Recommended breakpoints:
- Header nav already wraps via `flex-wrap` + `clamp()`; below ~768px replace it with a drawer.
- §2 3-col, §3 4-col, §5 3-col grids → 2-col at ~1024px, 1-col at ~640px. When they stack, **drop the `min-height` baseline hacks** (300px cards, 90px/60px title blocks) — they only exist to align items across columns.
- §4 panels are two-column grids → stack at ~900px; the arrow buttons can be dropped in favour of swipe.
- §6 cards are fixed 330×430px — keep the fixed size and let the marquee scroll.
- Hero H1 68px → `clamp(36px, 6vw, 68px)`.

### Accessibility to fix during implementation
The prototype is a visual mock; a production build should add:
- Real tab semantics on §4 (`role="tablist"` / `role="tab"` / `aria-selected` / `aria-controls`, arrow-key navigation).
- Pause-on-hover and pause-on-`prefers-reduced-motion` for the testimonial marquee.
- Semantic heading order (currently correct: one `h1`, `h2` per section) and `aria-label`s on the icon-only social links (already present).
- Visible focus rings — the prototype defines hover only.
- Contrast check: `#64748b` on `#ffffff` passes for body text; the 12.5px score line is borderline at small size — consider `#475569`.

## State Management
Minimal — this is a marketing page.
| State | Type | Purpose |
|---|---|---|
| `activeTab` | `0 \| 1 \| 2 \| 3` | Which feature panel shows. Initial `3` (Kho đề thi). |
| `wavePlaying` | boolean | Guards against overlapping canvas sweeps. |
| `heroAway` | boolean | Tracks whether the hero has left the viewport, to arm the replay. |
| `testimonialSpeed` | number (seconds) | Marquee duration; default 80, range 20–140. Was a design tweak — hardcode or expose in a CMS. |

No data fetching. Every number in the mock UIs (question counts, band scores, "612 / 973 từ", "+12 đề") is static illustrative content. If any of it becomes real, it should come from an API.

## Design Tokens

### Colors
| Token | Hex | Usage |
|---|---|---|
| Jade 500 | `#10b981` | Primary brand, CTAs, active states, accents |
| Jade 600 | `#059669` | CTA hover, subheadline text |
| Jade 700 | `#047857` | Strongest jade text, names, emphasis |
| Jade 800 | `#065f46` | Text on jade-tinted surfaces |
| Jade 400 | `#34d399` | Secondary accents, timer, waveform |
| Jade 300 | `#6ee7b7` | Waveform, gradient stop |
| Jade 200 | `#a7f3d0` | Borders on tinted surfaces, quote marks, dot grid |
| Jade 100 | `#d1fae5` | Connector gradient ends |
| Jade 50 | `#ecfdf5` | Tinted surface, final-CTA background |
| Footer gradient | `#10b981 → #0fb27c 55% → #0d9f72` | Footer only (160deg) |
| Ink 900 | `#0f172a` | Headings, dark surfaces (CBT header bar) |
| Ink 800 | `#1e293b` | Dark borders |
| Slate 600 | `#475569` | Body copy |
| Slate 500 | `#64748b` | Secondary copy, captions |
| Slate 400 | `#94a3b8` | Eyebrows, axis labels |
| Slate 300 | `#cbd5e1` | Dot grid on light gray, arrow borders |
| Slate 200 | `#e2e8f0` | Default borders, dividers |
| Slate 100 | `#f1f5f9` | Track backgrounds, §2 section background |
| Slate 50 | `#f8fafc` | Page background, inner tiles |
| White | `#ffffff` | Cards, panels |
| Red 500 | `#ef4444` | Problem indices, urgency pill, "Lỗ hổng" bar |
| Red 700 | `#b91c1c` | Red status text |
| Red 800 | `#991b1b` | Text on red tint |
| Red 100 | `#fee2e2` | Error highlight |
| Red 50 | `#fef2f2` | Error row background |
| Red 200 | `#fecaca` | Error row border |
| Amber 500 | `#f59e0b` | "Cần ôn" bar, coming-soon dot |
| Amber 700 | `#b45309` | Amber status + badge text |
| Amber 800 | `#92400e` | Text on amber tint |
| Amber 200 | `#fde68a` | Badge/row border |
| Amber 100 | `#fef3c7` | Suggestion highlight |
| Amber 50 | `#fffbeb` | Badge/row background |

### Typography
- **Primary**: `Be Vietnam Pro` — weights 400, 500, 600, 700, 800 (Google Fonts). Vietnamese diacritics are the reason for this choice; keep it or substitute another Vietnamese-complete family.
- **Display / Chinese accent**: `Ma Shan Zheng` (Google Fonts) — used only for hanzi (汉, 峰, 基, 升, 冲), the logo mark, and the oversized quotation marks. Never for body copy.
- Scale as used: 68 / 58 / 48 / 46 / 44 / 30 / 26 / 23 / 22 / 20 / 19 / 17 / 16.5 / 16 / 15.5 / 15 / 14.5 / 14 / 13.5 / 13 / 12.5 / 12 px.
- Heading letter-spacing: `-.035em` (h1, 58px h2), `-.03em` (48/46/44px), `-.02em` (30/26px). Eyebrows: `+.14em` to `+.16em`, uppercase, 12–13px/700.
- Body line-heights: 1.65–1.7. Heading line-heights: 1.1–1.35.
- `text-wrap: balance` on all large headings.

### Spacing
Section padding 76–150px vertical, 40–48px horizontal (footer uses `clamp(24px,4vw,64px)`). Grid gaps 20 / 24 / 26 / 28 px. Card padding 20 / 24 / 26 / 30 / 34 / 38 px. Inner stack gaps 3 / 6 / 10 / 12 / 14 / 16 / 18 / 20 / 22 / 26 / 30 / 34 / 44 / 48 / 56 / 64 px.

### Radii
`9999px` (pills, badges, circles, bars) · `28px` (feature panel) · `24px` (audience cards) · `22px` (testimonial cards) · `20px` (problem cards) · `18px` (panel tiles) · `16px` (word cards, footer strip) · `14px` (AI note) · `12px` (rows) · `10px` / `8px` (small logo chips) · `6px` (highlight bar) · `2px` (waveform bars).

### Shadows
```
0 4px 12px -6px rgba(15,23,42,.3)     // arrow buttons
0 4px 14px -8px rgba(15,23,42,.25)    // tab bar
0 6px 16px -6px rgba(16,185,129,.7)   // header CTA
0 10px 30px -26px rgba(15,23,42,.6)   // testimonial cards
0 12px 30px -26px rgba(15,23,42,.7)   // problem cards
0 18px 40px -14px rgba(16,185,129,.9) // hero CTA
0 18px 44px -14px rgba(16,185,129,.85)// final CTA
0 22px 44px -28px rgba(15,23,42,.5)   // audience card hover
0 24px 48px -14px rgba(16,185,129,1)  // hero CTA hover
0 24px 60px -34px rgba(15,23,42,.45)  // feature panel
```

## Assets
| Asset | Path | Notes |
|---|---|---|
| HanPeak logo | `assets/logo-hanpeak.png` | Provided by the client as a JPEG on a checkerboard background; the checkerboard was flood-filled to transparency and the image cropped to its content box. Used at 44px (header), 40px (footer). **Ask the client for a vector (SVG) original** before production. |
| Icons | inline SVG | Footer policy icons (shield, document, card, sparkle), contact icons (envelope, phone), social glyphs (TikTok, Facebook, Instagram, Threads), and the panel chevrons are all hand-inlined `stroke`/`fill` SVG. Replace with the codebase's icon library where equivalents exist. |
| Fonts | Google Fonts | `Be Vietnam Pro` 400–800, `Ma Shan Zheng` 400. Self-host for production. |
| Illustrations | inline SVG / canvas | The hero ascent graphic is inline SVG; the pixel wave is canvas. No raster imagery anywhere — nothing else to license. |

There are **no product screenshots**. Every "product UI" in §4 is a hand-built mock. If real screenshots exist, they would slot into the right-hand tile of each panel.

## Files
| File | What it is |
|---|---|
| `Hanpeak Landing.dc.html` | The source design. Template markup + logic class + tweak props. Read the template for structure and exact inline styles; read the logic class for the tab state, the canvas wave, and the IntersectionObserver replay. |
| `Hanpeak Landing Page.html` | Self-contained bundle — fonts, logo, and runtime inlined. Open directly in a browser to see the design running, including all motion. **Start here.** |
| `assets/logo-hanpeak.png` | Transparent logo used by both files. |
| `content landing hanpeak.md` | The client's original content brief (7 sections) the page was built from. |

Open `Hanpeak Landing Page.html` first to see the intended result, then read `Hanpeak Landing.dc.html` for exact values.
