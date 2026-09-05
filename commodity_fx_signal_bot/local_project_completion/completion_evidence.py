import pandas as pd
from pathlib import Path
from .completion_config import LocalProjectCompletionProfile

def map_project_completion_evidence_sources(project_root: Path, profile: LocalProjectCompletionProfile) -> pd.DataFrame:
    return pd.DataFrame([{"source": "docs/ARCHITECTURE.md", "mapped": True}])

def build_project_completion_evidence_map(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = map_project_completion_evidence_sources(project_root, profile)
    return df, summarize_project_completion_evidence(df)

def summarize_project_completion_evidence(df: pd.DataFrame) -> dict:
    return {"evidences": len(df), "note": "Evidence map is not proof of official completion."}
