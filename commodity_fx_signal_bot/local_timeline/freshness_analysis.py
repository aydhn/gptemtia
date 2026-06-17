"""
Freshness analysis module.
"""

import pandas as pd
from datetime import datetime, timezone

from local_timeline.timeline_config import LocalTimelineProfile

def classify_event_freshness(event_time_utc: str | None, profile: LocalTimelineProfile) -> str:
    if not event_time_utc:
        return "event_missing_timestamp"
    try:
        dt = datetime.fromisoformat(str(event_time_utc).replace("Z", "+00:00"))
        days_diff = (datetime.now(timezone.utc) - dt).days
        if days_diff > profile.stale_days_warning:
            return "event_stale"
        if days_diff > profile.freshness_days_warning:
            return "event_warning_stale"
        return "event_fresh"
    except Exception:
        return "event_unknown_time"

def build_event_freshness_report(event_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    if event_df.empty:
        return pd.DataFrame(), {"total_fresh": 0}

    mapped = event_df.copy()
    mapped['freshness'] = mapped['event_time_utc'].apply(lambda x: classify_event_freshness(x, profile))

    summary = summarize_freshness_report(mapped)
    return mapped, summary

def build_stale_artifact_timeline_report(evolution_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    if evolution_df.empty:
        return pd.DataFrame(), {"total_stale": 0}

    stale = evolution_df[evolution_df['temporal_status'] == 'event_stale'].copy()
    return stale, {"total_stale": len(stale)}

def summarize_freshness_report(freshness_df: pd.DataFrame, stale_df: pd.DataFrame | None = None) -> dict:
    if freshness_df.empty:
        return {"total_events": 0}

    counts = freshness_df['freshness'].value_counts().to_dict() if 'freshness' in freshness_df else {}
    return {
        "total_events": len(freshness_df),
        "fresh_count": counts.get("event_fresh", 0),
        "stale_count": counts.get("event_stale", 0),
        "warning_count": counts.get("event_warning_stale", 0),
        "missing_timestamp_count": counts.get("event_missing_timestamp", 0)
    }
