"""
DataLake artifact timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_datalake_domain(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if "data/lake/" in rel:
        parts = rel.split('/')
        if len(parts) > 2:
            return parts[2]
    return "unknown_domain"

def build_datalake_artifact_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def build_datalake_domain_activity_summary(datalake_df: pd.DataFrame) -> pd.DataFrame:
    if datalake_df.empty:
        return pd.DataFrame()

    if 'relative_path' not in datalake_df:
        return pd.DataFrame()

    datalake_df['domain'] = datalake_df['relative_path'].apply(lambda x: classify_datalake_domain(Path(x), Path(".")))
    summary = datalake_df.groupby('domain').size().reset_index(name='event_count')
    return summary

def summarize_datalake_timeline(datalake_df: pd.DataFrame) -> dict:
    if datalake_df.empty:
        return {"total_datalake_events": 0}
    return {
        "total_datalake_events": len(datalake_df),
        "unique_artifacts": datalake_df['relative_path'].nunique() if 'relative_path' in datalake_df else 0
    }
