"""Stale Artifact Detection for offline maintenance."""
import pandas as pd
from typing import Tuple, Dict

from maintenance.maintenance_config import MaintenanceProfile

def classify_staleness(age_days: float | None, retention_category: str, profile: MaintenanceProfile) -> str:
    if pd.isna(age_days):
        return "unknown_age"

    threshold = profile.stale_days_default

    if age_days > threshold * 3:
        return "very_stale"
    if age_days > threshold:
        return "stale"
    if age_days > threshold / 2:
        return "aging"
    return "fresh"

def detect_stale_artifacts(inventory_df: pd.DataFrame, profile: MaintenanceProfile) -> pd.DataFrame:
    if inventory_df.empty:
        return pd.DataFrame()

    df = inventory_df.copy()
    df["staleness_label"] = df.apply(lambda r: classify_staleness(r.get("age_days"), r.get("retention_category"), profile), axis=1)

    return df[df["staleness_label"].isin(["stale", "very_stale"])]

def build_stale_artifact_report(inventory_df: pd.DataFrame, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    stale_df = detect_stale_artifacts(inventory_df, profile)
    summary = summarize_stale_artifacts(stale_df)
    return stale_df, summary

def summarize_stale_artifacts(stale_df: pd.DataFrame) -> Dict:
    if stale_df.empty:
        return {"stale_count": 0}
    return {
        "stale_count": len(stale_df),
        "very_stale_count": len(stale_df[stale_df["staleness_label"] == "very_stale"]) if "staleness_label" in stale_df else 0
    }
