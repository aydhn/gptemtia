import pandas as pd
from pathlib import Path
from datetime import datetime
from .readiness_config import LocalReadinessProfile
from .readiness_models import HandoffManifest, build_handoff_manifest_id

def build_handoff_package_manifest(project_root: Path, readiness_score: float, gate_summary: dict, profile: LocalReadinessProfile) -> tuple[dict, dict]:
    created_at = datetime.utcnow().isoformat()
    manifest_id = build_handoff_manifest_id(profile.name, created_at)
    manifest = HandoffManifest(
        manifest_id=manifest_id,
        profile_name=profile.name,
        created_at_utc=created_at,
        local_only=True,
        readiness_score=readiness_score,
        gate_summary=gate_summary,
        included_sections=["docs", "safe first-run commands", "generated readiness reports", "known limitations", "known gaps", "manual review", "no-go/safe-go conditions", "DataLake/report locations", "local-only statement"],
        warnings=[]
    )
    from .readiness_models import handoff_manifest_to_dict
    manifest_dict = handoff_manifest_to_dict(manifest)
    manifest_dict = validate_handoff_manifest_safety(manifest_dict, profile)
    index_df, _ = build_handoff_manifest_index(project_root, profile)
    return manifest_dict, summarize_handoff_manifest(manifest_dict, index_df)

def build_handoff_manifest_index(project_root: Path, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"section": "docs", "status": "ok"}])
    return df, {"total_sections": len(df)}

def validate_handoff_manifest_safety(manifest: dict, profile: LocalReadinessProfile) -> dict:
    if "production release" in str(manifest).lower():
        manifest["warnings"].append("Forbidden term detected: production release")
    return manifest

def summarize_handoff_manifest(manifest: dict, index_df: pd.DataFrame) -> dict:
    return {"manifest_id": manifest["manifest_id"], "score": manifest["readiness_score"]}
