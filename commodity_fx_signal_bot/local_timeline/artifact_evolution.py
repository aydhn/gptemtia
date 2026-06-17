"""
Build artifact evolution registry.
"""

import pandas as pd
from datetime import datetime, timezone
from pathlib import Path

from local_timeline.timeline_config import LocalTimelineProfile
from local_timeline.timeline_models import ArtifactEvolutionRecord, build_artifact_evolution_id, artifact_evolution_record_to_dict

def build_artifact_evolution_record(relative_path: str, events_for_artifact: pd.DataFrame, profile: LocalTimelineProfile) -> ArtifactEvolutionRecord:
    first_seen = events_for_artifact['event_time_utc'].min() if 'event_time_utc' in events_for_artifact and not events_for_artifact['event_time_utc'].isna().all() else None
    last_seen = events_for_artifact['event_time_utc'].max() if 'event_time_utc' in events_for_artifact and not events_for_artifact['event_time_utc'].isna().all() else None

    event_types = events_for_artifact['event_type'].unique().tolist()
    module_name = events_for_artifact['module_name'].dropna().iloc[0] if not events_for_artifact['module_name'].dropna().empty else None

    temporal_status = "event_fresh"
    warnings = []

    if last_seen:
        try:
            last_date = datetime.fromisoformat(str(last_seen).replace("Z", "+00:00"))
            days_diff = (datetime.now(timezone.utc) - last_date).days
            if days_diff > profile.stale_days_warning:
                temporal_status = "event_stale"
                warnings.append("stale_artifact")
            elif days_diff > profile.freshness_days_warning:
                temporal_status = "event_warning_stale"
        except Exception:
            temporal_status = "event_unknown_time"
            warnings.append("invalid_timestamp")
    else:
        temporal_status = "event_missing_timestamp"
        warnings.append("missing_timestamp")

    impacts = events_for_artifact['change_impact'].unique()
    change_impact = "high_change_attention" if "high_change_attention" in impacts else "informational_change"

    return ArtifactEvolutionRecord(
        artifact_id=build_artifact_evolution_id(relative_path),
        relative_path=relative_path,
        module_name=module_name,
        first_seen_utc=first_seen,
        last_modified_utc=last_seen,
        event_count=len(events_for_artifact),
        event_types=event_types,
        temporal_status=temporal_status,
        change_impact=change_impact,
        warnings=warnings
    )

def build_artifact_evolution_registry(event_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    if event_df.empty:
        return pd.DataFrame(), {"total_artifacts": 0}

    records = []
    for rel_path, group in event_df.groupby('relative_path'):
        rec = build_artifact_evolution_record(str(rel_path), group, profile)
        records.append(artifact_evolution_record_to_dict(rec))

    df = pd.DataFrame(records)
    summary = summarize_artifact_evolution(df)
    return df, summary

def detect_artifact_evolution_patterns(evolution_df: pd.DataFrame) -> pd.DataFrame:
    if evolution_df.empty:
        return pd.DataFrame()

    patterns = []
    for _, row in evolution_df.iterrows():
        pats = []
        if row['temporal_status'] == 'event_stale':
            pats.append('stale_artifact')
        if row['event_count'] > 10:
            pats.append('frequently_updated')
        if row['event_count'] == 1:
            pats.append('single_event_artifact')
        if row['temporal_status'] == 'event_missing_timestamp':
            pats.append('missing_timestamp')

        patterns.append({
            "artifact_id": row['artifact_id'],
            "patterns": pats
        })

    return pd.DataFrame(patterns)

def summarize_artifact_evolution(evolution_df: pd.DataFrame) -> dict:
    if evolution_df.empty:
        return {"total_artifacts": 0}
    return {
        "total_artifacts": len(evolution_df),
        "stale_count": len(evolution_df[evolution_df['temporal_status'] == 'event_stale']) if 'temporal_status' in evolution_df else 0
    }
