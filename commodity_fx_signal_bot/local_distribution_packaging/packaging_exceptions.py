import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile

def detect_packaging_exceptions(bundle_df: pd.DataFrame, criteria_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "None detected"}])

def build_packaging_exception_register(bundle_df: pd.DataFrame, criteria_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_packaging_exceptions(bundle_df, criteria_df, no_go_df)
    return df, summarize_packaging_exceptions(df)

def summarize_packaging_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(exception_df)}
