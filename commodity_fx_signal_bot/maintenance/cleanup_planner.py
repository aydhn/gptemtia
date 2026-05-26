"""Cleanup Planner for offline maintenance."""
import pandas as pd
from typing import Tuple, Dict

from maintenance.maintenance_config import MaintenanceProfile
from maintenance.maintenance_models import build_maintenance_candidate_id

def identify_cleanup_candidates(inventory_df: pd.DataFrame, policies_df: pd.DataFrame, profile: MaintenanceProfile) -> pd.DataFrame:
    if inventory_df.empty:
        return pd.DataFrame()

    candidates = inventory_df[
        (inventory_df["lifecycle_label"] == "cleanup_candidate") &
        (~inventory_df["protected"])
    ].copy()

    if candidates.empty:
        return pd.DataFrame()

    cand_records = []
    for _, row in candidates.iterrows():
        cand_records.append({
            "candidate_id": build_maintenance_candidate_id(row["artifact_id"], "cleanup_dry_run_action"),
            "artifact_id": row["artifact_id"],
            "path": row["path"],
            "action_label": "cleanup_dry_run_action",
            "reason": "Lifecycle policy designated as cleanup candidate",
            "size_bytes": row["size_bytes"],
            "age_days": row["age_days"],
            "policy_id": None,
            "dry_run": True,
            "protected": False,
            "warnings": []
        })

    return pd.DataFrame(cand_records)

def build_cleanup_dry_run_plan(candidates_df: pd.DataFrame, profile: MaintenanceProfile) -> Tuple[pd.DataFrame, Dict]:
    summary = summarize_cleanup_plan(candidates_df)
    return candidates_df, summary

def estimate_reclaimable_storage(candidates_df: pd.DataFrame) -> Dict:
    if candidates_df.empty:
        return {"reclaimable_bytes": 0}
    return {"reclaimable_bytes": candidates_df["size_bytes"].sum()}

def classify_cleanup_risk(row: pd.Series) -> str:
    if row.get("protected"):
        return "blocked_cleanup_risk"

    age = row.get("age_days")
    if pd.isna(age):
        return "unknown_cleanup_risk"

    if age > 365:
        return "low_cleanup_risk"
    if age > 90:
        return "medium_cleanup_risk"
    return "high_cleanup_risk"

def summarize_cleanup_plan(plan_df: pd.DataFrame) -> Dict:
    if plan_df.empty:
        return {"candidate_count": 0, "reclaimable_bytes": 0}
    return {
        "candidate_count": len(plan_df),
        "reclaimable_bytes": plan_df["size_bytes"].sum()
    }
