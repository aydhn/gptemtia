import pandas as pd
from pathlib import Path
from .usability_config import LocalUsabilityProfile

def classify_navigation_item(path: Path, project_root: Path) -> dict:
    return {"path": str(path), "type": "doc"}

def build_datalake_navigation_index(project_root: Path, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"path": "data/lake/local_usability", "type": "dir"}])
    return df, {"total": len(df)}

def build_generated_docs_navigation_index(project_root: Path, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"path": "docs/generated", "type": "dir"}])
    return df, {"total": len(df)}

def summarize_navigation_index(nav_df: pd.DataFrame) -> dict:
    return {"total": len(nav_df)}
