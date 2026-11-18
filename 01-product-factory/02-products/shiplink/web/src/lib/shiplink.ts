export type MilestoneStatus = 'approved' | 'in_review' | 'in_progress' | 'planned';

export type AccentTheme = 'indigo' | 'emerald' | 'slate';

export interface MilestoneItem {
  id: string;
  title: string;
  status: MilestoneStatus;
  summary: string;
  linkLabel?: string;
  linkUrl?: string;
  approvedAt?: string;
  clientNote?: string;
}

export interface ShipLinkBoard {
  v: 1;
  id: string;
  projectTitle: string;
  clientName: string;
  senderName: string;
  targetDate: string;
  overviewNote: string;
  accent: AccentTheme;
  updatedAt: string;
  milestones: MilestoneItem[];
}

export interface WaitlistLead {
  id: string;
  email: string;
  tier: 'solo-19' | 'team-39' | 'ltd-69' | 'audit-consult';
  integration: string;
  notes?: string;
  createdAt: string;
}

export const PRESET_BOARDS: Record<'sprint' | 'audit' | 'retainer', ShipLinkBoard> = {
  sprint: {
    v: 1,
    id: 'sl-mvp-01',
    projectTitle: 'Checkout Microservice & Partner API v2',
    clientName: 'Apex Retail Ops',
    senderName: 'Sarwan Labs',
    targetDate: 'Dec 04, 2026',
    overviewNote:
      'Milestone 2 staging endpoint is live with idempotent webhook handling. Please test the checkout sandbox link below and click Approve to unlock Milestone 3 rollout.',
    accent: 'indigo',
    updatedAt: 'Nov 18, 2026 · 10:15 PM IST',
    milestones: [
      {
        id: 'm1',
        title: 'API Contract & DynamoDB Schema Lock',
        status: 'approved',
        summary:
          'Single-table partition keys, OpenAPI 3.1 contracts, and SQS dead-letter retry policy finalized.',
        linkLabel: 'View Spec Sheet',
        linkUrl: 'https://example.com/api-spec',
        approvedAt: 'Nov 12, 2026',
      },
      {
        id: 'm2',
        title: 'Idempotent Webhook & Sandbox Staging',
        status: 'in_review',
        summary:
          'Deployed Node.js/TypeScript Lambda worker with Stripe & partner webhook signature verification. Ready for stakeholder sign-off.',
        linkLabel: 'Open Staging Demo',
        linkUrl: 'https://example.com/staging-demo',
      },
      {
        id: 'm3',
        title: 'Load Testing & CloudWatch Canary Alerts',
        status: 'in_progress',
        summary:
          'Running 2,500 RPS artillery burst simulation and configuring P95 latency alarms.',
      },
      {
        id: 'm4',
        title: 'Production Cutover & Runbook Handoff',
        status: 'planned',
        summary:
          'Zero-downtime DNS cutover, rollback runbook, and engineering team walkthrough.',
      },
    ],
  },
  audit: {
    v: 1,
    id: 'sl-audit-02',
    projectTitle: 'AWS Serverless & AI Agent FinOps Audit',
    clientName: 'FinStack Series-A Team',
    senderName: 'Sarwan Architecture Advisory',
    targetDate: 'Nov 25, 2026',
    overviewNote:
      'Completed telemetry teardown across Lambda cold starts and LLM prompt caching. Review the 42% monthly AWS cost reduction blueprint in Milestone 2.',
    accent: 'emerald',
    updatedAt: 'Nov 18, 2026 · 09:40 PM IST',
    milestones: [
      {
        id: 'a1',
        title: 'CloudWatch & Token Burn Telemetry Baseline',
        status: 'approved',
        summary:
          'Audited 14 microservices and identified 3 uncached LLM context loops driving 58% of monthly spend.',
        approvedAt: 'Nov 15, 2026',
      },
      {
        id: 'a2',
        title: 'C4 Target Blueprint & FinOps Patch Plan',
        status: 'in_review',
        summary:
          'Delivered prioritized remediation roadmap: EventBridge batching, ARM64 Graviton Lambdas, and prompt prefix caching.',
        linkLabel: 'Inspect Blueprint',
        linkUrl: 'https://example.com/finops-audit',
      },
      {
        id: 'a3',
        title: 'PR Implementation & Guardrail Rollout',
        status: 'in_progress',
        summary:
          'Applying circuit-breaker middleware and budget alarms across staging cluster.',
      },
    ],
  },
  retainer: {
    v: 1,
    id: 'sl-ret-03',
    projectTitle: 'Q4 Product Launch Landing & Motion Pack',
    clientName: 'Kinetix SaaS',
    senderName: 'ThinkLate Studio',
    targetDate: 'Nov 29, 2026',
    overviewNote:
      'Hero landing layout and 45-second product walkthrough cut are ready for review. Leave a note directly on Milestone 2 if copy tweaks are needed.',
    accent: 'slate',
    updatedAt: 'Nov 18, 2026 · 08:20 PM IST',
    milestones: [
      {
        id: 'r1',
        title: 'Positioning Narrative & Wireframe Flow',
        status: 'approved',
        summary: 'Approved hero hook, interactive preview block, and comparison matrix.',
        approvedAt: 'Nov 10, 2026',
      },
      {
        id: 'r2',
        title: 'Staging Landing Page + 45s Launch Cut',
        status: 'in_review',
        summary: 'Responsive Next.js staging preview and mastered 1080p launch video ready for final look.',
        linkLabel: 'Preview Build',
        linkUrl: 'https://example.com/launch-preview',
      },
      {
        id: 'r3',
        title: 'Analytics Tags & Production Launch',
        status: 'planned',
        summary: 'Wire conversion tracking events and deploy to primary edge domain.',
      },
    ],
  },
};

