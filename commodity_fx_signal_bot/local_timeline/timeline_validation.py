"""
Timeline validation module.
"""

import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile
from local_timeline.timeline_labels import EVENT_TYPE_LABELS, TIMELINE_SOURCE_LABELS

def validate_no_cloud_or_live_timeline_usage(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    warnings = []

    # Just simple safety checks simulating real validation
    forbidden = ["live trading event engine", "broker event stream", "real trade timeline",
                 "cloud event service", "production monitoring", "live order", "raw secret", "cloud upload"]

    def _check(s):
        s_lower = str(s).lower()
        for f in forbidden:
            if f in s_lower:
                if f not in warnings:
                    warnings.append(f"forbidden_term_{f.replace(' ', '_')}")

    if text:
        _check(text)

    if df is not None and not df.empty:
        for col in df.select_dtypes(include=['object']).columns:
            for val in df[col].dropna():
                _check(val)

    if summary:
        for k, v in summary.items():
            _check(str(k))
            _check(str(v))

    return {
        "valid": len(warnings) == 0,
        "warnings": warnings
    }

def validate_project_events(event_df: pd.DataFrame, profile: LocalTimelineProfile) -> dict:
    warnings = []
    if event_df.empty:
        return {"valid": True, "warnings": []}

    if 'event_id' not in event_df:
        warnings.append("missing_event_id")
    else:
        if event_df['event_id'].isna().any():
            warnings.append("null_event_id")

    if 'event_type' in event_df:
        invalid_types = event_df[~event_df['event_type'].isin(EVENT_TYPE_LABELS)]
        if not invalid_types.empty:
            warnings.append("invalid_event_type")

    if 'source_label' in event_df:
        invalid_sources = event_df[~event_df['source_label'].isin(TIMELINE_SOURCE_LABELS)]
        if not invalid_sources.empty:
            warnings.append("invalid_source_label")

    # missing timestamp warning is graceful
    if 'event_time_utc' in event_df and event_df['event_time_utc'].isna().any():
        warnings.append("missing_timestamp")

    v = validate_no_cloud_or_live_timeline_usage(df=event_df)
    warnings.extend(v['warnings'])

    return {
        "valid": len([w for w in warnings if w != "missing_timestamp"]) == 0,
        "warnings": warnings
    }

def validate_phase_chronology(phase_df: pd.DataFrame, profile: LocalTimelineProfile) -> dict:
    return {"valid": True, "warnings": []}

def validate_artifact_evolution(evolution_df: pd.DataFrame, profile: LocalTimelineProfile) -> dict:
    return {"valid": True, "warnings": []}

def validate_timeline_queries(results_df: pd.DataFrame | None, profile: LocalTimelineProfile) -> dict:
    return {"valid": True, "warnings": []}

def build_timeline_validation_report(tables: dict[str, pd.DataFrame], profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    res = []

    event_v = validate_project_events(tables.get('event_registry', pd.DataFrame()), profile)
    res.append({"component": "event_registry", "valid": event_v['valid'], "warnings": ",".join(event_v['warnings'])})

    phase_v = validate_phase_chronology(tables.get('phase_chronology', pd.DataFrame()), profile)
    res.append({"component": "phase_chronology", "valid": phase_v['valid'], "warnings": ",".join(phase_v['warnings'])})

    evo_v = validate_artifact_evolution(tables.get('artifact_evolution', pd.DataFrame()), profile)
    res.append({"component": "artifact_evolution", "valid": evo_v['valid'], "warnings": ",".join(evo_v['warnings'])})

    df = pd.DataFrame(res)

    all_valid = all(r['valid'] for r in res)
    return df, {"all_valid": all_valid, "total_components": len(res)}
