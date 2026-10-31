"""fk: inch-based diagram kit for the SAFE-CARE white paper v2.0 figures.

Figures are drawn at their print size (6.5 in, the text width of the Conefia letterhead)
and inserted 1:1, so every point size below is the size on the page.
Body text 9 to 9.5 pt, headings 10 to 11 pt, nothing under 8.5 pt.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import rp_figkit as rk

W = 6.5
INK, MUTED, RULE, PANEL = rk.INK, rk.MUTED, rk.RULE, "#F2F3F5"
# one colour per lifecycle stage, used in every figure (darkened Okabe-Ito so white text passes contrast)
BUILD = "#0067A5"     # Design and Build (blue)
EVAL = "#00785A"      # Evaluate (bluish green)
RELEASE = "#B34A00"   # Release (vermillion)
OPERATE = "#E69F00"   # Operate (orange; carries ink text, not white)
DEFECT, DEFECT_FILL = "#B3261E", "#FBE4E1"
FIX, FIX_FILL = "#1E6B4A", "#E1F2E8"
CHAR = "#26292E"      # Conefia charcoal for header bands
HEAD = "Poppins"
BODY = "Liberation Sans"

plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": [BODY, "DejaVu Sans"],
                     "font.size": 9, "xtick.labelsize": 9, "ytick.labelsize": 9,
                     "axes.labelsize": 9.5, "legend.fontsize": 9})


def canvas(h, w=W):
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off"); ax.set_xlim(0, w); ax.set_ylim(0, h)
    fig._r = fig.canvas.get_renderer()
    return fig, ax


def _width(fig, s, size, weight, family):
    t = fig.text(0, 0, s, fontsize=size, weight=weight, family=family)
    w = t.get_window_extent(fig._r).width / fig.dpi
    t.remove()
    return w


def wrap(fig, s, width, size=9, weight="normal", family=BODY):
    out = []
    for para in s.split("\n"):
        line = ""
        for word in para.split():
            trial = (line + " " + word).strip()
            if line and _width(fig, trial, size, weight, family) > width:
                out.append(line); line = word
            else:
                line = trial
        out.append(line)
    return "\n".join(out)


def text(ax, x, y, s, size=9, color=INK, weight="normal", ha="left", va="top", width=None,
         family=BODY, style="normal", ls=1.22, z=5):
    if width:
        s = wrap(ax.figure, s, width, size, weight, family)
    return ax.text(x, y, s, fontsize=size, color=color, weight=weight, ha=ha, va=va, family=family,
                   style=style, linespacing=ls, zorder=z)


def box(ax, x, y, w, h, fc="white", ec=RULE, lw=1.0, r=0.06, z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                 fc=fc, ec=ec, lw=lw, zorder=z))


def rect(ax, x, y, w, h, fc, ec="none", lw=0, z=1):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, zorder=z))


def arrow(ax, x0, y0, x1, y1, color=MUTED, lw=1.4, ms=12, z=6, cs=None):
    kw = dict(arrowstyle="-|>", mutation_scale=ms, color=color, lw=lw, zorder=z)
    if cs: kw["connectionstyle"] = cs
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), **kw))


def pill(ax, x, y, s, fc, color="white", size=9, ha="left", va="center"):
    ax.text(x, y, s, fontsize=size, color=color, weight="bold", family=HEAD, ha=ha, va=va, zorder=7,
            bbox=dict(boxstyle="round,pad=0.32,rounding_size=0.55", fc=fc, ec="none"))


def save(fig, name):
    issues = rk.overflow_report(fig)
    small = sorted({round(t.get_fontsize(), 1) for t in fig.findobj(matplotlib.text.Text)
                    if t.get_visible() and t.get_text().strip() and t.get_fontsize() < 8.5})
    fig.savefig(f"{name}.pdf", pad_inches=0)
    fig.savefig(f"{name}.png", dpi=300, pad_inches=0)
    print(f"{name}: {'clean' if not issues else str(len(issues)) + ' issue(s)'}"
          f"{'' if not small else '  SMALL TEXT ' + str(small)}")
    for s in issues: print("  -", s)
