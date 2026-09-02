import pandas as pd
from pathlib import Path
from .usability_config import LocalUsabilityProfile

def build_default_reading_order_items(profile: LocalUsabilityProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item": "README.md", "order": 1}])

def build_script_reading_order_index(project_root: Path, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reading_order_items(profile)
    return df, {"total": len(df)}

def build_report_reading_order_index(project_root: Path, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reading_order_items(profile)
    return df, {"total": len(df)}

def summarize_reading_order_index(order_df: pd.DataFrame) -> dict:
    return {"total": len(order_df)}
