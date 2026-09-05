"""Reproducibility manual review."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_default_reproducibility_manual_review_items(profile: LocalReproducibilityGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"review": "review1"}])

def build_reproducibility_manual_review_ledger(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reproducibility_manual_review_items(profile)
    return df, summarize_reproducibility_manual_review(df)

def summarize_reproducibility_manual_review(df: pd.DataFrame) -> dict:
    return {"items": len(df), "note": "Manual review ledger approval degildir."}
