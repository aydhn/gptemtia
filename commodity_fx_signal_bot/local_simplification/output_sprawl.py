import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def group_outputs_by_family(project_root: Path, base_dir_name: str, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family": "csv", "outputs": 1}])

def build_report_output_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_outputs_by_family(project_root, "reports/output", profile)
    return df, summarize_output_sprawl(df)

def build_datalake_output_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_outputs_by_family(project_root, "data/lake", profile)
    return df, summarize_output_sprawl(df)

def summarize_output_sprawl(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["Output dosyasi tasinmaz/silinmez."]}
