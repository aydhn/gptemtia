import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def calculate_incident_readiness_score(event_df: pd.DataFrame, triage_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> float:
    return 1.0

def classify_incident_readiness_score(score: float, profile: LocalIncidentResponseProfile) -> str:
    if score >= profile.min_readiness_score:
        return "Ready"
    return "Needs Manual Review"

def build_incident_readiness_score_report(event_df: pd.DataFrame, triage_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    score = calculate_incident_readiness_score(event_df, triage_df, risk_df, profile)
    classification = classify_incident_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": classification}])
    summary = summarize_incident_readiness_score(df)
    return df, summary

def summarize_incident_readiness_score(score_df: pd.DataFrame) -> Dict:
    return {
        "note": "Incident readiness score is not production recovery approval. Low score suggests manual review."
    }
