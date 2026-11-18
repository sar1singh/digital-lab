'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { AlertTriangle, ArrowLeft, PlusCircle } from 'lucide-react';
import { Navbar } from '@/components/Navbar';
import { Footer } from '@/components/Footer';
import { ClientBoardPreview } from '@/components/ClientBoardPreview';
import { WaitlistModal } from '@/components/WaitlistModal';
import {
  decodeBoardFromHash,
  encodeBoardToHash,
  MilestoneStatus,
  PRESET_BOARDS,
  ShipLinkBoard,
  WaitlistLead,
} from '@/lib/shiplink';

export default function MagicClientPage() {
  const [board, setBoard] = useState<ShipLinkBoard>(PRESET_BOARDS.sprint);
  const [sourceMode, setSourceMode] = useState<'custom' | 'demo' | 'invalid'>('demo');
  const [waitlistOpen, setWaitlistOpen] = useState(false);
  const [waitlistTier, setWaitlistTier] = useState<WaitlistLead['tier']>('solo-19');

  useEffect(() => {
    const syncFromLocation = () => {
      const hash = window.location.hash;
      const params = new URLSearchParams(window.location.search);
      const demoParam = params.get('demo');

      if (hash && hash.includes('d=')) {
        const decoded = decodeBoardFromHash(hash);
        if (decoded) {
          setBoard(decoded);
          setSourceMode('custom');
        } else {
          setSourceMode('invalid');
        }
        return;
      }

      if (demoParam === 'audit') {
        setBoard(PRESET_BOARDS.audit);
      } else if (demoParam === 'retainer') {
        setBoard(PRESET_BOARDS.retainer);
      } else {
        setBoard(PRESET_BOARDS.sprint);
      }
      setSourceMode('demo');
    };

    syncFromLocation();
    window.addEventListener('hashchange', syncFromLocation);
    return () => window.removeEventListener('hashchange', syncFromLocation);
  }, []);

  const handleClientUpdate = (milestoneId: string, newStatus: MilestoneStatus, note?: string) => {
    setBoard((prev) => {
      const updated: ShipLinkBoard = {
        ...prev,
        updatedAt: 'Updated just now by Client',
        milestones: prev.milestones.map((m) =>
          m.id === milestoneId
            ? {
                ...m,
                status: newStatus,
                clientNote: note || m.clientNote,
                approvedAt:
                  newStatus === 'approved'
                    ? new Date().toLocaleDateString('en-US', {
                        month: 'short',
                        day: 'numeric',
                        year: 'numeric',
                      })
                    : m.approvedAt,
              }
            : m
        ),
      };
      if (sourceMode === 'custom') {
        window.history.replaceState(null, '', `#${encodeBoardToHash(updated)}`);
      }
      return updated;
    });
  };

  return (
    <>
      <Navbar
        onOpenWaitlist={(t) => {
          setWaitlistTier(t || 'solo-19');
          setWaitlistOpen(true);
        }}
      />

      <main className="flex-1 max-w-3xl w-full mx-auto px-4 sm:px-6 py-8 sm:py-12 space-y-6">
        {sourceMode === 'demo' && (
          <div className="rounded-xl bg-indigo-50 border border-indigo-200 px-4 py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div className="text-sm text-indigo-950">
              <strong>Live Client Demo Mode:</strong> Try clicking{' '}
              <strong>Approve Milestone</strong> or <strong>Request Change</strong> below—zero
              login required.
            </div>
            <div className="flex flex-wrap items-center gap-2 flex-shrink-0">
              <button
                type="button"
                onClick={() => setBoard(PRESET_BOARDS.sprint)}
                className="px-2.5 py-1 rounded-md bg-white border border-indigo-200 text-xs font-semibold text-indigo-800 hover:bg-indigo-100"
              >
                SaaS Sprint
              </button>
              <button
                type="button"
                onClick={() => setBoard(PRESET_BOARDS.audit)}
                className="px-2.5 py-1 rounded-md bg-white border border-indigo-200 text-xs font-semibold text-indigo-800 hover:bg-indigo-100"
              >
                AWS Audit
              </button>
              <Link
                href="/create"
                className="inline-flex items-center gap-1 px-3 py-1 rounded-md bg-indigo-600 text-white text-xs font-semibold hover:bg-indigo-700"
              >
                <PlusCircle className="w-3.5 h-3.5" />
                <span>Create Custom</span>
              </Link>
            </div>
          </div>
        )}

        {sourceMode === 'invalid' ? (
          <div className="rounded-2xl bg-white border border-amber-300 p-8 text-center space-y-4">
            <div className="w-12 h-12 rounded-full bg-amber-50 text-amber-600 flex items-center justify-center mx-auto border border-amber-200">
              <AlertTriangle className="w-6 h-6" />
            </div>
            <h1 className="font-display text-2xl font-bold text-slate-900">
              This Magic Link looks incomplete or corrupted
            </h1>
            <p className="text-[15px] text-slate-600 max-w-md mx-auto leading-relaxed">
              Magic links carry the entire milestone snapshot inside the URL fragment. Ask the
              sender to resend the full link, or load a live demo board below.
            </p>
            <div className="flex flex-wrap justify-center gap-3 pt-2">
              <button
                type="button"
                onClick={() => {
                  window.history.replaceState(null, '', '/m/');
                  setBoard(PRESET_BOARDS.sprint);
                  setSourceMode('demo');
                }}
                className="px-5 py-2.5 rounded-xl bg-indigo-600 text-white text-sm font-semibold hover:bg-indigo-700"
              >
                Load Sample Client Board
              </button>
              <Link
                href="/create"
                className="inline-flex items-center gap-1.5 px-5 py-2.5 rounded-xl border border-slate-300 bg-white text-slate-800 text-sm font-semibold hover:bg-slate-50"
              >
                <ArrowLeft className="w-4 h-4" />
                <span>Open Builder</span>
              </Link>
            </div>
          </div>
        ) : (
          <ClientBoardPreview
            board={board}
            interactive={true}
            onUpdateMilestone={handleClientUpdate}
          />
        )}
      </main>

      <Footer />

      <WaitlistModal
        open={waitlistOpen}
        initialTier={waitlistTier}
        onClose={() => setWaitlistOpen(false)}
      />
    </>
  );
}
