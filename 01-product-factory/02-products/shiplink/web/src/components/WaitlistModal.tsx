'use client';

import React, { useEffect, useState } from 'react';
import { X, CheckCircle2, Sparkles, ArrowRight } from 'lucide-react';
import { saveWaitlistLead, WaitlistLead } from '@/lib/shiplink';

interface WaitlistModalProps {
  open: boolean;
  initialTier?: WaitlistLead['tier'];
  triggerContext?: string;
  onClose: () => void;
}

const TIER_OPTIONS: Array<{
  id: WaitlistLead['tier'];
  label: string;
  price: string;
  sub: string;
}> = [
  {
    id: 'solo-19',
    label: 'Solo Pro',
    price: '$19/mo',
    sub: 'GitHub/Linear webhook sync + unlimited links + Slack/email receipts',
  },
  {
    id: 'team-39',
    label: 'Agency Team',
    price: '$39/mo',
    sub: 'Custom domain (status.agency.com) + white-label + multi-project portal',
  },
  {
    id: 'ltd-69',
    label: 'Early-Bird Lifetime',
    price: '$69 once',
    sub: 'Founder lifetime deal for first 50 agencies (locks Pro features forever)',
  },
  {
    id: 'audit-consult',
    label: 'Architecture Audit / Advisory',
    price: 'Custom Scope',
    sub: 'Book Sarwan Singh for AWS Serverless / Event-Driven / AI Systems review',
  },
];

