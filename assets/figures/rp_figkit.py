"""rp_figkit: print-ready research figures in matplotlib.

import rp_figkit as rk
fig, ax = rk.figure("double", 2.4)        # width preset, height in inches
rk.dot_interval(ax, rows)                 # forest plot with optional raw points
rk.save(fig, "fig_results")               # PDF (fonts embedded) + 300 dpi PNG + overflow report
"""
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)

# ---- tokens ---------------------------------------------------------------
WIDTH = {"single": 3.5, "onehalf": 5.0, "double": 7.2}   # inches; 89 / 127 / 183 mm
INK, MUTED, RULE, PANEL = "#1F2328", "#5B6470", "#C9CED6", "#F4F5F7"
# Okabe-Ito hues in an order that passes the dataviz validator (adjacent CVD dE >= 9.6)
CAT = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#56B4E9", "#CC79A7"]
SEQ = "Blues"                                             # one hue, light to dark
DIV = "RdBu_r"                                            # two hues, neutral midpoint
DEFECT, DEFECT_FILL = "#C0462B", "#FBE9E2"
FIX, FIX_FILL = "#2E7D5B", "#E3F1EA"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"],
    "font.size": 7, "axes.titlesize": 7, "axes.labelsize": 7,
    "xtick.labelsize": 6, "ytick.labelsize": 6, "legend.fontsize": 6,
    "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "lines.linewidth": 1.0, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "text.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.prop_cycle": matplotlib.cycler(color=CAT),
    "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none",
    "figure.dpi": 150, "savefig.dpi": 300,
})


def figure(width="double", height=2.4, ncols=1, nrows=1, **kw):
    w = WIDTH.get(width, width)
    fig, ax = plt.subplots(nrows, ncols, figsize=(w, height), constrained_layout=True, **kw)
    return fig, ax


def panel_label(ax, letter, title=""):
    """Bold panel letter plus optional short title, placed as the axes title so layout makes room."""
    ax.set_title(f"$\\bf{{{letter}}}$  {title}" if title else f"$\\bf{{{letter}}}$",
                 loc="left", fontsize=8 if not title else 7)


# ---- diagram primitives (axes coordinates on an axis-off canvas) ---------
def canvas(width="double", height=3.0):
    fig = plt.figure(figsize=(WIDTH.get(width, width), height))
    ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    return fig, ax


def card(ax, x, y, w, h, fc="white", ec=RULE, lw=0.8, r=0.012):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                 fc=fc, ec=ec, lw=lw, transform=ax.transAxes, zorder=2))


def chip(ax, x, y, label, fc=INK, color="white", size=5.5):
    ax.text(x, y, label.upper(), transform=ax.transAxes, fontsize=size, color=color,
            fontweight="bold", va="top", zorder=4,
            bbox=dict(boxstyle="round,pad=0.25,rounding_size=0.2", fc=fc, ec="none"))


def text(ax, x, y, s, size=6.4, color=INK, weight="normal", ha="left", va="top",
         wrap=None, style="normal"):
    if wrap:
        s = "\n".join(textwrap.fill(p, wrap) for p in s.split("\n"))
    return ax.text(x, y, s, fontsize=size, color=color, weight=weight, ha=ha, va=va,
                   style=style, transform=ax.transAxes, zorder=3, linespacing=1.25)


def arrow(ax, x0, y0, x1, y1, color=MUTED, lw=0.9):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=7,
                 color=color, lw=lw, transform=ax.transAxes, zorder=4))


