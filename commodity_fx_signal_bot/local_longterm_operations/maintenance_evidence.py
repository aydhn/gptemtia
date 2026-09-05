"""Maintenance evidence."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_maintenance_evidence_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"evidence_id": "ev_01", "type": "report", "warnings": ["audit proof değildir", "manual_review_required bağlamında kalmalı"]}
    ])

def build_maintenance_evidence_checklist(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_maintenance_evidence_items(profile)
    return df, summarize_maintenance_evidence(df)

def summarize_maintenance_evidence(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
