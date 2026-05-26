"""Large Artifact Review for offline maintenance."""
import pandas as pd
from typing import Tuple, Dict

from maintenance.maintenance_config import MaintenanceProfile

def identify_large_artifacts(inventory_df: pd.DataFrame, threshold_mb: int) -> pd.DataFrame:
    if inventory_df.empty:
        return pd.DataFrame()

    threshold_bytes = threshold_mb * 1024 * 1024

    large_df = inventory_df[inventory_df["size_bytes"] > threshold_bytes].copy()
    return large_df

def classify_large_artifact_action(row: pd.Series, profile: MaintenanceProfile) -> str:
    if row.get("protected"):
        return "review_required_action"

    if row.get("lifecycle_label") in ["archive_candidate", "cleanup_candidate"]:
        return row.get("lifecycle_label").replace("candidate", "dry_run_action")

    return "review_required_action"

def build_large_artifact_review_report(inventory_df: pd.DataFrame, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    large_df = identify_large_artifacts(inventory_df, profile.large_file_threshold_mb)
    if not large_df.empty:
        large_df["recommended_action"] = large_df.apply(lambda r: classify_large_artifact_action(r, profile), axis=1)

    summary = summarize_large_artifacts(large_df)
    return large_df, summary

def summarize_large_artifacts(large_df: pd.DataFrame) -> Dict:
    if large_df.empty:
        return {"large_count": 0}
    return {
        "large_count": len(large_df),
        "total_large_bytes": large_df["size_bytes"].sum()
    }
