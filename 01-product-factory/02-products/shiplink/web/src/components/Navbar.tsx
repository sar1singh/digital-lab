'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Link2, Menu, X, Sparkles } from 'lucide-react';

interface NavbarProps {
  onOpenWaitlist?: (tier?: 'solo-19' | 'team-39' | 'ltd-69' | 'audit-consult') => void;
}

export function Navbar({ onOpenWaitlist }: NavbarProps) {
  const pathname = usePathname() || '/';
  const [mobileOpen, setMobileOpen] = useState(false);

  const navItems = [
    { href: '/', label: 'Home' },
    { href: '/create', label: 'Create Magic Link' },
    { href: '/m', label: 'Live Client Demo' },
    { href: '/architecture', label: 'Architecture' },
  ];

  const isActive = (href: string) => {
    if (href === '/') return pathname === '/' || pathname === '';
    return pathname.startsWith(href);
  };

  return (
    <header className="sticky top-0 z-40 border-b border-slate-200/80 bg-white/90 backdrop-blur-md">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between gap-4">
        <Link
          href="/"
          className="inline-flex items-center gap-2.5 font-display font-extrabold text-lg tracking-tight text-slate-900 hover:opacity-90 transition"
        >
          <span className="w-8 h-8 rounded-lg bg-indigo-600 text-white flex items-center justify-center shadow-sm shadow-indigo-600/25">
            <Link2 className="w-4 h-4" />
          </span>
          <span>ShipLink</span>
          <span className="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-slate-100 text-slate-700 border border-slate-200">
            Zero-Login
          </span>
        </Link>

        <nav className="hidden md:flex items-center gap-1" aria-label="Main navigation">
          {navItems.map((item) => {
            const active = isActive(item.href);
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`px-3.5 py-2 rounded-lg text-[15px] font-medium transition ${
                  active
                    ? 'bg-indigo-50 text-indigo-700 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100/70'
                }`}
              >
                {item.label}
              </Link>
            );
          })}
        </nav>

        <div className="hidden md:flex items-center gap-2.5">
          {onOpenWaitlist && (
            <button
              type="button"
              onClick={() => onOpenWaitlist('solo-19')}
              className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 text-sm font-medium transition"
            >
              <Sparkles className="w-4 h-4 text-indigo-600" />
              <span>Pro Waitlist</span>
            </button>
          )}
          <Link
            href="/create"
            className="inline-flex items-center justify-center px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold shadow-sm shadow-indigo-600/20 transition"
          >
            Create Free Link
          </Link>
        </div>

        <button
          type="button"
          onClick={() => setMobileOpen((prev) => !prev)}
          className="md:hidden p-2 rounded-lg border border-slate-200 text-slate-700 hover:bg-slate-100"
          aria-label="Toggle menu"
        >
          {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
        </button>
      </div>

      {mobileOpen && (
        <div className="md:hidden border-t border-slate-200 bg-white px-4 py-4 space-y-2">
          {navItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              onClick={() => setMobileOpen(false)}
              className={`block px-3.5 py-2.5 rounded-lg text-[15px] font-medium ${
                isActive(item.href)
                  ? 'bg-indigo-50 text-indigo-700 font-semibold'
                  : 'text-slate-700 hover:bg-slate-100'
              }`}
            >
              {item.label}
            </Link>
          ))}
          <div className="pt-2 flex flex-col gap-2">
            {onOpenWaitlist && (
              <button
                type="button"
                onClick={() => {
                  setMobileOpen(false);
                  onOpenWaitlist('solo-19');
                }}
                className="w-full py-2.5 rounded-lg border border-slate-200 text-slate-800 text-[15px] font-medium"
              >
                Join Pro Early Access
              </button>
            )}
            <Link
              href="/create"
              onClick={() => setMobileOpen(false)}
              className="w-full py-2.5 rounded-lg bg-indigo-600 text-white text-[15px] font-semibold text-center"
            >
              Create Free Link
            </Link>
          </div>
        </div>
      )}
    </header>
  );
}