export function WaitlistModal({
  open,
  initialTier = 'solo-19',
  triggerContext,
  onClose,
}: WaitlistModalProps) {
  const [tier, setTier] = useState<WaitlistLead['tier']>(initialTier);
  const [email, setEmail] = useState('');
  const [integration, setIntegration] = useState('GitHub PRs & Issues');
  const [notes, setNotes] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    setTier(initialTier);
    setSubmitted(false);
    setError('');
  }, [initialTier, open]);

  if (!open) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const trimmed = email.trim();
    if (!trimmed || !trimmed.includes('@') || !trimmed.includes('.')) {
      setError('Please enter a valid work or personal email.');
      return;
    }
    setError('');
    saveWaitlistLead({
      id: `lead-${Date.now()}`,
      email: trimmed,
      tier,
      integration,
      notes: notes.trim() || triggerContext,
      createdAt: new Date().toISOString(),
    });
    setSubmitted(true);
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm"
      role="dialog"
      aria-modal="true"
      aria-labelledby="waitlist-modal-title"
    >
      <div className="relative w-full max-w-lg rounded-2xl bg-white border border-slate-200 shadow-2xl overflow-hidden max-h-[90vh] flex flex-col">
        <div className="px-6 py-5 border-b border-slate-200 flex items-start justify-between gap-4">
          <div className="min-w-0">
            <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-indigo-600 mb-1">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Phase 2 Early Access · Smoke Test</span>
            </div>
            <h2 id="waitlist-modal-title" className="font-display text-xl font-bold text-slate-900">
              {tier === 'audit-consult'
                ? 'Request an Architecture Audit'
                : 'Vote on Pro Pricing & Join Early Access'}
            </h2>
            {triggerContext && (
              <p className="text-sm text-slate-600 mt-1">
                Requested feature: <strong className="text-slate-900">{triggerContext}</strong>
              </p>
            )}
          </div>
          <button
            type="button"
            onClick={onClose}
            className="p-2 rounded-lg text-slate-500 hover:text-slate-900 hover:bg-slate-100 transition"
            aria-label="Close modal"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="p-6 overflow-y-auto min-h-0">
          {submitted ? (
            <div className="py-6 text-center space-y-4">
              <div className="w-12 h-12 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center mx-auto border border-emerald-200">
                <CheckCircle2 className="w-6 h-6" />
              </div>
              <h3 className="font-display text-xl font-bold text-slate-900">
                You&apos;re on the priority list
              </h3>
              <p className="text-[15px] text-slate-600 leading-relaxed max-w-md mx-auto">
                We recorded your interest for{' '}
                <strong className="text-slate-900">
                  {TIER_OPTIONS.find((t) => t.id === tier)?.label} (
                  {TIER_OPTIONS.find((t) => t.id === tier)?.price})
                </strong>{' '}
                using <strong className="text-slate-900">{email}</strong>. You can keep creating
                unlimited free magic links right now with zero account required.
              </p>
              <button
                type="button"
                onClick={onClose}
                className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-[15px] font-semibold transition"
              >
                <span>Back to ShipLink</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-5">
              <div>
                <label className="block text-sm font-semibold text-slate-800 mb-2">
                  Which plan would you actually pay for?
                </label>
                <div className="grid grid-cols-1 gap-2.5">
                  {TIER_OPTIONS.map((opt) => {
                    const selected = tier === opt.id;
                    return (
                      <button
                        key={opt.id}
                        type="button"
                        onClick={() => setTier(opt.id)}
                        className={`w-full text-left p-3.5 rounded-xl border transition ${
                          selected
                            ? 'border-indigo-600 bg-indigo-50/70 ring-2 ring-indigo-600/20'
                            : 'border-slate-200 hover:border-slate-300 bg-white'
                        }`}
                      >
                        <div className="flex items-center justify-between gap-2">
                          <span className="text-[15px] font-bold text-slate-900">{opt.label}</span>
                          <span
                            className={`text-sm font-mono font-semibold px-2.5 py-0.5 rounded-md ${
                              selected
                                ? 'bg-indigo-600 text-white'
                                : 'bg-slate-100 text-slate-700'
                            }`}
                          >
                            {opt.price}
                          </span>
                        </div>
                        <p className="text-sm text-slate-600 mt-1 leading-snug">{opt.sub}</p>
                      </button>
                    );
                  })}
                </div>
              </div>

              {tier !== 'audit-consult' && (
                <div>
                  <label
                    htmlFor="waitlist-integration"
                    className="block text-sm font-semibold text-slate-800 mb-1.5"
                  >
                    Must-have workflow sync
                  </label>
                  <select
                    id="waitlist-integration"
                    value={integration}
                    onChange={(e) => setIntegration(e.target.value)}
                    className="w-full rounded-xl border border-slate-300 bg-white px-3.5 py-2.5 text-[15px] text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  >
                    <option>GitHub PRs &amp; Issues</option>
                    <option>Linear / Jira Sprint Status</option>
                    <option>Custom Domain + Email/Slack Approval Receipts</option>
                    <option>Figma / Staging Review Links</option>
                  </select>
                </div>
              )}

              <div>
                <label
                  htmlFor="waitlist-email"
                  className="block text-sm font-semibold text-slate-800 mb-1.5"
                >
                  Email address
                </label>
                <input
                  id="waitlist-email"
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="founder@agency.com"
                  className="w-full rounded-xl border border-slate-300 bg-white px-3.5 py-2.5 text-[15px] text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
                {error && <p className="text-sm text-red-600 mt-1.5 font-medium">{error}</p>}
              </div>

              <div>
                <label
                  htmlFor="waitlist-notes"
                  className="block text-sm font-semibold text-slate-800 mb-1.5"
                >
                  Optional context (team size, problem, or audit scope)
                </label>
                <textarea
                  id="waitlist-notes"
                  rows={2}
                  value={notes}
                  onChange={(e) => setNotes(e.target.value)}
                  placeholder="e.g., 4-person dev shop sending weekly client updates..."
                  className="w-full rounded-xl border border-slate-300 bg-white px-3.5 py-2 text-[15px] text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
              </div>

              <button
                type="submit"
                className="w-full py-3 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-[15px] font-semibold shadow-sm transition"
              >
                {tier === 'audit-consult' ? 'Request Audit Slot' : 'Reserve Early Access (No Charge Today)'}
              </button>
              <p className="text-xs text-slate-500 text-center">
                No credit card required. Used strictly to validate Phase 2 roadmap priority.
              </p>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
