"""
Artifact temporal lineage mapping module.
"""

import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def infer_temporal_predecessors(relative_path: str, event_df: pd.DataFrame) -> list[str]:
    # Placeholder: Just finds other files updated before this one in the same module
    if event_df.empty or 'relative_path' not in event_df or 'event_time_utc' not in event_df:
        return []
    target = event_df[event_df['relative_path'] == relative_path]
    if target.empty:
        return []

    first_time = target['event_time_utc'].min()
    module = target['module_name'].iloc[0] if 'module_name' in target and not target['module_name'].isna().all() else None
    if not module:
        return []

    preds = event_df[(event_df['module_name'] == module) & (event_df['relative_path'] != relative_path) & (event_df['event_time_utc'] < first_time)]
    return preds['relative_path'].unique().tolist()[:5]

def infer_temporal_successors(relative_path: str, event_df: pd.DataFrame) -> list[str]:
    if event_df.empty or 'relative_path' not in event_df or 'event_time_utc' not in event_df:
        return []
    target = event_df[event_df['relative_path'] == relative_path]
    if target.empty:
        return []

    last_time = target['event_time_utc'].max()
    module = target['module_name'].iloc[0] if 'module_name' in target and not target['module_name'].isna().all() else None
    if not module:
        return []

    succs = event_df[(event_df['module_name'] == module) & (event_df['relative_path'] != relative_path) & (event_df['event_time_utc'] > last_time)]
    return succs['relative_path'].unique().tolist()[:5]

def build_artifact_temporal_lineage(event_df: pd.DataFrame, evolution_df: pd.DataFrame, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    if evolution_df.empty:
        return pd.DataFrame(), {"total_lineages": 0}

    lineages = []
    for _, row in evolution_df.iterrows():
        path = row['relative_path']
        preds = infer_temporal_predecessors(path, event_df)
        succs = infer_temporal_successors(path, event_df)
        lineages.append({
            "artifact_id": row['artifact_id'],
            "relative_path": path,
            "predecessors": preds,
            "successors": succs
        })

    df = pd.DataFrame(lineages)
    summary = summarize_temporal_lineage(df)
    return df, summary

def summarize_temporal_lineage(lineage_df: pd.DataFrame) -> dict:
    if lineage_df.empty:
        return {"total_lineages": 0}
    return {
        "total_lineages": len(lineage_df)
    }
