import pandas as pd
from typing import Tuple, Dict
import datetime
from .archive_config import LocalArchiveProfile

def build_cold_storage_manifest(item_df: pd.DataFrame, snapshot_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[Dict, Dict]:
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    included_domains = list(item_df['domain_label'].unique()) if not item_df.empty and 'domain_label' in item_df.columns else []
    excluded_count = int((item_df['item_status'] == 'archive_excluded').sum()) if not item_df.empty and 'item_status' in item_df.columns else 0

    manifest = {
        "manifest_created_at_utc": now,
        "profile_used": profile.name,
        "statements": {
            "local_only": True,
            "no_cloud_upload": True,
            "no_auto_compress": True,
            "disclaimer": "This is a cold storage manifest for manual archiving. It does NOT automatically upload or compress files."
        },
        "snapshot_catalog_summary": {"total_snapshots": len(snapshot_df) if not snapshot_df.empty else 0},
        "scope": {"included_domains": included_domains, "excluded_sensitive_items_count": excluded_count},
        "instructions": {
            "manual_archive": "Copy the project directory to an external encrypted drive. Do not include .env or secrets.",
            "verification": "Use the hash manifest to verify files after copy."
        }
    }
    manifest["safety_validation"] = validate_cold_storage_manifest_safety(manifest, profile)
    index_df = item_df[item_df['item_status'] == 'archive_candidate'].copy() if not item_df.empty and 'item_status' in item_df.columns else pd.DataFrame()
    summary = summarize_cold_storage_manifest(manifest, index_df)
    return manifest, summary

def build_cold_storage_manifest_index(item_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    if item_df.empty or 'item_status' not in item_df.columns:
        return pd.DataFrame(), {"count": 0}
    index_df = item_df[item_df['item_status'] == 'archive_candidate'].copy()
    return index_df, {"count": len(index_df)}

def validate_cold_storage_manifest_safety(manifest: Dict, profile: LocalArchiveProfile) -> Dict:
    valid = True
    reasons = []
    if profile.allow_cloud_upload:
        valid = False
        reasons.append("Profile allows cloud upload. Not safe for offline cold storage.")
    if not manifest.get("statements", {}).get("local_only", False):
        valid = False
        reasons.append("Manifest missing local-only statement.")
    return {"is_safe": valid, "reasons": reasons}

def summarize_cold_storage_manifest(manifest: Dict, index_df: pd.DataFrame) -> Dict:
    return {
        "is_safe": manifest.get("safety_validation", {}).get("is_safe", False),
        "manifest_date": manifest.get("manifest_created_at_utc"),
        "index_items": len(index_df)
    }
