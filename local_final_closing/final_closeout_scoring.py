import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def calculate_final_closeout_readiness_score(lock_df: pd.DataFrame, constitution_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> float:
    base = 1.0
    if risk_df is not None and not risk_df.empty:
        criticals = len(risk_df[risk_df["level"] == "final_closeout_critical_risk"])
        base -= (criticals * 0.2)
    return max(0.0, min(1.0, base))

def classify_final_closeout_readiness_score(score: float, profile: LocalFinalClosingProfile) -> str:
    if score >= profile.min_readiness_score:
        return "ready_for_manual_review"
    return "not_ready"

def build_final_closeout_readiness_score_report(lock_df: pd.DataFrame, constitution_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_final_closeout_readiness_score(lock_df, constitution_df, risk_df, profile)
    classification = classify_final_closeout_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": classification}])
    return df, summarize_final_closeout_readiness_score(df)

def summarize_final_closeout_readiness_score(score_df: pd.DataFrame) -> dict:
    if score_df is None or score_df.empty:
        return {"score": 0.0}
    return {"score": float(score_df.iloc[0]["score"])}
