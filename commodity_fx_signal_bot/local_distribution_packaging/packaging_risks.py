import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile

def classify_packaging_risk(row: pd.Series, profile: LocalDistributionPackagingProfile) -> str:
    return "packaging_low_risk"

def build_packaging_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "None detected", "level": "low"}])
    return df, summarize_packaging_risks(df)

def build_packaging_risk_digest(risk_df: pd.DataFrame, profile: LocalDistributionPackagingProfile) -> tuple[str, dict]:
    text = "Risk digest:\nLow risk."
    return text, {"status": "generated"}

def summarize_packaging_risks(risk_df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(risk_df)}
