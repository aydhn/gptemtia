"""
Documentation timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_documentation_type(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if "generated" in rel:
        return "generated_documentation"
    return "source_documentation"

def map_docs_to_phase_references(project_root: Path, doc_df: pd.DataFrame) -> pd.DataFrame:
    if doc_df.empty:
        return pd.DataFrame()

    # Just a placeholder structure
    mapped = doc_df.copy()
    mapped['inferred_phase_ref'] = mapped['phase_number']
    return mapped

def build_documentation_evolution_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def summarize_documentation_timeline(doc_df: pd.DataFrame) -> dict:
    if doc_df.empty:
        return {"total_doc_events": 0}
    return {
        "total_doc_events": len(doc_df),
        "unique_docs": doc_df['relative_path'].nunique() if 'relative_path' in doc_df else 0
    }
