window.THINKLATE_DECKS = window.THINKLATE_DECKS || {};

window.THINKLATE_DECKS["V0"] = {
  id: "V0",
  badge: "VIDEO 00 · ARCHITECT SERIES KICKOFF",
  title: "Staff vs Software vs Solution Architect",
  subtitle: "Why Every Syllabus Looks Identical — How to Pick Your Path & Our Focused 10-Video Software Architect Roadmap (Post-Gate-G2)",
  targetDuration: "8–10 mins",
  excalidrawFile: "decks/v0_architect_roles.excalidraw",
  b1Tags: ["Software Arch vs Solution Arch", "Consultancy", "Business Acumen", "B1-Aligned Roadmap (NDA-Safe)"],
  resources: [
    { label: "Open Native Excalidraw Board (Drag decks/v0_architect_roles.excalidraw)", url: "https://excalidraw.com/" },
    { label: "Mark Richards — Software vs Solution Architect (YT)", url: "https://www.youtube.com/results?search_query=Mark+Richards+Software+Architect+vs+Solution+Architect" },
    { label: "Mike Gibbs — 5 AI Architect Skills (Pq7_EDpQdbA)", url: "https://www.youtube.com/watch?v=Pq7_EDpQdbA" },
    { label: "Hello Interview — System Design in a Hurry", url: "https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction" },
    { label: "Refactoring.Guru — Enterprise Design Patterns", url: "https://refactoring.guru/design-patterns" }
  ],
  slides: [
    {
      type: "hero",
      kicker: "THINKLATE · ENTERPRISE ARCHITECTURE & AI SYSTEMS",
      headline: "Staff vs. Software vs. Solution Architect",
      subhead: "Same technical syllabus. Completely different jobs. Here is how to pick your lane at 8–12+ years of experience — plus the focused 10-video Software Architect roadmap to crack live panels.",
      pills: ["Senior (GCC)", "Software Architect", "Staff Engineer", "Solution Architect", "Principal", "Chief Architect"],
      notes: [
        "HOOK (0:00–0:25): Look up the interview syllabus for Senior Engineer, Staff Engineer, Software Architect, and Solution Architect. Notice something strange? Every single list has the exact same words: Databases, Queues, Caching, Cloud, Microservices, Security, GenAI.",
        "THE TENSION: If the syllabus is 90% identical, why does one role pay 40L while another pays 1 to 3 Crore — and why do great senior developers fail Architect interviews?",
        "PROMISE: In the next 8 minutes, I'll map all 6 roles on one board, show the 4 axes that actually separate them, help you choose your track, and lay out the focused 10-video Software Architect series we're covering next — zero 600-page textbooks needed."
      ],
      tip: "Start calm, clear, and conversational — like talking to a sharp colleague over coffee. Press C anytime to zoom out on the Infinite Canvas!"
    },
    {
      type: "steps",
      kicker: "BOARD 02 · WHY THE SYLLABUS LOOKS IDENTICAL",
      headline: "The Technical Bricks Don't Change — Only 4 Axes Scale",
      items: [
        { num: "01", title: "Blast Radius (Scope)", desc: "1 service/feature → 1 application → multiple business systems → entire engineering org → company-wide governance." },
        { num: "02", title: "Code vs. Decision Ratio", desc: "Engineers are paid to build & deploy (80% code). Architects are paid for decisions, trade-offs, risk & ROI (40% → 0% daily code)." },
        { num: "03", title: "Ambiguity Level", desc: "Solving a defined Jira ticket vs. turning 'Launch an MVP in 6 months under budget & compliance' into a defensible architecture." },
        { num: "04", title: "The Company Naming Trap", desc: "Product companies & FAANG use Senior → Staff → Principal. Enterprises, GCCs & consultancies use Lead → Software → Solution → Chief Architect." }
      ],
      notes: [
        "Key punchline: There is no secret 'Chief Architect-only database'. Every title uses the same technical bricks.",
        "Highlight Axis 2 (Mike Gibbs insight): Engineers ask 'How do I code and deploy this?' Architects ask 'Should we build this, what breaks under load, what does it cost, and what risk are we accepting?'",
        "Highlight Axis 4: Don't get tricked by titles — Staff Engineer (Product) and Software Architect (GCC/Enterprise) are cousins at the same influence level."
      ],
      tip: "Toggle the Pen/Highlighter tool (P) to circle 'Decisions, Trade-Offs, Risk & ROI' live while speaking!"
    },
    {
      type: "matrix",
      kicker: "BOARD 03 · THE 6-ROLE REALITY MAP",
      headline: "Side-by-Side: What Each Title Actually Owns & Interviews For",
      headers: ["Title", "Company Type", "Blast Radius", "Code / Strategy", "What Interviews Actually Test"],
      rows: [
        ["Senior Engineer", "All (incl. GCC)", "1 service / squad", "80% / 20%", "DSA / coding speed + basic HLD/LLD"],
        ["Software Architect", "Enterprise / GCC / Consulting", "1 small–med system", "40% / 60%", "Business case HLD+LLD, NFRs, ADRs, trade-offs"],
        ["Staff Engineer", "Product / FAANG / Remote", "2–4 squads / domain", "50% / 50%", "Coding + Deep HLD/LLD + cross-team RFCs"],
        ["Solution Architect", "GCC / Cloud / Consulting", "Multi-system business", "10% / 90%", "Discovery, cloud cost/ROI, compliance, clients"],
        ["Principal Engineer", "Product / Top GCC", "Whole department", "25% / 75%", "Multi-year technical strategy & org debt"],
        ["Chief Architect", "Enterprise / Banks / C-Suite", "Entire company", "0% / 100%", "Board governance, M&A, budgets, enterprise risk"]
      ],
      notes: [
        "Walk through the 3 sharpest contrasts instead of reading every cell:",
        "1) Senior vs Software Architect: Moving from 'how do I implement this ticket?' to 'what are our FR/NFRs, C4 boundaries, ADRs, and failure risks?'",
        "2) Software Architect vs Solution Architect: Software Architect owns runtime, databases, and component boundaries; Solution Architect zooms out to multi-system integration, CFO cloud costs, CISO security, and client advisory.",
        "3) Principal & Chief Architect (the 1–3 Crore tier): Paid to prevent multi-million-dollar architectural mistakes and align tech directly to revenue."
      ],
      tip: "Highlight the Software Architect and Solution Architect rows — those two overlap ~80% in external GCC hiring."
    },
    {
      type: "mermaid",
      kicker: "BOARD 04 · TWO PARALLEL CAREER LADDERS",
      headline: "Product IC Track vs. Enterprise / GCC Architect Track",
      diagram: `flowchart LR
    L0["Senior / Lead Engineer<br/>(8–12 YOE)"] --> P1["Staff Engineer<br/>(Product / Startups)"]
    P1 --> P2["Principal Engineer<br/>(Department Scope)"]
    L0 --> A1["Software Architect<br/>(System Scope / B1)"]
    A1 --> A2["Solution Architect<br/>(Business + Cloud + AI)"]
    A2 --> A3["Chief / Enterprise Architect<br/>(2–3 Cr GCC / C-Suite)"]
    A2 -.-> C1["Independent Consulting<br/>& Architecture Audits"]
    style L0 fill:#eff6ff,stroke:#2563eb,stroke-width:2px,color:#0f172a
    style P1 fill:#f0f9ff,stroke:#0284c7,stroke-width:2px,color:#0f172a
    style P2 fill:#f0f9ff,stroke:#0284c7,stroke-width:2px,color:#0f172a
    style A1 fill:#ecfdf5,stroke:#059669,stroke-width:2.5px,color:#0f172a
    style A2 fill:#ecfdf5,stroke:#059669,stroke-width:2.5px,color:#0f172a
    style A3 fill:#fffbeb,stroke:#d97706,stroke-width:2.5px,color:#0f172a
    style C1 fill:#fff1f2,stroke:#e11d48,stroke-width:2px,stroke-dasharray: 5 5,color:#0f172a`,
      caption: "Once you earn Software Architect, you unlock BOTH external Solution Architect roles and Staff Backend interviews.",
      notes: [
        "Show the fork clearly at 8–12 YOE: every senior engineer has BOTH ladders open.",
        "Top track (Product IC): Stay deep in code, build core infra, target product startups & remote Staff/Principal roles.",
        "Bottom track (Architect → Consulting): Start at Software Architect (mastering 1 system cleanly) → expand to Solution Architect (multi-system, cloud cost, AI, compliance) → scale into Chief Architect & fractional consulting.",
        "Key insight: You don't have to pick forever on Day 1 — Software Architect is the universal bridge."
      ],
      tip: "Use smooth zoom or laser pointer (L) to trace the green bottom lane."
    },
    {
      type: "tradeoff",
      kicker: "BOARD 05 · CHOOSING YOUR LANE",
      headline: "Track 1 (Solution/Chief Architect) vs. Track 2 (Staff/Principal)",
      leftTitle: "Track 1: Software → Solution → Chief Architect",
      leftTag: "BUSINESS · CLOUD · AI · CONSULTING",
      leftColor: "emerald",
      leftPoints: [
        "Connects architecture decisions directly to ROI, cloud bills, compliance & risk",
        "Interviews reward live business-case HLD/LLD & trade-offs over LeetCode speed",
        "Direct path to Tier-1 GCCs, cloud vendors, Chief Architect & consulting",
        "Trade-Off: Less daily coding as you climb; higher stakeholder & politics load"
      ],
      rightTitle: "Track 2: Senior → Staff → Principal Engineer",
      rightTag: "HANDS-ON CODE · DEEP INFRASTRUCTURE",
      rightColor: "blue",
      rightPoints: [
        "Stay hands-on shipping critical production code, RFCs & core frameworks",
        "Top compensation ceiling at global remote product startups & FAANG",
        "Technical authority earned directly through code reviews & systems shipped",
        "Trade-Off: Tougher DSA + machine-coding filters during every job switch"
      ],
      notes: [
        "Be transparent and grounded: neither track is 'better' — pick the one that matches your natural energy.",
        "Add the 2026 macro reality (1–2 lines): As AI makes writing boilerplate code cheap, BOTH tracks get paid MORE for the exact same reason — companies desperately need humans who own system architecture, security, compliance, and cloud/AI cost.",
        "Own your lane openly: On this channel, we're focusing on the Architect & AI Systems decision path (Track 1) — practical, enterprise-grade, zero syntax tutorials."
      ],
      tip: "Speak the AI macro line slowly and clearly — it's the emotional anchor of the whole video."
    },
    {
      type: "roadmap",
      kicker: "BOARD 06 · FOCUSED SOFTWARE ARCHITECT SERIES (V1 → V10)",
      headline: "The 10-Video Software Architect Roadmap (Zero Textbook Fluff)",
      acts: [
        {
          label: "ACT I · HLD PROCESS, STYLES & APIS",
          range: "V1 → V3",
          color: "blue",
          items: [
            { id: "V1", title: "6-Month MVP HLD From Scratch", sub: "FR/NFR, SLA/cost math, minimal C4 & ADRs" },
            { id: "V2", title: "Monolith to Event-Driven Styles", sub: "Modular Monolith, Layered, Microservices, EDA, Microkernel" },
            { id: "V3", title: "Sync vs Async APIs & Queues", sub: "REST, Webhooks, Idempotency, Outbox, SQS & DLQ" }
          ]
        },
        {
          label: "ACT II · DATA, LLD, CLOUD & SECURITY",
          range: "V4 → V6",
          color: "emerald",
          items: [
            { id: "V4", title: "SQL vs DynamoDB at Scale", sub: "Indexes, 5 isolation anomalies, keys, sharding & CQRS" },
            { id: "V5", title: "LLD, Concurrency & Fault Tolerance", sub: "Rule Engine/State LLD, locks, Bulkheads, Canary/Flags" },
            { id: "V6", title: "AWS VPC, OAuth2 & STRIDE Security", sub: "Private subnets, VPC Endpoints, OIDC/PKCE, Valet Key" }
          ]
        },
        {
          label: "ACT III · MIGRATION & GENAI FUNDAMENTALS",
          range: "V7 → V8",
          color: "amber",
          items: [
            { id: "V7", title: "DDD & Strangler Fig Modernization", sub: "Bounded Contexts, ACL, Cloud 6 Rs & CDC cutover" },
            { id: "V8", title: "GenAI Architecture for Architects", sub: "Prompting vs RAG vs Fine-Tuning, ACL-RAG, PII & ROI" }
          ]
        },
        {
          label: "ACT IV · LIVE WORKSHOP & FULL MOCK",
          range: "V9 → V10",
          color: "rose",
          items: [
            { id: "V9", title: "Leading a 40-Min Live Workshop", sub: "5 discovery Qs, live logs, CTO/CFO/CISO/PO curveballs" },
            { id: "V10", title: "End-to-End Original Mock Design", sub: "Full timed walkthrough on an original public scenario" }
          ]
        }
      ],
      notes: [
        "SERIES PROMISE: You do NOT need 100% mastery of 600-page textbooks to crack Software Architect panels. You need the repeatable HLD process and core decision trade-offs across these 10 focused topics.",
        "WALK ALL 4 ACTS IN ONE CLEAN GLANCE (35–45 seconds total):",
        "• Act I (V1–V3): The 6-step MVP HLD process, core architectural styles, and sync/async integration patterns.",
        "• Act II (V4–V6): Production depth — SQL/DynamoDB, Rule-Engine/State LLD & fault tolerance, and AWS VPC/OAuth2/STRIDE security.",
        "• Act III (V7–V8): DDD/Strangler Fig legacy modernization and practical governed GenAI architecture.",
        "• Act IV (V9–V10): Leading a live 40-minute stakeholder workshop plus a complete timed end-to-end mock on an original public scenario."
      ],
      tip: "Use the Laser Pointer (L) to sweep clockwise across Act I → Act II → Act III → Act IV in 40 seconds flat. (Note: Gate G2 — record publicly only after B1 result; 100% original non-confidential examples only.)"
    },
    {
      type: "hero",
      kicker: "BOARD 07 · NEXT UP — VIDEO 01",
      headline: "80/20 Decisions. Zero Textbook Fluff.",
      subhead: "Up Next in V1: A panel of 3 Senior Architects hands you a blank whiteboard — 'Launch a new business platform from scratch in 6 months.' Let's design the FRs, NFRs, HLD, LLD, and trade-offs step-by-step.",
      pills: ["Next: V1 (6-Month MVP Case)", "Free Diagrams + ADRs", "Own Your Decisions"],
      notes: [
        "CLEAN CLOSE (15 seconds): You don't need to memorize every AWS service or read 10 textbooks to become an Architect. Master the repeatable HLD process and core decision trade-offs across these 10 videos, practice defending them out loud, and build real proof.",
        "OPEN LOOP INTO V1: Next up in Video 1, we walk through the exact live case study Architect panels love to start with — building a greenfield platform with a hard 6-month MVP deadline. See you in V1."
      ],
      tip: "End sharp and confident. Zero 'smash the bell icon' filler!"
    }
  ]
};
