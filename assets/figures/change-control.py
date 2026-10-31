import fk
cols = ["Safety\ncore", "Escalation", "Knowledge", "Memory", "Tools", "Scope", "Timing"]
F, O = "full", "if"
rows = [
    ("Model version or snapshot",       [F, F, F, F, F, F, F]),
    ("System prompt or instructions",   [F, F, O, O, O, F, O]),
    ("Retrieval corpus or sources",     [F, O, F, O, "", O, ""]),
    ("Guardrail or filter rules",       [F, F, O, "", "", O, O]),
    ("Session or long-term memory"  , [F, O, "", F, O, "", O]),
    ("Tool definitions or permissions", [F, O, "", O, F, "", O]),
    ("Orchestration or routing logic",  [F, F, "", "", O, "", F]),
    ("No declared change (periodic)",   [F, O, O, O, O, O, O]),
]
H = 4.16
fig, ax = fk.canvas(H)
lab_w, cw, hdr, rh = 1.9, 0.64, 0.50, 0.37
cws = [0.62, 0.74, 0.74, 0.64, 0.54, 0.54, 0.56]
x0 = 6.46 - sum(cws)
cx = [x0 + sum(cws[:j]) + cws[j] / 2 for j in range(len(cws))]
top = H - 0.04
# header band
fk.box(ax, x0, top - hdr, sum(cws), hdr, fc=fk.CHAR, ec=fk.CHAR, r=0.05)
fk.text(ax, 0.04, top - hdr / 2, "Type of change", size=10, weight="bold", va="center", family=fk.HEAD)
for j, c in enumerate(cols):
    fk.text(ax, cx[j], top - hdr / 2, c, size=8.5, weight="bold", color="white", ha="center", va="center", ls=1.05)
y0 = top - hdr - 0.06
# safety-core column highlight
fk.rect(ax, x0, y0 - len(rows) * rh, cws[0], len(rows) * rh, fc=fk.DEFECT_FILL, z=0)
for i, (lab, cells) in enumerate(rows):
    yc = y0 - (i + 0.5) * rh
    if i % 2: fk.rect(ax, 0.02, yc - rh / 2, x0 - 0.02, rh, fc=fk.PANEL, z=0); fk.rect(ax, x0 + cws[0], yc - rh / 2, sum(cws[1:]), rh, fc=fk.PANEL, z=0)
    fk.text(ax, 0.06, yc, lab, size=9.5, va="center", width=x0 - 0.12)
    for j, c in enumerate(cells):
        xc = cx[j]
        if j == 0:
            ax.scatter(xc, yc, s=150, color=fk.DEFECT, marker="s", zorder=5, lw=0)
        elif c == F:
            ax.scatter(xc, yc, s=150, color=fk.EVAL, zorder=5, lw=0)
        elif c == O:
            ax.scatter(xc, yc, s=130, facecolor="white", edgecolor=fk.EVAL, lw=2.0, zorder=5)
yl = y0 - len(rows) * rh - 0.24
items = [("s", fk.DEFECT, fk.DEFECT, "Safety core, re-run unchanged every time"),
         ("o", fk.EVAL, fk.EVAL, "Re-test"), ("o", "white", fk.EVAL, "Re-test if the impact analysis says so")]
xs = [0.10, 3.35, 4.25]
for (m, fc, ec, t), x in zip(items, xs):
    ax.scatter(x, yl, s=120, marker=m, facecolor=fc, edgecolor=ec, lw=2.0 if fc == "white" else 0, zorder=5)
    fk.text(ax, x + 0.14, yl, t, size=9, va="center", width=3.1 if x < 1 else (0.8 if x < 4 else 2.2))
fk.save(fig, "change-control")
