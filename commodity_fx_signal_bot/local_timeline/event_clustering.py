"""
Event clustering by module, phase, and source.
"""

import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def cluster_events_by_module(event_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    if event_df.empty or 'module_name' not in event_df:
        return pd.DataFrame(), {}

    df = event_df.groupby('module_name').size().reset_index(name='event_count')
    return df, {"total_modules": len(df)}

def cluster_events_by_phase(event_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    if event_df.empty or 'phase_number' not in event_df:
        return pd.DataFrame(), {}

    df = event_df.groupby('phase_number').size().reset_index(name='event_count')
    return df, {"total_phases": len(df)}

def cluster_events_by_source(event_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    if event_df.empty or 'source_label' not in event_df:
        return pd.DataFrame(), {}

    df = event_df.groupby('source_label').size().reset_index(name='event_count')
    return df, {"total_sources": len(df)}

def build_module_event_cluster_report(event_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    module_df, _ = cluster_events_by_module(event_df, profile)
    if not module_df.empty:
        module_df = module_df.sort_values(by='event_count', ascending=False)
    summary = summarize_event_clusters(module_df)
    return module_df, summary

def summarize_event_clusters(cluster_df: pd.DataFrame) -> dict:
    if cluster_df.empty:
        return {"total_clusters": 0}
    return {
        "total_clusters": len(cluster_df),
        "top_cluster_count": int(cluster_df['event_count'].max()) if 'event_count' in cluster_df else 0
    }
