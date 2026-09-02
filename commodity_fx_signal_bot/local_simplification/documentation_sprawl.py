import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def group_docs_by_family(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family": "generated", "docs": 1}])

def build_documentation_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_docs_by_family(project_root, profile)
    return df, summarize_documentation_sprawl(df)

def summarize_documentation_sprawl(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["docs degistirilmez."]}
