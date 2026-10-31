#!/usr/bin/env python3
"""SAFE-CARE repeat-run tool: noise floor, bounds and comparisons for scored runs.

Input: one file per run (JSONL or CSV), one row per scenario, with
  scenario_id   the scenario identifier
  passed        true/false or 1/0 (or name another field with --outcome-field)
  config        optional; rows are grouped by this field (or --group-field)

Usage:
  python tools/repeat_run_floor.py --runs runs/r1.jsonl runs/r2.jsonl runs/r3.jsonl runs/r4.jsonl runs/r5.jsonl
  python tools/repeat_run_floor.py --runs runs/*.csv --threshold 0.95 --json out.json
  python tools/repeat_run_floor.py --demo
  python tools/repeat_run_floor.py --min-scenarios 0.95

Reports, per configuration:
  - pass rate (first run and mean over runs) and the share of scenarios with mixed outcomes
  - the within-scenario share of variance
  - the empirical noise floor (null band) for r runs per version
  - the smallest difference detectable at 1, 2, 3, 5 and 10 runs per version
  - a one-sided 95% lower bound on the pass rate (scenario-clustered bootstrap, capped so it
    never exceeds the Wilson bound; Wilson alone when there is one run) and whether it clears --threshold
  - for two or more configurations, the difference on shared scenarios with a 95% interval

Assumptions: runs are exchangeable (same configuration, no external change between
runs); scenarios and reference answers are fixed. See docs/10 and docs/07.
Standard library only. Apache-2.0.
"""
import argparse, csv, json, math, random, sys
from collections import defaultdict

Z95, Z80, Z95_ONE = 1.959964, 0.841621, 1.644854
TRUE = {"true", "1", "yes", "pass", "passed"}
FALSE = {"false", "0", "no", "fail", "failed"}


def read_rows(path):
    if path.lower().endswith(".csv"):
        with open(path, encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def to_outcome(v):
    s = str(v).strip().lower()
    if s in TRUE:
        return 1
    if s in FALSE:
        return 0
    return None


def load(paths, id_field, outcome_field, group_field):
    out = defaultdict(lambda: defaultdict(list))
    diag = defaultdict(lambda: defaultdict(int))
    for path in paths:
        seen = {}
        for r in read_rows(path):
            g = str(r.get(group_field) or "default")
            sid = r.get(id_field)
            y = to_outcome(r.get(outcome_field))
            if sid is None:
                diag[g]["rows without " + id_field] += 1
                continue
            if y is None:
                diag[g]["rows with unreadable " + outcome_field] += 1
                continue
            if (g, sid) in seen:
                diag[g]["duplicate rows in one run (last kept)"] += 1
            seen[(g, sid)] = y
        for (g, sid), y in seen.items():
            out[g][sid].append(y)
    return out, diag


def wilson_lower(k, n, z=Z95_ONE):
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - r) / d


def min_scenarios(threshold, z=Z95_ONE):
    """Smallest library where an all-pass result clears the one-sided Wilson bound."""
    n = 1
    while wilson_lower(n, n, z) < threshold:
        n += 1
    return n


