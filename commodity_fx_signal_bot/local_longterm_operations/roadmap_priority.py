"""Roadmap priority."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_roadmap_priority_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([{"priority": "low", "warnings": ["Kesin öncelik değildir."]}])

def build_v1x_roadmap_priority_matrix(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_roadmap_priority_items(profile)
    return df, summarize_roadmap_priority(df)

def summarize_roadmap_priority(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
