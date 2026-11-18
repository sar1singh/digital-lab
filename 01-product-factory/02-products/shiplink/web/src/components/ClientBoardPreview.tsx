'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import {
  CheckCircle2,
  Clock,
  ExternalLink,
  MessageSquare,
  ShieldCheck,
  Sparkles,
  Copy,
  Check,
  AlertCircle,
} from 'lucide-react';
import { computeCompletion, MilestoneItem, MilestoneStatus, ShipLinkBoard } from '@/lib/shiplink';

interface ClientBoardPreviewProps {
  board: ShipLinkBoard;
  interactive?: boolean;
  onUpdateMilestone?: (milestoneId: string, newStatus: MilestoneStatus, note?: string) => void;
}

const ACCENT_MAP = {
  indigo: {
    bar: 'bg-indigo-600',
    badge: 'bg-indigo-50 text-indigo-700 border-indigo-200',
    ring: 'border-indigo-200',
    btn: 'bg-indigo-600 hover:bg-indigo-700 text-white',
  },
  emerald: {
    bar: 'bg-emerald-600',
    badge: 'bg-emerald-50 text-emerald-700 border-emerald-200',
    ring: 'border-emerald-200',
    btn: 'bg-emerald-600 hover:bg-emerald-700 text-white',
  },
  slate: {
    bar: 'bg-slate-900',
    badge: 'bg-slate-100 text-slate-800 border-slate-300',
    ring: 'border-slate-300',
    btn: 'bg-slate-900 hover:bg-slate-800 text-white',
  },
};

function StatusBadge({ status }: { status: MilestoneStatus }) {
  switch (status) {
    case 'approved':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200">
          <CheckCircle2 className="w-3.5 h-3.5" />
          <span>Approved</span>
        </span>
      );
    case 'in_review':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-50 text-amber-800 border border-amber-300">
          <AlertCircle className="w-3.5 h-3.5" />
          <span>Ready for Review</span>
        </span>
      );
    case 'in_progress':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-50 text-indigo-700 border border-indigo-200">
          <Clock className="w-3.5 h-3.5" />
          <span>In Progress</span>
        </span>
      );
    default:
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-slate-100 text-slate-700 border border-slate-200">
          <span>Planned</span>
        </span>
      );
  }
}

