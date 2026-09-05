import pandas as pd
from .continuation_config import AdvancedContinuationProfile

def build_advanced_no_go_conditions(profile: AdvancedContinuationProfile) -> pd.DataFrame:
    conditions = ["canlı emir", "broker execution", "kesin AL/SAT", "yatırım tavsiyesi", "model deployment",
                  "production deployment", "scraping", "external LLM dependency", "vector DB dependency",
                  "archive/ZIP generation", "cloud publish", "official approval wording"]
    return pd.DataFrame([{"condition": c, "type": "no_go"} for c in conditions])

def build_advanced_safe_go_conditions(profile: AdvancedContinuationProfile) -> pd.DataFrame:
    conditions = ["local/offline research", "dry-run reports", "no scraping provider interfaces",
                  "ML research only", "backtest research only", "portfolio simulation only", "manual review required"]
    return pd.DataFrame([{"condition": c, "type": "safe_go"} for c in conditions])

def build_advanced_no_go_safe_go_boundary(profile: AdvancedContinuationProfile) -> tuple[pd.DataFrame, dict]:
    df1 = build_advanced_no_go_conditions(profile)
    df2 = build_advanced_safe_go_conditions(profile)
    df = pd.concat([df1, df2], ignore_index=True)
    return df, summarize_advanced_no_go_safe_go(df)

def summarize_advanced_no_go_safe_go(df: pd.DataFrame) -> dict:
    return {"total_conditions": len(df), "status": "continuation_ready"}
