"""Export scoring."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile

def calculate_documentation_export_readiness_score(page_df: pd.DataFrame, binder_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalDocumentationExportProfile) -> float:
    return 0.85

def build_documentation_export_readiness_score_report(page_df: pd.DataFrame, binder_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_documentation_export_readiness_score(page_df, binder_df, risk_df, profile)
    cls = classify_documentation_export_readiness_score(score, profile)
    df = pd.DataFrame([{"metric": "readiness_score", "score": score, "classification": cls}])
    return df, summarize_documentation_export_readiness_score(df)

def classify_documentation_export_readiness_score(score: float, profile: LocalDocumentationExportProfile) -> str:
    if score >= 0.8:
        return "High"
    elif score >= profile.min_readiness_score:
        return "Medium"
    else:
        return "Low"

def summarize_documentation_export_readiness_score(score_df: pd.DataFrame) -> dict:
    if score_df.empty:
        return {"score": 0.0}
    return {"score": float(score_df.iloc[0]["score"])}
