# 14-Day Smoke-Test & Willingness-to-Pay Validation Plan — ShipLink

> **Core Rule:** Zero AWS backend code, zero Stripe setup, zero GST/incorporation overhead until Day-14 validation clears the kill/scale thresholds below.

---

## 1. What We Are Testing (Hypotheses)

1. **Usage Demand (`H1`):** Freelance developers, boutique agencies, and engineering leads genuinely prefer a **10-second login-free Magic Status Link** over forcing clients into Jira/Asana/email threads.
2. **Willingness to Pay (`H2`):** Creators who use the free link generator will click **"Pro Sync / Custom Domain / Slack Receipts"** and submit their work email + preferred price (`$19/mo Solo` vs `$39/mo Agency` vs `$69 Early-Bird LTD`).
3. **Architect & Consulting Halo (`H3`):** Technical hiring managers and founders clicking `/architecture` convert into interview callbacks or AWS/AI Architecture audit inquiries.

---

## 2. 14-Day Execution Calendar

| Days | Focus | Concrete Actions |
|---|---|---|
| **Days 1–4** | **Build & Design QC** | Complete Next.js static frontend (`/`, `/create`, `/m`, `/architecture`, Pro Waitlist Modal), wire lightweight waitlist endpoint (Web3Forms / Formspree / static JSON fallback), run `browser` Design QC on desktop & mobile, deploy to **Vercel / Cloudflare Pages ($0/mo)**. |
| **Days 5–6** | **Portfolio & Architect Sync** | Add ShipLink live URL + Case Study link into `engineering-foundations/04-portfolio/index.html` and LinkedIn Featured section. |
| **Days 7–10** | **Watering-Hole Distribution (Zero Ad Spend)** | Launch genuinely helpful breakdown posts (no spam):<br>1. `r/freelance` & `r/webdev`: *"Clients kept ignoring Jira/Notion links so I built a 10-second login-free milestone & sign-off link tool (free, no signup)"*<br>2. `r/agencies` & `r/SaaS`: *"Testing if agencies actually want a lightweight magic-link alternative to $100/mo portals"*<br>3. `Show HN` + LinkedIn Technical Post highlighting the `/architecture` capability-token & AWS single-table design.<br>4. Direct outreach to **20 boutique dev/design agency founders** on LinkedIn/X asking for 2 minutes of blunt critique. |
| **Days 11–14** | **Measure & Decide** | Audit conversion numbers against the Kill / Pivot / Scale gates below. |

---

## 3. Hard Decision Gates (Day 14 Verdict)

| Outcome Signal (Over Days 5–14) | Verdict | Next Action |
|---|---|---|
| **`< 150` unique visitors OR `< 20` magic links created** | **Distribution Failure / Weak Hook** | Rewrite positioning headline & run 1 more focused distribution wave (or Product Hunt launch) before judging product merit. |
| **`>= 300` link creations BUT `0–2` Pro Waitlist emails** | **Free Utility Only (Low WTP)** | **DO NOT BUILD BACKEND.** Keep static app deployed permanently as a **$0 Architect Portfolio Flagship** & consulting demo (`monzy.co` utility play), and stop investing product hours. |
| **`>= 15` Pro Waitlist work-emails OR `>= 3` CTO/Consulting inquiries** | **Validated Demand -> Greenlight Phase 2** | Only *now* build the AWS Serverless backend (`API Gateway + Lambda + DynamoDB Single-Table + EventBridge + GitHub Webhooks`) and launch paid MVP. |
