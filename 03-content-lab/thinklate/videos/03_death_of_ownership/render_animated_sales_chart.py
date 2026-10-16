"""
ThinkLate (@wethinklate) — Video 03 Animated Chart Generator
Renders Broadcast-Grade 1080p60 MP4: 20-Year Sales Divergence Chart
Physical Software Collapse (90% -> 8%) vs Digital Software Soar (10% -> 92%)
Outputs: assets/CHART_SALES_COLLAPSE_animated.mp4
"""

import os
import subprocess
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from matplotlib.patches import FancyBboxPatch
from scipy.interpolate import make_interp_spline

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)
OUT_MP4 = os.path.join(ASSETS_DIR, "CHART_SALES_COLLAPSE_animated.mp4")

# Configure Matplotlib fonts and styling
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']

# Historical Data
years = np.array([2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024])
physical_pct = np.array([90.0, 86.0, 80.0, 71.0, 62.0, 52.0, 42.0, 31.0, 19.0, 12.0, 8.0])
digital_pct = np.array([10.0, 14.0, 20.0, 29.0, 38.0, 48.0, 58.0, 69.0, 81.0, 88.0, 92.0])

# Spline interpolation (500 smooth points)
n_points = 500
years_smooth = np.linspace(years.min(), years.max(), n_points)
spl_phys = make_interp_spline(years, physical_pct, k=3)
spl_dig = make_interp_spline(years, digital_pct, k=3)
phys_smooth = np.clip(spl_phys(years_smooth), 0, 100)
dig_smooth = np.clip(spl_dig(years_smooth), 0, 100)

# Animation Specs
FPS = 30
DURATION_SEC = 8
TOTAL_FRAMES = FPS * DURATION_SEC  # 240 frames
DRAW_FRAMES = int(FPS * 5.5)       # 5.5 seconds drawing, 2.5 seconds hold

WIDTH, HEIGHT = 1920, 1080
DPI = 100

print(f"[INFO] Initializing Animated Chart Pipeline ({WIDTH}x{HEIGHT} @ {FPS}fps, {TOTAL_FRAMES} frames)...")

# Setup FFmpeg process for direct raw pipe
ffmpeg_cmd = [
    'ffmpeg', '-y',
    '-f', 'rawvideo',
    '-vcodec', 'rawvideo',
    '-s', f'{WIDTH}x{HEIGHT}',
    '-pix_fmt', 'rgba',
    '-r', str(FPS),
    '-i', '-',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-preset', 'fast',
    '-crf', '18',
    OUT_MP4
]

proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

fig = plt.figure(figsize=(WIDTH / DPI, HEIGHT / DPI), dpi=DPI)
fig.patch.set_facecolor('#070B14')

