"""End-to-end smoke tests for instance I/O and the command-line scripts.

Scratch output goes to a temporary directory *inside* the repository
(``tests/_tmp*``), which is removed afterwards.
"""

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests._util import ROOT
from scs.generators import generate
from scs.instance_io import load_instances, save_batch, save_instance

SCRIPTS = ROOT / "scripts"


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def run(script, *args):
    proc = subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)], cwd=ROOT,
                          capture_output=True, text=True, timeout=600)
    if proc.returncode != 0:
        raise AssertionError(f"{script} failed:\n{proc.stdout}\n{proc.stderr}")
    return proc.stdout


class TestInstanceIO(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=ROOT / "tests", prefix="_tmp")
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_roundtrip(self):
        insts = [dict(generate("random", s, n=5), id=f"r{s}") for s in range(3)]
        save_batch(self.dir / "b.json", name="t@tiny/n=5", family="random", params={"n": 5}, master_seed=1,
                   instances=insts)
        save_instance(self.dir / "single.json", {"id": "one", "strings": ["ab", "bc", "αx"]})
        (self.dir / "plain.txt").write_text("ATT\nTTA\n\nTAC\n")
        (self.dir / "manifest.json").write_text("{}")
        loaded = {i["id"]: i for i in load_instances(self.dir)}
        self.assertEqual(set(loaded), {"r0", "r1", "r2", "one", "plain"})
        self.assertEqual(loaded["r1"]["strings"], insts[1]["strings"])
        self.assertEqual(loaded["r1"]["seed"], insts[1]["seed"])
        self.assertEqual(loaded["r1"]["master_seed"], 1)
        self.assertEqual(loaded["one"]["strings"][2], "αx")
        self.assertEqual(loaded["plain"]["strings"], ["ATT", "TTA", "TAC"])


class TestPipeline(unittest.TestCase):
    def test_generate_benchmark_summarize(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "tests", prefix="_tmp") as tmp:
            tmp = Path(tmp)
            run("generate_instances.py", "--out", tmp / "data", "--tier", "tiny", "--sizes", "4,6", "--count", "2",
                "--variants", "random/bin_l4-8,repetitive/cyclic_k6", "--master-seed", 5)
            manifest = json.loads((tmp / "data" / "manifest.json").read_text())
            self.assertEqual(len(manifest["batches"]), 4)
            # Regenerating from the manifest reproduces the stored instance.
            rel, entry = next(iter(manifest["batches"].items()))
            batch = json.loads((tmp / "data" / rel).read_text())
            inst = batch["instances"][0]
            regen = generate(entry["family"], inst["seed"], n=entry["n"], **entry["params"])
            self.assertEqual(regen["strings"], inst["strings"])

            run("run_benchmark.py", tmp / "data", "--out", tmp / "res", "--random-ties", 3, "--explore-max-n", 6)
            rows = read_csv(tmp / "res" / "instances.csv")
            self.assertEqual(len(rows), 8)
            for r in rows:
                self.assertEqual(r["opt_method"], "dp")
                self.assertGreaterEqual(float(r["ratio_first"]), 1.0)
                self.assertLessEqual(int(r["explore_min"]), int(r["greedy_min_observed"]))
            runs = read_csv(tmp / "res" / "runs.csv")
            self.assertTrue({"dp", "bruteforce", "greedy", "greedy_worst_tie"} <= {r["algo"] for r in runs})
            meta = json.loads((tmp / "res" / "meta.json").read_text())
            self.assertEqual(meta["instances"], 8)

            run("summarize_results.py", tmp / "res")
            self.assertIn("Tie sensitivity", (tmp / "res" / "summary.md").read_text())

    def test_literature_and_tools(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "tests", prefix="_tmp") as tmp:
            tmp = Path(tmp)
            out = run("import_literature.py", "--out", tmp / "lit", "--explore-max-n", 6, "--dp-max-n", 16)
            self.assertIn("all reported values reproduced", out)
            run("run_benchmark.py", tmp / "lit" / "shibata_k10_t1.json", tmp / "lit" / "chukhin_k6_t1.json",
                "--out", tmp / "res", "--random-ties", 2)
            rows = {r["instance"]: r for r in read_csv(tmp / "res" / "instances.csv")}
            self.assertEqual(rows["shibata_k10_t1"]["opt"], "31")
            self.assertEqual(rows["shibata_k10_t1"]["greedy_max_observed"], "47")  # the paper's execution
            run("bench_scaling.py", "--out", tmp / "scal", "--dp-sizes", "4,6", "--greedy-sizes", "50",
                "--reps", 1, "--repeats", 1)
            self.assertTrue((tmp / "scal" / "scaling.csv").exists())
            out = run("search_worst_case.py", "--k", 3, "--alphabet", "AB", "--max-size", 5, "--out", tmp / "s")
            report = json.loads((tmp / "s" / "search.json").read_text())
            self.assertEqual(report["stats"]["compression_bound_violations"], 0)
            self.assertLessEqual(report["worst_ratio"], 9 / 5)
            self.assertIn("Shibata", run("demo.py"))

    @unittest.skipUnless((ROOT / "data" / "real" / "sources.json").exists(), "real data not fetched")
    def test_generate_real_instances(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "tests", prefix="_tmp") as tmp:
            tmp = Path(tmp)
            args = ["--out", tmp / "real", "--count", 2]
            if not (ROOT / "data" / "real" / "raw" / "ERR098007.fastq.gz").exists():
                args.append("--skip-reads")
            run("generate_real_instances.py", *args)
            manifest = json.loads((tmp / "real" / "manifest.json").read_text())
            self.assertIn("sim_sars2_errfree/large_len100_cov5.json", manifest["batches"])
            run("run_benchmark.py", tmp / "real" / "sim_phix_errfree", "--out", tmp / "res", "--tier", "small",
                "--random-ties", 2)
            rows = read_csv(tmp / "res" / "instances.csv")
            self.assertTrue(rows and all(r["opt_method"] == "dp" for r in rows))

    def test_experiment_12_5(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "tests", prefix="_tmp") as tmp:
            tmp = Path(tmp)
            run("experiment_12_5.py", "--out", tmp, "--r", "1,2,6", "--small-p-r", "2", "--random-ties", 3)
            rows = {r["instance"]: r for r in read_csv(tmp / "theorem.csv")}
            self.assertEqual(rows["greedy125_r2_P1"]["greedy_paper"], rows["greedy125_r2_P1"]["greedy_formula"])
            self.assertEqual(rows["greedy125_r2_P4"]["opt"], "202")
            insts = {r["instance"]: r for r in read_csv(tmp / "instances.csv")}
            self.assertEqual(insts["greedy125_r2_P4"]["ref_kind"], "exact")
            self.assertEqual(insts["greedy125_r6_P36"]["ref_kind"], "upper_bound")
            self.assertEqual(insts["greedy125_r6_P36"]["ref"], insts["greedy125_r6_P36"]["opt_upper"])
            self.assertIn("G/|H| (lower bound)", (tmp / "summary.md").read_text())


if __name__ == "__main__":
    unittest.main()
