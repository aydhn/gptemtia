import pandas as pd
from local_simplification.simplification_config import LocalSimplificationProfile

def detect_simplification_exceptions(candidate_df: pd.DataFrame, plan_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "example"}])

def build_simplification_exception_register(candidate_df: pd.DataFrame, plan_df: pd.DataFrame, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_simplification_exceptions(candidate_df, plan_df)
    return df, summarize_simplification_exceptions(df)

def summarize_simplification_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"items": len(exception_df), "warnings": ["Exception official failure degildir."]}
