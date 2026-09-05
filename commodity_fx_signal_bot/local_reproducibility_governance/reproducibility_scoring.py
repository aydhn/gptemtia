"""Reproducibility scoring."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def calculate_reproducibility_readiness_score(dossier_df: pd.DataFrame, runbook_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalReproducibilityGovernanceProfile) -> float:
    return 1.0

def classify_reproducibility_readiness_score(score: float, profile: LocalReproducibilityGovernanceProfile) -> str:
    return "ready" if score >= profile.min_readiness_score else "low"

def build_reproducibility_readiness_score_report(dossier_df: pd.DataFrame, runbook_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_reproducibility_readiness_score(dossier_df, runbook_df, risk_df, profile)
    df = pd.DataFrame([{"score": score, "class": classify_reproducibility_readiness_score(score, profile)}])
    return df, summarize_reproducibility_readiness_score(df)

def summarize_reproducibility_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"score": float(score_df["score"].iloc[0]) if not score_df.empty else 0.0, "note": "Reproducibility readiness score official certification degildir. Low score manual review onerir."}
