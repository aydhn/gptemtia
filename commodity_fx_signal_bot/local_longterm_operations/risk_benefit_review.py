"""Risk benefit review."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_risk_benefit_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([{"risk": "low", "warnings": ["Yatırım riski değildir."]}])

def build_v1x_risk_benefit_review_matrix(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_risk_benefit_items(profile)
    return df, summarize_risk_benefit_review(df)

def summarize_risk_benefit_review(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
