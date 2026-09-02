"""
Seal Rehearsal Manifest.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def build_archival_seal_manifest_items(hash_df: pd.DataFrame, inventory_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    return hash_df.copy(), {"total_items": len(hash_df)}

def validate_archival_seal_manifest_safety(manifest: dict, profile: LocalArchivalProfile) -> dict:
    return {"safe": True}

def build_final_archival_seal_rehearsal_manifest(
    hash_df: pd.DataFrame,
    hoh_df: pd.DataFrame,
    inventory_df: pd.DataFrame,
    profile: LocalArchivalProfile,
) -> tuple[dict, dict]:
    manifest = {
        "statement": "This is a local-only dry-run seal rehearsal. Not a real immutable seal.",
        "hash_policy_reference": "default_hash_algorithm",
        "exclusion_policy_reference": "sensitive_files",
        "no_immutable_lock_statement": True,
        "no_chmod_statement": True,
        "no_legal_hold_statement": True,
        "no_compliance_statement": True,
        "no_cloud_archive_statement": True,
        "hash_of_hashes": hoh_df.to_dict(orient="records")[0]["hash_of_hashes"] if not hoh_df.empty else None
    }
    items_df, _ = build_archival_seal_manifest_items(hash_df, inventory_df, profile)
    return manifest, summarize_archival_seal_manifest(manifest, items_df)

def summarize_archival_seal_manifest(manifest: dict, item_df: pd.DataFrame) -> dict:
    return {"manifest_generated": True, "items_count": len(item_df) if item_df is not None else 0}
