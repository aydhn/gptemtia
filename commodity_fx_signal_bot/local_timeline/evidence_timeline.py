"""
Evidence timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_evidence_event(path: Path, project_root: Path) -> str:
    return "evidence_update"

def link_evidence_events_to_controls(project_root: Path, evidence_df: pd.DataFrame) -> pd.DataFrame:
    if evidence_df.empty:
        return pd.DataFrame()
    mapped = evidence_df.copy()
    mapped['linked_control'] = "inferred_control"
    return mapped

def build_evidence_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def summarize_evidence_timeline(evidence_df: pd.DataFrame) -> dict:
    if evidence_df.empty:
        return {"total_evidence_events": 0}
    return {
        "total_evidence_events": len(evidence_df),
        "unique_evidence_artifacts": evidence_df['relative_path'].nunique() if 'relative_path' in evidence_df else 0
    }
