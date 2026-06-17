"""
File modification timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_file_timeline_category(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if rel.startswith("scripts/"):
        return "script"
    if rel.startswith("config/"):
        return "config"
    return "source"

def build_file_modification_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    # In practice this is extracted from the global event dataframe via the pipeline
    # returning empty df here and letting the pipeline handle the data filtering
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def build_file_change_summary(file_timeline_df: pd.DataFrame) -> dict:
    if file_timeline_df.empty:
        return {"total_file_events": 0}
    return {
        "total_file_events": len(file_timeline_df),
        "unique_files": file_timeline_df['relative_path'].nunique() if 'relative_path' in file_timeline_df else 0
    }

def summarize_file_timeline(file_timeline_df: pd.DataFrame) -> dict:
    return build_file_change_summary(file_timeline_df)
