'use client';

import React, { useEffect, useMemo, useState } from 'react';
import Link from 'next/link';
import {
  ArrowDown,
  ArrowUp,
  Check,
  Copy,
  ExternalLink,
  GitPullRequest,
  Globe,
  Lock,
  Plus,
  RotateCcw,
  Trash2,
} from 'lucide-react';
import { Navbar } from '@/components/Navbar';
import { Footer } from '@/components/Footer';
import { ClientBoardPreview } from '@/components/ClientBoardPreview';
import { WaitlistModal } from '@/components/WaitlistModal';
import {
  AccentTheme,
  encodeBoardToHash,
  loadBoardDrafts,
  MilestoneItem,
  MilestoneStatus,
  PRESET_BOARDS,
  saveBoardDraft,
  ShipLinkBoard,
  WaitlistLead,
} from '@/lib/shiplink';

export default function CreatePage() {
  const [board, setBoard] = useState<ShipLinkBoard>(() => ({
    ...PRESET_BOARDS.sprint,
    milestones: PRESET_BOARDS.sprint.milestones.map((m) => ({ ...m })),
  }));
  const [savedDrafts, setSavedDrafts] = useState<ShipLinkBoard[]>([]);
  const [copiedUrl, setCopiedUrl] = useState(false);
  const [origin, setOrigin] = useState('');

  const [waitlistOpen, setWaitlistOpen] = useState(false);
  const [waitlistTier, setWaitlistTier] = useState<WaitlistLead['tier']>('solo-19');
  const [waitlistContext, setWaitlistContext] = useState<string | undefined>(undefined);

  useEffect(() => {
    setOrigin(window.location.origin);
    setSavedDrafts(loadBoardDrafts());
  }, []);

  const magicPath = useMemo(() => {
    const hash = encodeBoardToHash(board);
    return `/m/#${hash}`;
  }, [board]);

  const fullMagicUrl = origin ? `${origin}${magicPath}` : magicPath;

  const updateBoardField = <K extends keyof ShipLinkBoard>(key: K, value: ShipLinkBoard[K]) => {
    setBoard((prev) => ({
      ...prev,
      [key]: value,
      updatedAt: 'Just now',
    }));
  };

  const applyPreset = (presetKey: 'sprint' | 'audit' | 'retainer') => {
    const src = PRESET_BOARDS[presetKey];
    setBoard({
      ...src,
      id: `sl-${presetKey}-${Date.now().toString().slice(-4)}`,
      updatedAt: 'Just now',
      milestones: src.milestones.map((m) => ({ ...m })),
    });
  };

  const updateMilestone = (idx: number, patch: Partial<MilestoneItem>) => {
    setBoard((prev) => {
      const next = [...prev.milestones];
      next[idx] = { ...next[idx], ...patch };
      return { ...prev, updatedAt: 'Just now', milestones: next };
    });
  };

  const addMilestone = () => {
    setBoard((prev) => ({
      ...prev,
      updatedAt: 'Just now',
      milestones: [
        ...prev.milestones,
        {
          id: `ms-${Date.now()}`,
          title: 'New Deliverable Milestone',
          status: 'planned',
          summary: 'Describe what will be delivered and ready for client sign-off.',
        },
      ],
    }));
  };

  const removeMilestone = (idx: number) => {
    setBoard((prev) => ({
      ...prev,
      updatedAt: 'Just now',
      milestones: prev.milestones.filter((_, i) => i !== idx),
    }));
  };

  const moveMilestone = (idx: number, dir: -1 | 1) => {
    const target = idx + dir;
    if (target < 0 || target >= board.milestones.length) return;
    setBoard((prev) => {
      const next = [...prev.milestones];
      const temp = next[idx];
      next[idx] = next[target];
      next[target] = temp;
      return { ...prev, updatedAt: 'Just now', milestones: next };
    });
  };

  const handleCopyMagicLink = async () => {
    saveBoardDraft(board);
    setSavedDrafts(loadBoardDrafts());
    try {
      await navigator.clipboard.writeText(fullMagicUrl);
      setCopiedUrl(true);
      setTimeout(() => setCopiedUrl(false), 2200);
    } catch {
      // Fallback if clipboard blocked
    }
  };

  const triggerProSmokeTest = (tier: WaitlistLead['tier'], featureName: string) => {
    setWaitlistTier(tier);
    setWaitlistContext(featureName);
    setWaitlistOpen(true);
  };

  return (
    <>
      <Navbar
        onOpenWaitlist={(t) => triggerProSmokeTest(t || 'solo-19', 'Creator Studio Pro Upgrade')}
      />

      <main className="flex-1 max-w-6xl w-full mx-auto px-4 sm:px-6 py-8 sm:py-10 space-y-6">
        {/* Top Studio Bar */}
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-200 pb-6">
          <div className="space-y-1">
            <h1 className="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
              Magic-Link Builder Studio
            </h1>
            <p className="text-[15px] text-slate-600">
              Edit milestones below and copy your zero-login client link in 10 seconds.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2">
            <span className="text-sm font-medium text-slate-500 mr-1">Starter presets:</span>
            <button
              type="button"
              onClick={() => applyPreset('sprint')}
              className="px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-50 text-sm font-semibold text-slate-800 transition"
            >
              SaaS MVP Sprint
            </button>
            <button
              type="button"
              onClick={() => applyPreset('audit')}
              className="px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-50 text-sm font-semibold text-slate-800 transition"
            >
              AWS / AI Audit
            </button>
            <button
              type="button"
              onClick={() => applyPreset('retainer')}
              className="px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-50 text-sm font-semibold text-slate-800 transition"
            >
              Launch Retainer
            </button>
          </div>
        </div>

        {/* Sticky Generated Magic Link Banner */}
        <div className="rounded-2xl bg-indigo-50 border border-indigo-200 p-4 flex flex-col lg:flex-row lg:items-center justify-between gap-3">
          <div className="min-w-0 flex-1 space-y-0.5">
            <div className="text-xs font-mono font-bold uppercase tracking-wider text-indigo-700">
              Your Live Zero-Login Client URL
            </div>
            <div className="font-mono text-sm text-slate-800 truncate bg-white/90 border border-indigo-200/80 px-3 py-1.5 rounded-lg">
              {fullMagicUrl}
            </div>
          </div>

          <div className="flex flex-wrap items-center gap-2.5 flex-shrink-0">
            <button
              type="button"
              onClick={handleCopyMagicLink}
              className="inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold shadow-sm transition min-h-[44px]"
            >
              {copiedUrl ? <Check className="w-4 h-4" /> : <Copy className="w-4 h-4" />}
              <span>{copiedUrl ? 'Copied Magic Link!' : 'Copy Magic Link'}</span>
            </button>
            <Link
              href={magicPath}
              onClick={() => {
                saveBoardDraft(board);
                setSavedDrafts(loadBoardDrafts());
              }}
              className="inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl bg-white hover:bg-slate-50 text-slate-800 border border-slate-300 text-sm font-semibold transition min-h-[44px]"
            >
              <span>Open Client View</span>
              <ExternalLink className="w-4 h-4" />
            </Link>
          </div>
        </div>

        {/* Split Editor + Live Preview */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          {/* LEFT EDITOR (7 Cols) */}
          <div className="lg:col-span-7 space-y-6 min-w-0 min-h-0">
            {/* Project Meta Card */}
            <section className="rounded-2xl bg-white border border-slate-200 p-5 sm:p-6 space-y-4">
              <div className="flex items-center justify-between">
                <h2 className="font-display text-lg font-bold text-slate-900">1. Project Header</h2>
                <button
                  type="button"
                  onClick={() => applyPreset('sprint')}
                  className="inline-flex items-center gap-1 text-sm text-slate-600 hover:text-slate-900"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span>Reset</span>
                </button>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="sm:col-span-2">
                  <label
                    htmlFor="project-title"
                    className="block text-sm font-semibold text-slate-800 mb-1"
                  >
                    Project / Deliverable Name
                  </label>
                  <input
                    id="project-title"
                    type="text"
                    value={board.projectTitle}
                    onChange={(e) => updateBoardField('projectTitle', e.target.value)}
                    className="w-full rounded-xl border border-slate-300 px-3.5 py-2.5 text-[15px] text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  />
                </div>

                <div>
                  <label
                    htmlFor="client-name"
                    className="block text-sm font-semibold text-slate-800 mb-1"
                  >
                    Client / Stakeholder
                  </label>
                  <input
                    id="client-name"
                    type="text"
                    value={board.clientName}
                    onChange={(e) => updateBoardField('clientName', e.target.value)}
                    className="w-full rounded-xl border border-slate-300 px-3.5 py-2.5 text-[15px] text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  />
                </div>

                <div>
                  <label
                    htmlFor="sender-name"
                    className="block text-sm font-semibold text-slate-800 mb-1"
                  >
                    Your Brand / Name
                  </label>
                  <input
                    id="sender-name"
                    type="text"
                    value={board.senderName}
                    onChange={(e) => updateBoardField('senderName', e.target.value)}
                    className="w-full rounded-xl border border-slate-300 px-3.5 py-2.5 text-[15px] text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  />
                </div>

                <div>
                  <label
                    htmlFor="target-date"
                    className="block text-sm font-semibold text-slate-800 mb-1"
                  >
                    Target Delivery Date
                  </label>
                  <input
                    id="target-date"
                    type="text"
                    value={board.targetDate}
                    onChange={(e) => updateBoardField('targetDate', e.target.value)}
                    className="w-full rounded-xl border border-slate-300 px-3.5 py-2.5 text-[15px] text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  />
                </div>

                <div>
                  <label
                    htmlFor="accent-theme"
                    className="block text-sm font-semibold text-slate-800 mb-1"
                  >
                    Card Accent Color
                  </label>
                  <select
                    id="accent-theme"
                    value={board.accent}
                    onChange={(e) => updateBoardField('accent', e.target.value as AccentTheme)}
                    className="w-full rounded-xl border border-slate-300 bg-white px-3.5 py-2.5 text-[15px] text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  >
                    <option value="indigo">Indigo (SaaS / Tech)</option>
                    <option value="emerald">Emerald (Audit / Finance)</option>
                    <option value="slate">Obsidian Slate (Studio)</option>
                  </select>
                </div>

                <div className="sm:col-span-2">
                  <label
                    htmlFor="overview-note"
                    className="block text-sm font-semibold text-slate-800 mb-1"
                  >
                    Executive Summary Note
                  </label>
                  <textarea
                    id="overview-note"
                    rows={2}
                    value={board.overviewNote}
                    onChange={(e) => updateBoardField('overviewNote', e.target.value)}
                    className="w-full rounded-xl border border-slate-300 px-3.5 py-2 text-[15px] text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  />
                </div>
              </div>
            </section>

            {/* Milestones Editor */}
            <section className="rounded-2xl bg-white border border-slate-200 p-5 sm:p-6 space-y-4">
              <div className="flex items-center justify-between">
                <h2 className="font-display text-lg font-bold text-slate-900">
                  2. Milestones ({board.milestones.length})
                </h2>
                <button
                  type="button"
                  onClick={addMilestone}
                  className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-sm font-semibold transition"
                >
                  <Plus className="w-4 h-4" />
                  <span>Add Milestone</span>
                </button>
              </div>

              <div className="space-y-4">
                {board.milestones.map((item, idx) => (
                  <div
                    key={item.id}
                    className="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3"
                  >
                    <div className="flex flex-wrap items-center justify-between gap-2">
                      <span className="font-mono text-xs font-bold text-slate-500">
                        MILESTONE 0{idx + 1}
                      </span>
                      <div className="flex items-center gap-1">
                        <button
                          type="button"
                          onClick={() => moveMilestone(idx, -1)}
                          disabled={idx === 0}
                          className="p-1.5 rounded-lg border border-slate-200 bg-white text-slate-600 hover:text-slate-900 disabled:opacity-40"
                          aria-label="Move milestone up"
                        >
                          <ArrowUp className="w-4 h-4" />
                        </button>
                        <button
                          type="button"
                          onClick={() => moveMilestone(idx, 1)}
                          disabled={idx === board.milestones.length - 1}
                          className="p-1.5 rounded-lg border border-slate-200 bg-white text-slate-600 hover:text-slate-900 disabled:opacity-40"
                          aria-label="Move milestone down"
                        >
                          <ArrowDown className="w-4 h-4" />
                        </button>
                        <button
                          type="button"
                          onClick={() => removeMilestone(idx)}
                          className="p-1.5 rounded-lg border border-slate-200 bg-white text-rose-600 hover:bg-rose-50"
                          aria-label="Delete milestone"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </div>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                      <div className="sm:col-span-2">
                        <input
                          type="text"
                          value={item.title}
                          onChange={(e) => updateMilestone(idx, { title: e.target.value })}
                          placeholder="Milestone title"
                          className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-[15px] font-semibold text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                        />
                      </div>
                      <div>
                        <select
                          value={item.status}
                          onChange={(e) =>
                            updateMilestone(idx, { status: e.target.value as MilestoneStatus })
                          }
                          className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-[15px] text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                        >
                          <option value="approved">Approved</option>
                          <option value="in_review">Ready for Review</option>
                          <option value="in_progress">In Progress</option>
                          <option value="planned">Planned</option>
                        </select>
                      </div>
                    </div>

                    <textarea
                      rows={2}
                      value={item.summary}
                      onChange={(e) => updateMilestone(idx, { summary: e.target.value })}
                      placeholder="Short plain-English summary for the client..."
                      className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-[15px] text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                    />

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      <input
                        type="text"
                        value={item.linkLabel || ''}
                        onChange={(e) => updateMilestone(idx, { linkLabel: e.target.value })}
                        placeholder="Preview button text (e.g., Open Staging)"
                        className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                      />
                      <input
                        type="url"
                        value={item.linkUrl || ''}
                        onChange={(e) => updateMilestone(idx, { linkUrl: e.target.value })}
                        placeholder="https://staging.example.com"
                        className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                      />
                    </div>
                  </div>
                ))}
              </div>
            </section>

            {/* Pro Smoke-Test Locked Integrations */}
            <section className="rounded-2xl bg-white border border-slate-200 p-5 sm:p-6 space-y-4">
              <div className="flex items-center justify-between">
                <h2 className="font-display text-lg font-bold text-slate-900">
                  3. Pro Automation (Phase 2 Early Access)
                </h2>
                <span className="text-xs font-mono font-semibold px-2.5 py-1 rounded bg-indigo-50 text-indigo-700">
                  Waitlist Vote
                </span>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <button
                  type="button"
                  onClick={() =>
                    triggerProSmokeTest('solo-19', 'Auto-Sync GitHub PRs & Linear Status')
                  }
                  className="p-4 rounded-xl border border-slate-200 hover:border-indigo-400 bg-slate-50 text-left transition flex items-start gap-3"
                >
                  <GitPullRequest className="w-5 h-5 text-indigo-600 flex-shrink-0 mt-0.5" />
                  <div>
                    <div className="text-[15px] font-bold text-slate-900 flex items-center gap-1.5">
                      <span>Auto-Sync GitHub / Linear</span>
                      <Lock className="w-3.5 h-3.5 text-slate-400" />
                    </div>
                    <p className="text-sm text-slate-600 mt-0.5">
                      Advance milestones automatically when PRs merge.
                    </p>
                  </div>
                </button>

                <button
                  type="button"
                  onClick={() =>
                    triggerProSmokeTest('team-39', 'Custom Domain & Slack Sign-Off Receipts')
                  }
                  className="p-4 rounded-xl border border-slate-200 hover:border-indigo-400 bg-slate-50 text-left transition flex items-start gap-3"
                >
                  <Globe className="w-5 h-5 text-indigo-600 flex-shrink-0 mt-0.5" />
                  <div>
                    <div className="text-[15px] font-bold text-slate-900 flex items-center gap-1.5">
                      <span>Custom Domain + Alerts</span>
                      <Lock className="w-3.5 h-3.5 text-slate-400" />
                    </div>
                    <p className="text-sm text-slate-600 mt-0.5">
                      Host on status.youragency.com + Slack pings.
                    </p>
                  </div>
                </button>
              </div>
            </section>

            {/* Saved Local Drafts */}
            {savedDrafts.length > 0 && (
              <section className="rounded-2xl bg-white border border-slate-200 p-5 sm:p-6 space-y-3">
                <h2 className="font-display text-base font-bold text-slate-900">
                  Recent Browser Drafts
                </h2>
                <div className="flex flex-wrap gap-2">
                  {savedDrafts.map((d) => (
                    <button
                      key={d.id}
                      type="button"
                      onClick={() => setBoard(d)}
                      className="px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-indigo-50 text-sm font-medium text-slate-800 border border-slate-200 transition"
                    >
                      {d.projectTitle} ({d.clientName})
                    </button>
                  ))}
                </div>
              </section>
            )}
          </div>

          {/* RIGHT LIVE CLIENT PREVIEW (5 Cols) */}
          <div className="lg:col-span-5 lg:sticky lg:top-24 space-y-3 min-w-0 min-h-0">
            <div className="flex items-center justify-between px-1">
              <span className="text-sm font-bold uppercase tracking-wider text-slate-500">
                Live Client View Preview
              </span>
              <span className="text-xs font-mono text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200">
                Interactive on /m
              </span>
            </div>
            <ClientBoardPreview
              board={board}
              interactive={true}
              onUpdateMilestone={(id, status, note) => {
                setBoard((prev) => ({
                  ...prev,
                  updatedAt: 'Just now',
                  milestones: prev.milestones.map((m) =>
                    m.id === id
                      ? {
                          ...m,
                          status,
                          clientNote: note || m.clientNote,
                          approvedAt:
                            status === 'approved'
                              ? new Date().toLocaleDateString('en-US', {
                                  month: 'short',
                                  day: 'numeric',
                                  year: 'numeric',
                                })
                              : m.approvedAt,
                        }
                      : m
                  ),
                }));
              }}
            />
          </div>
        </div>
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