for f in range(TOTAL_FRAMES):
    fig.clf()
    ax = fig.add_axes([0.10, 0.16, 0.82, 0.64])
    ax.set_facecolor('#0B1120')
    
    # Progress: 0.0 to 1.0 (with smooth cubic ease-out)
    if f < DRAW_FRAMES:
        t = f / DRAW_FRAMES
        # ease out cubic: 1 - (1 - t)^3
        progress = 1 - pow(1 - t, 3)
    else:
        progress = 1.0
        
    curr_idx = max(2, int(progress * n_points))
    sub_years = years_smooth[:curr_idx]
    sub_phys = phys_smooth[:curr_idx]
    sub_dig = dig_smooth[:curr_idx]
    
    current_year = sub_years[-1]
    curr_phys_val = sub_phys[-1]
    curr_dig_val = sub_dig[-1]
    
    # Gridlines
    ax.grid(True, linestyle='--', color='#1E293B', alpha=0.7, zorder=0)
    ax.set_xlim(2003.5, 2024.5)
    ax.set_ylim(-2, 105)
    ax.set_xticks(years)
    ax.set_yticks([0, 20, 40, 50, 60, 80, 100])
    ax.set_yticklabels(['0%', '20%', '40%', '50%', '60%', '80%', '100%'], color='#94A3B8', fontsize=13, fontweight='bold')
    ax.set_xticklabels([str(y) for y in years], color='#94A3B8', fontsize=14, fontweight='bold')
    
    # Spines
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    for s in ['bottom', 'left']:
        ax.spines[s].set_color('#334155')
        ax.spines[s].set_linewidth(1.5)
        
    # 50% Parity Line
    ax.axhline(50, color='#64748B', linestyle=':', linewidth=1.8, alpha=0.5, zorder=1)
    
    # Area fills under curves
    ax.fill_between(sub_years, sub_phys, color='#EF4444', alpha=0.10, zorder=2)
    ax.fill_between(sub_years, sub_dig, color='#06B6D4', alpha=0.10, zorder=2)
    
    # Curve lines
    glow_eff_red = [path_effects.Stroke(linewidth=10, foreground='#EF4444', alpha=0.25),
                    path_effects.Stroke(linewidth=6, foreground='#EF4444', alpha=0.45),
                    path_effects.Normal()]
    glow_eff_cyan = [path_effects.Stroke(linewidth=10, foreground='#06B6D4', alpha=0.25),
                     path_effects.Stroke(linewidth=6, foreground='#06B6D4', alpha=0.45),
                     path_effects.Normal()]
                     
    ax.plot(sub_years, sub_phys, color='#EF4444', linewidth=4.5, path_effects=glow_eff_red, zorder=4)
    ax.plot(sub_years, sub_dig, color='#06B6D4', linewidth=4.5, path_effects=glow_eff_cyan, zorder=4)
    
    # Draw historical dots passed so far
    for y_val, p_val, d_val in zip(years, physical_pct, digital_pct):
        if y_val <= current_year:
            ax.scatter(y_val, p_val, color='#EF4444', s=60, edgecolors='#FFFFFF', linewidth=1.5, zorder=5)
            ax.scatter(y_val, d_val, color='#06B6D4', s=60, edgecolors='#FFFFFF', linewidth=1.5, zorder=5)
            
    # Leading pulse tip dots
    ax.scatter(current_year, curr_phys_val, color='#FFFFFF', s=160, edgecolors='#EF4444', linewidth=3.5, zorder=7)
    ax.scatter(current_year, curr_dig_val, color='#FFFFFF', s=160, edgecolors='#06B6D4', linewidth=3.5, zorder=7)
    
    # Dynamic live badges tracking the line tips
    ax.text(current_year - 0.2, curr_phys_val + 6, f"PHYSICAL: {curr_phys_val:.0f}%",
            color='#F8FAFC', fontsize=13, fontweight='bold', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#7F1D1D', edgecolor='#EF4444', linewidth=1.5, alpha=0.95), zorder=8)
            
    ax.text(current_year - 0.2, curr_dig_val - 8, f"DIGITAL: {curr_dig_val:.0f}%",
            color='#F8FAFC', fontsize=13, fontweight='bold', ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#083344', edgecolor='#06B6D4', linewidth=1.5, alpha=0.95), zorder=8)
            
    # 2013 Crossover Point Badge (appears when current_year >= 2013)
    if current_year >= 2013.2:
        ax.scatter(2013.4, 50, color='#F59E0B', s=180, marker='*', zorder=6)
        ax.text(2013.4, 56, "2013: PARITY CROSSOVER (50/50)",
                color='#FDE68A', fontsize=11, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#451A03', edgecolor='#F59E0B', linewidth=1.2, alpha=0.9), zorder=6)
                
    # Headers & Super-titles
    fig.text(0.10, 0.94, "INDUSTRY DATA CITATION • 2004 – 2024", color='#F59E0B', fontsize=13, fontweight='bold', family='sans-serif')
    fig.text(0.10, 0.89, "THE 20-YEAR EXTINCTION OF PHYSICAL OWNERSHIP", color='#F8FAFC', fontsize=26, fontweight='bold', family='sans-serif')
    fig.text(0.10, 0.85, "Physical disc sales collapsed from 90% to 8%, while revocable digital licenses reached 92%.", color='#94A3B8', fontsize=14, family='sans-serif')
    
    # Legend & Source Footnote
    fig.text(0.10, 0.08, "● PHYSICAL MEDIA (DISCS / CARTS)", color='#EF4444', fontsize=13, fontweight='bold')
    fig.text(0.38, 0.08, "● DIGITAL DOWNLOADS (STEAM / PSN / XBOX)", color='#06B6D4', fontsize=13, fontweight='bold')
    fig.text(0.92, 0.08, "SOURCE: Circana (NPD) / GSD / ESA / Valve Market Reports", color='#64748B', fontsize=11, ha='right', style='italic')
    
    # Canvas frame buffer extraction
    fig.canvas.draw()
    rgba_buffer = fig.canvas.buffer_rgba()
    proc.stdin.write(rgba_buffer)
    
    if (f + 1) % 60 == 0 or f == TOTAL_FRAMES - 1:
        print(f"[PROGRESS] Rendered {f + 1}/{TOTAL_FRAMES} frames ({(f + 1)/TOTAL_FRAMES*100:.1f}%)...")

plt.close(fig)
proc.stdin.close()
proc.wait()

print(f"[SUCCESS] Broadcast Animated Chart Generated: {OUT_MP4}")
