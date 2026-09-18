#!/usr/bin/env python3
"""
ThinkLate animated charts.

Static charts are why the earlier set looked like a slide deck. These render
motion: lines draw on, bars grow, numbers count up, shares fill in.

Output: MP4 with alpha-free solid background (import straight into Resolve),
plus optional GIF for quick review.

Usage
-----
    python3 animate.py                     # render the demo set

    from animate import line_draw, bars_grow, counter, share_fill
    line_draw(df, x="t", ys=["Railways"], title="...", source="...",
              highlight="Railways", out="charts/v01_manias", seconds=6)

Timing guidance
---------------
    A chart that draws on over 4-6 seconds and then HOLDS for 30-60 is the
    correct grammar for long-form. Do not loop. Do not cut away at 3s.
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation, FFMpegWriter, PillowWriter

from brand import AMBER, SLATE, PAPER, PAPER_DIM, INK, GRID, INK_SOFT
from charts import _frame, _pick, _colors, MPL_MONO, MPL_SERIF, FIGSIZE, DPI

HERE = os.path.dirname(os.path.abspath(__file__))
FPS = 30


# ----------------------------------------------------------------- helpers
def _ease(t):
    """Ease-out cubic. Motion should decelerate — linear reads mechanical."""
    return 1 - (1 - t) ** 3


def _chrome(fig, source):
    fig.text(0.085, 0.045, source, fontsize=15, color=PAPER_DIM,
             family="monospace", fontname=_pick(MPL_MONO))
    fig.text(0.955, 0.045, "ThinkLate", fontsize=15, color=PAPER_DIM,
             family="serif", fontname=_pick(MPL_SERIF), ha="right")


def _save(anim, out, gif=False):
    path = out if os.path.isabs(out) else os.path.join(HERE, out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    mp4 = f"{path}.mp4"
    anim.save(mp4, writer=FFMpegWriter(fps=FPS, bitrate=8000,
                                       extra_args=["-pix_fmt", "yuv420p"]))
    made = [mp4]
    if gif:
        g = f"{path}.gif"
        anim.save(g, writer=PillowWriter(fps=15))
        made.append(g)
    plt.close("all")
    return made


# ----------------------------------------------------------------- 1. line draw-on
def line_draw(df, x, ys, title, source, subtitle=None, highlight=None,
              ylabel=None, seconds=5, hold=1.5, out="charts/anim_line",
              gif=False):
    """Lines draw left to right. The core motion for any time series."""
    fig, ax = _frame(title, subtitle)
    _chrome(fig, source)
    cmap = _colors(ys, highlight)

    xs = df[x].values
    # reserve right-hand room for the trailing series labels
    span = xs.max() - xs.min()
    ax.set_xlim(xs.min(), xs.max() + span * 0.22)
    lo = min(df[c].min() for c in ys)
    hi = max(df[c].max() for c in ys)
    pad = (hi - lo) * 0.12
    ax.set_ylim(lo - pad, hi + pad)
    if ylabel:
        ax.set_ylabel(ylabel)

    lines, labels = {}, {}
    for c in ys:
        lw = 4.5 if c == highlight else 2.4
        lines[c], = ax.plot([], [], color=cmap[c], linewidth=lw,
                            zorder=3 if c == highlight else 2)
        labels[c] = ax.annotate(
            "", (0, 0), color=cmap[c], fontsize=20,
            fontweight="bold" if c == highlight else "normal",
            va="center", xytext=(10, 0), textcoords="offset points")

    draw_f = int(seconds * FPS)
    total = draw_f + int(hold * FPS)

    def frame(i):
        raw = min(i / draw_f, 1.0)
        t = _ease(raw)
        n = max(int(t * len(xs)), 1)
        # labels only appear once the draw is nearly done — otherwise they
        # track across the plot and collide with the title
        show = raw > 0.80
        for c in ys:
            lines[c].set_data(xs[:n], df[c].values[:n])
            labels[c].xy = (xs[n - 1], df[c].values[n - 1])
            labels[c].set_position((xs[n - 1], df[c].values[n - 1]))
            labels[c].set_text(f" {c}" if show else "")
        return list(lines.values()) + list(labels.values())

    anim = FuncAnimation(fig, frame, frames=total, interval=1000 / FPS,
                         blit=False)
    return _save(anim, out, gif)


# ----------------------------------------------------------------- 2. bars grow
def bars_grow(labels, values, title, source, subtitle=None, highlight=None,
              pct=False, seconds=4, hold=1.5, stagger=0.12,
              out="charts/anim_bars", gif=False):
    """Bars grow in sequence, not together. Sequence directs the eye."""
    longest = max(len(str(l)) for l in labels)
    left = min(0.085 + 0.0105 * longest, 0.30)
    fig, ax = _frame(title, subtitle, left=left)
    _chrome(fig, source)

    cols = [AMBER if l == highlight else SLATE for l in labels]
    ypos = np.arange(len(labels))
    bars = ax.barh(ypos, [0] * len(labels), color=cols, height=0.62)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlim(0, max(values) * 1.16)
    ax.grid(True, axis="x", alpha=0.55)
    ax.grid(False, axis="y")

    texts = [ax.annotate("", (0, y), xytext=(10, 0),
                         textcoords="offset points", va="center", fontsize=19,
                         color=AMBER if labels[i] == highlight else PAPER_DIM,
                         fontweight="bold" if labels[i] == highlight else "normal")
             for i, y in enumerate(ypos)]

    grow_f = int(seconds * FPS)
    stag_f = int(stagger * FPS)
    total = grow_f + stag_f * len(labels) + int(hold * FPS)

    def frame(i):
        for k, (b, v) in enumerate(zip(bars, values)):
            local = (i - k * stag_f) / grow_f
            t = _ease(min(max(local, 0.0), 1.0))
            b.set_width(v * t)
            texts[k].xy = (v * t, ypos[k])
            texts[k].set_position((v * t, ypos[k]))
            texts[k].set_text(f"{v * t:,.0f}{'%' if pct else ''}" if t > 0.02 else "")
        return list(bars) + texts

    anim = FuncAnimation(fig, frame, frames=total, interval=1000 / FPS,
                         blit=False)
    return _save(anim, out, gif)


# ----------------------------------------------------------------- 3. counter
def counter(value, label, sub="", source="", prefix="", suffix="",
            seconds=2.2, hold=2.0, out="charts/anim_counter", gif=False):
    """
    The kicker number, counting up. Replaces the static kicker card.
    3-6 seconds total. This is the frame that makes a number land.
    """
    plt.rcParams.update({"figure.facecolor": INK, "axes.facecolor": INK,
                         "savefig.facecolor": INK})
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off")

    num = ax.text(0.5, 0.56, "", fontsize=150, color=AMBER, ha="center",
                  va="center", family="serif", fontname=_pick(MPL_SERIF))
    ax.text(0.5, 0.36, label, fontsize=40, color=PAPER, ha="center",
            va="center", family="sans-serif")
    if sub:
        ax.text(0.5, 0.29, sub, fontsize=26, color=PAPER_DIM, ha="center",
                va="center", family="sans-serif")
    rule = ax.add_patch(plt.Rectangle((0.5, 0.44), 0.0, 0.005,
                                      color=AMBER, transform=ax.transAxes))
    if source:
        _chrome(fig, source)

    up_f = int(seconds * FPS)
    total = up_f + int(hold * FPS)

    def frame(i):
        t = _ease(min(i / up_f, 1.0))
        num.set_text(f"{prefix}{value * t:,.0f}{suffix}")
        rule.set_width(0.09 * t)
        rule.set_x(0.5 - 0.045 * t)
        return [num, rule]

    anim = FuncAnimation(fig, frame, frames=total, interval=1000 / FPS,
                         blit=False)
    return _save(anim, out, gif)


# ----------------------------------------------------------------- 4. share fill
def share_fill(df, x, ys, title, source, subtitle=None, highlight=None,
               seconds=5, hold=1.5, out="charts/anim_share", gif=False):
    """Composition fills in over time. For 'who came to control what'."""
    fig, ax = _frame(title, subtitle)
    _chrome(fig, source)
    shades = [AMBER if n == highlight else c for n, c in
              zip(ys, [SLATE, "#4B5563", "#374151", INK_SOFT, "#0F1621"])]

    xs = df[x].values
    ax.set_xlim(xs.min(), xs.max())
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))

    draw_f = int(seconds * FPS)
    total = draw_f + int(hold * FPS)
    handles = []

    def frame(i):
        nonlocal handles
        for h in handles:
            h.remove()
        t = _ease(min(i / draw_f, 1.0))
        n = max(int(t * len(xs)), 2)
        handles = list(ax.stackplot(xs[:n], *[df[c].values[:n] for c in ys],
                                    colors=shades))
        return handles

    anim = FuncAnimation(fig, frame, frames=total, interval=1000 / FPS,
                         blit=False)
    return _save(anim, out, gif)


# ----------------------------------------------------------------- demo
def render_demo(gif=True):
    made = []

    made += bars_grow(
        ["China", "United States", "Myanmar", "Australia", "Rest of world"],
        [69, 12, 11, 5, 3],
        title="Rare earth mine production, share of global output",
        subtitle="Illustrative — verify against USGS before publishing",
        source="Source: placeholder · replace with USGS Mineral Commodity Summaries",
        highlight="China", pct=True, out="preview/anim_01_bars", gif=gif)

    df = pd.DataFrame({
        "t": list(range(0, 11)),
        "Railways 1840s": [100, 140, 195, 260, 330, 380, 300, 190, 120, 95, 88],
        "Telecom 1990s":  [100, 155, 220, 300, 395, 470, 340, 170, 95, 70, 62],
        "Dot-com":        [100, 160, 250, 360, 500, 560, 380, 200, 140, 118, 110],
    })
    made += line_draw(
        df, x="t", ys=["Railways 1840s", "Telecom 1990s", "Dot-com"],
        title="Three manias, indexed to their own starting point",
        subtitle="Illustrative shape only",
        source="Source: placeholder · replace before publishing",
        highlight="Railways 1840s", out="preview/anim_02_line", gif=gif)

    made += counter(
        90, "OF ADVANCED CHIPS", "made on one island",
        suffix="%", source="Source: placeholder · verify before publishing",
        out="preview/anim_03_counter", gif=gif)

    return made


if __name__ == "__main__":
    for p in render_demo():
        print(p)
