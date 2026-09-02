import pandas as pd
from .performance_config import LocalPerformanceProfile

def detect_performance_exceptions(budget_df: pd.DataFrame, footprint_df: pd.DataFrame, warning_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "example_exception", "type": "info", "warning": "official failure degildir."}])

def build_performance_exception_register(budget_df: pd.DataFrame, footprint_df: pd.DataFrame, warning_df: pd.DataFrame, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_performance_exceptions(budget_df, footprint_df, warning_df)
    return df, summarize_performance_exceptions(df)

def summarize_performance_exceptions(exception_df: pd.DataFrame) -> dict: return {"total": len(exception_df) if exception_df is not None else 0}
