"""
Build phase chronology registry from project events.
"""

from pathlib import Path
import pandas as pd
import re

from local_timeline.timeline_config import LocalTimelineProfile
from local_timeline.timeline_models import PhaseChronologyItem, phase_chronology_item_to_dict

def infer_phase_titles_from_phase_log(project_root: Path) -> pd.DataFrame:
    phase_log_path = project_root / "docs" / "PHASE_LOG.md"
    phases = []
    if phase_log_path.exists():
        with open(phase_log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                match = re.match(r'^##\s*Phase\s*(\d+)\s*(.*)', line, re.IGNORECASE)
                if match:
                    phase_num = int(match.group(1))
                    phase_title = match.group(2).strip()
                    if not phase_title:
                        phase_title = f"Phase {phase_num}"
                    phases.append({"phase_number": phase_num, "phase_title": phase_title})
    return pd.DataFrame(phases)

def map_events_to_phases(event_df: pd.DataFrame, phase_df: pd.DataFrame | None = None) -> pd.DataFrame:
    if event_df.empty:
        return pd.DataFrame()

    # Just return event_df sorted by phase if we want to show mapping
    mapped = event_df.dropna(subset=['phase_number']).copy()
    if phase_df is not None and not phase_df.empty and not mapped.empty:
        mapped = pd.merge(mapped, phase_df, on="phase_number", how="left")
    return mapped

def build_phase_chronology_registry(event_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    if event_df.empty:
        return pd.DataFrame(), {"total_phases": 0}

    mapped = event_df.dropna(subset=['phase_number']).copy()

    phases_dict = {}
    for phase_num, group in mapped.groupby('phase_number'):
        first_seen = group['event_time_utc'].min() if 'event_time_utc' in group and not group['event_time_utc'].isna().all() else None
        last_seen = group['event_time_utc'].max() if 'event_time_utc' in group and not group['event_time_utc'].isna().all() else None
        modules = group['module_name'].dropna().unique().tolist()
        artifacts = group['relative_path'].dropna().unique().tolist()

        phases_dict[phase_num] = phase_chronology_item_to_dict(PhaseChronologyItem(
            phase_number=int(phase_num),
            phase_title=f"Phase {int(phase_num)}",
            first_seen_utc=first_seen,
            last_seen_utc=last_seen,
            related_modules=modules,
            related_artifacts=artifacts,
            event_count=len(group),
            status="completed",
            warnings=[]
        ))

    df = pd.DataFrame(list(phases_dict.values()))
    summary = summarize_phase_chronology(df)
    return df, summary

def build_phase_event_digest(event_df: pd.DataFrame, phase_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[str, dict]:
    if phase_df.empty:
        return "No phase events found.", {}

    lines = ["# Phase Event Digest\n"]
    for _, row in phase_df.iterrows():
        lines.append(f"## {row['phase_title']}")
        lines.append(f"- Event Count: {row['event_count']}")
        if row['first_seen_utc']:
            lines.append(f"- First Seen: {row['first_seen_utc']}")
        if row['last_seen_utc']:
            lines.append(f"- Last Seen: {row['last_seen_utc']}")
        lines.append(f"- Related Modules: {len(row['related_modules'])}")
        lines.append("")

    text = "\n".join(lines)
    return text, {"total_lines": len(lines)}

def summarize_phase_chronology(phase_df: pd.DataFrame) -> dict:
    if phase_df.empty:
        return {"total_phases": 0}
    return {
        "total_phases": len(phase_df),
        "total_phase_events": phase_df['event_count'].sum() if 'event_count' in phase_df else 0
    }
