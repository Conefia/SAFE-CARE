import fk
H = 2.86
fig, ax = fk.canvas(H)
# the patient message
fk.box(ax, 0.04, H - 0.66, 6.42, 0.62, fc=fk.PANEL, ec=fk.RULE, lw=1.0)
fk.pill(ax, 0.18, H - 0.22, "PATIENT", fc=fk.CHAR, size=9)
fk.text(ax, 0.18, H - 0.37, "“I am 52, I have hot flashes, and today I am bleeding heavily and feel dizzy.”",
        size=11, style="italic", weight="bold", width=6.1)
rows = [("Red flag", "Missed. Answers the hot-flash question.", "Detected before anything else."),
        ("Tone", "Reassures, with lifestyle tips.", "No reassurance. States the urgency."),
        ("Next step", "None. The conversation goes on.", "Urgent care now, or a human."),
        ("Record", "Nothing explains why it answered.", "Logs what it saw and why it acted.")]
cols = [("UNGUARDED REPLY", fk.DEFECT, fk.DEFECT_FILL, "✗"), ("SAFE-CARE™ REPLY", fk.FIX, fk.FIX_FILL, "✓")]
lab_w, cw, x0 = 1.0, 2.60, 1.16
top = H - 0.80; band = 0.36; rh = 0.40
for k, (title, c, fill, mark) in enumerate(cols):
    x = x0 + k * (cw + 0.04)
    fk.box(ax, x, top - band - len(rows) * rh - 0.06, cw, band + len(rows) * rh + 0.06, fc=fill, ec=c, lw=1.6)
    fk.box(ax, x, top - band, cw, band, fc=c, ec=c, lw=1.6)
    fk.text(ax, x + 0.14, top - band / 2, title, size=10.5, weight="bold", color="white", va="center", family=fk.HEAD)
    ax.text(x + cw - 0.14, top - band / 2, mark, fontsize=17, color="white", weight="bold", ha="right",
            va="center", family="DejaVu Sans", zorder=7)
    for i, r in enumerate(rows):
        fk.text(ax, x + 0.14, top - band - i * rh - rh / 2, r[1 + k], size=9.5, width=cw - 0.26, va="center",
                weight="bold" if k else "normal")
for i, r in enumerate(rows):
    fk.text(ax, 0.06, top - band - i * rh - rh / 2, r[0], size=9.5, va="center", weight="bold", color=fk.MUTED, family=fk.HEAD)
    if i:
        ax.plot([0.06, x0 + 2 * cw + 0.04], [top - band - i * rh] * 2, color=fk.RULE, lw=0.6, zorder=3)
fk.save(fig, "two-behaviors")
