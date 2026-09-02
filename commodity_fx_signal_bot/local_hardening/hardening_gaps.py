
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def detect_missing_contract_surfaces(contract_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_freeze_docs(doc_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def detect_missing_health_reports(health_df: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame()
def summarize_hardening_gaps(gap_df: pd.DataFrame) -> dict: return {"total": len(gap_df)}
def build_final_hardening_gap_register(
    dead_code_df: pd.DataFrame,
    contract_df: pd.DataFrame,
    doc_df: pd.DataFrame,
    health_df: pd.DataFrame,
    profile: LocalHardeningProfile,
) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_hardening_gaps(df)
