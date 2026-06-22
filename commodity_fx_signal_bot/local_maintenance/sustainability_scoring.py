import pandas as pd
from typing import Tuple, Dict, Any

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def calculate_sustainability_score(
    task_df: pd.DataFrame,
    gap_df: pd.DataFrame,
    risk_df: pd.DataFrame,
    profile: LocalMaintenanceProfile
) -> float:
    # A simple scoring heuristic
    base_score = 1.0

    penalty = 0.0
    if gap_df is not None and not gap_df.empty:
        penalty += len(gap_df) * 0.05

    if risk_df is not None and not risk_df.empty:
        if "risk_level" in risk_df:
            high_risks = len(risk_df[risk_df["risk_level"] == "sustainability_high_risk"])
            medium_risks = len(risk_df[risk_df["risk_level"] == "sustainability_medium_risk"])
            penalty += (high_risks * 0.1) + (medium_risks * 0.05)

    score = max(0.0, base_score - penalty)
    return float(score)

def classify_sustainability_score(score: float, profile: LocalMaintenanceProfile) -> str:
    if score >= 0.9:
        return "Excellent"
    elif score >= 0.7:
        return "Good"
    elif score >= profile.min_sustainability_score:
        return "Needs Improvement"
    else:
        return "Poor (Requires Manual Review)"

def build_sustainability_score_report(
    task_df: pd.DataFrame,
    gap_df: pd.DataFrame,
    risk_df: pd.DataFrame,
    profile: LocalMaintenanceProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:

    score = calculate_sustainability_score(task_df, gap_df, risk_df, profile)
    classification = classify_sustainability_score(score, profile)

    df = pd.DataFrame([{
        "metric": "Overall Sustainability Score",
        "value": score,
        "classification": classification
    }])

    summary = summarize_sustainability_score(df)
    return df, summary

def summarize_sustainability_score(score_df: pd.DataFrame) -> Dict[str, Any]:
    if score_df is None or score_df.empty:
        return {"score": 0.0, "classification": "Unknown"}

    score = score_df.iloc[0]["value"]
    classification = score_df.iloc[0]["classification"]

    return {
        "score": score,
        "classification": classification,
        "disclaimer": "Sustainability score is not a production health score or an official maintenance/SLA score. Low score suggests manual review."
    }
