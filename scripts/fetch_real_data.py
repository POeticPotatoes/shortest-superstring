#!/usr/bin/env python3
"""Download the real-world sequencing data used by the project and verify it.

Sources (all public INSDC / RefSeq records):

* Reference genomes from NCBI RefSeq (E-utilities ``efetch``), saved to
  ``data/real/reference/<accession>.fasta`` (small; kept in the repository):

  - NC_001422.1  Escherichia phage phiX174, complete genome (5,386 bp, circular).
    phiX174 is the standard Illumina sequencing control.
  - NC_045512.2  SARS-CoV-2 isolate Wuhan-Hu-1, complete genome (29,903 bp, linear)
  - NC_001416.1  Enterobacteria phage lambda, complete genome (48,502 bp, linear here)

* Real Illumina reads of phiX174 from ENA: run ERR098007 (study PRJEB2910,
  Illumina Genome Analyzer IIx, single-end, 23,332 reads of mostly 76 bp, 1.8 MB
  gzipped), saved to ``data/real/raw/ERR098007.fastq.gz``.  It is not kept in the
  repository (``data/real/raw/.gitignore``), because derived instances record its
  accession and MD5.

Every download is checked.  Genomes must be one FASTA record, ACGT only, with
the length NCBI reports.  The reads must match ENA's published MD5.
``data/real/sources.json`` records URLs, accessions, sizes, SHA-256 and retrieval
time.  Re-running skips files that already verify.

    python scripts/fetch_real_data.py [--skip-reads] [--force]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

import _common  # noqa: F401
from scs.realdata import read_fasta, read_fastq

ROOT = _common.ROOT
REAL = ROOT / "data" / "real"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
ENA_FILEREPORT = "https://www.ebi.ac.uk/ena/portal/api/filereport"

GENOMES = {
    "NC_001422.1": {"name": "phiX174", "circular": True},
    "NC_045512.2": {"name": "SARS-CoV-2 Wuhan-Hu-1", "circular": False},
    "NC_001416.1": {"name": "lambda phage", "circular": False},
}
READ_RUNS = {
    "ERR098007": {"organism": "phiX174", "reference": "NC_001422.1"},
}
USER_AGENT = "scs-greedy-study/0.1 (student research; python urllib)"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def get_genome(acc: str, force: bool) -> dict:
    path = REAL / "reference" / f"{acc}.fasta"
    summary = json.loads(fetch(EUTILS + "esummary.fcgi?" + urllib.parse.urlencode(
        {"db": "nuccore", "id": acc, "retmode": "json"})))["result"]
    info = summary[summary["uids"][0]]
    expected_len = int(info["slen"])
    url = EUTILS + "efetch.fcgi?" + urllib.parse.urlencode(
        {"db": "nuccore", "id": acc, "rettype": "fasta", "retmode": "text"})
    if force or not path.exists():
        data = fetch(url)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".part")
        tmp.write_bytes(data)
        tmp.replace(path)
    records = read_fasta(path)
    if len(records) != 1:
        raise SystemExit(f"{acc}: expected one FASTA record, got {len(records)}")
    header, seq = records[0]
    if seq.strip("ACGT") or len(seq) != expected_len or not header.startswith(acc):
        raise SystemExit(f"{acc}: unexpected content (len {len(seq)} vs {expected_len}, header {header!r})")
    data = path.read_bytes()
    print(f"  {acc}: {len(seq)} bp, {info['title']}")
    return {"accession": acc, "title": info["title"], "length": len(seq), **GENOMES[acc],
            "path": str(path.relative_to(ROOT)), "url": url, "sha256": sha256(data), "bytes": len(data),
            "source": "NCBI RefSeq via E-utilities efetch"}


def get_reads(run: str, force: bool) -> dict:
    fields = "run_accession,study_accession,sample_accession,instrument_model,library_layout," \
             "read_count,base_count,fastq_ftp,fastq_md5,fastq_bytes,first_public"
    report = fetch(ENA_FILEREPORT + "?" + urllib.parse.urlencode(
        {"accession": run, "result": "read_run", "fields": fields, "format": "tsv"})).decode()
    head, row = report.strip().split("\n")[:2]
    meta = dict(zip(head.split("\t"), row.split("\t")))
    url = "https://" + meta["fastq_ftp"]
    path = REAL / "raw" / f"{run}.fastq.gz"
    if force or not path.exists() or hashlib.md5(path.read_bytes()).hexdigest() != meta["fastq_md5"]:
        data = fetch(url)
        if hashlib.md5(data).hexdigest() != meta["fastq_md5"]:
            raise SystemExit(f"{run}: MD5 mismatch; refusing to save")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    data = path.read_bytes()
    n = sum(1 for _ in read_fastq(path))
    if n != int(meta["read_count"]):
        raise SystemExit(f"{run}: parsed {n} reads, ENA reports {meta['read_count']}")
    print(f"  {run}: {n} reads, {meta['instrument_model']}, MD5 ok")
    return {**meta, **READ_RUNS[run], "path": str(path.relative_to(ROOT)), "url": url,
            "sha256": sha256(data), "bytes": len(data), "source": "ENA (European Nucleotide Archive)"}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skip-reads", action="store_true", help="only fetch the reference genomes")
    ap.add_argument("--force", action="store_true", help="re-download even if files verify")
    args = ap.parse_args(argv)

    raw_ignore = REAL / "raw" / ".gitignore"
    raw_ignore.parent.mkdir(parents=True, exist_ok=True)
    if not raw_ignore.exists():
        raw_ignore.write_text("# Raw downloads are fetched by scripts/fetch_real_data.py (MD5-verified).\n*\n!.gitignore\n")

    sources = {"retrieved": datetime.now(timezone.utc).isoformat(timespec="seconds"), "genomes": {}, "reads": {}}
    print("reference genomes:")
    for acc in GENOMES:
        sources["genomes"][acc] = get_genome(acc, args.force)
    if not args.skip_reads:
        print("read runs:")
        for run in READ_RUNS:
            sources["reads"][run] = get_reads(run, args.force)
    out = REAL / "sources.json"
    if out.exists() and args.skip_reads:
        sources["reads"] = json.loads(out.read_text()).get("reads", {})
    out.write_text(json.dumps(sources, indent=1) + "\n", encoding="utf-8")
    print(f"-> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
