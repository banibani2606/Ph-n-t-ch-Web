# Build Brief — HanPeak Landing Page (production rebuild)

Read this file **before** touching code. It is the contract for the rebuild.

`README.md` in this same folder is the **visual specification** — every color, font size, spacing value, animation timing, and line of copy is documented there, section by section. This file covers everything the visual spec deliberately leaves open: what to build it *in*, what is broken in the prototype, what must not be copied, and what "done" means.

---

## 1. What you are building

A single-page marketing site for **HanPeak**, a Vietnamese platform for HSK 3.0 exam prep. Eight sections, one scroll, one conversion goal: get the visitor into the **free placement assessment** ("Làm bài đánh giá năng lực miễn phí").

All copy is Vietnamese. Do not translate it, do not rewrite it, do not "improve" it. Copy the strings verbatim from the spec — including diacritics, the `·` separators, and the curly quotes.

## 2. What the bundled files are — and are not

| File | Status |
|---|---|
| `Hanpeak Landing Page.html` | **Reference render.** Open it in a browser first. This is what the client approved. It is the source of truth for *appearance and motion*. |
| `Hanpeak Landing.dc.html` | **Source of exact values.** Read it when you need a precise hex/px/timing. |
| `README.md` | **The spec.** Written for you; work from it. |
| `assets/logo-hanpeak.png` | The only raster asset. |
| `content landing hanpeak.md` | Client's original content brief. |

**Do not port the HTML.** Both HTML files were produced by a design-prototyping tool and carry two artifacts that must not reach production:

1. A custom template runtime (`<x-dc>`, `{{ hole }}` placeholders, `class Component extends DCLogic`). This is not a real framework. Read it as *structure and state description*, then throw it away.
2. **Every single style is an inline `style` attribute.** This was a hard constraint of the prototyping tool, not a design decision. Inline styles must not survive the rebuild.

Your job is to **recreate the design in a real stack**, matching it closely, with production-grade markup, styling, accessibility, and responsive behaviour.

## 3. Stack

No codebase exists yet — pick the stack. Unless there is a reason to deviate:

- **Next.js (App Router) + TypeScript**
- **Tailwind CSS** — express the tokens in §Design Tokens of the spec as `theme.extend` entries (jade + ink/slate scales, the shadow list, the radius list). Do not hardcode hexes in class strings.
- **Self-hosted fonts** via `next/font/local` — `Be Vietnam Pro` (400/500/600/700/800) and `Ma Shan Zheng` (400). Do not ship a render-blocking Google Fonts `<link>`.
- Static export is fine; there is no backend.

If you choose differently, that is acceptable — but keep: a component model, a real styling layer with design tokens, and self-hosted fonts.

## 4. THE priority: responsive

**This is the single most important requirement of the rebuild.** The prototype is desktop-only and collapses badly on mobile. The client hit this immediately. A pixel-perfect desktop rebuild that repeats the mobile failure is a failed deliverable.

Build **mobile-first**. Write the 375px layout first, then scale up. Do not build desktop and add breakpoints after.

### What specifically breaks in the prototype — fix each

