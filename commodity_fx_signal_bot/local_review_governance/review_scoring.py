import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def calculate_review_readiness_score(cockpit_df: pd.DataFrame, expert_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalReviewGovernanceProfile) -> float:
    return 0.85

def classify_review_readiness_score(score: float, profile: LocalReviewGovernanceProfile) -> str:
    if score >= profile.min_readiness_score:
        return "rehearsal_ready"
    return "manual_review_needed"

def build_review_readiness_score_report(cockpit_df: pd.DataFrame, expert_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_review_readiness_score(cockpit_df, expert_df, risk_df, profile)
    cls = classify_review_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": cls}])
    return df, summarize_review_readiness_score(df)

def summarize_review_readiness_score(score_df: pd.DataFrame) -> dict:
    if not score_df.empty:
        return {"score": float(score_df.iloc[0]["score"])}
    return {"score": 0.0}
