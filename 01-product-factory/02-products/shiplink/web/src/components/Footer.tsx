import React from 'react';
import Link from 'next/link';
import { Link2, ShieldCheck } from 'lucide-react';

export function Footer() {
  return (
    <footer className="mt-auto border-t border-slate-200 bg-white">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 py-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div className="space-y-2">
          <div className="inline-flex items-center gap-2 font-display font-bold text-slate-900">
            <span className="w-7 h-7 rounded-md bg-indigo-600 text-white flex items-center justify-center">
              <Link2 className="w-4 h-4" />
            </span>
            <span>ShipLink</span>
            <span className="text-xs font-mono text-slate-500">by ThinkLate Labs</span>
          </div>
          <p className="text-sm text-slate-600 max-w-md leading-relaxed">
            Built by Sarwan Singh (Lead Software &amp; AWS Serverless Architect). Zero-login client
            milestone tracking designed for friction-free engineering and agency delivery.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-5 text-[15px] font-medium text-slate-700">
          <Link href="/" className="hover:text-indigo-600 transition">
            Home
          </Link>
          <Link href="/create" className="hover:text-indigo-600 transition">
            Create Magic Link
          </Link>
          <Link href="/m" className="hover:text-indigo-600 transition">
            Client Demo
          </Link>
          <Link href="/architecture" className="hover:text-indigo-600 transition">
            System Architecture
          </Link>
        </div>
      </div>
      <div className="border-t border-slate-100 bg-slate-50/70">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 py-4 flex flex-col sm:flex-row items-center justify-between gap-2 text-sm text-slate-600">
          <span>Phase 1 Static Smoke-Test MVP — URL fragments stay local to your browser.</span>
          <span className="inline-flex items-center gap-1.5 text-emerald-700 font-medium">
            <ShieldCheck className="w-4 h-4" />
            <span>Zero tracking · No forced signup</span>
          </span>
        </div>
      </div>
    </footer>
  );
}
