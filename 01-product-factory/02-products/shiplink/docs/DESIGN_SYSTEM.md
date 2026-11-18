# Design System & UI/UX Quality Contract — ShipLink

> **Governed by:** `.agents/skills/design-qc/SKILL.md`  
> **Aesthetic Anchor:** Swiss SaaS Clarity (Linear / Stripe / Cal.com / `monzy.co` frictionless speed) — **explicitly zero generic dark-purple AI gradient slop**.

---

## 1. Color Tokens (High-Trust Light-First + Obsidian Technical Blocks)

| Token | Hex | Usage | Contrast Guarantee |
|---|---|---|---|
| `--canvas` | `#F8FAFC` | Primary page background (soft slate tint) | Clean separation against white cards |
| `--surface` | `#FFFFFF` | Elevated cards, builder workspace, client card | `1px solid #E2E8F0` hairline border |
| `--ink-primary` | `#0F172A` | Headlines, titles, primary body text | `> 15:1` contrast against white |
| `--ink-secondary` | `#475569` | Supporting descriptions, metadata labels | `> 7:1` contrast against white |
| `--brand-primary` | `#4F46E5` | Primary buttons, active borders, brand mark | White text `#FFFFFF` (`> 6.2:1`) |
| `--brand-hover` | `#4338CA` | Primary button hover state | Clear interactive feedback |
| `--success-bg / ink` | `#ECFDF5` / `#047857` | `Approved` milestone badge & receipt confirmation | Crisp accessible emerald |
| `--review-bg / ink` | `#FEF3C7` / `#B45309` | `Ready for Review` milestone action state | Clear attention cue without neon glare |
| `--progress-bg / ink` | `#EEF2FF` / `#4338CA` | `In Progress` milestone badge | Cohesive with Indigo primary |
| `--tech-obsidian` | `#0B0F19` | Code blocks, C4 terminal diagrams on `/architecture` | High-contrast `#F1F5F9` text (`text-slate-100`) |

---

## 2. Typography Scale (Anti-Squint Law Enforced)

- **Display / Headings:** `Plus Jakarta Sans` (`700` / `800`), tight tracking (`-0.025em`)
- **UI & Body Copy:** `Inter` (`400` / `500` / `600`) — **minimum body text `15px` (`text-[15px]`) or `16px` (`text-base`), NEVER `< 14px` for readable prose or form inputs**
- **Technical Badges / IDs / Timestamps:** `JetBrains Mono` (`>= 12px` for secondary tags; never `9px`/`10px` on essential controls)
- **Line Height:** `leading-relaxed` (`1.625`) on all descriptions and client notes

---

## 3. Layout, Navigation & Ergonomic Rules

1. **Orientation Clarity:** Sticky top navigation (`h-16`) with unmistakable `ShipLink` home mark (`/`), active route indicator across **Home (`/`) · Create Link (`/create`) · Live Client Demo (`/m`) · Architecture (`/architecture`)**, plus primary **"Create Free Link"** CTA.
2. **Zero 404s & Graceful Fallbacks:** Every declared route (`/`, `/create`, `/m`, `/architecture`) resolves HTTP 200. Invalid/corrupted `#d=` payloads on `/m` fall back cleanly to an informative recovery state with a 1-click button to load the sample Sprint board or open `/create`.
3. **Zero Scroll Hijacking:** No forced `.scrollIntoView()`. Split-screen builder (`/create`) places editor (`lg:col-span-7`) and live client preview (`lg:col-span-5`) cleanly side-by-side with `min-h-0 min-w-0` flex/grid safety.
4. **Mobile First (`375px` Client View Guarantee):** Over 50% of busy clients/founders open magic status links from WhatsApp/Slack on their phone. `/m` MUST render flawlessly at `375px` width with full-width tap-friendly **Approve Milestone** buttons (`min-h-[44px]`).

---

## 4. Pre-Flight QC Checklist (Executed via `browser` Subagent)

Before handing Phase 1 over to the founder:
- [ ] `npm run build` exits `0` with zero TypeScript or ESLint errors.
- [ ] Desktop (`1440x900`) and Mobile (`375x812`) visual audit across `/`, `/create`, `/m`, and `/architecture`.
- [ ] All interactive controls tested live: preset switching, adding/editing milestone, copying generated Magic URL, opening Magic URL in clean view, clicking **Approve Milestone** & verifying receipt render, opening Pro Pricing Waitlist modal, and selecting tier.
- [ ] Contrast, body font size (`>= 14px`), and horizontal overflow (`0px` overflow) verified across all pages.
