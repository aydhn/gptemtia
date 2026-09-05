"""Maintenance cadence."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_maintenance_cadence_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"cadence": "yearly", "action": "full_review", "warnings": ["scheduler oluşturmaz"]},
        {"cadence": "monthly", "action": "quick_check", "warnings": ["scheduler oluşturmaz"]}
    ])

def build_maintenance_cadence_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_maintenance_cadence_items(profile)
    return df, summarize_maintenance_cadence(df)

def summarize_maintenance_cadence(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
