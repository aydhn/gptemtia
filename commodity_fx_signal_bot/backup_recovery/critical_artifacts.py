"""
Critical artifact registry.
"""

import pandas as pd

def build_critical_artifact_registry(inventory_df: pd.DataFrame) -> pd.DataFrame:
    if inventory_df is None or inventory_df.empty:
        return pd.DataFrame()
    return inventory_df[inventory_df["criticality"] == "critical_artifact"].copy()

def build_noncritical_artifact_registry(inventory_df: pd.DataFrame) -> pd.DataFrame:
    if inventory_df is None or inventory_df.empty:
        return pd.DataFrame()
    return inventory_df[inventory_df["criticality"] != "critical_artifact"].copy()

def build_excluded_secret_artifact_registry(inventory_df: pd.DataFrame) -> pd.DataFrame:
    if inventory_df is None or inventory_df.empty:
        return pd.DataFrame()
    # Content has been prevented from being read in inventory scanner
    return inventory_df[inventory_df["backup_scope"] == "excluded_secret_scope"][["artifact_id", "relative_path", "backup_scope"]].copy()

def rank_artifacts_by_restore_priority(inventory_df: pd.DataFrame) -> pd.DataFrame:
    if inventory_df is None or inventory_df.empty:
        return pd.DataFrame()
    return inventory_df.sort_values(by="restore_priority", ascending=True).copy()

def summarize_critical_artifacts(critical_df: pd.DataFrame, excluded_df: pd.DataFrame) -> dict:
    return {
        "critical_count": len(critical_df) if critical_df is not None else 0,
        "excluded_secrets": len(excluded_df) if excluded_df is not None else 0
    }
