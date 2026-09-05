"""Reproducibility gaps."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def detect_missing_reproducibility_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_dossier_items(dossier_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_environment_replay_items(replay_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_deterministic_runbook_items(runbook_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_reproducibility_gap_register(
    domain_df: pd.DataFrame,
    dossier_df: pd.DataFrame,
    replay_df: pd.DataFrame,
    runbook_df: pd.DataFrame,
    profile: LocalReproducibilityGovernanceProfile,
) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"gap": "none"}])
    return df, summarize_reproducibility_gaps(df)

def summarize_reproducibility_gaps(gap_df: pd.DataFrame) -> dict:
    return {"gaps": len(gap_df), "note": "Auto-fix yoktur."}
