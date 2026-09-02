import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def group_scripts_by_family(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family": "run", "scripts": 1}])

def build_script_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_scripts_by_family(project_root, profile)
    return df, summarize_script_sprawl(df)

def summarize_script_sprawl(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["Script calistirilmaz."]}
