import fk
layers = [
    ("Input safety gateway", "Screens each message for red flags, injection and out-of-scope requests before any reasoning."),
    ("Evidence and context", "Approved, versioned sources, plus confirmed and time-stamped facts about the user."),
    ("Orchestrator and model", "Plans the reply. The model sits here and nowhere else."),
    ("Governed tools", "Reads and writes only through permissioned tools, with confirmation, audit and rollback."),
    ("Output safety gateway", "Checks the draft for diagnosis, prescription and unsupported citations before display."),
]
H = 5.20
fig, ax = fk.canvas(H)
gx, gw = 0.04, 0.58           # governance bar (left)
lx, lw = 0.76, 4.24           # layers
rx, rw = 5.30, 1.16           # route bar (right)
rowh, gap = 0.70, 0.15
top = H - 0.50
# endpoints
fk.box(ax, lx, top + 0.08, lw, 0.40, fc=fk.PANEL, ec=fk.RULE)
fk.text(ax, lx + lw / 2, top + 0.28, "Patient message", size=10, weight="bold", ha="center", va="center", family=fk.HEAD)
ys = []
for i, (name, desc) in enumerate(layers):
    y = top - (i + 1) * (rowh + gap) + gap; ys.append(y)
    fk.box(ax, lx, y, lw, rowh, fc="white", ec=fk.BUILD, lw=1.6)
    fk.box(ax, lx, y, 0.10, rowh, fc=fk.BUILD, ec=fk.BUILD, lw=1.6, r=0.04)
    fk.text(ax, lx + 0.24, y + rowh - 0.07, name, size=10, weight="bold", family=fk.HEAD)
    fk.text(ax, lx + 0.24, y + rowh - 0.33, desc, size=9, width=lw - 0.36)
    prev = top + 0.08 if i == 0 else ys[i - 1]
    fk.arrow(ax, lx + lw / 2, prev - 0.005, lx + lw / 2, y + rowh + 0.005, color=fk.MUTED, lw=1.6)
    # every layer can route
    fk.arrow(ax, lx + lw + 0.01, y + rowh / 2, rx - 0.01, y + rowh / 2, color=fk.DEFECT, lw=1.6, ms=13)
yb = ys[-1] - gap - 0.40
fk.box(ax, lx, yb, lw, 0.40, fc=fk.PANEL, ec=fk.RULE)
fk.arrow(ax, lx + lw / 2, ys[-1] - 0.005, lx + lw / 2, yb + 0.405, color=fk.MUTED, lw=1.6)
fk.text(ax, lx + lw / 2, yb + 0.20, "Reply with citations and a next step", size=10, weight="bold", ha="center", va="center", family=fk.HEAD)
# route bar
ry0, ry1 = ys[-1], ys[0] + rowh
fk.box(ax, rx, ry0, rw, ry1 - ry0, fc=fk.DEFECT, ec=fk.DEFECT, lw=1.6)
fk.text(ax, rx + rw / 2, ry1 - 0.14, "ROUTE", size=11, weight="bold", color="white", ha="center", family=fk.HEAD)
fk.text(ax, rx + 0.12, ry1 - 0.52, "Risk found at any layer goes to a human or to emergency guidance, by fixed rules.",
        size=9.5, weight="bold", color="white", width=rw - 0.22)
fk.text(ax, rx + 0.12, ry0 + 0.12, "For example: heavy bleeding, chest pain, suicidal thoughts, a dose request.",
        size=9, color="white", width=rw - 0.22, va="bottom")
# governance bar
gy0, gy1 = yb, top + 0.48
fk.box(ax, gx, gy0, gw, gy1 - gy0, fc=fk.CHAR, ec=fk.CHAR, lw=1.2)
ax.text(gx + gw / 2 - 0.10, (gy0 + gy1) / 2, "GOVERNANCE AND MONITORING UNDER EVERY LAYER", rotation=90, fontsize=10,
        color="white", weight="bold", family=fk.HEAD, ha="center", va="center", zorder=7)
ax.text(gx + gw / 2 + 0.13, (gy0 + gy1) / 2, "safety card · registries · logs · evaluation · release gates · change control", rotation=90,
        fontsize=9, color="white", ha="center", va="center", zorder=7)
fk.save(fig, "architecture-v2")
