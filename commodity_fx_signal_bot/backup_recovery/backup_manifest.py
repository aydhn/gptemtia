"""
Backup manifest builder.
"""

from datetime import datetime, timezone
import pandas as pd

from .backup_config import BackupRecoveryProfile
from .backup_models import BackupManifest, build_backup_manifest_id, backup_manifest_to_dict

def build_backup_manifest(profile: BackupRecoveryProfile, inventory_df: pd.DataFrame) -> BackupManifest:
    now = datetime.now(timezone.utc).isoformat()

    total = len(inventory_df) if inventory_df is not None else 0
    inc = 0
    exc = 0
    mo = 0
    sz = 0
    ids = []

    if inventory_df is not None and not inventory_df.empty:
        inc = len(inventory_df[inventory_df["include_policy"] == "include"])
        exc = len(inventory_df[inventory_df["include_policy"] == "exclude"])
        mo = len(inventory_df[inventory_df["include_policy"] == "manifest_only"])
        sz = inventory_df[inventory_df["include_policy"] == "include"]["size_bytes"].sum()
        ids = inventory_df[inventory_df["include_policy"].isin(["include", "manifest_only"])]["artifact_id"].tolist()

    return BackupManifest(
        manifest_id=build_backup_manifest_id(profile.name, now),
        profile_name=profile.name,
        created_at_utc=now,
        dry_run=profile.dry_run_default,
        artifact_count=total,
        included_count=inc,
        excluded_count=exc,
        manifest_only_count=mo,
        total_size_bytes=int(sz) if pd.notna(sz) else 0,
        artifact_ids=ids,
        warnings=[]
    )

def build_backup_manifest_json(manifest: BackupManifest, inventory_df: pd.DataFrame) -> dict:
    return backup_manifest_to_dict(manifest)

def validate_backup_manifest(manifest_json: dict, profile: BackupRecoveryProfile) -> dict:
    if not manifest_json.get("dry_run", False) and profile.dry_run_default:
        return {"valid": False, "error": "Manifest dry_run contradicts profile"}
    return {"valid": True}

def summarize_backup_manifest(manifest_json: dict) -> dict:
    if not manifest_json:
        return {"status": "empty"}
    return {
        "manifest_id": manifest_json.get("manifest_id"),
        "included": manifest_json.get("included_count", 0),
        "excluded": manifest_json.get("excluded_count", 0)
    }
