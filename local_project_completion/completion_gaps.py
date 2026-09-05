import pandas as pd
from .completion_config import LocalProjectCompletionProfile

def detect_missing_completion_domains(domain_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_inventory_items(inventory_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_completion_criteria(criteria_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_handoff_items(handoff_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()

def build_completion_gap_register(domain_df: pd.DataFrame, inventory_df: pd.DataFrame, criteria_df: pd.DataFrame, handoff_df: pd.DataFrame, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"gap": "mock_gap"}])
    return df, summarize_completion_gaps(df)

def summarize_completion_gaps(gap_df: pd.DataFrame) -> dict:
    return {"gaps": len(gap_df), "note": "No auto-fix."}
