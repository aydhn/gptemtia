"""
Hash Catalog.
"""
import pandas as pd
import hashlib
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.sensitive_exclusions import is_sensitive_archival_path

def compute_file_hash_rehearsal(path: Path, project_root: Path, profile: LocalArchivalProfile) -> dict:
    if is_sensitive_archival_path(path, project_root):
        return {"hash_value": None, "hash_status": "hash_rehearsal_skipped_sensitive"}
    if path.stat().st_size > profile.max_file_size_mb_for_hash * 1024 * 1024:
        return {"hash_value": None, "hash_status": "hash_rehearsal_skipped_large_file"}
    
    h = hashlib.new(profile.hash_algorithm)
    try:
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return {"hash_value": h.hexdigest(), "hash_status": "hash_rehearsal_ready"}
    except Exception:
        return {"hash_value": None, "hash_status": "hash_rehearsal_error"}

def detect_hash_catalog_warnings(hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> pd.DataFrame:
    df = hash_df.copy()
    if "warnings" not in df.columns:
        df["warnings"] = ""
    return df

def build_final_hash_catalog(project_root: Path, inventory_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    results = []
    if not inventory_df.empty:
        for _, row in inventory_df.iterrows():
            p = project_root / row["relative_path"]
            if p.exists():
                h_info = compute_file_hash_rehearsal(p, project_root, profile)
                res = row.to_dict()
                res.update(h_info)
                results.append(res)
    df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    df = detect_hash_catalog_warnings(df, profile)
    return df, summarize_final_hash_catalog(df)

def summarize_final_hash_catalog(hash_df: pd.DataFrame) -> dict:
    return {"total_hashes": len(hash_df) if hash_df is not None else 0}