# ---- chart templates -------------------------------------------------------
def dot_interval(ax, rows, ref=0.0, xlabel="Mean difference", show_counts=True):
    """Forest plot. rows: dicts with label, est, lo, hi, optional points (raw unit values),
    optional note (e.g. '0 up, 6 down, 3 same'), optional highlight=True."""
    for i, r in enumerate(rows[::-1]):
        c = DEFECT if r.get("highlight") else CAT[0]
        if r.get("points") is not None:
            pts = np.asarray(r["points"], float)
            jitter = (np.random.default_rng(i).random(len(pts)) - 0.5) * 0.25
            ax.scatter(pts, i + jitter, s=8, color=MUTED, alpha=0.6, lw=0, zorder=2)
        ax.plot([r["lo"], r["hi"]], [i, i], color=c, lw=1.4, solid_capstyle="round", zorder=3)
        ax.plot(r["est"], i, "o", color=c, ms=4.5, mec="white", mew=0.8, zorder=4)
        if show_counts and r.get("note"):
            ax.text(1.02, i, r["note"], transform=ax.get_yaxis_transform(), fontsize=5.8,
                    color=MUTED, va="center")
    ax.axvline(ref, color=MUTED, lw=0.6, ls=(0, (3, 2)), zorder=1)
    ax.set_yticks(range(len(rows)), [r["label"] for r in rows[::-1]])
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel(xlabel)
    ax.grid(axis="x", color=RULE, lw=0.4); ax.set_axisbelow(True)


def slope(ax, labels, before, after, xticks=("Before", "After"), groups=None, fmt="{:.0f}"):
    """Paired before/after per unit, labels at the line ends (no legend)."""
    for i, (lab, b, a) in enumerate(zip(labels, before, after)):
        c = CAT[(groups[i] if groups else i) % len(CAT)]
        ax.plot([0, 1], [b, a], "-o", color=c, ms=3, lw=1.1)
    _end_labels(ax, 1.04, [f"{l} {fmt.format(a)}" for l, a in zip(labels, after)], after)
    ax.set_xticks([0, 1], xticks); ax.set_xlim(-0.08, 1.45)
    ax.spines["bottom"].set_visible(False); ax.tick_params(axis="x", length=0)


def _end_labels(ax, x, texts, ys, min_gap_frac=0.07):
    """Direct labels at line ends, pushed apart so they never collide."""
    lo, hi = ax.get_ylim(); gap = (hi - lo) * min_gap_frac
    order = np.argsort(ys); placed = []
    for k in order:
        y = ys[k] if not placed else max(ys[k], placed[-1] + gap)
        placed.append(y)
        ax.text(x, y, texts[k], color=INK, fontsize=5.8, va="center")


def stacked_share(ax, categories, parts, part_labels, colors=None, pct=True, min_label=0.07):
    """100% stacked bars with in-bar percentages; parts: list of arrays (one per part)."""
    parts = np.asarray(parts, float); tot = parts.sum(0); share = parts / tot
    colors = colors or CAT; left = np.zeros(len(categories))
    for k, (row, lab) in enumerate(zip(share, part_labels)):
        ax.barh(categories, row, left=left, color=colors[k], edgecolor="white", lw=1, label=lab)
        for j, v in enumerate(row):
            if v >= min_label:
                rgb = matplotlib.colors.to_rgb(colors[k])
                lum = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
                ax.text(left[j] + v / 2, j, f"{v:.0%}" if pct else f"{parts[k][j]:.0f}",
                        ha="center", va="center", fontsize=5.8, fontweight="bold",
                        color="white" if lum < 0.55 else INK)
        left += row
    ax.set_xlim(0, 1); ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    ax.legend(ncol=len(part_labels), loc="upper left", bbox_to_anchor=(0, -0.28), frameon=False,
              handlelength=1, columnspacing=1)
    ax.invert_yaxis(); ax.tick_params(axis="y", length=0)


