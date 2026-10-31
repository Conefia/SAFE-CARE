import fk
layers = ["Base model", "Approved evidence and citations", "Guardrails and escalation",
          "Profiling, read tools, time-aware context", "Write tools, closed-loop memory"]
levels = [("A0", "Unguided"), ("A1", "Grounded"), ("A2", "Guarded"), ("A3", "Personalized"), ("A4", "Agentic")]
shades = ["#C9DDF0", "#9DC3E6", "#6BA3D6", "#3A7FC0", fk.BUILD]
H = 3.73
fig, ax = fk.canvas(H)
lab_w, x0, cw, hdr = 1.42, 1.50, 0.98, 0.66
top = H - 0.04
rh, gap = 0.44, 0.07
# column headers: the layer each level adds
for j, name in enumerate(layers):
    x = x0 + j * cw
    fk.box(ax, x + 0.03, top - hdr, cw - 0.06, hdr, fc=fk.CHAR, ec=fk.CHAR, r=0.05)
    fk.text(ax, x + cw / 2, top - hdr / 2, ("" if j == 0 else "+ ") + name, size=8.5, weight="bold", color="white",
            ha="center", va="center", width=cw - 0.16, ls=1.1)
for i, (code, name) in enumerate(levels):
    y = top - hdr - 0.10 - (i + 1) * rh - i * gap
    fk.text(ax, 0.04, y + rh / 2, code, size=13, weight="bold", va="center", family=fk.HEAD, color=fk.BUILD)
    fk.text(ax, 0.50, y + rh / 2, name, size=10, weight="bold", va="center", family=fk.HEAD)
    for j in range(i + 1):
        x = x0 + j * cw
        new = j == i
        fk.box(ax, x + 0.03, y, cw - 0.06, rh, fc=shades[j], ec=fk.DEFECT if (new and i) else shades[j],
               lw=2.6 if (new and i) else 1.0, r=0.05)
        if new and i:
            fk.text(ax, x + cw / 2, y + rh / 2, f"Δ {levels[i-1][0]}→{code}", size=10, weight="bold",
                    color="white" if j >= 3 else fk.INK, ha="center", va="center")
foot = top - hdr - 0.10 - 5 * rh - 4 * gap - 0.10
fk.box(ax, x0 + 0.03, foot - 0.30, 0.34, 0.20, fc="white", ec=fk.DEFECT, lw=2.6, r=0.04)
fk.text(ax, x0 + 0.48, foot - 0.20, "The new group at each level. The difference between adjacent levels estimates what it adds, in this order.",
        size=9, va="center", width=6.46 - x0 - 0.48)
fk.save(fig, "ablation-ladder")
