import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def classify_preservation_risk(row: pd.Series, profile: LocalPostCompletionPreservationProfile) -> str:
    return "preservation_low_risk"

def build_preservation_risk_digest(risk_df: pd.DataFrame, profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    return "Digest", {"len": 1}

def build_preservation_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "none"}])
    return df, summarize_preservation_risks(df)

def summarize_preservation_risks(risk_df: pd.DataFrame) -> dict:
    return {"count": len(risk_df)}
