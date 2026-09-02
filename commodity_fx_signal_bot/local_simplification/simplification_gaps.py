import pandas as pd
from local_simplification.simplification_config import LocalSimplificationProfile

def detect_missing_simplification_domains(domain_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_complexity_metrics(complexity_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_candidates(candidate_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_slimming_plan_items(plan_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()

def build_simplification_gap_register(domain_df: pd.DataFrame, complexity_df: pd.DataFrame, candidate_df: pd.DataFrame, plan_df: pd.DataFrame, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"gap": "example"}])
    return df, summarize_simplification_gaps(df)

def summarize_simplification_gaps(gap_df: pd.DataFrame) -> dict:
    return {"items": len(gap_df), "warnings": ["Auto-fix yoktur."]}
