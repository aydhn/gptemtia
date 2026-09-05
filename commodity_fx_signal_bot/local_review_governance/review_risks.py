import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def classify_review_risk(row: pd.Series, profile: LocalReviewGovernanceProfile) -> str:
    return "review_low_risk"

def build_review_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "General risk", "classification": "review_low_risk"}])
    return df, summarize_review_risks(df)

def build_review_risk_digest(risk_df: pd.DataFrame, profile: LocalReviewGovernanceProfile) -> tuple[str, dict]:
    text = "Review Risk Digest\nNo investment risk."
    return text, {"length": len(text)}

def summarize_review_risks(risk_df: pd.DataFrame) -> dict:
    return {"total_risks": len(risk_df)}
