import fk
stages = [
    ("1", "DESIGN", "Scope · Anchor", "Write the safety card before choosing a model. Ground every health claim in approved, versioned evidence.", fk.BUILD, "white"),
    ("2", "BUILD", "Fence · Contextualize · Act · Route", "Layer the guardrails, govern every tool, and make escalation deterministic.", fk.BUILD, "white"),
    ("3", "EVALUATE", "Evaluate", "Run the ablation ladder on held-out scenarios. Qualify the instrument first: noise floor, clinician band, judge distance.", fk.EVAL, "white"),
    ("4", "RELEASE", "Gate", "Any critical miss blocks release. Every other gate is read against a confidence bound, never a point score.", fk.RELEASE, "white"),
    ("5", "OPERATE", "Evidence", "Monitor the running agent and confirm it is the approved one. Every incident becomes a new test.", fk.OPERATE, fk.INK),
]
H = 4.55
fig, ax = fk.canvas(H)
top, rowh, gap = H - 0.06, 0.74, 0.16
lw_, x_mid, x_end = 1.42, 1.62, 5.22
ys = []
for i, (n, name, princ, desc, c, tc) in enumerate(stages):
    y = top - rowh - i * (rowh + gap); ys.append(y)
    fk.box(ax, 0.04, y, x_end - 0.04, rowh, fc="white", ec=c, lw=1.6)
    fk.box(ax, 0.04, y, lw_, rowh, fc=c, ec=c, lw=1.6)
    fk.text(ax, 0.16, y + rowh / 2, n, size=20, weight="bold", color=tc, va="center", family=fk.HEAD)
    fk.text(ax, 0.50, y + rowh / 2, name, size=10.5, weight="bold", color=tc, va="center", family=fk.HEAD)
    fk.text(ax, x_mid, y + rowh - 0.08, princ, size=10, weight="bold", family=fk.HEAD)
    fk.text(ax, x_mid, y + rowh - 0.31, desc, size=9, color=fk.INK, width=x_end - x_mid - 0.12)
    if i:
        fk.arrow(ax, 0.04 + lw_ / 2, ys[i - 1] - 0.005, 0.04 + lw_ / 2, y + rowh + 0.005, color=fk.MUTED, lw=1.6)
# feedback loop: Operate back to Evaluate, on the right margin
y_op, y_ev = ys[4] + rowh / 2, ys[2] + rowh / 2
xl = x_end + 0.17
ax.plot([x_end + 0.01, xl, xl], [y_op, y_op, y_ev], color=fk.OPERATE, lw=2.6, solid_capstyle="round", solid_joinstyle="round", zorder=6)
fk.arrow(ax, xl + 0.01, y_ev, x_end + 0.005, y_ev, color=fk.OPERATE, lw=2.6, ms=16)
fk.text(ax, x_end + 0.30, (y_op + y_ev) / 2, "Any change to model, prompt, sources or tools re-enters at Evaluate", size=9,
        weight="bold", va="center", color=fk.INK, width=6.48 - x_end - 0.30)
fk.save(fig, "lifecycle-loop")
