#!/usr/bin/env python3
"""
ThinkLate chart pipeline.

CSV or list in -> on-brand SVG + PNG out. Source line baked into every chart.
This is the file that turns your biggest bottleneck into your fastest step.

Usage
-----
    python3 charts.py                       # render the demo set

    from charts import line, bars, stacked_share, slope
    line(df, x="year", ys=["uk","us"], title="...", source="...",
         highlight="us", out="charts/v01_gdp")

Every function writes <out>.svg and <out>.png and returns (svg_path, png_path).

Rules enforced by this module, deliberately:
  - one accent colour per chart (the series you name in `highlight`)
  - no dual axes
  - no pie charts
  - source line always present
  - max 5 series (raises if exceeded)
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

from brand import (
    INK, PAPER, AMBER, SLATE, BRICK, INK_SOFT, PAPER_DIM, GRID,
    MPL_SERIF, MPL_SANS, MPL_MONO, SIZE,
)

HERE = os.path.dirname(os.path.abspath(__file__))
FIGSIZE = (16, 9)      # 16:9
DPI = 120              # 1920x1080
MAX_SERIES = 5


# ----------------------------------------------------------------- base style
def _style():
    plt.rcParams.update({
        "figure.facecolor":  INK,
        "axes.facecolor":    INK,
        "savefig.facecolor": INK,
        "text.color":        PAPER,
        "axes.labelcolor":   PAPER_DIM,
        "xtick.color":       PAPER_DIM,
        "ytick.color":       PAPER_DIM,
        "axes.edgecolor":    GRID,
        "grid.color":        GRID,
        "grid.linewidth":    0.8,
        "font.family":       "sans-serif",
        "font.sans-serif":   MPL_SANS,
        "font.size":         18,
        "axes.titlesize":    32,
        "axes.labelsize":    18,
        "legend.frameon":    False,
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "figure.autolayout": False,
    })


def _frame(title, subtitle=None, left=0.085):
    _style()
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.subplots_adjust(left=left, right=0.955, top=0.78, bottom=0.16)
    if title:
        fig.text(0.085, 0.925, title, fontsize=38, color=PAPER,
                 family="serif", fontname=_pick(MPL_SERIF), va="top")
    if subtitle:
        fig.text(0.085, 0.855, subtitle, fontsize=21, color=PAPER_DIM, va="top")
    ax.grid(True, axis="y", alpha=0.55)
    ax.set_axisbelow(True)
    return fig, ax


def _pick(candidates):
    """First installed font from the list, else matplotlib default."""
    from matplotlib import font_manager
    have = {f.name for f in font_manager.fontManager.ttflist}
    for c in candidates:
        if c in have:
            return c
    return candidates[-1]


def _finish(fig, out, source):
    fig.text(0.085, 0.045, source, fontsize=15, color=PAPER_DIM,
             family="monospace", fontname=_pick(MPL_MONO))
    fig.text(0.955, 0.045, "ThinkLate", fontsize=15, color=PAPER_DIM,
             family="serif", fontname=_pick(MPL_SERIF), ha="right")
    path = out if os.path.isabs(out) else os.path.join(HERE, out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    svg, png = f"{path}.svg", f"{path}.png"
    fig.savefig(svg, format="svg")
    fig.savefig(png, format="png")
    plt.close(fig)
    return svg, png


def _colors(names, highlight):
    """One amber series. Everything else recedes."""
    out = {}
    for n in names:
        out[n] = AMBER if n == highlight else SLATE
    return out


def _check(ys):
    if len(ys) > MAX_SERIES:
        raise ValueError(
            f"{len(ys)} series requested; max is {MAX_SERIES}. "
            "Split into two charts — the viewer cannot track more than five lines."
        )


# ----------------------------------------------------------------- chart types
def line(df, x, ys, title, source, subtitle=None, highlight=None,
         ylabel=None, pct=False, out="charts/line", annotate_last=True):
    _check(ys)
    fig, ax = _frame(title, subtitle)
    cmap = _colors(ys, highlight)
    for name in ys:
        lw = 4.5 if name == highlight else 2.4
        z = 3 if name == highlight else 2
        ax.plot(df[x], df[name], color=cmap[name], linewidth=lw, zorder=z)
        if annotate_last:
            ax.annotate(
                f" {name}", (df[x].iloc[-1], df[name].iloc[-1]),
                color=cmap[name], fontsize=20,
                fontweight="bold" if name == highlight else "normal",
                va="center", xytext=(10, 0), textcoords="offset points")
    if ylabel:
        ax.set_ylabel(ylabel)
    if pct:
        ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
    ax.margins(x=0.06)
    return _finish(fig, out, source)


def bars(labels, values, title, source, subtitle=None, highlight=None,
         ylabel=None, pct=False, horizontal=True, out="charts/bars"):
    # horizontal bars need room for the category labels on the left
    if horizontal:
        longest = max(len(str(l)) for l in labels)
        left = min(0.085 + 0.0105 * longest, 0.30)
    else:
        left = 0.085
    fig, ax = _frame(title, subtitle, left=left)
    cols = [AMBER if (highlight is not None and l == highlight) else SLATE
            for l in labels]
    if horizontal:
        ax.barh(labels, values, color=cols, height=0.62)
        ax.invert_yaxis()
        ax.grid(True, axis="x", alpha=0.55)
        ax.grid(False, axis="y")
        for l, v in zip(labels, values):
            ax.annotate(f"{v:,.0f}{'%' if pct else ''}", (v, l),
                        xytext=(10, 0), textcoords="offset points",
                        va="center", fontsize=19,
                        color=AMBER if l == highlight else PAPER_DIM,
                        fontweight="bold" if l == highlight else "normal")
        ax.margins(x=0.13)
    else:
        ax.bar(labels, values, color=cols, width=0.62)
        if pct:
            ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
    if ylabel:
        ax.set_ylabel(ylabel)
    return _finish(fig, out, source)


def stacked_share(df, x, ys, title, source, subtitle=None, highlight=None,
                  out="charts/share"):
    """Composition over time. Use for 'who controls what share'."""
    _check(ys)
    fig, ax = _frame(title, subtitle)
    shades = [AMBER if n == highlight else c for n, c in
              zip(ys, [SLATE, "#4B5563", "#374151", INK_SOFT, "#0F1621"])]
    ax.stackplot(df[x], *[df[n] for n in ys], colors=shades, labels=ys)
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
    ax.legend(loc="upper left", fontsize=18, labelcolor=PAPER_DIM, ncol=len(ys))
    ax.margins(x=0)
    return _finish(fig, out, source)


def slope(before_label, after_label, items, title, source, subtitle=None,
          highlight=None, out="charts/slope"):
    """
    items: {name: (before_value, after_value)}
    Two-point comparison. Strongest chart for 'what changed'.
    """
    fig, ax = _frame(title, subtitle)
    for name, (b, a) in items.items():
        c = AMBER if name == highlight else SLATE
        lw = 4.5 if name == highlight else 2.2
        ax.plot([0, 1], [b, a], color=c, linewidth=lw, marker="o", markersize=11)
        ax.annotate(f"{name}  {b:,.0f}", (0, b), xytext=(-14, 0),
                    textcoords="offset points", ha="right", va="center",
                    color=c, fontsize=19)
        ax.annotate(f"{a:,.0f}", (1, a), xytext=(14, 0),
                    textcoords="offset points", ha="left", va="center",
                    color=c, fontsize=19,
                    fontweight="bold" if name == highlight else "normal")
    ax.set_xticks([0, 1])
    ax.set_xticklabels([before_label, after_label], fontsize=22, color=PAPER)
    ax.set_xlim(-0.34, 1.34)
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.set_yticks([])
    return _finish(fig, out, source)


def from_csv(path, **kw):
    """Convenience: charts.from_csv('data/x.csv', x='year', ys=['a'], ...)"""
    df = pd.read_csv(path if os.path.isabs(path) else os.path.join(HERE, path))
    return line(df, **kw)


# ----------------------------------------------------------------- demo
def render_demo():
    made = []

    # 1. bars — rare earth concentration. Illustrative values; verify with USGS.
    made.append(bars(
        ["China", "United States", "Myanmar", "Australia", "Rest of world"],
        [69, 12, 11, 5, 3],
        title="Rare earth mine production, share of global output",
        subtitle="Illustrative figures — verify against USGS before publishing",
        source="Source: placeholder · replace with USGS Mineral Commodity Summaries",
        highlight="China", pct=True, out="preview/chart_01_bars"))

    # 2. line — bubble comparison, indexed
    df = pd.DataFrame({
        "t": list(range(0, 11)),
        "Railways 1840s": [100, 140, 195, 260, 330, 380, 300, 190, 120, 95, 88],
        "Telecom 1990s":  [100, 155, 220, 300, 395, 470, 340, 170, 95, 70, 62],
        "Dot-com":        [100, 160, 250, 360, 500, 560, 380, 200, 140, 118, 110],
    })
    made.append(line(
        df, x="t", ys=["Railways 1840s", "Telecom 1990s", "Dot-com"],
        title="Three manias, indexed to their own starting point",
        subtitle="Illustrative shape only — not real index values",
        source="Source: placeholder · replace before publishing",
        highlight="Railways 1840s", out="preview/chart_02_line"))

    # 3. slope — before/after
    made.append(slope(
        "Before Red Sea disruption", "After",
        {"Suez route (days)": (26, 26),
         "Cape of Good Hope (days)": (26, 36),
         "Cost index": (100, 148)},
        title="What rerouting around Africa actually costs",
        subtitle="Illustrative — verify with UNCTAD / carrier data",
        source="Source: placeholder · replace before publishing",
        highlight="Cost index", out="preview/chart_03_slope"))

    # 4. stacked share
    df2 = pd.DataFrame({
        "year": [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025],
        "Taiwan":   [8, 14, 22, 34, 45, 55, 62, 68],
        "Korea":    [6, 10, 14, 16, 17, 16, 15, 14],
        "US":       [40, 33, 27, 21, 16, 13, 11, 10],
        "Japan":    [38, 33, 26, 19, 13, 9, 6, 4],
        "Other":    [8, 10, 11, 10, 9, 7, 6, 4],
    })
    made.append(stacked_share(
        df2, x="year", ys=["Taiwan", "Korea", "US", "Japan", "Other"],
        title="Nobody planned this concentration",
        subtitle="Illustrative shares — verify before publishing",
        source="Source: placeholder · replace before publishing",
        highlight="Taiwan", out="preview/chart_04_share"))

    return made


if __name__ == "__main__":
    for svg, png in render_demo():
        print(svg)
