"""Reading and writing instances.

Two JSON file formats are used (UTF-8, ``ensure_ascii=False``):

``scs-batch/1``
    One generator configuration with a list of instances::

        {"format": "scs-batch/1", "name": ..., "family": ..., "generator": ...,
         "params": {...}, "master_seed": 123, "created": ..., "python": ...,
         "command": ..., "instances": [{"id": ..., "seed": ..., "strings": [...], ...}]}

    Each instance has its own ``seed`` (derived from ``master_seed``), so it
    can be regenerated on its own with ``scs.generators.generate``.

``scs-instance/1``
    A single instance, as used in ``data/literature``.

:func:`load_instances` accepts files, directories (searched recursively for
``*.json``) or ``.txt`` files with one string per line.  It yields flat
instance dicts that always have ``id``, ``family``, ``strings`` and ``path``.
"""

from __future__ import annotations

import json
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator

BATCH_FORMAT = "scs-batch/1"
INSTANCE_FORMAT = "scs-instance/1"
METADATA_FILES = {"manifest.json", "index.json"}  # skipped when loading a directory


def environment_info() -> dict:
    return {
        "python": sys.version.split()[0],
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "command": " ".join([os.path.basename(sys.argv[0])] + sys.argv[1:]),
    }


def _dump(obj, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def save_batch(path, *, name: str, family: str, params: dict, master_seed: int,
               instances: list[dict], extra: dict | None = None) -> None:
    batch = {"format": BATCH_FORMAT, "name": name, "family": family, "params": params,
             "master_seed": master_seed, **environment_info(), **(extra or {}),
             "instances": instances}
    _dump(batch, Path(path))


def save_instance(path, instance: dict) -> None:
    _dump({"format": INSTANCE_FORMAT, **instance}, Path(path))


def _iter_files(paths: Iterable) -> Iterator[Path]:
    for p in paths:
        p = Path(p)
        if p.is_dir():
            yield from sorted(q for q in p.rglob("*") if q.suffix in (".json", ".txt") and q.name not in METADATA_FILES)
        else:
            yield p


def load_instances(*paths) -> Iterator[dict]:
    """Yield instances from JSON batches, single-instance JSON, or plain text files."""
    for path in _iter_files(paths):
        if path.suffix == ".txt":
            strings = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
            yield {"id": path.stem, "family": "file", "strings": strings, "path": str(path)}
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        fmt = data.get("format")
        if fmt == BATCH_FORMAT:
            for inst in data["instances"]:
                out = {"family": data.get("family"), "batch": data.get("name"),
                       "batch_params": data.get("params"), "master_seed": data.get("master_seed"), **inst}
                out["path"] = str(path)
                yield out
        elif fmt == INSTANCE_FORMAT or "strings" in data:
            out = {"id": path.stem, "family": "file", **data}
            out.pop("format", None)
            out["path"] = str(path)
            yield out
        else:
            raise ValueError(f"{path}: unrecognised instance file")
