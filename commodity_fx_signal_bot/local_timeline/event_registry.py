"""
Build project event registry from local files.
"""

from pathlib import Path
import pandas as pd
from datetime import datetime, timezone
import re
import os

from local_timeline.timeline_config import LocalTimelineProfile
from local_timeline.timeline_models import ProjectEvent, build_project_event_id, project_event_to_dict

def _infer_event_type_from_path(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if "reports/output" in rel:
        return "report_generated_event"
    if "data/lake" in rel:
        return "datalake_artifact_event"
    if "docs/" in rel and not "generated" in rel:
        return "documentation_event"
    if "docs/generated" in rel:
        return "documentation_event"
    if "scripts/" in rel or "config/" in rel:
        return "command_script_event"
    if "evidence" in rel:
        return "evidence_event"
    if "metadata" in rel:
        return "metadata_card_event"
    if "graph" in rel:
        return "graph_event"
    if "scenario" in rel or "regression" in rel:
        return "regression_event"
    if "quality" in rel or "safety" in rel:
        return "quality_event"
    if "backup" in rel or "packaging" in rel or "secrets" in rel:
        return "security_event"
    return "file_modified_event"

def _infer_event_source_label(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if "reports/output" in rel:
        return "reports_output_source"
    if "data/lake" in rel:
        return "data_lake_source"
    if "docs" in rel:
        if "generated" in rel:
            return "generated_docs_source"
        return "docs_source"
    return "project_files_source"

def _infer_event_module_name(path: Path, project_root: Path) -> str | None:
    rel = path.relative_to(project_root).as_posix()
    parts = rel.split('/')
    if len(parts) > 1 and parts[0] in ["data", "reports", "docs", "scripts"]:
        # Try to infer module from second or third folder
        if len(parts) > 2:
            return parts[2] if parts[0] in ["data", "reports"] else parts[1]
    return parts[0] if parts else None

def _infer_event_phase_number(path: Path, text_hint: str | None = None) -> int | None:
    # Basic regex to catch "phase 67" or "phase_67" in path
    match = re.search(r'phase[_\s]?(\d+)', str(path).lower())
    if match:
        return int(match.group(1))
    if text_hint:
        match = re.search(r'phase[_\s]?(\d+)', text_hint.lower())
        if match:
            return int(match.group(1))
    return None

def _classify_event_change_impact(path: Path, event_type: str) -> str:
    if "quality" in str(path) or "safety" in str(path) or "security" in str(path):
        return "high_change_attention"
    if event_type in ["report_generated_event", "documentation_event"]:
        return "medium_change_attention"
    return "informational_change"


def build_event_from_path(path: Path, project_root: Path, profile: LocalTimelineProfile) -> ProjectEvent:
    event_type = _infer_event_type_from_path(path, project_root)
    source_label = _infer_event_source_label(path, project_root)
    module_name = _infer_event_module_name(path, project_root)
    rel_path = path.relative_to(project_root).as_posix()

    # event time from mtime
    try:
        mtime = path.stat().st_mtime
        event_time_utc = datetime.fromtimestamp(mtime, tz=timezone.utc).isoformat()
    except Exception:
        event_time_utc = None

    title = f"File event: {path.name}"
    summary = f"Event for {rel_path}"
    phase_number = _infer_event_phase_number(path)
    change_impact = _classify_event_change_impact(path, event_type)

    event_id = build_project_event_id(event_type, rel_path, event_time_utc, title)

    warnings = []
    if event_time_utc is None:
        warnings.append("missing_timestamp")

    return ProjectEvent(
        event_id=event_id,
        event_type=event_type,
        event_time_utc=event_time_utc,
        source_label=source_label,
        module_name=module_name,
        relative_path=rel_path,
        title=title,
        summary=summary,
        phase_number=phase_number,
        change_impact=change_impact,
        metadata={"file_size": path.stat().st_size if path.exists() else 0},
        warnings=warnings
    )

def build_project_event_registry(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    events = []

    directories_to_scan = []
    if profile.scan_reports:
        directories_to_scan.append(project_root / "reports" / "output")
    if profile.scan_data_lake:
        directories_to_scan.append(project_root / "data" / "lake")
    if profile.scan_docs:
        directories_to_scan.append(project_root / "docs")
    if profile.scan_project_files:
        directories_to_scan.append(project_root / "scripts")
        directories_to_scan.append(project_root / "config")

    for d in directories_to_scan:
        if not d.exists():
            continue
        for root, dirs, files in os.walk(d):
            # Skip hidden and cache dirs
            dirs[:] = [di for di in dirs if not di.startswith('.') and di != '__pycache__']
            for f in files:
                if f.startswith('.'):
                    continue
                path = Path(root) / f
                if path.suffix in ['.pyc', '.pyo']:
                    continue
                # Skip secrets/credentials by name
                if any(sec in f.lower() for sec in ["secret", "credential", "private", "key"]):
                    continue

                evt = build_event_from_path(path, project_root, profile)
                events.append(project_event_to_dict(evt))
                if len(events) >= profile.max_events:
                    break
            if len(events) >= profile.max_events:
                break

    df = pd.DataFrame(events)
    summary = summarize_project_events(df)
    return df, summary

def summarize_project_events(event_df: pd.DataFrame) -> dict:
    if event_df.empty:
        return {"total_events": 0}
    return {
        "total_events": len(event_df),
        "event_types": event_df['event_type'].value_counts().to_dict(),
        "modules": event_df['module_name'].value_counts().head(10).to_dict()
    }

# Provide the rest of the inferred stubs matching the requested names for backwards compatibility
infer_event_type_from_path = _infer_event_type_from_path
infer_event_source_label = _infer_event_source_label
infer_event_module_name = _infer_event_module_name
infer_event_phase_number = _infer_event_phase_number
classify_event_change_impact = _classify_event_change_impact
