"""
Quality and safety timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_quality_safety_event(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if "safety" in rel:
        return "safety_update"
    return "quality_update"

def build_quality_safety_activity_summary(qs_df: pd.DataFrame) -> pd.DataFrame:
    if qs_df.empty:
        return pd.DataFrame()

    if 'relative_path' not in qs_df:
        return pd.DataFrame()

    qs_df['category'] = qs_df['relative_path'].apply(lambda x: classify_quality_safety_event(Path(x), Path(".")))
    summary = qs_df.groupby('category').size().reset_index(name='event_count')
    return summary

def build_quality_safety_event_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def summarize_quality_safety_timeline(qs_df: pd.DataFrame) -> dict:
    if qs_df.empty:
        return {"total_qs_events": 0}
    return {
        "total_qs_events": len(qs_df),
        "unique_qs_files": qs_df['relative_path'].nunique() if 'relative_path' in qs_df else 0
    }
