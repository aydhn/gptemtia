"""Storage Lifecycle Health for offline maintenance."""
import pandas as pd
from typing import Tuple, Dict

from maintenance.maintenance_config import MaintenanceProfile

def calculate_storage_pressure_score(inventory_df: pd.DataFrame, profile: MaintenanceProfile) -> float:
    if inventory_df.empty:
        return 0.0

    score = 0.0

    total_bytes = inventory_df["size_bytes"].sum()
    if total_bytes > 1 * 1024 * 1024 * 1024: # 1 GB
        score += 0.2
    if total_bytes > 5 * 1024 * 1024 * 1024: # 5 GB
        score += 0.3

    if "lifecycle_label" in inventory_df:
        cleanup_candidates = inventory_df[inventory_df["lifecycle_label"] == "cleanup_candidate"]
        if not cleanup_candidates.empty:
            cleanup_bytes = cleanup_candidates["size_bytes"].sum()
            if cleanup_bytes > total_bytes * 0.3:
                score += 0.2
            if cleanup_bytes > total_bytes * 0.5:
                score += 0.3

    return min(1.0, score)

def infer_storage_health_label(score: float) -> str:
    if score < 0.3:
        return "healthy_storage"
    if score < 0.6:
        return "moderate_storage_pressure"
    if score < 0.9:
        return "high_storage_pressure"
    return "critical_storage_pressure"

def build_storage_lifecycle_health_report(inventory_df: pd.DataFrame, cleanup_df: pd.DataFrame | None, archive_df: pd.DataFrame | None, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    score = calculate_storage_pressure_score(inventory_df, profile)
    label = infer_storage_health_label(score)

    records = [{
        "metric": "storage_pressure_score",
        "value": score,
        "label": label,
        "description": "Calculated based on size, cleanup candidates, and age."
    }]

    df = pd.DataFrame(records)
    summary = summarize_lifecycle_health(df)
    return df, summary

def summarize_lifecycle_health(health_df: pd.DataFrame) -> Dict:
    if health_df.empty:
        return {"score": 0.0, "label": "unknown_storage_health"}

    row = health_df[health_df["metric"] == "storage_pressure_score"].iloc[0]
    return {
        "score": row["value"],
        "label": row["label"]
    }
