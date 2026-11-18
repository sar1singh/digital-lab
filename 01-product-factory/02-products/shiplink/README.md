# ShipLink — Zero-Login Magic Client Status & Sign-Off Portal

> **Parent Umbrella:** ThinkLate Digital Lab (`digital-lab/01-product-factory`)  
> **Phase:** Phase 1 — Documentation, UI/UX Architecture & Client-Side Smoke-Test Frontend (Zero Backend)  
> **Strategic Role:** 3-in-1 Core Engine Flagship — (1) Production Architect Portfolio Proof, (2) Consulting Client Deliverable Portal, (3) B2B Micro-SaaS Willingness-to-Pay Test

---

## Why ShipLink Exists

Freelancers, boutique engineering/AI agencies, and consulting leads face the same recurring friction every week:
- Clients and executive stakeholders **refuse to log into Jira, Linear, Asana, or heavy portals** to check sprint status.
- Teams fall back to chaotic WhatsApp/Slack screenshots and *"Hey, quick update on X?"* email threads.
- Existing client portal suites (`Assembly/Copilot`, `SuiteDash`, `Motion.io`) force heavy workspace setup and `$19–$79+/user` seat fees.

**ShipLink fixes this in 10 seconds:** Create a clean milestone board with preview links and zero signup, copy **one Magic URL**, and send it. Your client opens the link with **zero password** and clicks **Approve Milestone** or **Request Change**.

---

## Repository Structure

```text
digital-lab/01-product-factory/02-products/shiplink/
├── README.md                          # Product overview & phase tracker
├── docs/
│   ├── PRODUCT_SPEC.md                # Functional/NFR spec, MVP scope, anti-bloat guardrails
│   ├── USER_FLOWS_AND_FEATURES.md     # End-to-end Mermaid user flows & route matrix
│   ├── DESIGN_SYSTEM.md               # Linear/Stripe light-first design tokens & Design QC contract
│   └── SMOKE_TEST_LAUNCH_PLAN.md      # 14-day zero-ad launch & willingness-to-pay validation plan
└── web/                               # Next.js 14 + TypeScript + Tailwind static/client frontend (Phase 1)
```

**Architect Case Study (Companion Repo):**  
`engineering-foundations/04-portfolio/case-studies/shiplink-zero-login-status-portal.md`

---

## Phase Roadmap (Strict Gate Discipline)

| Phase | Scope | Cloud Cost | Status |
|---|---|---|---|
| **Phase 1 (Current)** | Complete docs, UI/UX design system, landing page, interactive URL-compressed Magic-Link Creator (`/create`), Client View (`/m`), `/architecture` showcase, and Pro Pricing Waitlist smoke test. | **$0/mo** (Static Edge) | **In Progress** |
| **Phase 2 (Gated on Signal)** | AWS Serverless Backend (`API Gateway -> Lambda -> DynamoDB Single-Table -> EventBridge -> GitHub/Linear Webhooks + SES/Slack Receipts`) — **built ONLY if Phase 1 proves user creation + paid waitlist demand**. | ~$3–$8/mo | **Locked / Parked** |
