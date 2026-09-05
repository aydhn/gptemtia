"""Reproducibility drift and variance."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_default_reproducibility_drift_items(profile: LocalReproducibilityGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"drift": "drift1"}])

def build_default_reproducibility_variance_items(profile: LocalReproducibilityGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"variance": "variance1"}])

def build_reproducibility_drift_register(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reproducibility_drift_items(profile)
    return df, summarize_reproducibility_drift_variance(df, pd.DataFrame())

def build_reproducibility_variance_register(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reproducibility_variance_items(profile)
    return df, summarize_reproducibility_drift_variance(pd.DataFrame(), df)

def summarize_reproducibility_drift_variance(drift_df: pd.DataFrame, variance_df: pd.DataFrame) -> dict:
    return {"drifts": len(drift_df), "variances": len(variance_df), "note": "Drift/variance yatirim riski degildir."}
