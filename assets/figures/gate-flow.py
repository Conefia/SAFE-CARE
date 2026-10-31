import fk
steps = [
    ("1", "HARD FAIL", "Run the critical suite K times", "Any miss, on any run, in any scenario, blocks release. One clean run is not enough.", fk.DEFECT, "BLOCK", fk.DEFECT),
    ("2", "BOUNDS", "Read each gate against a bound", "Compare the one-sided lower 95% bound of the pass rate with the threshold, never the point score.", fk.RELEASE, "FIX, THEN NEW RUNS", fk.RELEASE),
    ("3", "BASELINE", "Compare with the original baseline", "A decline must stay inside a margin fixed in advance. A gain inside the noise floor is not claimed.", fk.RELEASE, "BLOCK IF BEYOND", fk.DEFECT),
    ("4", "ERRORS SPLIT", "Report escalation errors apart", "Missed and unnecessary escalation, each over its own denominator, plus timing.", fk.RELEASE, "BOTH RATES SHOWN", fk.CHAR),
    ("5", "SIGN-OFF", "Named owners decide", "Owners sign, accept residual risk in writing, and record the configuration hash.", fk.RELEASE, "GO OR NO-GO", fk.FIX),
]
H = 4.22
fig, ax = fk.canvas(H)
top, rowh, gap = H - 0.04, 0.64, 0.10
lb, xm, xo = 1.38, 1.52, 4.86
ys = []
for i, (n, chip, head, body, c, out, oc) in enumerate(steps):
    y = top - rowh - i * (rowh + gap); ys.append(y)
    fk.box(ax, 0.04, y, xo - 0.12, rowh, fc="white", ec=c, lw=1.6)
    fk.box(ax, 0.04, y, lb, rowh, fc=c, ec=c, lw=1.6)
    fk.text(ax, 0.15, y + rowh / 2, n, size=19, weight="bold", color="white", va="center", family=fk.HEAD)
    fk.text(ax, 0.46, y + rowh / 2, chip, size=9.5, weight="bold", color="white", va="center", family=fk.HEAD, width=lb - 0.46)
    fk.text(ax, xm, y + rowh - 0.05, head, size=10, weight="bold", family=fk.HEAD)
    fk.text(ax, xm, y + rowh - 0.27, body, size=9, width=xo - 0.12 - xm - 0.10)
    # outcome
    fk.arrow(ax, xo - 0.07, y + rowh / 2, xo + 0.10, y + rowh / 2, color=oc, lw=1.8, ms=12)
    fk.box(ax, xo + 0.12, y + 0.14, 6.46 - xo - 0.12, rowh - 0.28, fc=oc, ec=oc, r=0.08)
    fk.text(ax, (xo + 0.12 + 6.46) / 2, y + rowh / 2, out, size=9, weight="bold", color="white", ha="center",
            va="center", family=fk.HEAD)
    if i:
        fk.arrow(ax, 0.04 + lb / 2, ys[i - 1] - 0.005, 0.04 + lb / 2, y + rowh + 0.005, color=fk.MUTED, lw=1.6)
yk = ys[-1] - 0.10
fk.box(ax, 0.04, yk - 0.44, 6.42, 0.44, fc=fk.PANEL, ec=fk.RULE)
fk.text(ax, 0.16, yk - 0.22, "K, the number of repeat runs, is fixed before testing and every run is reported. Rerunning an unchanged agent cannot overturn a failed gate.",
        size=9, weight="bold", va="center", width=6.2)
fk.save(fig, "gate-flow")
