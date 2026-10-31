import numpy as np, fk
import matplotlib.pyplot as plt
rng = np.random.default_rng(2026)
R = 30
p_hi = np.clip(rng.beta(30, 1.4, 200), 0, 1)
hi_rates = np.array([(rng.random(200) < p_hi).mean() for _ in range(R)])
print("true mean pass prob", p_hi.mean().round(4), "runs >=95%:", (hi_rates >= 0.95).sum())
fig = plt.figure(figsize=(fk.W, 3.25))
a = fig.add_axes([0.085, 0.19, 0.55, 0.64]); b = fig.add_axes([0.785, 0.24, 0.195, 0.55])
fig._r = fig.canvas.get_renderer()
for ax in (a, b):
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=9, colors=fk.MUTED)
x = np.arange(1, R + 1); ok = hi_rates >= 0.95
a.scatter(x[ok], hi_rates[ok] * 100, s=42, color=fk.FIX, marker="o", lw=0, label="passes", zorder=3)
a.scatter(x[~ok], hi_rates[~ok] * 100, s=58, color=fk.DEFECT, marker="X", lw=0, label="fails", zorder=3)
a.axhline(95, color=fk.INK, lw=1.4, ls=(0, (4, 2)))
a.text(R + 0.7, 95.12, "95% gate", va="bottom", fontsize=9, color=fk.INK, weight="bold")
a.set_xlim(0, R + 6.5); a.set_xticks([1, 10, 20, 30]); a.set_ylim(91, 99.5); a.set_yticks([92, 94, 96, 98])
a.set_xlabel("Repeat run of the same, unchanged agent", fontsize=9.5)
a.set_ylabel("Scenarios passed (%)", fontsize=9.5)
a.grid(axis="y", color=fk.RULE, lw=0.6); a.set_axisbelow(True)
a.legend(frameon=False, loc="lower left", fontsize=9, handletextpad=0.2, ncol=2, columnspacing=0.8)
fig.text(0.085, 0.955, "a", fontsize=13, weight="bold", family=fk.HEAD, va="top")
fig.text(0.115, 0.955, f"Point-score gate: passes {ok.sum()} of {R} runs", fontsize=10,
         weight="bold", family=fk.HEAD, va="top")
fig.text(0.115, 0.885, "Illustrative simulation, 200 high-risk scenarios. Not SAFE-CARE data.", fontsize=9,
         color=fk.MUTED, style="italic", va="top")
# panel b: exact probability that an agent with 3 flaky critical scenarios (each passes 90%) is released
p_run = 0.9 ** 3
ks = [1, 5, 10]; probs = [p_run ** k for k in ks]
cols = [fk.DEFECT, fk.RELEASE, fk.FIX]
b.barh(range(3)[::-1], [p * 100 for p in probs], color=cols, height=0.62)
for y, p in zip(range(3)[::-1], probs):
    b.text(p * 100 + 3, y, f"{p:.0%}", va="center", fontsize=12, weight="bold", family=fk.HEAD, color=fk.INK)
b.set_yticks(range(3)[::-1], ["1 run", "5 runs", "10 runs"], fontsize=9.5, color=fk.INK)
b.set_xlim(0, 100); b.set_xticks([0, 50, 100])
b.set_xlabel("Chance the flaky agent\nis released (%)", fontsize=9.5)
b.tick_params(axis="y", length=0); b.spines["left"].set_visible(False)
fig.text(0.70, 0.955, "b", fontsize=13, weight="bold", family=fk.HEAD, va="top")
fig.text(0.73, 0.955, "Zero-miss rule, K runs", fontsize=10, weight="bold", family=fk.HEAD, va="top")
fig.text(0.73, 0.885, "3 of 40 critical scenarios\npass 90% of the time", fontsize=9, color=fk.MUTED, style="italic", va="top")
fk.save(fig, "gate-noise")
