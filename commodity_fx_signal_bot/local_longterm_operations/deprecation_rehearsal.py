"""Deprecation rehearsal."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_deprecation_rehearsal_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"action": "rehearsal", "warnings": ["otomatik deprecation yapmaz"]}])
    return df, summarize_deprecation_rehearsal(df)

def build_deprecation_decision_checklist(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"step": "check", "warnings": ["otomatik deprecation yapmaz"]}])
    return df, summarize_deprecation_rehearsal(df)

def summarize_deprecation_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
