"""
Event gap detection module.
"""

import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def detect_missing_phase_events(phase_df: pd.DataFrame, event_df: pd.DataFrame) -> pd.DataFrame:
    # Just a stub logic to represent gap detection
    gaps = []
    if phase_df.empty or event_df.empty:
        return pd.DataFrame(gaps)

    # Check if there are phases in phase_df that have 0 events mapped
    # In our phase_chronology builder we already filter out 0 event phases,
    # but theoretically if phase log has phase 60 and no events exist:
    if 'event_count' in phase_df:
        missing = phase_df[phase_df['event_count'] == 0]
        for _, row in missing.iterrows():
            gaps.append({
                "gap_type": "missing_phase_events",
                "target": f"Phase {row['phase_number']}",
                "description": "Phase log exists but no events found."
            })
    return pd.DataFrame(gaps)

def detect_missing_expected_timeline_domains(event_df: pd.DataFrame) -> pd.DataFrame:
    gaps = []
    if event_df.empty:
        return pd.DataFrame(gaps)

    expected_domains = ["reports_output_source", "data_lake_source", "docs_source", "project_files_source"]
    if 'source_label' in event_df:
        found_domains = set(event_df['source_label'].unique())
        for d in expected_domains:
            if d not in found_domains:
                gaps.append({
                    "gap_type": "missing_expected_domain",
                    "target": d,
                    "description": f"Expected domain {d} has no events."
                })
    return pd.DataFrame(gaps)

def detect_stale_or_missing_artifact_events(evolution_df: pd.DataFrame, profile: LocalTimelineProfile) -> pd.DataFrame:
    gaps = []
    if evolution_df.empty:
        return pd.DataFrame(gaps)

    if 'temporal_status' in evolution_df:
        stale = evolution_df[evolution_df['temporal_status'].isin(['event_stale', 'event_missing_timestamp'])]
        for _, row in stale.iterrows():
            gaps.append({
                "gap_type": row['temporal_status'],
                "target": row['relative_path'],
                "description": f"Artifact is {row['temporal_status']}."
            })
    return pd.DataFrame(gaps)

def detect_event_gaps(event_df: pd.DataFrame, phase_df: pd.DataFrame, evolution_df: pd.DataFrame, profile: LocalTimelineProfile) -> pd.DataFrame:
    gaps_dfs = [
        detect_missing_phase_events(phase_df, event_df),
        detect_missing_expected_timeline_domains(event_df),
        detect_stale_or_missing_artifact_events(evolution_df, profile)
    ]
    gaps_dfs = [df for df in gaps_dfs if not df.empty]
    if not gaps_dfs:
        return pd.DataFrame()
    return pd.concat(gaps_dfs, ignore_index=True)

def build_event_gap_report(event_df: pd.DataFrame, phase_df: pd.DataFrame, evolution_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    gaps_df = detect_event_gaps(event_df, phase_df, evolution_df, profile)
    summary = summarize_event_gaps(gaps_df)
    return gaps_df, summary

def summarize_event_gaps(gap_df: pd.DataFrame) -> dict:
    if gap_df.empty:
        return {"total_gaps": 0}
    return {
        "total_gaps": len(gap_df),
        "gap_types": gap_df['gap_type'].value_counts().to_dict() if 'gap_type' in gap_df else {}
    }
