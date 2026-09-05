"""Reproducibility exceptions."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def detect_reproducibility_exceptions(dossier_df: pd.DataFrame, runbook_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "none"}])

def build_reproducibility_exception_register(dossier_df: pd.DataFrame, runbook_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_reproducibility_exceptions(dossier_df, runbook_df, no_go_df)
    return df, summarize_reproducibility_exceptions(df)

def summarize_reproducibility_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"exceptions": len(exception_df), "note": "Exception register auto-fix yapmaz."}
