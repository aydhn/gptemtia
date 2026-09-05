"""Deprecation boundaries."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_non_deprecation_boundaries(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"boundary": "no automatic file deletion", "warnings": ["Dosya silme yok."]},
        {"boundary": "no automatic module removal", "warnings": ["Dosya silme yok."]},
        {"boundary": "no API breakage without manual review", "warnings": ["Dosya silme yok."]},
        {"boundary": "no live/broker/deploy/advice feature enablement", "warnings": ["Dosya silme yok."]},
        {"boundary": "no official deprecation claim", "warnings": ["Dosya silme yok."]},
        {"boundary": "no production migration", "warnings": ["Dosya silme yok."]}
    ])

def build_non_deprecation_boundary_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_non_deprecation_boundaries(profile)
    return df, summarize_non_deprecation_boundaries(df)

def summarize_non_deprecation_boundaries(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
