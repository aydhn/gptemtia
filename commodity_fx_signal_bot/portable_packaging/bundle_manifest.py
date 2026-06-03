import datetime
import os
from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any, Optional

from portable_packaging.packaging_models import PortableBundleManifest, build_portable_bundle_manifest_id, EnvironmentSnapshot
from portable_packaging.packaging_config import PortablePackagingProfile

def classify_bundle_artifact(path: Path, project_root: Path) -> str:
    rel = str(path.relative_to(project_root))
    if rel.startswith("data/lake"):
        return "data_manifest_artifact"
    if rel.startswith("reports/output"):
        return "reports_manifest_artifact"
    if rel.endswith(".py"):
        return "source_artifact"
    if rel.startswith("docs/"):
        return "docs_artifact"
    if rel.startswith("tests/"):
        return "tests_artifact"
    if rel == ".env.example" or rel.startswith("config/"):
        return "config_artifact"
    if "requirements" in rel:
        return "requirements_artifact"
    return "unknown_artifact"

def decide_artifact_include_policy(path: Path, label: str, profile: PortablePackagingProfile) -> Dict[str, str]:
    name = path.name
    if name == ".env" or "secret" in name.lower() or "token" in name.lower() or "credential" in name.lower():
        return {"policy": "exclude_secret", "safety": "packaging_blocked_secret_risk"}

    if label == "data_manifest_artifact" and profile.include_data_manifest_only:
        return {"policy": "manifest_only_data", "safety": "packaging_safe_manifest_only"}
    if label == "reports_manifest_artifact" and profile.include_reports_manifest_only:
        return {"policy": "manifest_only_reports", "safety": "packaging_safe_manifest_only"}

    if label == "source_artifact" and not profile.include_source:
        return {"policy": "exclude_source", "safety": "packaging_safe_local_only"}
    if label == "docs_artifact" and not profile.include_docs:
        return {"policy": "exclude_docs", "safety": "packaging_safe_local_only"}
    if label == "tests_artifact" and not profile.include_tests:
        return {"policy": "exclude_tests", "safety": "packaging_safe_local_only"}

    return {"policy": "include", "safety": "packaging_safe_local_only"}

def scan_bundle_artifacts(project_root: Path, profile: PortablePackagingProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    data = []

    for root, dirs, files in os.walk(project_root):
        if ".git" in dirs:
            dirs.remove(".git")
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        if ".pytest_cache" in dirs:
            dirs.remove(".pytest_cache")

        for file in files:
            path = Path(root) / file
            label = classify_bundle_artifact(path, project_root)
            policy = decide_artifact_include_policy(path, label, profile)

            data.append({
                "relative_path": str(path.relative_to(project_root)),
                "artifact_label": label,
                "include_policy": policy["policy"],
                "safety_label": policy["safety"]
            })

            if len(data) >= profile.max_inventory_files:
                break
        if len(data) >= profile.max_inventory_files:
            break

    df = pd.DataFrame(data)
    summary = {
        "total_artifacts": len(df),
        "included_artifacts": len(df[df["include_policy"] == "include"]),
        "excluded_secrets": len(df[df["include_policy"] == "exclude_secret"])
    }
    return df, summary

def build_portable_bundle_manifest(profile: PortablePackagingProfile, artifact_df: pd.DataFrame, snapshot: Optional[EnvironmentSnapshot] = None) -> PortableBundleManifest:
    dt_str = datetime.datetime.utcnow().isoformat()
    included = artifact_df[artifact_df["include_policy"] == "include"]["relative_path"].tolist()
    excluded = artifact_df[artifact_df["include_policy"].str.startswith("exclude")]["relative_path"].tolist()

    return PortableBundleManifest(
        manifest_id=build_portable_bundle_manifest_id(profile.name, dt_str),
        profile_name=profile.name,
        created_at_utc=dt_str,
        dry_run=True,
        artifact_count=len(artifact_df),
        included_artifacts=included,
        excluded_artifacts=excluded,
        environment_snapshot_id=snapshot.snapshot_id if snapshot else None,
        requirements_artifacts=[],
        setup_guide_path=None,
        warnings=[]
    )

def build_portable_bundle_manifest_json(manifest: PortableBundleManifest, artifact_df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "manifest_id": manifest.manifest_id,
        "profile_name": manifest.profile_name,
        "created_at_utc": manifest.created_at_utc,
        "included_artifacts": manifest.included_artifacts,
        "excluded_artifacts": manifest.excluded_artifacts
    }

def save_portable_bundle_manifest(manifest_json: Dict[str, Any], output_path: Path) -> Path:
    import json
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(manifest_json, f, indent=2)
    return output_path
