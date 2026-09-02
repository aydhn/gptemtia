import pandas as pd
from .usability_config import LocalUsabilityProfile

def detect_usability_exceptions(friction_df: pd.DataFrame, command_df: pd.DataFrame, nav_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "Missing doc for x"}])

def build_usability_exception_register(friction_df: pd.DataFrame, command_df: pd.DataFrame, nav_df: pd.DataFrame, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_usability_exceptions(friction_df, command_df, nav_df)
    return df, {"total": len(df)}

def summarize_usability_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total": len(exception_df)}
