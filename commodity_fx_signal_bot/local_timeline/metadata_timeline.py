"""
Metadata card timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_metadata_card_event(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if "model" in rel:
        return "model_metadata"
    if "dataset" in rel:
        return "dataset_metadata"
    if "experiment" in rel:
        return "experiment_metadata"
    return "general_metadata"

def link_metadata_events_to_artifacts(project_root: Path, metadata_df: pd.DataFrame) -> pd.DataFrame:
    if metadata_df.empty:
        return pd.DataFrame()
    mapped = metadata_df.copy()
    mapped['linked_artifact'] = "inferred_artifact"
    return mapped

def build_metadata_card_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def summarize_metadata_timeline(metadata_df: pd.DataFrame) -> dict:
    if metadata_df.empty:
        return {"total_metadata_events": 0}
    return {
        "total_metadata_events": len(metadata_df),
        "unique_metadata_cards": metadata_df['relative_path'].nunique() if 'relative_path' in metadata_df else 0
    }
