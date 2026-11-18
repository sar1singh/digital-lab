'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import {
  ArrowRight,
  Cpu,
  Database,
  DollarSign,
  ExternalLink,
  Layers,
  Lock,
  Server,
  ShieldCheck,
} from 'lucide-react';
import { Navbar } from '@/components/Navbar';
import { Footer } from '@/components/Footer';
import { WaitlistModal } from '@/components/WaitlistModal';
import { WaitlistLead } from '@/lib/shiplink';

export default function ArchitecturePage() {
  const [phaseView, setPhaseView] = useState<'phase2' | 'phase1'>('phase2');
  const [waitlistOpen, setWaitlistOpen] = useState(false);
  const [waitlistTier, setWaitlistTier] = useState<WaitlistLead['tier']>('audit-consult');

  const openAuditModal = (tier: WaitlistLead['tier'] = 'audit-consult') => {
    setWaitlistTier(tier);
    setWaitlistOpen(true);
  };

  return (
    <>
      <Navbar onOpenWaitlist={(t) => openAuditModal(t)} />

      <main className="flex-1 max-w-6xl w-full mx-auto px-4 sm:px-6 py-10 sm:py-14 space-y-12">
        {/* Header */}
        <section className="space-y-4 border-b border-slate-200 pb-8">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-900 text-indigo-300 text-xs font-mono font-semibold">
            <Cpu className="w-3.5 h-3.5" />
            <span>SYSTEM ARCHITECTURE &amp; ADRs · BY SARWAN SINGH</span>
          </div>
          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6">
            <div className="space-y-3 max-w-3xl">
              <h1 className="font-display text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
                How ShipLink Scales from $0 Validation to AWS Event-Driven Serverless
              </h1>
              <p className="text-[16px] text-slate-600 leading-relaxed">
                Designed around strict FinOps and Capability-URL security: validate demand at{' '}
                <strong className="text-slate-900">$0.00/mo</strong> on the static edge before
                activating <strong className="text-slate-900">API Gateway, Lambda, EventBridge,</strong>{' '}
                and <strong className="text-slate-900">DynamoDB Single-Table</strong>.
              </p>
            </div>
            <button
              type="button"
              onClick={() => openAuditModal('audit-consult')}
              className="inline-flex items-center justify-center gap-2 px-5 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-[15px] font-semibold shadow-sm flex-shrink-0 transition"
            >
              <span>Book Architecture Audit</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </section>

        {/* Interactive C4 Container Topology */}
        <section className="space-y-5">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 className="font-display text-2xl font-bold text-slate-900">
                C4 Container Architecture
              </h2>
              <p className="text-[15px] text-slate-600">
                Toggle between the live Phase 1 Edge build and target Phase 2 AWS Serverless stack.
              </p>
            </div>
            <div className="inline-flex p-1 rounded-xl bg-slate-200/70 border border-slate-200">
              <button
                type="button"
                onClick={() => setPhaseView('phase1')}
                className={`px-4 py-2 rounded-lg text-sm font-semibold transition ${
                  phaseView === 'phase1'
                    ? 'bg-white text-slate-900 shadow-sm'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                Phase 1: $0 Static Edge
              </button>
              <button
                type="button"
                onClick={() => setPhaseView('phase2')}
                className={`px-4 py-2 rounded-lg text-sm font-semibold transition ${
                  phaseView === 'phase2'
                    ? 'bg-white text-slate-900 shadow-sm'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                Phase 2: AWS Serverless
              </button>
            </div>
          </div>

          <div className="rounded-2xl bg-[#0B0F19] border border-slate-800 p-6 sm:p-8 text-slate-100 overflow-x-auto">
            {phaseView === 'phase1' ? (
              <div className="space-y-6 min-w-[640px]">
                <div className="flex items-center justify-between text-xs font-mono text-emerald-400">
                  <span>ACTIVE NOW · PHASE 1 ($0.00/MO)</span>
                  <span>Zero DB · Zero Server PII · Zero Cold Start</span>
                </div>
                <div className="grid grid-cols-3 gap-5 items-center">
                  <div className="p-5 rounded-xl bg-slate-900 border border-slate-700 space-y-2">
                    <div className="text-xs font-mono text-indigo-400">BUILDER BROWSER</div>
                    <div className="font-display font-bold text-white">/create Studio</div>
                    <p className="text-sm text-slate-300">
                      Serializes milestones to URL-safe Base64 inside fragment{' '}
                      <code className="text-emerald-300">#d=...</code> + local draft backup.
                    </p>
                  </div>
                  <div className="p-5 rounded-xl bg-indigo-950/60 border border-indigo-700/70 space-y-2 text-center">
                    <div className="text-xs font-mono text-indigo-300">STATIC EDGE CDN</div>
                    <div className="font-display font-bold text-white">Next.js Static Export</div>
                    <p className="text-sm text-slate-300">
                      Serves pure HTML/JS/CSS globally (&lt;40ms TTFB). Fragment hash never hits
                      server access logs.
                    </p>
                  </div>
                  <div className="p-5 rounded-xl bg-slate-900 border border-emerald-700/60 space-y-2">
                    <div className="text-xs font-mono text-emerald-400">CLIENT BROWSER</div>
                    <div className="font-display font-bold text-white">/m Magic Card</div>
                    <p className="text-sm text-slate-300">
                      Decodes capability payload locally, renders mobile progress &amp; generates
                      copyable sign-off receipt.
                    </p>
                  </div>
                </div>
              </div>
            ) : (
              <div className="space-y-6 min-w-[700px]">
                <div className="flex items-center justify-between text-xs font-mono text-indigo-400">
                  <span>PHASE 2 PRODUCTION BLUEPRINT · &lt;$6.50/MO @ 50K VIEWS</span>
                  <span>Node.js 20 · TypeScript · AWS CDK</span>
                </div>
                <div className="grid grid-cols-4 gap-4 items-stretch">
                  <div className="p-4 rounded-xl bg-slate-900 border border-slate-700 space-y-2">
                    <div className="text-xs font-mono text-amber-300">EVENT SOURCES</div>
                    <div className="font-display font-bold text-white">GitHub / Linear / UI</div>
                    <p className="text-sm text-slate-300">
                      HMAC-SHA256 signed webhooks + Client Approve mutations via HTTP API Gateway.
                    </p>
                  </div>
                  <div className="p-4 rounded-xl bg-slate-900 border border-indigo-700/70 space-y-2">
                    <div className="text-xs font-mono text-indigo-400">ASYNC BACKBONE</div>
                    <div className="font-display font-bold text-white">EventBridge + SQS DLQ</div>
                    <p className="text-sm text-slate-300">
                      Returns <code className="text-emerald-300">202 Accepted</code> in &lt;50ms;
                      decouples webhook normalization &amp; fan-out retries.
                    </p>
                  </div>
                  <div className="p-4 rounded-xl bg-slate-900 border border-emerald-700/70 space-y-2">
                    <div className="text-xs font-mono text-emerald-400">STORAGE</div>
                    <div className="font-display font-bold text-white">DynamoDB Single-Table</div>
                    <p className="text-sm text-slate-300">
                      SHA-256 token lookup + atomic <code className="text-emerald-300">TransactWrite</code>{' '}
                      sign-off audit trail + Streams.
                    </p>
                  </div>
                  <div className="p-4 rounded-xl bg-slate-900 border border-slate-700 space-y-2">
                    <div className="text-xs font-mono text-sky-400">RECEIPTS</div>
                    <div className="font-display font-bold text-white">SES + Slack Block Kit</div>
                    <p className="text-sm text-slate-300">
                      Triggered on DynamoDB Stream approval events for instant creator receipts.
                    </p>
                  </div>
                </div>
              </div>
            )}
          </div>
        </section>

        {/* DynamoDB Single-Table Access Patterns */}
        <section className="space-y-4">
          <div className="flex items-center gap-2.5">
            <Database className="w-5 h-5 text-indigo-600" />
            <h2 className="font-display text-2xl font-bold text-slate-900">
              DynamoDB Single-Table Access Patterns (Zero Joins · &lt;10ms Point Reads)
            </h2>
          </div>
          <div className="overflow-x-auto rounded-2xl border border-slate-200 bg-white">
            <table className="w-full text-left border-collapse text-[15px]">
              <thead className="bg-slate-50 border-b border-slate-200 text-slate-700">
                <tr>
                  <th className="py-3 px-4 font-bold">Entity</th>
                  <th className="py-3 px-4 font-bold">PK</th>
                  <th className="py-3 px-4 font-bold">SK</th>
                  <th className="py-3 px-4 font-bold">GSI1PK / GSI1SK</th>
                  <th className="py-3 px-4 font-bold">Primary Query</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200 font-mono text-sm">
                <tr>
                  <td className="py-3 px-4 font-sans font-semibold text-slate-900">
                    Magic Capability Token
                  </td>
                  <td className="py-3 px-4 text-indigo-700">TOKEN#&lt;sha256&gt;</td>
                  <td className="py-3 px-4 text-slate-700">LINK</td>
                  <td className="py-3 px-4 text-slate-600">BOARD#&lt;id&gt; / TOKEN#&lt;scope&gt;</td>
                  <td className="py-3 px-4 font-sans text-slate-600">
                    Validate unguessable token + scope in 1 GetItem
                  </td>
                </tr>
                <tr>
                  <td className="py-3 px-4 font-sans font-semibold text-slate-900">
                    Board + Milestones
                  </td>
                  <td className="py-3 px-4 text-indigo-700">BOARD#&lt;id&gt;</td>
                  <td className="py-3 px-4 text-slate-700">META | MS#01#&lt;id&gt;</td>
                  <td className="py-3 px-4 text-slate-600">WS#&lt;ws&gt; / BOARD#&lt;ts&gt;</td>
                  <td className="py-3 px-4 font-sans text-slate-600">
                    1 partition Query returns full client card
                  </td>
                </tr>
                <tr>
                  <td className="py-3 px-4 font-sans font-semibold text-slate-900">
                    Immutable Audit Trail
                  </td>
                  <td className="py-3 px-4 text-indigo-700">BOARD#&lt;id&gt;</td>
                  <td className="py-3 px-4 text-slate-700">AUDIT#&lt;iso&gt;#&lt;uuid&gt;</td>
                  <td className="py-3 px-4 text-slate-600">—</td>
                  <td className="py-3 px-4 font-sans text-slate-600">
                    Atomic TransactWrite on Approve click
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        {/* 4 ADRs */}
        <section className="space-y-4">
          <div className="flex items-center gap-2.5">
            <Layers className="w-5 h-5 text-indigo-600" />
            <h2 className="font-display text-2xl font-bold text-slate-900">
              Architecture Decision Records (ADRs)
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <article className="p-6 rounded-2xl bg-white border border-slate-200 space-y-2.5">
              <div className="flex items-center justify-between">
                <span className="font-mono text-xs font-bold text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded">
                  ADR-001 · SECURITY
                </span>
                <Lock className="w-4 h-4 text-slate-400" />
              </div>
              <h3 className="font-display text-lg font-bold text-slate-900">
                SHA-256 Capability URLs over Email OTP Sessions
              </h3>
              <p className="text-[15px] text-slate-600 leading-relaxed">
                OTP magic logins break when a CTO forwards a link to a VP in Slack. High-entropy
                128-bit+ capability tokens stored exclusively as SHA-256 hashes enable instant link
                forwarding, scoped permissions, and single-click revocation.
              </p>
            </article>

            <article className="p-6 rounded-2xl bg-white border border-slate-200 space-y-2.5">
              <div className="flex items-center justify-between">
                <span className="font-mono text-xs font-bold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded">
                  ADR-002 · FINOPS
                </span>
                <DollarSign className="w-4 h-4 text-slate-400" />
              </div>
              <h3 className="font-display text-lg font-bold text-slate-900">
                Fragment-Encoded Client State for $0 Phase 1 Validation
              </h3>
              <p className="text-[15px] text-slate-600 leading-relaxed">
                Serializing prototype state into URL fragments (<code className="font-mono">#d=</code>
                ) guarantees $0/mo cloud cost and zero server PII exposure during the 14-day market
                smoke test before provisioning AWS infrastructure.
              </p>
            </article>

            <article className="p-6 rounded-2xl bg-white border border-slate-200 space-y-2.5">
              <div className="flex items-center justify-between">
                <span className="font-mono text-xs font-bold text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded">
                  ADR-003 · STORAGE
                </span>
                <Server className="w-4 h-4 text-slate-400" />
              </div>
              <h3 className="font-display text-lg font-bold text-slate-900">
                DynamoDB On-Demand Single-Table over Managed RDS
              </h3>
              <p className="text-[15px] text-slate-600 leading-relaxed">
                Point lookups and per-board milestone timelines require zero relational joins.
                DynamoDB eliminates RDS idle minimums (~$15–$50/mo) and connection-pool exhaustion
                under viral traffic spikes.
              </p>
            </article>

            <article className="p-6 rounded-2xl bg-white border border-slate-200 space-y-2.5">
              <div className="flex items-center justify-between">
                <span className="font-mono text-xs font-bold text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded">
                  ADR-004 · RESILIENCE
                </span>
                <ShieldCheck className="w-4 h-4 text-slate-400" />
              </div>
              <h3 className="font-display text-lg font-bold text-slate-900">
                EventBridge Async Webhook Fan-Out with SQS DLQ
              </h3>
              <p className="text-[15px] text-slate-600 leading-relaxed">
                GitHub and Linear enforce tight webhook timeouts. Verifying HMAC signatures upfront
                and emitting normalized domain events to EventBridge keeps ingestion &lt;50ms with
                durable DLQ retries.
              </p>
            </article>
          </div>
        </section>

        {/* Bottom Consulting & Portfolio CTA */}
        <section className="rounded-2xl bg-indigo-50 border border-indigo-200 p-6 sm:p-8 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
          <div className="space-y-2 max-w-2xl">
            <h2 className="font-display text-xl sm:text-2xl font-bold text-slate-900">
              Need an AWS Serverless, Node.js, or AI Agent Architecture Review?
            </h2>
            <p className="text-[15px] text-slate-700 leading-relaxed">
              Built by <strong>Sarwan Singh</strong> — 10+ yrs architecting production platforms at
              EPAM Systems (Cox Automotive), Niyo Solutions, and MediaAgility.
            </p>
          </div>
          <div className="flex flex-wrap gap-3 flex-shrink-0">
            <button
              type="button"
              onClick={() => openAuditModal('audit-consult')}
              className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-[15px] font-semibold transition"
            >
              <span>Request Architecture Audit</span>
            </button>
            <Link
              href="/create"
              className="inline-flex items-center gap-1.5 px-5 py-3 rounded-xl bg-white hover:bg-slate-50 text-slate-800 border border-slate-300 text-[15px] font-semibold transition"
            >
              <span>Try Live Builder</span>
              <ExternalLink className="w-4 h-4" />
            </Link>
          </div>
        </section>
      </main>

      <Footer />

      <WaitlistModal
        open={waitlistOpen}
        initialTier={waitlistTier}
        triggerContext="AWS / AI Architecture Audit & System Review"
        onClose={() => setWaitlistOpen(false)}
      />
    </>
  );
}
