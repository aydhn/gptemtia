from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any

from portable_packaging.packaging_config import PortablePackagingProfile

def build_archive_plan_from_bundle_manifest(artifact_df: pd.DataFrame, profile: PortablePackagingProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    # Dry-run plan
    if not profile.allow_archive_create:
        pass # Note: we still build the plan, but we don't zip it.

    plan = artifact_df[artifact_df["include_policy"] == "include"].copy()
    plan["archive_action"] = "add"

    return plan, {"archive_planned": len(plan), "dry_run": not profile.allow_archive_create}

def build_archive_manifest_json(archive_plan_df: pd.DataFrame, profile: PortablePackagingProfile) -> Dict[str, Any]:
    return {
        "profile": profile.name,
        "planned_files": archive_plan_df["relative_path"].tolist() if not archive_plan_df.empty else [],
        "allow_archive_create": profile.allow_archive_create
    }

def save_archive_manifest_json(manifest: Dict[str, Any], output_path: Path) -> Path:
    import json
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    return output_path

def validate_archive_plan_safety(archive_plan_df: pd.DataFrame, profile: PortablePackagingProfile) -> Dict[str, Any]:
    # Check if any excluded files sneaked in
    unsafe = archive_plan_df[archive_plan_df["safety_label"].str.contains("blocked", na=False)]
    return {
        "is_safe": unsafe.empty,
        "unsafe_files": unsafe["relative_path"].tolist() if not unsafe.empty else []
    }
