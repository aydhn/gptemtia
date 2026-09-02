import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def count_files_by_layer(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"layer": "core", "count": 1}])

def build_file_count_complexity_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = count_files_by_layer(project_root, profile)
    return df, summarize_file_count_complexity(df)

def summarize_file_count_complexity(df: pd.DataFrame) -> dict:
    return {"layers": len(df), "warnings": ["File count cleanup talimati degildir."]}
