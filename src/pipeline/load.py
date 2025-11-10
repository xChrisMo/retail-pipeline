from __future__ import annotations

import pandas as pd

from .config import ensure_output_paths, marts_path, staging_path


def persist_tables(tables):
    """Storing each table to Parquet."""
    output_paths = {}

    ensure_output_paths()
    for name, frame in tables.items():
        if name.startswith("fact"):
            target_dir = marts_path
        else:
            target_dir = staging_path
        path = target_dir / f"{name}.parquet"
        frame.to_parquet(path, index=False)
        output_paths[name] = path

    return output_paths


