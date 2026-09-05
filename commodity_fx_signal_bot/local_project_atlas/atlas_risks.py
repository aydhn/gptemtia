"""Atlas risks module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def classify_meta_index_risk(row: pd.Series, profile: LocalProjectAtlasProfile) -> str:
    return "atlas_low_risk"

def build_meta_index_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "minimal", "label": "atlas_low_risk"}])
    return df, summarize_meta_index_risks(df)

def build_meta_index_risk_digest(risk_df: pd.DataFrame, profile: LocalProjectAtlasProfile) -> tuple[str, dict]:
    return "Digest: low risk", {"status": "ok"}

def summarize_meta_index_risks(risk_df: pd.DataFrame) -> dict:
    return {"risks": len(risk_df)}