def summarize(per_id, boots=2000, seed=7):
    rng = random.Random(seed)
    vs = [v for v in per_id.values() if len(v) >= 1]
    if not vs:
        return None
    ids = [i for i, v in per_id.items() if len(v) >= 1]
    n = len(vs)
    ks = [len(v) for v in vs]
    means = [sum(v) / len(v) for v in vs]
    mean_p = sum(means) / n
    first = sum(v[0] for v in vs) / n
    s = dict(n=n, kmin=min(ks), kmax=max(ks), first=first, mean_p=mean_p,
             means=dict(zip(ids, means)), k=dict(zip(ids, ks)))
    # lower bound on pass rate
    if max(ks) == 1:
        s["lower"] = wilson_lower(sum(v[0] for v in vs), n)
        s["lower_method"] = "one-sided Wilson"
    else:
        bs = sorted(sum(rng.choice(means) for _ in range(n)) / n for _ in range(boots))
        # A bootstrap of a perfect or near-perfect library collapses to 100%; never report
        # a lower bound higher than the Wilson bound on the scenario count.
        wl = wilson_lower(sum(means), n)
        s["lower"] = min(bs[int(0.05 * boots)], wl)
        s["lower_method"] = "one-sided, scenario-clustered bootstrap capped by Wilson"
    multi = [v for v in vs if len(v) >= 2]
    s["multi"] = len(multi)
    if multi:
        w = [len(v) / (len(v) - 1) * (sum(v) / len(v)) * (1 - sum(v) / len(v)) for v in multi]
        s["w"] = dict((i, len(v) / (len(v) - 1) * m * (1 - m)) for i, v, m in zip(ids, vs, means) if len(v) >= 2)
        s["mixed"] = sum(1 for v in multi if 0 < sum(v) < len(v)) / len(multi)
        tot = mean_p * (1 - mean_p)
        s["within_share"] = min(sum(w) / len(multi) / tot, 1.0) if tot > 0 else None
        bands = {}
        for r in range(1, min(len(v) for v in multi) // 2 + 1):
            diffs = []
            for _ in range(boots):
                d = 0.0
                for v in multi:
                    x = rng.sample(v, 2 * r)
                    d += sum(x[:r]) / r - sum(x[r:]) / r
                diffs.append(d / len(multi))
            diffs.sort()
            bands[r] = (diffs[int(0.025 * boots)], diffs[int(0.975 * boots) - 1])
        s["bands"] = bands
        s["se"] = {r: math.sqrt(2 * sum(w) / r) / len(multi) for r in (1, 2, 3, 5, 10)}
    return s


def compare(a, b):
    shared = sorted(set(a.get("w", {})) & set(b.get("w", {})))
    if not shared:
        return None
    m = len(shared)
    diff = sum(a["means"][i] - b["means"][i] for i in shared) / m
    var = sum(a["w"][i] / a["k"][i] + b["w"][i] / b["k"][i] for i in shared) / m ** 2
    se = math.sqrt(var)
    return dict(m=m, diff=diff, lo=diff - Z95 * se, hi=diff + Z95 * se)


def pct(x):
    return "n/a" if x is None else f"{x:.1%}"


def report(g, s, threshold, diag):
    k = f"{s['kmin']}" if s["kmin"] == s["kmax"] else f"{s['kmin']}-{s['kmax']}"
    print(f"\n{g} | {s['n']} scenarios x {k} runs")
    for what, c in sorted((diag or {}).items()):
        print(f"  note: {c} rows skipped, {what}")
    print(f"  pass rate, first run only          {pct(s['first'])}")
    print(f"  pass rate, mean over runs          {pct(s['mean_p'])}")
    print(f"  lower 95% bound ({s['lower_method']})  {pct(s['lower'])}")
    if threshold is not None:
        verdict = "clears" if s["lower"] is not None and s["lower"] >= threshold else "does not clear"
        print(f"  gate at {threshold:.0%}: bound {verdict} it (library needs >= {min_scenarios(threshold)} all-passing scenarios)")
    if s["multi"]:
        print(f"  scenarios with mixed outcomes      {pct(s['mixed'])}   (rises with K)")
        print(f"  within-scenario share of variance  {pct(s['within_share'])}")
        for r, (lo, hi) in s["bands"].items():
            print(f"  noise floor, {r} vs {r} run(s)          [{lo:+.1%}, {hi:+.1%}]")
        print("  smallest difference between two versions, by runs per version:")
        for r, se in s["se"].items():
            print(f"    {r:>2}: significant beyond +/-{Z95 * se:.1%}, detectable with 80% power at {(Z95 + Z80) * se:.1%}")
    else:
        print("  one run per scenario: pass two or more run files to measure the noise floor")


def demo():
    rng = random.Random(1)
    for name, draw in [("stable agent", lambda: rng.choice([1.0] * 39 + [0.0])),
                       ("variable agent", lambda: rng.uniform(0.90, 1.0))]:
        per = {f"s{i}": [] for i in range(200)}
        ps = {k: draw() for k in per}
        for _ in range(5):
            for k in per:
                per[k].append(int(rng.random() < ps[k]))
        report(f"simulated {name}", summarize(per), 0.95, {})


def main(argv=None):
    ap = argparse.ArgumentParser(description="SAFE-CARE repeat-run tool")
    ap.add_argument("--runs", nargs="+", help="one scored file per run")
    ap.add_argument("--id-field", default="scenario_id")
    ap.add_argument("--outcome-field", default="passed")
    ap.add_argument("--group-field", default="config")
    ap.add_argument("--threshold", type=float, default=None, help="gate threshold, for example 0.95")
    ap.add_argument("--boots", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--json", help="write results to this JSON file")
    ap.add_argument("--min-scenarios", type=float, metavar="THRESHOLD",
                    help="print the smallest all-passing library that clears THRESHOLD")
    ap.add_argument("--demo", action="store_true")
    a = ap.parse_args(argv)
    if a.min_scenarios is not None:
        print(f"{min_scenarios(a.min_scenarios)} scenarios")
        return
    if a.demo:
        demo()
        return
    if not a.runs:
        ap.error("pass --runs (one file per run), --demo or --min-scenarios")
    data, diag = load(a.runs, a.id_field, a.outcome_field, a.group_field)
    if not data:
        sys.exit("no usable rows: check --id-field and --outcome-field")
    res = {}
    for g in sorted(data):
        s = summarize(data[g], a.boots, a.seed)
        if s:
            res[g] = s
            report(g, s, a.threshold, diag.get(g))
    gs = list(res)
    pairs = [(x, y, compare(res[x], res[y])) for i, x in enumerate(gs) for y in gs[i + 1:]]
    pairs = [p for p in pairs if p[2]]
    if pairs:
        print("\nComparisons on shared scenarios (95% interval, conditional on these scenarios)")
        for x, y, c in pairs:
            v = "difference" if c["lo"] > 0 or c["hi"] < 0 else "within run-to-run noise"
            print(f"  {x} minus {y}: {c['diff']:+.1%} [{c['lo']:+.1%}, {c['hi']:+.1%}] on {c['m']} scenarios -> {v}")
    if a.json:
        out = {g: {k: v for k, v in s.items() if k not in ("means", "w", "k")} for g, s in res.items()}
        for g in out:
            out[g]["bands"] = {str(r): list(b) for r, b in res[g].get("bands", {}).items()}
            out[g]["se"] = {str(r): v for r, v in res[g].get("se", {}).items()}
        out["comparisons"] = [{"a": x, "b": y, **c} for x, y, c in pairs]
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
