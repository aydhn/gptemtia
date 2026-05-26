"""Archive Strategy for offline maintenance."""
import pandas as pd
from typing import Tuple, Dict
from datetime import datetime, timezone
from pathlib import Path

from maintenance.maintenance_config import MaintenanceProfile
from maintenance.maintenance_models import ArchiveManifest, build_archive_id, build_maintenance_candidate_id

def identify_archive_candidates(inventory_df: pd.DataFrame, policies_df: pd.DataFrame, profile: MaintenanceProfile) -> pd.DataFrame:
    if inventory_df.empty:
        return pd.DataFrame()

    candidates = inventory_df[
        (inventory_df["lifecycle_label"] == "archive_candidate") &
        (~inventory_df["protected"]) &
        (inventory_df["size_bytes"] > 0)
    ].copy()

    if candidates.empty:
        return pd.DataFrame()

    # Build candidate records
    cand_records = []
    for _, row in candidates.iterrows():
        cand_records.append({
            "candidate_id": build_maintenance_candidate_id(row["artifact_id"], "archive_dry_run_action"),
            "artifact_id": row["artifact_id"],
            "path": row["path"],
            "action_label": "archive_dry_run_action",
            "reason": "Lifecycle policy designated as archive candidate",
            "size_bytes": row["size_bytes"],
            "age_days": row["age_days"],
            "policy_id": None, # Could look this up
            "dry_run": True,
            "protected": False,
            "warnings": []
        })

    return pd.DataFrame(cand_records)

def build_archive_manifest(candidates_df: pd.DataFrame, profile: MaintenanceProfile, archive_name: str = "local_research_archive") -> ArchiveManifest:
    now_str = datetime.now(timezone.utc).isoformat()

    if candidates_df.empty:
        return ArchiveManifest(
            archive_id=build_archive_id(archive_name, now_str),
            archive_name=archive_name,
            created_at_utc=now_str,
            archive_format=profile.archive_format,
            candidate_count=0,
            total_size_bytes=0,
            candidate_artifact_ids=[],
            manifest_path=None,
            dry_run=True,
            warnings=["No candidates to archive"]
        )

    # Apply max bundle size limit
    total_size = 0
    selected_ids = []

    max_bytes = profile.archive_max_bundle_mb * 1024 * 1024

    for _, row in candidates_df.iterrows():
        size = row.get("size_bytes", 0)
        if total_size + size <= max_bytes:
            total_size += size
            selected_ids.append(row["artifact_id"])

    return ArchiveManifest(
        archive_id=build_archive_id(archive_name, now_str),
        archive_name=archive_name,
        created_at_utc=now_str,
        archive_format=profile.archive_format,
        candidate_count=len(selected_ids),
        total_size_bytes=total_size,
        candidate_artifact_ids=selected_ids,
        manifest_path=None,
        dry_run=True,
        warnings=[]
    )

def build_archive_plan(candidates_df: pd.DataFrame, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    summary = summarize_archive_candidates(candidates_df)
    return candidates_df, summary

def save_archive_manifest(manifest: ArchiveManifest, output_dir: Path) -> Path:
    # Just a placeholder, actual save happens in datalake
    import json
    from maintenance.maintenance_models import archive_manifest_to_dict

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{manifest.archive_id}.json"
    with open(out_path, "w") as f:
        json.dump(archive_manifest_to_dict(manifest), f, indent=2)
    return out_path

def summarize_archive_candidates(candidates_df: pd.DataFrame) -> Dict:
    if candidates_df.empty:
        return {"candidate_count": 0, "total_size_bytes": 0}
    return {
        "candidate_count": len(candidates_df),
        "total_size_bytes": candidates_df["size_bytes"].sum()
    }
