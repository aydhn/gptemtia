"""Atlas scoring module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def calculate_meta_index_readiness_score(meta_df: pd.DataFrame, lookup_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalProjectAtlasProfile) -> float:
    return 1.0

def classify_meta_index_readiness_score(score: float, profile: LocalProjectAtlasProfile) -> str:
    if score < profile.min_readiness_score: return "atlas_rehearsal_missing"
    return "atlas_rehearsal_ready"

def build_meta_index_readiness_score_report(meta_df: pd.DataFrame, lookup_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_meta_index_readiness_score(meta_df, lookup_df, risk_df, profile)
    label = classify_meta_index_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "label": label}])
    return df, summarize_meta_index_readiness_score(df)

def summarize_meta_index_readiness_score(score_df: pd.DataFrame) -> dict:
    return {"score": float(score_df["score"].iloc[0]) if not score_df.empty else 0.0}
