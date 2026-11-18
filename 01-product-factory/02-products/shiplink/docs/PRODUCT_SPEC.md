# Product Specification — ShipLink (Phase 1 MVP)

> **Product:** ShipLink — Zero-Login Magic Client Status & Milestone Sign-Off Portal  
> **Phase Constraint:** **100% Frontend / Static Edge MVP (ZERO backend code, ZERO database, ZERO user login required).**  
> **Target Validation Window:** 14 days post-deploy.

---

## 1. Strategic Objectives (3-in-1 Mandate)

1. **Software Architect Showcase:** Demonstrate Linear/Stripe-caliber frontend UX (`Next.js 14`, `TypeScript`, `Tailwind CSS`) paired with an open `/architecture` engineering blueprint (`C4`, `DynamoDB Single-Table`, `EventBridge`, capability-token security) for Principal/Solutions Architect roles.
2. **Consulting Client Portal:** Give Sarwan an immediately usable, branded status-and-sign-off link tool to showcase and use with prospective cloud/AI advisory clients.
3. **Zero-Waste SaaS Smoke Test:** Validate whether freelance developers, agencies, and engineering leads actually create/share links *and* click to reserve a paid Pro tier (`$19/mo Solo · $39/mo Agency · $69 Early-Bird LTD`) before writing backend infrastructure.

---

## 2. Target Personas

| Persona | Core Frustration | What ShipLink Delivers in 10 Seconds |
|---|---|---|
| **P1: Builder / Agency Lead / Consultant** | Clients ignore Jira/Linear links and ask for status updates on Slack/email; creating a portal takes hours. | Zero-signup interactive builder (`/create`) that generates a clean shareable Magic URL (`#d=...`) with milestones, preview URLs, and approval toggles. |
| **P2: Client / CTO / Stakeholder** | Password fatigue; refuses another workspace invite just to check sprint status or sign off a deliverable. | Opens one Magic URL (`/m`) on mobile or desktop with **zero login**, views crisp progress bar + staging previews, and clicks **Approve Milestone** or **Request Change**. |
| **P3: Technical Interviewer / Hiring VP** | Candidates talk about architectures behind NDAs without showing live, shipped, end-to-end production craft. | Visits `/architecture` right inside the live app to inspect C4 diagrams, ADRs, DynamoDB single-table access patterns, and latency/cost telemetry. |

---

## 3. Phase 1 Functional Requirements (Strictly Client-Side / Static)

| ID | Feature | Phase 1 Implementation (`Zero Backend`) |
|---|---|---|
| `FR-01` | **High-Converting Landing Page (`/`)** | Value prop above the fold, interactive live preview widget, 3-step explanation, competitor comparison (*Jira/Email vs Heavy Portals vs ShipLink*), BLUF FAQ, and transparent Pricing / Pro Waitlist triggers. |
| `FR-02` | **10-Second Login-Free Builder (`/create`)** | Instant form with 3 one-click starter templates (*SaaS MVP Sprint*, *Cloud Architecture Audit*, *Design & Launch Retainer*), project metadata, milestone list (add/remove/reorder/status toggle + staging/Figma/PR link), and live split-screen preview. |
| `FR-03` | **Self-Contained Shareable Magic URL (`/m#d=...`)** | Serializes and URL-compresses the project board cleanly into a URL-safe hash payload so generated links open identically across tabs, incognito windows, or any external device with **$0 server database**. Also saves draft history to browser `localStorage` for quick re-editing. |
| `FR-04` | **Zero-Login Client View (`/m`)** | Clean, distraction-free client card showing sender identity, overall `%` completion bar, milestone timeline (`Approved`, `Ready for Review`, `In Progress`, `Planned`), clickable deliverable preview cards, and a clean **"Powered by ShipLink"** footer loop. |
| `FR-05` | **Interactive Sign-Off & Change Request Flow** | Clicking **Approve Milestone** or **Request Change** lets the client optionally attach a short note and generates a **verified timestamped receipt card** + copyable summary text (and updates state cleanly in-session/hash for instant demo testing). |
| `FR-06` | **Pro Smoke-Test Waitlist & Willingness-to-Pay Modal** | Triggered by high-intent actions (*"Auto-Sync GitHub / Linear"*, *"Custom Domain `status.company.com`"*, *"Instant Email/Slack Read Receipts"*, or Pricing CTA). Captures: **Selected Tier (`$19/mo` vs `$39/mo` vs `$69 LTD`)**, **Workflow Integration Needed (`GitHub`, `Linear`, `Jira`, `Figma`)**, and **Work Email**, logged cleanly via client-side Form/Webhook adapter (or local telemetry log ready for Formspree/Web3Forms key drop-in). |
| `FR-07` | **Live Engineering `/architecture` Showcase** | Embedded interactive C4 Container topology, DynamoDB Single-Table entity/access-pattern table, capability-token security comparison, FinOps cost model (`$0` Phase 1 $\rightarrow$ `<$8/mo` Phase 2 AWS), and **"Book an AWS / AI Architecture Audit"** consulting lead card. |

---

## 4. Non-Functional Requirements (`NFR`)

- **`NFR-01` Zero-Cost Hosting:** Pure static Next.js export (`output: 'export'`) deployable free on Vercel, Cloudflare Pages, or GitHub Pages.
- **`NFR-02` Sub-Second First Paint:** Static assets, inline SVG diagrams, zero blocking third-party trackers.
- **`NFR-03` Design QC Baseline:** Body font `>= 14px` (default `15px–16px`), crisp contrast (`>= 4.5:1`), `min-h-0 min-w-0` responsive layout across `375px` mobile and `1440px` desktop, zero horizontal overflow, zero dead `404` links.
- **`NFR-04` AI-Extraction Readiness (Technical GEO):** Semantic HTML5 landmarks, `SoftwareApplication` + `FAQPage` JSON-LD structured data, BLUF answers, and comparison tables on `/`.

---

## 5. Explicit Anti-Scope-Creep Exclusions (Deferred to Phase 2)

Do **NOT** build any of the following until Phase 1 validation clears KPIs:
- AWS Lambda / API Gateway / DynamoDB provisioning
- OAuth login, magic-link email dispatch, or Stripe billing webhooks
- Real GitHub / Linear / Jira webhook consumers
- Multi-tenant custom DNS proxy
