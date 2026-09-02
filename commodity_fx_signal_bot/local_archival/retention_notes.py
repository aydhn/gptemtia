"""
Retention Notes.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def build_default_retention_notes(profile: LocalArchivalProfile) -> pd.DataFrame:
    notes = [
        {"note_id": "r1", "policy": "local_dry_run_only", "description": "Retention is purely local.", "legal_claim": False}
    ]
    return pd.DataFrame(notes)

def build_retention_note_registry(profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_retention_notes(profile)
    return df, summarize_retention_notes(df)

def summarize_retention_notes(retention_df: pd.DataFrame) -> dict:
    return {"total_retention_notes": len(retention_df) if retention_df is not None else 0}
