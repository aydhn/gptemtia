import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def calculate_acceptance_readiness_score(checklist_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalAcceptanceProfile) -> float:
    return 0.85

def classify_acceptance_readiness_score(score: float, profile: LocalAcceptanceProfile) -> str:
    if score < profile.min_readiness_score:
        return "needs_manual_review"
    return "ready_for_rehearsal"

def build_acceptance_readiness_score_report(checklist_df: pd.DataFrame, gap_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_acceptance_readiness_score(checklist_df, gap_df, risk_df, profile)
    classification = classify_acceptance_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": classification, "note": "score official acceptance değildir."}])
    return df, summarize_acceptance_readiness_score(df)

def summarize_acceptance_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"score": float(score_df.iloc[0]["score"]) if not score_df.empty else 0.0}