export function encodeBoardToHash(board: ShipLinkBoard): string {
  const json = JSON.stringify(board);
  const bytes = new TextEncoder().encode(json);
  let binary = '';
  for (let i = 0; i < bytes.length; i += 1) {
    binary += String.fromCharCode(bytes[i]);
  }
  const b64 = btoa(binary).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  return `d=${b64}`;
}

export function decodeBoardFromHash(hashString: string): ShipLinkBoard | null {
  try {
    const clean = hashString.replace(/^#/, '');
    if (!clean.startsWith('d=')) return null;
    const raw = clean.slice(2);
    if (!raw) return null;
    const padded = raw.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((raw.length + 3) % 4);
    const binary = atob(padded);
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i += 1) {
      bytes[i] = binary.charCodeAt(i);
    }
    const json = new TextDecoder().decode(bytes);
    const parsed = JSON.parse(json) as Partial<ShipLinkBoard>;
    if (!parsed || parsed.v !== 1 || !Array.isArray(parsed.milestones) || !parsed.projectTitle) {
      return null;
    }
    return parsed as ShipLinkBoard;
  } catch {
    return null;
  }
}

export function computeCompletion(board: ShipLinkBoard): {
  total: number;
  approved: number;
  inReview: number;
  inProgress: number;
  percent: number;
} {
  const total = board.milestones.length;
  if (total === 0) {
    return { total: 0, approved: 0, inReview: 0, inProgress: 0, percent: 0 };
  }
  const approved = board.milestones.filter((m) => m.status === 'approved').length;
  const inReview = board.milestones.filter((m) => m.status === 'in_review').length;
  const inProgress = board.milestones.filter((m) => m.status === 'in_progress').length;
  // Approved counts full weight, In Review counts half progress so clients see momentum accurately
  const weighted = approved + inReview * 0.5 + inProgress * 0.25;
  const percent = Math.min(100, Math.round((weighted / total) * 100));
  return { total, approved, inReview, inProgress, percent };
}

const DRAFTS_KEY = 'shiplink_drafts_v1';
const WAITLIST_KEY = 'shiplink_waitlist_v1';

export function saveBoardDraft(board: ShipLinkBoard): void {
  if (typeof window === 'undefined') return;
  try {
    const existing = loadBoardDrafts().filter((b) => b.id !== board.id);
    const updated = [board, ...existing].slice(0, 8);
    window.localStorage.setItem(DRAFTS_KEY, JSON.stringify(updated));
  } catch {
    // Ignore storage quota errors in private browsing
  }
}

export function loadBoardDrafts(): ShipLinkBoard[] {
  if (typeof window === 'undefined') return [];
  try {
    const raw = window.localStorage.getItem(DRAFTS_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

export function saveWaitlistLead(lead: WaitlistLead): void {
  if (typeof window === 'undefined') return;
  try {
    const raw = window.localStorage.getItem(WAITLIST_KEY);
    const existing: WaitlistLead[] = raw ? JSON.parse(raw) : [];
    window.localStorage.setItem(WAITLIST_KEY, JSON.stringify([lead, ...existing].slice(0, 20)));
  } catch {
    // Ignore storage quota errors
  }
}
