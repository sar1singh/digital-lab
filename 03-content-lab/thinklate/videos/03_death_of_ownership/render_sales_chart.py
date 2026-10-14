"""
ThinkLate (@wethinklate) — Video 03 Asset Generator
Renders Broadcast-Grade 20-Year Sales Divergence Chart:
Physical Software Collapse (90% -> 8%) vs Digital Software Soar (10% -> 92%)
Outputs:
  1. assets/CHART_SALES_COLLAPSE.png (1080p full slate with dark studio aesthetic)
  2. assets/CHART_SALES_COLLAPSE_transparent.png (Floating card with transparent background)
  3. assets/CHART_SALES_COLLAPSE_4K.png (4K 3840x2160 master)
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from matplotlib.patches import FancyBboxPatch, Circle

# Configure Matplotlib for ultra-clean rendering
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Inter', 'Montserrat', 'DejaVu Sans', 'Arial']
plt.rcParams['text.color'] = '#F8FAFC'
plt.rcParams['axes.labelcolor'] = '#94A3B8'
plt.rcParams['xtick.color'] = '#94A3B8'
plt.rcParams['ytick.color'] = '#94A3B8'

# Output directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# 20-Year Historical Industry Data (Circana / GSD / ESA / Newzoo)
years = np.array([2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024])
physical_pct = np.array([90.0, 86.0, 80.0, 71.0, 62.0, 52.0, 42.0, 31.0, 19.0, 12.0, 8.0])
digital_pct = np.array([10.0, 14.0, 20.0, 29.0, 38.0, 48.0, 58.0, 69.0, 81.0, 88.0, 92.0])

# Smooth spline interpolation for silky broadcast curves
from scipy.interpolate import make_interp_spline
years_smooth = np.linspace(years.min(), years.max(), 300)
spl_phys = make_interp_spline(years, physical_pct, k=3)
spl_dig = make_interp_spline(years, digital_pct, k=3)
physical_smooth = np.clip(spl_phys(years_smooth), 0, 100)
digital_smooth = np.clip(spl_dig(years_smooth), 0, 100)

def render_chart(transparent=False, is_4k=False):
    width, height = (3840, 2160) if is_4k else (1920, 1080)
    dpi = 200 if is_4k else 100
    figsize = (width / dpi, height / dpi)
    
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    
    # Background styling
    if transparent:
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
        # Frosted glass floating card backing with subtle border
        rect = FancyBboxPatch((0.04, 0.05), 0.92, 0.90, transform=fig.transFigure,
                              boxstyle="round,pad=0.02,rounding_size=0.03",
                              facecolor='#0B1120', edgecolor='#334155', linewidth=2.5,
                              zorder=-1, alpha=0.88)
        fig.patches.append(rect)
    else:
        fig.patch.set_facecolor('#070B14')
        ax.patch.set_facecolor('#0B1120')
        
        # Add subtle card border on non-transparent version
        rect = FancyBboxPatch((0.04, 0.05), 0.92, 0.90, transform=fig.transFigure,
                              boxstyle="round,pad=0.02,rounding_size=0.03",
                              facecolor='#0F172A', edgecolor='#1E293B', linewidth=2,
                              zorder=-1, alpha=0.95)
        fig.patches.append(rect)
    
    # Margins and layout
    plt.subplots_adjust(left=0.10, right=0.90, top=0.82, bottom=0.14)
    
    # Colors
    crimson = '#EF4444'      # Physical Collapse
    crimson_glow = '#F87171'
    cyan = '#06B6D4'         # Digital Explosion
    cyan_glow = '#38BDF8'
    gold = '#F59E0B'
    grid_col = '#1E293B'
    
    # Grid lines
    ax.grid(True, which='both', color=grid_col, linestyle='--', linewidth=0.8, alpha=0.6, zorder=1)
    ax.set_axisbelow(True)
    
    # Shaded Area Fills
    ax.fill_between(years_smooth, physical_smooth, color=crimson, alpha=0.14, zorder=2)
    ax.fill_between(years_smooth, digital_smooth, color=cyan, alpha=0.14, zorder=2)
    
    # Glow / Stroke effects on main lines
    glow_effect_phys = [
        path_effects.Stroke(linewidth=12, foreground=crimson, alpha=0.25),
        path_effects.Stroke(linewidth=7, foreground=crimson_glow, alpha=0.45),
        path_effects.Normal()
    ]
    glow_effect_dig = [
        path_effects.Stroke(linewidth=12, foreground=cyan, alpha=0.25),
        path_effects.Stroke(linewidth=7, foreground=cyan_glow, alpha=0.45),
        path_effects.Normal()
    ]
    
    line_phys = ax.plot(years_smooth, physical_smooth, color='#FCA5A5', linewidth=4.0, zorder=4, path_effects=glow_effect_phys)
    line_dig = ax.plot(years_smooth, digital_smooth, color='#E0F2FE', linewidth=4.0, zorder=4, path_effects=glow_effect_dig)
    
    # Historical Data Points
    ax.scatter(years, physical_pct, color=crimson, edgecolor='#FFFFFF', s=70, linewidth=2, zorder=5)
    ax.scatter(years, digital_pct, color=cyan, edgecolor='#FFFFFF', s=70, linewidth=2, zorder=5)
    
    # Crossover 50/50 Inflection Line (2015)
    ax.axvline(x=2015, color='#64748B', linestyle=':', linewidth=2.0, alpha=0.7, zorder=3)
    ax.text(2015, 50, '  THE FLIP (2015)\n  50% / 50%', color='#CBD5E1', fontsize=12,
            fontweight='bold', verticalalignment='center', zorder=6,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#0F172A', edgecolor='#334155', alpha=0.9))
    
    # Axes limits and ticks
    ax.set_xlim(2003.5, 2024.5)
    ax.set_ylim(0, 105)
    ax.set_xticks(years)
    ax.set_xticklabels([str(y) for y in years], fontsize=13, fontweight='bold')
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'], fontsize=13, fontweight='bold')
    
    # Spines styling
    for spine in ax.spines.values():
        spine.set_color('#334155')
        spine.set_linewidth(1.5)
        
    # Headers & Super-Titles
    fig.text(0.10, 0.93, "GLOBAL VIDEO GAME SOFTWARE REVENUE (2004 — 2024)",
             fontsize=14, fontweight='bold', color=gold)
    fig.text(0.10, 0.86, "The 20-Year Extinction of Physical Media",
             fontsize=26, fontweight='heavy', color='#F8FAFC')
    fig.text(0.90, 0.86, "SOURCE: Circana / GSD / Newzoo Reports",
             fontsize=11, fontweight='normal', color='#64748B', horizontalalignment='right')
    
    # Key Empirical Callout Badges
    # 1. 2004 Physical Peak Callout
    ax.annotate(
        "2004: 90% PHYSICAL\nDiscs Dominate",
        xy=(2004, 90), xytext=(2005.5, 96),
        arrowprops=dict(facecolor=crimson, shrink=0.08, width=2, headwidth=8),
        fontsize=12, fontweight='bold', color='#FFFFFF',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#7F1D1D', edgecolor=crimson, linewidth=1.5, alpha=0.95),
        zorder=7
    )
    
    # 2. 2024 Physical Collapse Callout
    ax.annotate(
        "2024: 8% PHYSICAL\n▼ 91% COLLAPSE",
        xy=(2024, 8), xytext=(2019.5, 12),
        arrowprops=dict(facecolor=crimson, shrink=0.08, width=2, headwidth=8),
        fontsize=13, fontweight='heavy', color='#FCA5A5',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#450A0A', edgecolor=crimson, linewidth=2.0, alpha=0.98),
        zorder=7
    )
    
    # 3. 2024 Digital Monopoly Callout
    ax.annotate(
        "2024: 92% DIGITAL\n▲ STOREFRONT MONOPOLY",
        xy=(2024, 92), xytext=(2018.5, 84),
        arrowprops=dict(facecolor=cyan, shrink=0.08, width=2, headwidth=8),
        fontsize=13, fontweight='heavy', color='#E0F2FE',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#083344', edgecolor=cyan, linewidth=2.0, alpha=0.98),
        zorder=7
    )
    
    # Legend Pills in Upper Left Inside Chart
    ax.plot([], [], color=cyan, linewidth=4, label='DIGITAL SALES (92%) — Revocable Software Licenses')
    ax.plot([], [], color=crimson, linewidth=4, label='PHYSICAL SALES (8%) — Resellable / Permanent Media')
    leg = ax.legend(loc='upper left', bbox_to_anchor=(0.02, 0.76), frameon=True, fontsize=12,
                    facecolor='#0F172A', edgecolor='#334155', framealpha=0.95)
    for text in leg.get_texts():
        text.set_color('#F1F5F9')
        text.set_fontweight('bold')
        
    # Bottom Note
    fig.text(0.10, 0.07, "ThinkLate Investigation: Over 90% of gaming revenue now flows through closed digital storefronts with zero resale rights.",
             fontsize=11, color='#94A3B8', style='italic')

    # Save
    if transparent:
        out_path = os.path.join(ASSETS_DIR, "CHART_SALES_COLLAPSE_transparent.png")
    elif is_4k:
        out_path = os.path.join(ASSETS_DIR, "CHART_SALES_COLLAPSE_4K.png")
    else:
        out_path = os.path.join(ASSETS_DIR, "CHART_SALES_COLLAPSE.png")
        
    plt.savefig(out_path, dpi=dpi, facecolor=fig.get_facecolor(), edgecolor='none', transparent=transparent)
    plt.close()
    print(f"[SUCCESS] Exported: {out_path} ({width}x{height})")
    return out_path

if __name__ == "__main__":
    print("=== Rendering ThinkLate Video 03 Broadcast Chart ===")
    p1 = render_chart(transparent=False, is_4k=False)
    p2 = render_chart(transparent=True, is_4k=False)
    p3 = render_chart(transparent=False, is_4k=True)
    print("=== All 3 chart variants successfully generated! ===")
