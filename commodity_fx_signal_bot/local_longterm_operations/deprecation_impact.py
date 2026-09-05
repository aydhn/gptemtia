"""Deprecation impact."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_deprecation_impact_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([{"impact": "none", "warnings": ["Gerçek migration planı değildir."]}])

def build_deprecation_impact_rehearsal_matrix(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_deprecation_impact_items(profile)
    return df, summarize_deprecation_impact(df)

def summarize_deprecation_impact(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