export function ClientBoardPreview({
  board,
  interactive = false,
  onUpdateMilestone,
}: ClientBoardPreviewProps) {
  const stats = computeCompletion(board);
  const accent = ACCENT_MAP[board.accent] || ACCENT_MAP.indigo;

  const [activeNoteFor, setActiveNoteFor] = useState<string | null>(null);
  const [draftNote, setDraftNote] = useState('');
  const [receipt, setReceipt] = useState<{
    milestoneTitle: string;
    action: 'Approved' | 'Changes Requested';
    note?: string;
    timestamp: string;
  } | null>(null);
  const [copiedReceipt, setCopiedReceipt] = useState(false);

  const handleAction = (item: MilestoneItem, action: 'approve' | 'changes') => {
    const nowLabel = new Date().toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: 'numeric',
      minute: '2-digit',
    });
    const cleanNote = draftNote.trim() || undefined;
    if (onUpdateMilestone) {
      onUpdateMilestone(
        item.id,
        action === 'approve' ? 'approved' : 'in_progress',
        cleanNote
      );
    }
    setReceipt({
      milestoneTitle: item.title,
      action: action === 'approve' ? 'Approved' : 'Changes Requested',
      note: cleanNote,
      timestamp: nowLabel,
    });
    setActiveNoteFor(null);
    setDraftNote('');
  };

  const copyReceiptSnippet = async () => {
    if (!receipt) return;
    const text = `[ShipLink Sign-Off] ${board.projectTitle} — "${receipt.milestoneTitle}" marked as ${receipt.action} by ${board.clientName} (${receipt.timestamp})${
      receipt.note ? ` | Note: ${receipt.note}` : ''
    }`;
    try {
      await navigator.clipboard.writeText(text);
      setCopiedReceipt(true);
      setTimeout(() => setCopiedReceipt(false), 2000);
    } catch {
      // Ignore clipboard failures
    }
  };

  return (
    <div className="rounded-2xl bg-white border border-slate-200 shadow-sm overflow-hidden min-w-0">
      {/* Top Status Header */}
      <div className="p-5 sm:p-7 border-b border-slate-200 space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div className="inline-flex items-center gap-2">
            <span
              className={`inline-flex items-center px-2.5 py-1 rounded-md text-xs font-semibold border ${accent.badge}`}
            >
              {board.senderName || 'Your Team'}
            </span>
            <span className="text-sm text-slate-500">for {board.clientName || 'Client'}</span>
          </div>
          <span className="inline-flex items-center gap-1.5 text-xs font-mono text-slate-600 bg-slate-100 px-2.5 py-1 rounded-md">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
            <span>No Login Required</span>
          </span>
        </div>

        <div className="space-y-2">
          <h2 className="font-display text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight break-words">
            {board.projectTitle || 'Untitled Client Project'}
          </h2>
          {board.overviewNote && (
            <p className="text-[15px] text-slate-600 leading-relaxed">{board.overviewNote}</p>
          )}
        </div>

        {/* Completion Progress Bar */}
        <div className="p-4 rounded-xl bg-slate-50 border border-slate-200/80 space-y-2.5">
          <div className="flex flex-wrap items-center justify-between gap-2 text-sm">
            <span className="font-semibold text-slate-800">
              {stats.approved} of {stats.total} milestones approved
              {stats.inReview > 0 && ` · ${stats.inReview} awaiting your review`}
            </span>
            <span className="font-mono font-bold text-slate-900">{stats.percent}%</span>
          </div>
          <div className="w-full h-2.5 rounded-full bg-slate-200 overflow-hidden">
            <div
              className={`h-full rounded-full transition-all duration-300 ${accent.bar}`}
              style={{ width: `${stats.percent}%` }}
            />
          </div>
          <div className="flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600 font-mono">
            <span>Target Delivery: {board.targetDate || 'TBD'}</span>
            <span>Updated: {board.updatedAt}</span>
          </div>
        </div>
      </div>

      {/* Live Sign-Off Receipt Banner */}
      {receipt && (
        <div className="mx-5 sm:mx-7 mt-5 p-4 rounded-xl bg-emerald-50 border border-emerald-200 space-y-2">
          <div className="flex flex-wrap items-start justify-between gap-2">
            <div className="flex items-start gap-2.5">
              <CheckCircle2 className="w-5 h-5 text-emerald-600 flex-shrink-0 mt-0.5" />
              <div>
                <div className="text-[15px] font-bold text-emerald-950">
                  {receipt.action}: {receipt.milestoneTitle}
                </div>
                <div className="text-sm text-emerald-800 mt-0.5">
                  Recorded on {receipt.timestamp}
                  {receipt.note ? ` — "${receipt.note}"` : ''}
                </div>
              </div>
            </div>
            <button
              type="button"
              onClick={copyReceiptSnippet}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white border border-emerald-300 text-emerald-800 text-xs font-semibold hover:bg-emerald-100 transition"
            >
              {copiedReceipt ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
              <span>{copiedReceipt ? 'Copied Receipt' : 'Copy Slack/Email Receipt'}</span>
            </button>
          </div>
        </div>
      )}

      {/* Milestones Feed */}
      <div className="p-5 sm:p-7 space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="text-sm font-bold uppercase tracking-wider text-slate-500">
            Delivery Milestones
          </h3>
          <span className="text-sm text-slate-500">{board.milestones.length} items</span>
        </div>

        <div className="space-y-3.5">
          {board.milestones.map((item, idx) => {
            const isReview = item.status === 'in_review';
            const noteOpen = activeNoteFor === item.id;

            return (
              <div
                key={item.id}
                className={`rounded-xl border p-4 sm:p-5 transition ${
                  isReview
                    ? 'border-amber-300 bg-amber-50/30 ring-1 ring-amber-200/70'
                    : 'border-slate-200 bg-white'
                }`}
              >
                <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-3">
                  <div className="space-y-1.5 min-w-0">
                    <div className="flex flex-wrap items-center gap-2">
                      <span className="text-xs font-mono font-semibold text-slate-500">
                        0{idx + 1}
                      </span>
                      <h4 className="font-display text-base font-bold text-slate-900 break-words">
                        {item.title}
                      </h4>
                    </div>
                    <p className="text-[15px] text-slate-600 leading-relaxed">{item.summary}</p>

                    {item.clientNote && (
                      <div className="mt-2 inline-flex items-start gap-1.5 text-sm text-slate-700 bg-slate-100 px-3 py-1.5 rounded-lg">
                        <MessageSquare className="w-4 h-4 text-slate-500 flex-shrink-0 mt-0.5" />
                        <span>Client note: &ldquo;{item.clientNote}&rdquo;</span>
                      </div>
                    )}

                    {item.approvedAt && item.status === 'approved' && (
                      <div className="text-xs font-mono text-emerald-700 font-medium pt-0.5">
                        ✓ Signed off on {item.approvedAt}
                      </div>
                    )}
                  </div>

                  <div className="flex-shrink-0">
                    <StatusBadge status={item.status} />
                  </div>
                </div>

                {/* Deliverable Link & Client Sign-Off Actions */}
                {(item.linkUrl || (interactive && isReview)) && (
                  <div className="mt-4 pt-3.5 border-t border-slate-200/70 flex flex-wrap items-center justify-between gap-3">
                    {item.linkUrl ? (
                      <a
                        href={item.linkUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-1.5 text-sm font-semibold text-indigo-700 hover:text-indigo-900 transition"
                      >
                        <ExternalLink className="w-4 h-4" />
                        <span>{item.linkLabel || 'Open Deliverable Preview'}</span>
                      </a>
                    ) : (
                      <span />
                    )}

                    {interactive && isReview && (
                      <div className="flex flex-wrap items-center gap-2 w-full sm:w-auto">
                        <button
                          type="button"
                          onClick={() => setActiveNoteFor(noteOpen ? null : item.id)}
                          className="flex-1 sm:flex-initial min-h-[44px] px-3.5 py-2 rounded-lg border border-slate-300 bg-white hover:bg-slate-50 text-slate-700 text-sm font-semibold transition"
                        >
                          Request Change
                        </button>
                        <button
                          type="button"
                          onClick={() => handleAction(item, 'approve')}
                          className={`flex-1 sm:flex-initial min-h-[44px] px-4 py-2 rounded-lg text-sm font-semibold shadow-sm transition ${accent.btn}`}
                        >
                          Approve Milestone
                        </button>
                      </div>
                    )}
                  </div>
                )}

                {interactive && noteOpen && (
                  <div className="mt-3.5 p-3.5 rounded-xl bg-white border border-slate-200 space-y-3">
                    <label
                      htmlFor={`note-${item.id}`}
                      className="block text-sm font-semibold text-slate-800"
                    >
                      Optional note for {board.senderName}
                    </label>
                    <textarea
                      id={`note-${item.id}`}
                      rows={2}
                      value={draftNote}
                      onChange={(e) => setDraftNote(e.target.value)}
                      placeholder="e.g., Looks solid, please tweak mobile padding on step 2..."
                      className="w-full rounded-lg border border-slate-300 px-3 py-2 text-[15px] text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                    />
                    <div className="flex flex-wrap items-center justify-end gap-2">
                      <button
                        type="button"
                        onClick={() => setActiveNoteFor(null)}
                        className="px-3.5 py-2 rounded-lg text-sm font-medium text-slate-600 hover:bg-slate-100"
                      >
                        Cancel
                      </button>
                      <button
                        type="button"
                        onClick={() => handleAction(item, 'changes')}
                        className="px-4 py-2 rounded-lg bg-amber-600 hover:bg-amber-700 text-white text-sm font-semibold"
                      >
                        Submit Feedback
                      </button>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* Built-in Viral Flywheel Footer */}
      <div className="px-5 sm:px-7 py-4 bg-slate-50 border-t border-slate-200 flex flex-wrap items-center justify-between gap-3 text-sm">
        <span className="text-slate-600">
          Powered by <strong className="text-slate-900">ShipLink</strong> — client progress with
          zero passwords.
        </span>
        <Link
          href="/create"
          className="inline-flex items-center gap-1.5 font-semibold text-indigo-700 hover:text-indigo-900 transition"
        >
          <Sparkles className="w-4 h-4" />
          <span>Create your own link in 10s →</span>
        </Link>
      </div>
    </div>
  );
}