| # | Problem | Where | Fix |
|---|---|---|---|
| 1 | **No viewport meta tag at all** | `<head>` | `<meta name="viewport" content="width=device-width, initial-scale=1">`. Everything else is moot without this. |
| 2 | Hardcoded column counts: `repeat(3,1fr)` (§Vấn đề, §Ai dùng), `repeat(4,1fr)` (§Giải pháp), `1fr 1.2fr` / `1.25fr 1fr` / `1fr 1.15fr` (feature panels) | §2, §3, §4, §5 | Prefer `repeat(auto-fit, minmax(260px, 1fr))` so reflow is intrinsic. Where the step order matters (§3), explicit breakpoints: 4 → 2 → 1 col. |
| 3 | Fixed section padding `130px 48px`, `150px 48px`, `120px 40px` | all sections | `clamp()` both axes, e.g. `padding: clamp(64px, 9vw, 130px) clamp(20px, 5vw, 48px)`. At 375px the current 48px side padding eats 26% of the screen. |
| 4 | Fixed heading sizes: h1 68px, h2 58/48/46/44px, panel titles 30px | all sections | `clamp(32px, 6vw, 68px)` for h1; `clamp(28px, 4.5vw, 48px)` for h2. Never let h1 exceed ~36px at 375px. |
| 5 | **`min-height` baseline hacks** — 300px problem cards, 90px problem-card titles, 60px step titles | §2, §3 | These exist **only** to align text baselines across columns. The moment the grid is 1-col they become dead whitespace. Drop them below the stacking breakpoint — or better, delete them entirely and use CSS `subgrid` / a shared grid row so alignment is intrinsic at every width. |
| 6 | Header nav: 5 links + wordmark + CTA in one flex row | header | Already wraps, but wrapping to 3 lines on mobile looks broken. Below ~768px: hamburger → slide-in or full-screen drawer. Keep the CTA visible in the bar if it fits, otherwise put it at the top of the drawer. |
| 7 | Feature panel: prev/next arrow buttons flanking the card | §4 | Arrows waste ~150px of horizontal space on mobile. Below ~900px hide them and use horizontal swipe (scroll-snap) + the tab pills. |
| 8 | Feature tab bar: 4 pills, `white-space: nowrap` | §4 | Below ~640px make it a horizontally scrollable strip with scroll-snap and hidden scrollbar, active pill auto-scrolled into view. Do not let it wrap into 3 stacked rows. |
| 9 | Testimonial cards fixed 330×430px | §6 | Keep the fixed size — the marquee needs it. Just verify the section still clips correctly and the 120px edge fades scale down (`clamp(48px, 12vw, 120px)`). |
| 10 | Hero ascent SVG `viewBox="0 0 1100 360"` with 15px axis labels | §1 | It scales, but at 375px the "HSK 1…6" labels become ~5px. Either bump label size at small widths or simplify the graphic on mobile (fewer gridlines). |
| 11 | Hero canvas wave sized from hero box, grid 86×44 | §1 | 3,784 cells per frame is wasteful on a phone. Scale `COLS`/`ROWS` with viewport width (e.g. `COLS = clamp(40, w/16, 86)`), and cap DPR at 2 (already done). |
| 12 | Decorative hanzi 汉 340px / 峰 260px positioned off-canvas edges | §1, §7 | Recheck at every width — on mobile they can force horizontal scroll if `overflow: hidden` is ever lost. Shrink them with `vw` units. |
| 13 | Footer 3-col grid `1.2fr 1fr 1.3fr`, gap 48px | footer | 3 → 1 col at ~768px. Social row stays horizontal. |
| 14 | Hero text `max-width: 1260px` inside a 1300px container | §1 | Fine on desktop; make sure it is `width: 100%` constrained, not a fixed width, at small sizes. |

### Test matrix — verify all of these before calling it done

375×667 (iPhone SE) · 390×844 (iPhone 14) · 414×896 · 768×1024 (iPad portrait) · 1024×768 (iPad landscape) · 1280 · 1440 · 1920.

At every width: **no horizontal scrollbar**, no text clipped or overlapping, no element narrower than its content, all tap targets ≥44×44px.

## 5. Known defects in the prototype — do not reproduce

Beyond responsive, these are real problems in the reference. Fix them; do not faithfully recreate them.