def heatmap(ax, mat, rows, cols, center=None, cmap=None, fmt="{:.2f}", vmin=None, vmax=None,
            cbar_label=None):
    """Annotated heatmap. Diverging (centered) when center is given, else sequential."""
    mat = np.asarray(mat, float)
    if center is not None:
        span = np.nanmax(np.abs(mat - center)); vmin, vmax = center - span, center + span
    im = ax.imshow(mat, cmap=cmap or (DIV if center is not None else SEQ), vmin=vmin, vmax=vmax,
                   aspect="auto")
    for (i, j), v in np.ndenumerate(mat):
        if not np.isnan(v):
            rgba = im.cmap(im.norm(v)); lum = 0.299 * rgba[0] + 0.587 * rgba[1] + 0.114 * rgba[2]
            ax.text(j, i, fmt.format(v), ha="center", va="center", fontsize=5.8,
                    color="white" if lum < 0.5 else INK)
    ax.set_xticks(range(len(cols)), cols); ax.set_yticks(range(len(rows)), rows)
    ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    cb = plt.colorbar(im, ax=ax, fraction=0.04, pad=0.02); cb.outline.set_visible(False)
    if cbar_label: cb.set_label(cbar_label)
    return im


def small_multiples(axes, panels, x, xlabel=None, ylabel=None, n_under=None):
    """Same y-scale line panels. panels: list of (title, {series: values}); labels at line ends."""
    ymin = min(min(v) for _, d in panels for v in d.values())
    ymax = max(max(v) for _, d in panels for v in d.values())
    for ax, (title, d) in zip(np.ravel(axes), panels):
        for k, (name, vals) in enumerate(d.items()):
            ax.plot(range(len(x)), vals, "-o", color=CAT[k % len(CAT)], ms=2.5, lw=1)
        ax.set_xlim(-0.25, len(x) - 1 + 0.9)
        ax.set_title(title, loc="left", fontweight="bold")
        ax.set_ylim(ymin - 0.05 * (ymax - ymin), ymax + 0.05 * (ymax - ymin))
        ax.set_xticks(range(len(x)), x if n_under is None else
                      [f"{a}\nn={b}" for a, b in zip(x, n_under)])
        ax.grid(axis="y", color=RULE, lw=0.4); ax.set_axisbelow(True)
        _end_labels(ax, len(x) - 1 + 0.12, list(d.keys()), [v[-1] for v in d.values()])
    if ylabel: np.ravel(axes)[0].set_ylabel(ylabel)
    if xlabel:
        for ax in np.ravel(axes): ax.set_xlabel(xlabel)


# ---- quality gate ----------------------------------------------------------
def overflow_report(fig):
    """List text that leaves the figure or collides with other text. Empty list = clean."""
    fig.canvas.draw(); r = fig.canvas.get_renderer(); fb = fig.bbox
    items = [t for t in fig.findobj(matplotlib.text.Text) if t.get_visible() and t.get_text().strip()]
    boxes = [(t, t.get_window_extent(r)) for t in items]
    issues = []
    for t, b in boxes:
        if b.x0 < fb.x0 - 1 or b.x1 > fb.x1 + 1 or b.y0 < fb.y0 - 1 or b.y1 > fb.y1 + 1:
            issues.append(f"outside figure: {t.get_text()[:40]!r}")
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a, b = boxes[i][1], boxes[j][1]
            if a.overlaps(b) and a.width * a.height > 0 and b.width * b.height > 0:
                ov = (min(a.x1, b.x1) - max(a.x0, b.x0)) * (min(a.y1, b.y1) - max(a.y0, b.y0))
                if ov > 0.15 * min(a.width * a.height, b.width * b.height):
                    issues.append(f"overlap: {boxes[i][0].get_text()[:25]!r} x "
                                  f"{boxes[j][0].get_text()[:25]!r}")
    return issues


def save(fig, name, check=True):
    issues = overflow_report(fig) if check else []
    fig.savefig(f"{name}.pdf", bbox_inches="tight", pad_inches=0.02)
    fig.savefig(f"{name}.png", dpi=300, bbox_inches="tight", pad_inches=0.02)
    print(f"{name}: {'clean' if not issues else str(len(issues)) + ' issue(s)'}")
    for s in issues: print("  -", s)
    return issues
