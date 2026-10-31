import fk
lv = [("M4", "Clinical evidence", "Prospective clinical evaluation", "Clinical benefit or effectiveness, and only when validated."),
      ("M3", "Controlled deployment", "Human oversight, monitored users, incident review", "Safety and experience findings for this deployment."),
      ("M2", "Shadow or pilot", "Production-like telemetry, no autonomous high-risk action", "Operational feasibility and the observed failure profile."),
      ("M1", "Offline tested", "Scenario simulations, automated checks, a calibrated review subset", "Technical performance inside the tested scenarios."),
      ("M0", "Concept", "Architecture and intended controls only", "A design hypothesis. No performance claim.")]
shades = ["#8F5400", "#AD6800", "#E69F00", "#F0BF55", "#F7DCA0"]
H = 4.02
fig, ax = fk.canvas(H)
top, hdr, rh, gap = H - 0.04, 0.40, 0.62, 0.08
xs, x1, x2, xe = 0.04, 2.10, 4.20, 6.46
fk.box(ax, x1, top - hdr, xe - x1, hdr, fc=fk.CHAR, ec=fk.CHAR, r=0.05)
fk.text(ax, x1 + 0.14, top - hdr / 2, "EVIDENCE HELD", size=9.5, weight="bold", color="white", va="center", family=fk.HEAD)
fk.text(ax, x2 + 0.14, top - hdr / 2, "CLAIM ALLOWED", size=9.5, weight="bold", color="white", va="center", family=fk.HEAD)
fk.text(ax, xs, top - hdr / 2, "Maturity level", size=10, weight="bold", va="center", family=fk.HEAD)
for i, (code, name, ev, claim) in enumerate(lv):
    y = top - hdr - 0.08 - (i + 1) * rh - i * gap
    lvl = 4 - i
    fk.box(ax, xs, y, x1 - xs - 0.08, rh, fc=shades[i], ec=shades[i], lw=1.4)
    fk.text(ax, xs + 0.10, y + rh / 2, code, size=13, weight="bold", va="center", family=fk.HEAD,
            color="white" if lvl >= 3 else fk.INK)
    fk.text(ax, xs + 0.62, y + rh / 2, name, size=9.5, weight="bold", va="center", width=1.32,
            color="white" if lvl >= 3 else fk.INK, family=fk.HEAD)
    fk.box(ax, x1, y, xe - x1, rh, fc=fk.PANEL if i % 2 else "white", ec=fk.RULE, lw=0.8)
    fk.text(ax, x1 + 0.14, y + rh / 2, ev, size=9, va="center", width=x2 - x1 - 0.24)
    fk.text(ax, x2 + 0.14, y + rh / 2, claim, size=9, weight="bold", va="center", width=xe - x2 - 0.24)
fk.save(fig, "evidence-maturity")