**Accessibility**
- **§4 tabs have no ARIA and no keyboard support.** They are plain `<button>`s toggling `display`. Build real tabs: `role="tablist"` / `role="tab"` / `aria-selected` / `aria-controls` / `role="tabpanel"` / `aria-labelledby`, arrow-key + Home/End navigation, roving tabindex.
- **No visible focus states anywhere.** The prototype defines hover only. Every interactive element needs a visible focus ring (`:focus-visible`), meeting 3:1 contrast against its background.
- **`prefers-reduced-motion` is not honoured.** Under reduce: skip the canvas wave entirely (leave the canvas blank — it is decorative and `aria-hidden`), freeze the testimonial marquee, skip the SVG draw-in and the pulsing/floating loops. This is not optional; the page has a lot of continuous motion.
- **Testimonial marquee cannot be paused.** Add pause-on-hover and pause-on-focus-within. An 80-second infinite scroll with no stop control is a WCAG 2.2.2 failure.
- Contrast: `#64748b` on white is fine for 16px body, but the **12.5px score line** under each testimonial name is borderline. Use `#475569` there.
- The decorative hanzi and the canvas must be `aria-hidden="true"` and out of the accessibility tree (they already are in the prototype — keep it).

**Semantics / SEO**
- The prototype has **no `<head>` metadata**: no title, description, Open Graph, `lang="vi"`, canonical, or favicon. Add all of it. `<html lang="vi">` matters for Vietnamese text rendering and screen readers.
- Add JSON-LD: `Organization` + `WebSite`, and `Product`/`Course` if appropriate.
- Section elements should be `<section>` with an `aria-labelledby` pointing at their `<h2>` (heading hierarchy in the prototype is already correct: one `h1`, one `h2` per section — preserve it).
- The footer policy links and social links are all `href="#"`. Wire them to real routes; if a page does not exist yet, the link should not ship.

**Wiring**
- **No CTA is connected.** "Bắt đầu ngay" (header, hero) and "Làm bài đánh giá năng lực miễn phí" (final CTA) have no handler and no href. All of them point at the free-assessment entry point. Confirm the URL with the client.
- Anchor nav: use plain `href="#id"` + `scroll-behavior: smooth` on the root, and keep `scroll-margin-top` on every target (currently 82px — recompute it from the real header height, and remember the header height changes on mobile).

**Performance**
- The logo is a **PNG converted from a JPEG** with the background flood-filled to transparency. It is not clean. **Ask the client for the SVG original.** If none exists, at minimum re-export at 2× the largest render size (44px → 88px+) and serve WebP/AVIF with a PNG fallback.
- The bundled reference file is 5.8 MB because fonts and the logo are base64-inlined. That is an artifact of bundling, not a target. Real build should be well under 300 KB of JS.
- Canvas: cancel the rAF on unmount, disconnect the IntersectionObserver, and do not run the loop while the hero is off-screen.

## 6. Content that is placeholder — flag before launch

Do not present any of this as fact. Either get real values from the client or remove the element.

| Item | Where | Note |
|---|---|---|
| All 10 testimonial score lines ("Thi đỗ HSK 3 · 280/300" etc.) | §6 | **Invented.** The quotes themselves came from the client; the scores did not. Get verified results or drop the line. |
| `hello@hanpeak.vn`, `0901 234 567` | footer | Placeholder. |
| All social links (`href="#"`) | footer | No real profiles supplied. |
| Question bank counts: 64 / 128 / 96 đề, "+12 đề" | §4 panel A | Illustrative. |
| "Đã thuộc 612 / 973 từ band HSK 3" | §4 panel C | Illustrative. |
| Every score, bar percentage, and 汉字 example in the four feature panels | §4 | These are **hand-built mock UIs**, not screenshots of a real product. If real product screenshots exist, they belong in the right-hand tile of each panel — ask. |
| "© 2026 Hanpeak" | footer | Confirm the year at launch. |

Also note: **§4 panel "AI chấm Viết & Nói" carries a COMING SOON badge.** That feature does not exist yet. Keep the badge; do not link the panel to anything.

## 7. Behaviour that must be preserved exactly

Two pieces of motion are load-bearing to the design. Getting them wrong will be noticed.

### Hero pixel wave (§1)
Full math, constants, and projection are in the spec under *Interactions & Behavior*. The three rules the client explicitly set, in priority order:

1. **One sweep on page load, then it clears itself and stops.** No idle loop, no second crest.
2. **One more sweep each time the hero re-enters the viewport** after having left it (scroll down, scroll back up). `IntersectionObserver`, thresholds `[0, 0.05, 0.55, 1]`: mark `away` when ratio < 0.05; when ratio > 0.55 **and** `away`, replay once and clear the flag. Guard against overlapping sweeps.
3. **Exactly one crest visible at any moment.** The spatial frequency `K = 1.7` is tuned for this — an earlier value showed two crests and was rejected by the client.

The crest must look **irregular**, not like a clean rhombus. Three layered sine warps plus a grain term do this; the coefficients are in the spec. Keep them.

In React this is a straightforward `useRef` + `useEffect`. The prototype has a rAF retry loop working around a late-attaching ref — that hack is unnecessary; do not port it.

### Feature tabs (§4)
- Display order: **Kho đề thi · Review & test · Kho từ vựng · AI chấm Viết & Nói**. Default open = **Kho đề thi**.
- The prototype stores panels under internal indices `0=AI chấm, 1=Kho từ vựng, 2=Review & test, 3=Kho đề thi` and maps display order through `[3,2,1,0]`. **Do not reproduce this indirection** — store the tabs in one array already in display order. It exists only because tabs were reordered late.
- Prev/next wrap around in display order.

### Everything else
The seven CSS keyframe animations (`hp-marquee`, `hp-draw`, `hp-rise`, `hp-glow`, `hp-halo`, `hp-pulse`, `hp-float`) are tabulated in the spec with exact durations, easings, and delays. Reproduce them, all gated behind `prefers-reduced-motion`.

Marquee duration is **80s** (was tuned down from 60s at the client's request). The prototype exposed it as a tweakable prop, range 20–140s — hardcode 80s or expose it in whatever CMS/config you use.

## 8. State

Trivial. No data fetching; every number on the page is static.

| State | Type | Notes |
|---|---|---|
| `activeTab` | index into the display-ordered tab array | Initial: Kho đề thi |
| `mobileNavOpen` | boolean | New — did not exist in the prototype |
| `wavePlaying` | boolean | Guards overlapping canvas sweeps |
| `heroAway` | boolean | Arms the wave replay |

## 9. Definition of done

- [ ] Renders correctly at all 8 widths in the test matrix, no horizontal scroll anywhere
- [ ] Zero inline `style` attributes; all values come from theme tokens
- [ ] Lighthouse ≥ 95 on Performance, Accessibility, Best Practices, SEO (mobile profile)
- [ ] Full keyboard traversal: every interactive element reachable, visible focus, tabs respond to arrow keys
- [ ] `prefers-reduced-motion: reduce` disables all seven animations and the canvas
- [ ] Wave plays once on load, once per hero re-entry, never twice at once, never two crests
- [ ] Every string matches the spec character-for-character (Vietnamese diacritics intact)
- [ ] Every CTA points at a real destination
- [ ] Every placeholder from §6 is either replaced with client-supplied data or removed
- [ ] `<html lang="vi">`, title/description/OG tags, favicon present
- [ ] Fonts self-hosted, subset, `font-display: swap`

## 10. Open questions for the client

Ask these before or during the build — do not guess:

1. What is the destination URL for the assessment CTA?
2. Is there a vector (SVG) version of the logo?
3. Real contact email and phone number?
4. Real URLs for TikTok, Facebook, Instagram, Threads?
5. Do the policy pages (Privacy Policy, Term of Use, Chính sách thanh toán, Chính sách dùng AI) exist yet, and where do they live?
6. Are the testimonial scores real? If so, which numbers are correct?
7. Are the question-bank counts (64/128/96) real?
8. Are there real product screenshots to replace the four hand-built mock UIs in §4?
9. Should the page be Vietnamese-only, or is i18n needed later? (Affects whether copy gets externalised now.)
10. Analytics — which platform, and which events should be tracked beyond CTA clicks?
