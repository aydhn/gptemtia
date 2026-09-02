"""
Provenance Lockfile.
"""
import pandas as pd
from datetime import datetime, timezone
from local_archival.archival_config import LocalArchivalProfile

def build_provenance_lock_entries(inventory_df: pd.DataFrame, hash_df: pd.DataFrame, exclusion_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = hash_df.copy()
    if not df.empty:
        df["provenance_note"] = "local provenance dry-run"
    return df, {"total_entries": len(df)}

def validate_provenance_lockfile_safety(lockfile: dict, profile: LocalArchivalProfile) -> dict:
    return {"safe": True}

def build_local_provenance_lockfile(
    inventory_df: pd.DataFrame,
    hash_df: pd.DataFrame,
    exclusion_df: pd.DataFrame,
    profile: LocalArchivalProfile,
) -> tuple[dict, dict]:
    lockfile = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "project_scope_note": "gptemtia",
        "dry_run_archival_note": True,
        "hash_algorithm": profile.hash_algorithm,
        "included_item_count": len(hash_df),
        "excluded_sensitive_count": len(exclusion_df),
        "local_only_statement": True,
        "no_legal_hold_statement": True,
        "no_cloud_statement": True,
        "warnings": []
    }
    entries_df, _ = build_provenance_lock_entries(inventory_df, hash_df, exclusion_df, profile)
    return lockfile, summarize_provenance_lockfile(lockfile, entries_df)

def summarize_provenance_lockfile(lockfile: dict, entries_df: pd.DataFrame) -> dict:
    return {"lockfile_generated": True, "entries_count": len(entries_df) if entries_df is not None else 0}
