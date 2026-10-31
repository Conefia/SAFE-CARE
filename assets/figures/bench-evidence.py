"""Figure: what the first published SAFE-CARE Bench run found.

Every number is read from the public SAFE-CARE Bench results (commit da7be4e):
  panel a  results/run_2026-09-01/analysis/P1_04_per_scenario_deltas.csv  (A1 -> A2, 9 in-scope scenarios)
  panel b  results/run_2026-09-08/rescoring_C1_C1prime_C2/P2_T1_agreement_matrix.csv  (M2 84.1%, M4 94.1%)
  panel c  results/run_2026-09-01/analysis/P1_01_guardrail_census.csv  (33 of 75 turns per tier; 12 of 36 enforced turns)
Panel a is recomputed from the file; panels b and c carry the counts read from the files named above.
Pass the Bench repository root as the first argument.
"""
import sys, csv, math, statistics as st
import numpy as np, fk
import matplotlib.pyplot as plt

DIMS = [("safety_singleturn", "Safety, single-turn"), ("safety_multiturn", "Safety, multi-turn"),
        ("escalation_singleturn", "Escalation, single-turn"), ("escalation_multiturn", "Escalation, multi-turn"),
        ("completeness", "Completeness"), ("medical_accuracy", "Medical accuracy")]
root = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/uploads/SAFE-CARE/safe-care-bench"
rows = list(csv.DictReader(open(f"{root}/results/run_2026-09-01/analysis/P1_04_per_scenario_deltas.csv", encoding="utf-8-sig")))
T8 = 2.306  # t, 8 degrees of freedom, two-sided 95%

fig = plt.figure(figsize=(fk.W, 4.75))
fig._r = fig.canvas.get_renderer()
a = fig.add_axes([0.255, 0.475, 0.555, 0.40])
b = fig.add_axes([0.20, 0.075, 0.25, 0.165])
c = fig.add_axes([0.70, 0.075, 0.25, 0.165])
for ax in (a, b, c):
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=9, colors=fk.MUTED)
for i, (key, lab) in enumerate(DIMS[::-1]):
    v = np.array([float(r["delta_A1_A2"]) for r in rows if r["dimension"] == key])
    m, se = v.mean(), v.std(ddof=1) / math.sqrt(len(v))
    col = fk.DEFECT if key == "medical_accuracy" else (fk.BUILD if key == "safety_singleturn" else fk.INK)
    jit = (np.random.default_rng(i).random(len(v)) - 0.5) * 0.30
    a.scatter(v, i + jit, s=16, color=fk.MUTED, alpha=0.45, lw=0, zorder=2)
    a.plot([m - T8 * se, m + T8 * se], [i, i], color=col, lw=2.4, solid_capstyle="round", zorder=3)
    a.plot(m, i, "o", color=col, ms=7, mec="white", mew=1.0, zorder=4)
    up, dn = int((v > 0).sum()), int((v < 0).sum())
    a.text(1.02, i, f"{up} up, {dn} down", transform=a.get_yaxis_transform(), fontsize=8.5, color=fk.INK, va="center")
    print(f"{key}: mean {m:+.4f} se {se:.4f} ci [{m - T8 * se:+.3f}, {m + T8 * se:+.3f}] up {up} down {dn}")
a.axvline(0, color=fk.INK, lw=1.0, ls=(0, (3, 2)), zorder=1)
a.set_yticks(range(len(DIMS)), [d[1] for d in DIMS[::-1]], fontsize=9.5, color=fk.INK)
a.tick_params(axis="y", length=0); a.spines["left"].set_visible(False)
a.set_xlim(-1.05, 1.05); a.set_xticks([-1, -0.5, 0, 0.5, 1])
a.set_xlabel("Change in score per scenario, A1 to A2", fontsize=9.5)
a.grid(axis="x", color=fk.RULE, lw=0.5); a.set_axisbelow(True)
fig.text(0.015, 0.985, "a", fontsize=13, weight="bold", family=fk.HEAD, va="top")
fig.text(0.045, 0.985, "Adding the guardrail flag, 9 scenarios", fontsize=10, weight="bold", family=fk.HEAD, va="top")
fig.text(0.045, 0.935, "Dot: mean. Bar: 95% interval. Grey: scenarios. Exploratory, uncorrected.", fontsize=8.5,
         color=fk.MUTED, style="italic", va="top")

def bars(ax, labels, vals, notes, colors, letter, title, x_title):
    ax.barh([1, 0], vals, color=colors, height=0.62)
    for y, v, n in zip([1, 0], vals, notes):
        ax.text(v + 1.5, y, f"{v:.1f}%  {n}", va="center", fontsize=8.5, color=fk.INK)
    ax.set_yticks([1, 0], labels, fontsize=9, color=fk.INK, linespacing=1.1)
    ax.tick_params(axis="y", length=0); ax.spines["left"].set_visible(False)
    ax.set_xlim(0, 80); ax.set_xticks([0, 25, 50])
    pos = ax.get_position()
    x0 = pos.x0 - (0.185 if letter == "b" else 0.20)
    fig.text(x0, pos.y1 + 0.115, letter, fontsize=13, weight="bold", family=fk.HEAD, va="top")
    fig.text(x0 + 0.03, pos.y1 + 0.115, title, fontsize=10, weight="bold", family=fk.HEAD, va="top")
    fig.text(x0 + 0.03, pos.y1 + 0.065, x_title, fontsize=8.5, color=fk.MUTED, style="italic", va="top")

bars(b, ["Three runs", "Two scorings,\nsame transcripts"], [100 - 84.1, 100 - 94.1], ["43 of 270", "16 of 270"],
     [fk.RELEASE, fk.CHAR], "b", "Scores changed across repeats", "In-scope cells that changed, dated judge snapshot")
bars(c, ["No judge at all", "No safety or\nescalation judge"], [100 * 33 / 75, 100 * 12 / 36], ["33 of 75", "12 of 36"],
     [fk.DEFECT, fk.DEFECT], "c", "What the judges never read", "In-scope turns per tier; enforced safety actions at A2")
fk.save(fig, "bench-evidence")
