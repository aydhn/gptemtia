import pandas as pd
from .usability_config import LocalUsabilityProfile

def build_default_troubleshooting_items(profile: LocalUsabilityProfile) -> pd.DataFrame:
    return pd.DataFrame([{"issue": "command not found"}])

def build_operator_troubleshooting_index(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_troubleshooting_items(profile)
    return df, {"total": len(df)}

def summarize_troubleshooting_index(troubleshooting_df: pd.DataFrame) -> dict:
    return {"total": len(troubleshooting_df)}
