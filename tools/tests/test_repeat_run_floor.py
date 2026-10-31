"""Run: python tools/tests/test_repeat_run_floor.py"""
import csv, json, os, random, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "..", "repeat_run_floor.py")
sys.path.insert(0, os.path.join(HERE, ".."))
import repeat_run_floor as R

def cli(args):
    p = subprocess.run([sys.executable, TOOL] + args, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr

def test_min_scenarios():
    assert [R.min_scenarios(t) for t in (0.90, 0.95, 0.99)] == [25, 52, 268]

def test_wilson():
    assert abs(R.wilson_lower(40, 40) - 0.9366) < 1e-3
    assert R.wilson_lower(196, 200) >= 0.95 > R.wilson_lower(195, 200)

def test_files_and_compare():
    rng = random.Random(3); d = tempfile.mkdtemp(); paths = []
    ps = {f"s{i}": rng.uniform(0.5, 1) for i in range(60)}
    for k in range(5):
        p = os.path.join(d, f"run{k}.jsonl" if k % 2 else f"run{k}.csv"); paths.append(p)
        rows = []
        for sid, q in ps.items():
            rows.append({"scenario_id": sid, "config": "A", "passed": rng.random() < q})
            rows.append({"scenario_id": sid, "config": "B", "passed": rng.random() < min(1, q + 0.2)})
        if p.endswith(".csv"):
            with open(p, "w", newline="") as f:
                w = csv.DictWriter(f, ["scenario_id", "config", "passed"]); w.writeheader(); w.writerows(rows)
        else:
            open(p, "w").write("\n".join(json.dumps(r) for r in rows))
    code, out = cli(["--runs"] + paths + ["--threshold", "0.95", "--json", os.path.join(d, "o.json")])
    assert code == 0 and "60 scenarios x 5 runs" in out and "Comparisons on shared scenarios" in out, out
    assert "B minus A" in out or "A minus B" in out

def test_single_run_uses_wilson():
    d = tempfile.mkdtemp(); p = os.path.join(d, "r.jsonl")
    open(p, "w").write("\n".join(json.dumps({"scenario_id": f"s{i}", "passed": True}) for i in range(52)))
    code, out = cli(["--runs", p, "--threshold", "0.95"])
    assert code == 0 and "one-sided Wilson" in out and "bound clears it" in out, out

def test_noise_floor_calibrated():
    rng = random.Random(5); cover = 0; T = 200
    for t in range(T):
        ps = [rng.uniform(0, 1) for _ in range(50)]
        per = {i: [int(rng.random() < p) for _ in range(5)] for i, p in enumerate(ps)}
        lo, hi = R.summarize(per, boots=400, seed=t)["bands"][1]
        fresh = sum((rng.random() < p) - (rng.random() < p) for p in ps) / 50
        cover += lo <= fresh <= hi
    assert 0.88 <= cover / T <= 0.99, cover / T

def test_small_perfect_library_cannot_clear_95():
    per = {f"s{i}": [1, 1, 1, 1, 1] for i in range(20)}
    s = R.summarize(per)
    assert s["lower"] < 0.95, s["lower"]
    per = {f"s{i}": [1, 1, 1, 1, 1] for i in range(60)}
    assert R.summarize(per)["lower"] >= 0.95

def test_demo_and_min_cli():
    assert cli(["--demo"])[0] == 0
    code, out = cli(["--min-scenarios", "0.99"]); assert "268" in out

if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(); print("PASS", name)
    print("ALL TESTS PASSED")
