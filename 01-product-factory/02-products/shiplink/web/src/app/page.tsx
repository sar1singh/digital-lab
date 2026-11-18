'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import {
  ArrowRight,
  Check,
  CheckCircle2,
  Clock,
  Code2,
  GitPullRequest,
  Globe,
  Link2,
  LockOpen,
  MessageSquareOff,
  ShieldCheck,
  Sparkles,
  Zap,
} from 'lucide-react';
import { Navbar } from '@/components/Navbar';
import { Footer } from '@/components/Footer';
import { WaitlistModal } from '@/components/WaitlistModal';
import { PRESET_BOARDS, WaitlistLead } from '@/lib/shiplink';
import { ClientBoardPreview } from '@/components/ClientBoardPreview';

export default function HomePage() {
  const [comparisonView, setComparisonView] = useState<'shiplink' | 'chaos'>('shiplink');
  const [waitlistOpen, setWaitlistOpen] = useState(false);
  const [waitlistTier, setWaitlistTier] = useState<WaitlistLead['tier']>('solo-19');
  const [waitlistContext, setWaitlistContext] = useState<string | undefined>(undefined);

  const openWaitlist = (tier: WaitlistLead['tier'] = 'solo-19', context?: string) => {
    setWaitlistTier(tier);
    setWaitlistContext(context);
    setWaitlistOpen(true);
  };

  return (
    <>
      <Navbar onOpenWaitlist={(t) => openWaitlist(t)} />

      <main className="flex-1">
        {/* HERO SECTION */}
        <section className="relative border-b border-slate-200 bg-white bg-architect-grid overflow-hidden">
          <div className="max-w-6xl mx-auto px-4 sm:px-6 py-14 sm:py-20 grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
            <div className="lg:col-span-6 space-y-6 min-w-0">
              <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-700 text-sm font-semibold">
                <LockOpen className="w-4 h-4" />
                <span>Zero client logins · Build &amp; send in 10 seconds</span>
              </div>

              <h1 className="font-display text-4xl sm:text-5xl font-extrabold tracking-tight text-slate-900 leading-[1.12]">
                Share client progress with{' '}
                <span className="text-indigo-600">one magic link</span>. Skip the portal passwords.
              </h1>

              <p className="text-[16px] sm:text-lg text-slate-600 leading-relaxed max-w-xl">
                Clients ignore Jira invites and heavy dashboards. Spin up a crisp milestone &amp;
                sign-off link in 10 seconds—clients view live progress, inspect staging previews,
                and click <strong className="text-slate-900">Approve</strong> with zero login
                friction.
              </p>

              <div className="flex flex-wrap items-center gap-3.5 pt-1">
                <Link
                  href="/create"
                  className="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-[15px] font-semibold shadow-sm shadow-indigo-600/25 transition min-h-[48px]"
                >
                  <span>Create Free Magic Link</span>
                  <ArrowRight className="w-4 h-4" />
                </Link>
                <Link
                  href="/m"
                  className="inline-flex items-center justify-center gap-2 px-5 py-3.5 rounded-xl bg-white hover:bg-slate-50 text-slate-800 border border-slate-300 text-[15px] font-semibold transition min-h-[48px]"
                >
                  <span>Open Live Client Demo</span>
                </Link>
              </div>

              <div className="flex flex-wrap items-center gap-x-6 gap-y-2 pt-2 text-sm text-slate-600">
                <span className="inline-flex items-center gap-1.5">
                  <Check className="w-4 h-4 text-emerald-600" />
                  <span>No signup required</span>
                </span>
                <span className="inline-flex items-center gap-1.5">
                  <Check className="w-4 h-4 text-emerald-600" />
                  <span>Mobile-ready sign-off</span>
                </span>
                <span className="inline-flex items-center gap-1.5">
                  <Check className="w-4 h-4 text-emerald-600" />
                  <span>Open AWS / C4 architecture</span>
                </span>
              </div>
            </div>

            {/* Right Hero: Interactive Before/After Switcher */}
            <div className="lg:col-span-6 space-y-3 min-w-0">
              <div className="inline-flex p-1 rounded-xl bg-slate-100 border border-slate-200 w-full sm:w-auto">
                <button
                  type="button"
                  onClick={() => setComparisonView('shiplink')}
                  className={`flex-1 sm:flex-initial px-4 py-2 rounded-lg text-sm font-semibold transition ${
                    comparisonView === 'shiplink'
                      ? 'bg-white text-slate-900 shadow-sm'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  With ShipLink (10s)
                </button>
                <button
                  type="button"
                  onClick={() => setComparisonView('chaos')}
                  className={`flex-1 sm:flex-initial px-4 py-2 rounded-lg text-sm font-semibold transition ${
                    comparisonView === 'chaos'
                      ? 'bg-white text-slate-900 shadow-sm'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  Without ShipLink
                </button>
              </div>

              {comparisonView === 'shiplink' ? (
                <div className="transform transition-all">
                  <ClientBoardPreview board={PRESET_BOARDS.sprint} interactive={false} />
                </div>
              ) : (
                <div className="rounded-2xl bg-slate-900 text-slate-100 border border-slate-800 p-6 sm:p-7 space-y-4 shadow-lg">
                  <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                    <span className="font-mono text-sm text-rose-400 font-semibold">
                      ⚠ Typical Friday Status Chase
                    </span>
                    <span className="text-xs font-mono text-slate-400">5 unread threads</span>
                  </div>
                  <div className="space-y-3 text-[15px]">
                    <div className="p-3.5 rounded-xl bg-slate-800/80 border border-slate-700">
                      <div className="text-xs font-mono text-amber-300 mb-1">
                        Client (WhatsApp · 6:42 PM)
                      </div>
                      <p className="text-slate-200">
                        &ldquo;Hey, I forgot my Jira password again. Is checkout v2 deployed? Can
                        you resend the staging URL and tell me what&apos;s left?&rdquo;
                      </p>
                    </div>
                    <div className="p-3.5 rounded-xl bg-slate-800/80 border border-slate-700">
                      <div className="text-xs font-mono text-sky-300 mb-1">
                        Founder / Lead (Slack · 7:15 PM)
                      </div>
                      <p className="text-slate-200">
                        &ldquo;Let me take 4 screenshots of Linear, crop out internal bugs, and
                        write a 300-word email recap...&rdquo;
                      </p>
                    </div>
                    <div className="p-3.5 rounded-xl bg-rose-950/50 border border-rose-800/70 text-rose-200 text-sm">
                      Result: 2 hours wasted weekly + zero formal milestone sign-off trail when
                      invoices go out.
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </section>

        {/* 3-STEP WORKFLOW */}
        <section className="max-w-6xl mx-auto px-4 sm:px-6 py-16 space-y-10">
          <div className="text-center max-w-2xl mx-auto space-y-3">
            <h2 className="font-display text-3xl font-extrabold text-slate-900 tracking-tight">
              From scattered tickets to client sign-off in 3 steps
            </h2>
            <p className="text-[16px] text-slate-600 leading-relaxed">
              No workspace setup, no onboarding calls, and no client password resets.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-6 rounded-2xl bg-white border border-slate-200 space-y-3">
              <div className="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center font-display font-extrabold">
                1
              </div>
              <h3 className="font-display text-lg font-bold text-slate-900">
                Drop milestones in 10 seconds
              </h3>
              <p className="text-[15px] text-slate-600 leading-relaxed">
                Start from a SaaS sprint, architecture audit, or launch retainer preset. Add staging
                URLs, PR links, or Figma previews.
              </p>
            </div>

            <div className="p-6 rounded-2xl bg-white border border-slate-200 space-y-3">
              <div className="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center font-display font-extrabold">
                2
              </div>
              <h3 className="font-display text-lg font-bold text-slate-900">
                Share one Magic URL
              </h3>
              <p className="text-[15px] text-slate-600 leading-relaxed">
                Send the generated link in Slack, WhatsApp, or email. Anyone with the link opens a
                crisp mobile-ready progress view immediately.
              </p>
            </div>

            <div className="p-6 rounded-2xl bg-white border border-slate-200 space-y-3">
              <div className="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center font-display font-extrabold">
                3
              </div>
              <h3 className="font-display text-lg font-bold text-slate-900">
                Capture 1-click sign-off
              </h3>
              <p className="text-[15px] text-slate-600 leading-relaxed">
                Stakeholders click <strong>Approve Milestone</strong> or attach a concise change
                note—generating a clean timestamped receipt.
              </p>
            </div>
          </div>
        </section>

        {/* FEATURE BENTO + COMPARISON TABLE */}
        <section className="border-y border-slate-200 bg-white">
          <div className="max-w-6xl mx-auto px-4 sm:px-6 py-16 space-y-14">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
              <div className="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2.5">
                <Zap className="w-5 h-5 text-indigo-600" />
                <h3 className="font-display text-base font-bold text-slate-900">
                  Zero-Login Capability Links
                </h3>
                <p className="text-[15px] text-slate-600 leading-relaxed">
                  Clients never create accounts or reset passwords. Instant open rate on mobile &amp;
                  desktop.
                </p>
              </div>
              <div className="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2.5">
                <CheckCircle2 className="w-5 h-5 text-emerald-600" />
                <h3 className="font-display text-base font-bold text-slate-900">
                  Signed Approval Receipts
                </h3>
                <p className="text-[15px] text-slate-600 leading-relaxed">
                  Eliminate scope ambiguity with timestamped milestone sign-off and instant Slack
                  snippets.
                </p>
              </div>
              <div className="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2.5">
                <GitPullRequest className="w-5 h-5 text-indigo-600" />
                <div className="flex items-center justify-between gap-2">
                  <h3 className="font-display text-base font-bold text-slate-900">
                    GitHub / Linear Sync
                  </h3>
                  <span className="text-xs font-mono font-semibold px-2 py-0.5 rounded bg-indigo-100 text-indigo-700">
                    Pro
                  </span>
                </div>
                <p className="text-[15px] text-slate-600 leading-relaxed">
                  Auto-advance client milestones when PRs merge via EventBridge webhooks.
                </p>
              </div>
              <div className="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2.5">
                <Globe className="w-5 h-5 text-indigo-600" />
                <div className="flex items-center justify-between gap-2">
                  <h3 className="font-display text-base font-bold text-slate-900">
                    Custom Branded Domain
                  </h3>
                  <span className="text-xs font-mono font-semibold px-2 py-0.5 rounded bg-indigo-100 text-indigo-700">
                    Pro
                  </span>
                </div>
                <p className="text-[15px] text-slate-600 leading-relaxed">
                  Host on <code className="font-mono text-sm">status.youragency.com</code> with
                  automatic read &amp; approval alerts.
                </p>
              </div>
            </div>

            {/* Comparison Table */}
            <div className="space-y-4">
              <h2 className="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
                Why teams switch from Jira shares &amp; $99/mo portals
              </h2>
              <div className="overflow-x-auto rounded-2xl border border-slate-200">
                <table className="w-full text-left border-collapse text-[15px]">
                  <thead className="bg-slate-50 border-b border-slate-200 text-slate-700">
                    <tr>
                      <th className="py-3.5 px-4 font-bold">Capability</th>
                      <th className="py-3.5 px-4 font-bold">Jira / Linear Guest</th>
                      <th className="py-3.5 px-4 font-bold">Heavy Portals ($49–$150/mo)</th>
                      <th className="py-3.5 px-4 font-bold text-indigo-700 bg-indigo-50/50">
                        ShipLink
                      </th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-200 bg-white">
                    <tr>
                      <td className="py-3.5 px-4 font-medium text-slate-900">
                        Zero-login client access
                      </td>
                      <td className="py-3.5 px-4 text-slate-600">No (Account + SSO/2FA)</td>
                      <td className="py-3.5 px-4 text-slate-600">Often OTP / portal login</td>
                      <td className="py-3.5 px-4 font-semibold text-emerald-700 bg-indigo-50/30">
                        Yes — instant 1-click link
                      </td>
                    </tr>
                    <tr>
                      <td className="py-3.5 px-4 font-medium text-slate-900">
                        Time to send first status link
                      </td>
                      <td className="py-3.5 px-4 text-slate-600">30+ min permissions setup</td>
                      <td className="py-3.5 px-4 text-slate-600">2–4 hours workspace setup</td>
                      <td className="py-3.5 px-4 font-semibold text-emerald-700 bg-indigo-50/30">
                        10 seconds
                      </td>
                    </tr>
                    <tr>
                      <td className="py-3.5 px-4 font-medium text-slate-900">
                        Hides messy internal ticket noise
                      </td>
                      <td className="py-3.5 px-4 text-slate-600">No (Exposes dev backlog)</td>
                      <td className="py-3.5 px-4 text-slate-600">Yes</td>
                      <td className="py-3.5 px-4 font-semibold text-emerald-700 bg-indigo-50/30">
                        Yes — milestone-level clarity
                      </td>
                    </tr>
                    <tr>
                      <td className="py-3.5 px-4 font-medium text-slate-900">Pricing</td>
                      <td className="py-3.5 px-4 text-slate-600">Per-seat license tax</td>
                      <td className="py-3.5 px-4 text-slate-600">$49–$150+/month</td>
                      <td className="py-3.5 px-4 font-semibold text-indigo-700 bg-indigo-50/30">
                        $0 Free · $19–$39/mo Pro
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </section>

        {/* PRICING / SMOKE TEST */}
        <section id="pricing" className="max-w-6xl mx-auto px-4 sm:px-6 py-16 space-y-10">
          <div className="text-center max-w-2xl mx-auto space-y-3">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 text-indigo-700 text-xs font-semibold uppercase tracking-wider">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Simple Pricing</span>
            </span>
            <h2 className="font-display text-3xl font-extrabold text-slate-900 tracking-tight">
              Free forever for manual links. Pay only for automation.
            </h2>
            <p className="text-[16px] text-slate-600">
              Start creating shareable links today with zero login. Reserve Phase 2 Pro automation
              if your team wants GitHub/Linear sync.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
            {/* Free */}
            <div className="p-6 rounded-2xl bg-white border border-slate-200 flex flex-col justify-between space-y-6">
              <div className="space-y-4">
                <div>
                  <h3 className="font-display text-lg font-bold text-slate-900">Free Link Studio</h3>
                  <div className="mt-2 flex items-baseline gap-1">
                    <span className="font-display text-4xl font-extrabold text-slate-900">$0</span>
                    <span className="text-sm text-slate-600">/ forever</span>
                  </div>
                </div>
                <ul className="space-y-2.5 text-[15px] text-slate-700">
                  <li className="flex items-start gap-2">
                    <Check className="w-4 h-4 text-emerald-600 mt-1 flex-shrink-0" />
                    <span>Unlimited login-free magic links</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <Check className="w-4 h-4 text-emerald-600 mt-1 flex-shrink-0" />
                    <span>Instant preset templates + preview URLs</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <Check className="w-4 h-4 text-emerald-600 mt-1 flex-shrink-0" />
                    <span>Interactive client milestone approval receipts</span>
                  </li>
                </ul>
              </div>
              <Link
                href="/create"
                className="w-full py-3 rounded-xl border border-slate-300 bg-white hover:bg-slate-50 text-slate-900 text-[15px] font-semibold text-center transition"
              >
                Create Link Free Now
              </Link>
            </div>

            {/* Solo Pro */}
            <div className="p-6 rounded-2xl bg-white border-2 border-indigo-600 shadow-lg shadow-indigo-600/10 flex flex-col justify-between space-y-6 relative">
              <div className="space-y-4">
                <div className="flex items-center justify-between gap-2">
                  <h3 className="font-display text-lg font-bold text-slate-900">Solo Pro</h3>
                  <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-600 text-white">
                    Most Popular
                  </span>
                </div>
                <div className="mt-2 flex items-baseline gap-1">
                  <span className="font-display text-4xl font-extrabold text-slate-900">$19</span>
                  <span className="text-sm text-slate-600">/ month</span>
                </div>
                <ul className="space-y-2.5 text-[15px] text-slate-700">
                  <li className="flex items-start gap-2">
                    <Check className="w-4 h-4 text-indigo-600 mt-1 flex-shrink-0" />
                    <span>Short hosted links + persistent AWS DynamoDB state</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <Check className="w-4 h-4 text-indigo-600 mt-1 flex-shrink-0" />
                    <span>GitHub PR &amp; Linear auto-sync webhooks</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <Check className="w-4 h-4 text-indigo-600 mt-1 flex-shrink-0" />
                    <span>Instant email &amp; Slack sign-off alerts</span>
                  </li>
                </ul>
              </div>
              <button
                type="button"
                onClick={() => openWaitlist('solo-19', 'Solo Pro ($19/mo)')}
                className="w-full py-3 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-[15px] font-semibold transition"
              >
                Join Solo Pro Waitlist
              </button>
            </div>

            {/* Agency Team / LTD */}
            <div className="p-6 rounded-2xl bg-white border border-slate-200 flex flex-col justify-between space-y-6">
              <div className="space-y-4">
                <div>
                  <h3 className="font-display text-lg font-bold text-slate-900">
                    Agency Team / Founder LTD
                  </h3>
                  <div className="mt-2 flex items-baseline gap-2">
                    <span className="font-display text-4xl font-extrabold text-slate-900">$39</span>
                    <span className="text-sm text-slate-600">/ mo · or $69 Lifetime</span>
                  </div>
                </div>
                <ul className="space-y-2.5 text-[15px] text-slate-700">
                  <li className="flex items-start gap-2">
                    <Check className="w-4 h-4 text-emerald-600 mt-1 flex-shrink-0" />
                    <span>Custom white-label domain (status.agency.com)</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <Check className="w-4 h-4 text-emerald-600 mt-1 flex-shrink-0" />
                    <span>Unlimited client boards &amp; immutable audit logs</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <Check className="w-4 h-4 text-emerald-600 mt-1 flex-shrink-0" />
                    <span>Priority AI weekly digest formatter</span>
                  </li>
                </ul>
              </div>
              <button
                type="button"
                onClick={() => openWaitlist('team-39', 'Agency Team ($39/mo) or $69 Early-Bird LTD')}
                className="w-full py-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-[15px] font-semibold transition"
              >
                Reserve Agency / $69 LTD Spot
              </button>
            </div>
          </div>
        </section>

        {/* ARCHITECT CASE STUDY & CONSULTING BRIDGE */}
        <section className="max-w-6xl mx-auto px-4 sm:px-6 pb-16">
          <div className="rounded-2xl bg-[#0B0F19] text-slate-100 p-7 sm:p-10 border border-slate-800 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-8">
            <div className="space-y-3 max-w-2xl">
              <div className="inline-flex items-center gap-2 text-xs font-mono font-semibold uppercase tracking-wider text-indigo-400">
                <Code2 className="w-4 h-4" />
                <span>Open System Architecture &amp; Consulting</span>
              </div>
              <h2 className="font-display text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                Inspect the C4 diagram, DynamoDB Single-Table design &amp; ADRs behind ShipLink
              </h2>
              <p className="text-[15px] text-slate-300 leading-relaxed">
                Designed by Sarwan Singh (10+ yr Lead Software Engineer &amp; Anthropic Certified
                Claude Architect). Inspect how Phase 1 validates at $0/mo before scaling cleanly onto
                AWS Lambda, EventBridge, and DynamoDB.
              </p>
            </div>
            <div className="flex flex-wrap gap-3 flex-shrink-0">
              <Link
                href="/architecture"
                className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-[15px] font-semibold transition"
              >
                <span>Explore /architecture</span>
                <ArrowRight className="w-4 h-4" />
              </Link>
              <button
                type="button"
                onClick={() => openWaitlist('audit-consult', 'AWS / AI Architecture Audit')}
                className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-100 border border-slate-700 text-[15px] font-semibold transition"
              >
                <span>Book Architecture Audit</span>
              </button>
            </div>
          </div>
        </section>

        {/* BLUF FAQ (FOR USERS & AI ENGINES) */}
        <section className="border-t border-slate-200 bg-white">
          <div className="max-w-4xl mx-auto px-4 sm:px-6 py-14 space-y-6">
            <h2 className="font-display text-2xl font-extrabold text-slate-900 tracking-tight">
              Frequently Asked Questions
            </h2>
            <div className="space-y-4">
              <div className="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                <h3 className="font-display text-base font-bold text-slate-900">
                  Do clients need to create an account or log in?
                </h3>
                <p className="text-[15px] text-slate-600 leading-relaxed">
                  No. Every board generates a standalone magic URL. Clients open it directly on
                  mobile or desktop without a password, view progress, and click Approve or Request
                  Change in seconds.
                </p>
              </div>
              <div className="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                <h3 className="font-display text-base font-bold text-slate-900">
                  Where is my project data stored in Phase 1?
                </h3>
                <p className="text-[15px] text-slate-600 leading-relaxed">
                  Phase 1 encodes board state cleanly inside the URL hash fragment (never sent to
                  server logs) and saves your personal drafts inside your browser&apos;s local
                  storage—delivering full functionality with zero tracking.
                </p>
              </div>
              <div className="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                <h3 className="font-display text-base font-bold text-slate-900">
                  When does GitHub PR / Linear automatic syncing ship?
                </h3>
                <p className="text-[15px] text-slate-600 leading-relaxed">
                  Automated webhook syncing and custom domains roll out in Phase 2 on AWS Serverless
                  once early-access demand is verified. Join the Solo Pro waitlist to prioritize your
                  stack.
                </p>
              </div>
            </div>
          </div>
        </section>
      </main>

      <Footer />

      <WaitlistModal
        open={waitlistOpen}
        initialTier={waitlistTier}
        triggerContext={waitlistContext}
        onClose={() => setWaitlistOpen(false)}
      />
    </>
  );
}
