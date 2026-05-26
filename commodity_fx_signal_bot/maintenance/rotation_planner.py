"""Rotation Planner for offline maintenance."""
import pandas as pd
from typing import Tuple, Dict

from maintenance.maintenance_config import MaintenanceProfile
from maintenance.maintenance_models import build_maintenance_candidate_id

def _build_rotation_plan_generic(inventory_df: pd.DataFrame, category: str, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    if inventory_df.empty:
        return pd.DataFrame(), summarize_rotation_plans({})

    filtered = inventory_df[inventory_df["retention_category"] == category].copy()
    if filtered.empty:
        return pd.DataFrame(), summarize_rotation_plans({})

    # Sort by age (newest first)
    filtered = filtered.sort_values(by="age_days", ascending=True)

    # Very basic rotation logic: identify what exceeds rotation limits
    records = []

    # Since we don't group by report family here for simplicity, we just look at the category as a whole
    # For a real implementation, we'd need to extract family IDs from paths

    for i, (_, row) in enumerate(filtered.iterrows()):
        records.append({
            "artifact_id": row["artifact_id"],
            "path": row["path"],
            "age_days": row["age_days"],
            "action": "keep_action" if i < profile.keep_latest_n_reports else "rotate_dry_run_action"
        })

    df = pd.DataFrame(records)
    summary = {"total": len(df), "to_rotate": len(df[df["action"] == "rotate_dry_run_action"])}

    return df, summary


def build_report_rotation_plan(inventory_df: pd.DataFrame, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    return _build_rotation_plan_generic(inventory_df, "report_retention", profile)

def build_log_rotation_plan(inventory_df: pd.DataFrame, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    return _build_rotation_plan_generic(inventory_df, "log_retention", profile)

def build_cache_pruning_plan(inventory_df: pd.DataFrame, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    return _build_rotation_plan_generic(inventory_df, "cache_retention", profile)

def build_checkpoint_rotation_plan(inventory_df: pd.DataFrame, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    return _build_rotation_plan_generic(inventory_df, "checkpoint_retention", profile)

def summarize_rotation_plans(plans: Dict[str, pd.DataFrame]) -> Dict:
    return {k: len(v) for k, v in plans.items()}
