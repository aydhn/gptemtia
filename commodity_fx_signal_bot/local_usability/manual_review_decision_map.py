import pandas as pd
from .usability_config import LocalUsabilityProfile

def build_default_manual_review_decisions(profile: LocalUsabilityProfile) -> pd.DataFrame:
    return pd.DataFrame([{"decision": "review docs"}])

def build_manual_review_decision_map(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_manual_review_decisions(profile)
    return df, {"total": len(df)}

def summarize_manual_review_decision_map(decision_df: pd.DataFrame) -> dict:
    return {"total": len(decision_df)}
