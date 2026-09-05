import pandas as pd
from .continuation_config import AdvancedContinuationProfile

def build_default_development_risks(profile: AdvancedContinuationProfile) -> pd.DataFrame:
    risks = ["scope creep", "overfitting", "data leakage", "poor provider quality", "missing macro calendar source",
             "news data licensing ambiguity", "GPU environment mismatch", "unrealistic backtest",
             "transaction cost underestimation", "portfolio concentration", "false confidence in ML",
             "accidental investment advice language", "accidental broker/live wording", "accidental scraping implementation"]
    return pd.DataFrame([{"risk": r, "severity": "High", "mitigation": "Review"} for r in risks])

def build_advanced_development_risk_register(profile: AdvancedContinuationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_development_risks(profile)
    return df, summarize_development_risks(df)

def summarize_development_risks(df: pd.DataFrame) -> dict:
    return {"total_risks": len(df), "status": "continuation_ready"}
