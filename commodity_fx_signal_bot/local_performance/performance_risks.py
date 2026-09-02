import pandas as pd
from .performance_config import LocalPerformanceProfile

def classify_performance_risk(row: pd.Series, profile: LocalPerformanceProfile) -> str:
    return "performance_low_risk"

def build_performance_risk_digest(risk_df: pd.DataFrame, profile: LocalPerformanceProfile) -> tuple[str, dict]:
    return "No major risks.", {"total": 0}

def build_performance_risk_summary(gap_df: pd.DataFrame, exception_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "example", "level": "performance_low_risk", "warning": "yatirim riski degildir"}])
    return df, summarize_performance_risks(df)

def summarize_performance_risks(risk_df: pd.DataFrame) -> dict: return {"total": len(risk_df) if risk_df is not None else 0}
