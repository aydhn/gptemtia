"""
DataLake Hash Rehearsal.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archive_candidate_inventory import discover_archive_candidate_items
from local_archival.hash_catalog import compute_file_hash_rehearsal

def build_datalake_hash_rehearsal(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    df = df[df["source_layer"] == "datalake"] if "source_layer" in df.columns else pd.DataFrame(columns=df.columns)
    results = []
    for _, row in df.iterrows():
        p = project_root / row["relative_path"]
        if p.exists():
            h_info = compute_file_hash_rehearsal(p, project_root, profile)
            res = row.to_dict()
            res.update(h_info)
            results.append(res)
    res_df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    return res_df, summarize_datalake_hash_rehearsal(res_df)

def summarize_datalake_hash_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_datalake_items": len(df) if df is not None else 0}
