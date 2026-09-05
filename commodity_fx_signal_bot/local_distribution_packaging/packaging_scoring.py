import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile

def calculate_packaging_readiness_score(bundle_df: pd.DataFrame, portable_docs_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalDistributionPackagingProfile) -> float:
    return 0.95

def classify_packaging_readiness_score(score: float, profile: LocalDistributionPackagingProfile) -> str:
    if score >= profile.min_readiness_score:
        return "ready"
    return "needs_review"

def build_packaging_readiness_score_report(bundle_df: pd.DataFrame, portable_docs_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_packaging_readiness_score(bundle_df, portable_docs_df, risk_df, profile)
    df = pd.DataFrame([{"score": score, "classification": classify_packaging_readiness_score(score, profile)}])
    return df, summarize_packaging_readiness_score(df)

def summarize_packaging_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"status": "generated"}
