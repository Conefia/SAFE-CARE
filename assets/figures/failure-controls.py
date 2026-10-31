import fk
cols = ["Evidence\nlayer", "Input and\noutput\nguardrails", "Escalation", "Governed\ntools", "Memory\nand context", "Governance\nand\nmonitoring"]
P, S = 2, 1
rows = [
    ("Hallucination",                [P, S, 0, 0, 0, 0]),
    ("Unsafe advice",                [0, P, 0, 0, 0, 0]),
    ("Missing escalation",           [0, S, P, 0, 0, 0]),
    ("Overdiagnosis, overclaiming",  [0, P, 0, 0, S, 0]),
    ("Lack of personalization",      [0, 0, 0, P, P, 0]),
    ("Tool misuse",                  [0, 0, 0, P, 0, S]),
    ("Memory misuse",                [0, 0, 0, 0, P, 0]),
    ("Citation laundering",          [P, S, 0, 0, 0, 0]),
    ("Overreliance",                 [0, S, P, 0, 0, 0]),
    ("Privacy failure",              [0, 0, 0, 0, 0, P]),
]
H = 4.50
fig, ax = fk.canvas(H)
cw, hdr, rh = 0.735, 0.68, 0.305
x0 = 6.46 - len(cols) * cw
top = H - 0.04
fk.box(ax, x0, top - hdr, len(cols) * cw, hdr, fc=fk.CHAR, ec=fk.CHAR, r=0.05)
fk.text(ax, 0.04, top - hdr / 2, "Failure mode", size=10, weight="bold", va="center", family=fk.HEAD)
for j, c in enumerate(cols):
    fk.text(ax, x0 + (j + 0.5) * cw, top - hdr / 2, c, size=8.5, weight="bold", color="white", ha="center", va="center", ls=1.05)
y0 = top - hdr - 0.06
for i, (lab, cells) in enumerate(rows):
    yc = y0 - (i + 0.5) * rh
    if i % 2: fk.rect(ax, 0.02, yc - rh / 2, 6.44, rh, fc=fk.PANEL, z=0)
    fk.text(ax, 0.06, yc, lab, size=9.5, va="center")
    for j, c in enumerate(cells):
        xc = x0 + (j + 0.5) * cw
        if c == P: ax.scatter(xc, yc, s=150, color=fk.BUILD, zorder=5, lw=0)
        elif c == S: ax.scatter(xc, yc, s=130, facecolor="white", edgecolor=fk.BUILD, lw=2.0, zorder=5)
yl = y0 - len(rows) * rh - 0.24
for x, fc, t in [(0.12, fk.BUILD, "Primary control"), (1.75, "white", "Supporting control")]:
    ax.scatter(x, yl, s=130, facecolor=fc, edgecolor=fk.BUILD, lw=2.0, zorder=5)
    fk.text(ax, x + 0.16, yl, t, size=9, va="center")
fk.text(ax, 6.46, yl, "Evaluation tests every row.", size=9, va="center", ha="right", weight="bold")
fk.save(fig, "failure-controls")
