"""
Timeline JSON/CSV local export module.
"""

from pathlib import Path
import pandas as pd
from datetime import datetime, timezone
import json

from local_timeline.timeline_config import LocalTimelineProfile

def validate_timeline_export_safety(manifest: dict, profile: LocalTimelineProfile) -> dict:
    warnings = []
    if profile.allow_cloud_upload:
        warnings.append("cloud_upload_should_be_false")
    if profile.allow_external_event_service:
        warnings.append("external_service_should_be_false")

    # Just to simulate the contract constraints
    manifest["safety_validated"] = len(warnings) == 0
    manifest["safety_warnings"] = warnings
    return manifest

def build_timeline_export_manifest(event_df: pd.DataFrame, phase_df: pd.DataFrame, evolution_df: pd.DataFrame, profile: LocalTimelineProfile) -> dict:
    manifest = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "total_events": len(event_df) if not event_df.empty else 0,
        "total_phases": len(phase_df) if not phase_df.empty else 0,
        "total_artifacts": len(evolution_df) if not evolution_df.empty else 0,
        "profile": profile.name,
        "language": profile.language,
        "safety_validated": False,
        "safety_warnings": []
    }
    return validate_timeline_export_safety(manifest, profile)

def export_timeline_to_json(event_df: pd.DataFrame, phase_df: pd.DataFrame, evolution_df: pd.DataFrame, output_path: Path) -> Path:
    data = {
        "events": event_df.to_dict(orient="records") if not event_df.empty else [],
        "phases": phase_df.to_dict(orient="records") if not phase_df.empty else [],
        "artifacts": evolution_df.to_dict(orient="records") if not evolution_df.empty else []
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return output_path

def export_timeline_to_csv(event_df: pd.DataFrame, phase_df: pd.DataFrame, evolution_df: pd.DataFrame, output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {}

    if not event_df.empty:
        p = output_dir / "timeline_export_events.csv"
        event_df.to_csv(p, index=False)
        paths["events"] = p

    if not phase_df.empty:
        p = output_dir / "timeline_export_phases.csv"
        phase_df.to_csv(p, index=False)
        paths["phases"] = p

    if not evolution_df.empty:
        p = output_dir / "timeline_export_artifact_evolution.csv"
        evolution_df.to_csv(p, index=False)
        paths["artifacts"] = p

    return paths

def summarize_timeline_export(manifest: dict) -> dict:
    return {
        "export_timestamp": manifest.get("timestamp_utc"),
        "safety_passed": manifest.get("safety_validated", False)
    }
