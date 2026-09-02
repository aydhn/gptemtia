import pandas as pd
from .performance_config import LocalPerformanceProfile

def detect_missing_performance_domains(domain_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_budget_items(budget_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_resource_estimates(footprint_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_efficiency_candidates(efficiency_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()

def build_performance_gap_register(domain_df: pd.DataFrame, budget_df: pd.DataFrame, footprint_df: pd.DataFrame, efficiency_df: pd.DataFrame, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df1 = detect_missing_performance_domains(domain_df)
    df2 = detect_missing_budget_items(budget_df)
    df3 = detect_missing_resource_estimates(footprint_df)
    df4 = detect_missing_efficiency_candidates(efficiency_df)
    df = pd.concat([df1, df2, df3, df4], ignore_index=True) if not all(x.empty for x in [df1, df2, df3, df4]) else pd.DataFrame([{"gap": "None", "warning": "auto-fix yoktur"}])
    return df, summarize_performance_gaps(df)

def summarize_performance_gaps(gap_df: pd.DataFrame) -> dict: return {"total": len(gap_df) if gap_df is not None else 0}
