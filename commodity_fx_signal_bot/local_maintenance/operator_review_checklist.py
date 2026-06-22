import pandas as pd
from typing import Tuple, Dict, Any

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def build_monthly_operator_review_checklist(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = [
        {"task": "status reports refresh", "type": "monthly"},
        {"task": "docs quick review", "type": "monthly"},
        {"task": "secrets hygiene status", "type": "monthly"},
        {"task": "backup recovery status", "type": "monthly"},
        {"task": "consistency status", "type": "monthly"},
        {"task": "readiness status", "type": "monthly"},
        {"task": "known gaps review", "type": "monthly"}
    ]
    df = pd.DataFrame(items)
    return df, {"total_items": len(df)}

def build_quarterly_operator_review_checklist(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = [
        {"task": "dependency review", "type": "quarterly"},
        {"task": "full report regeneration dry-run plan", "type": "quarterly"},
        {"task": "metadata/evidence/graph/timeline refresh", "type": "quarterly"},
        {"task": "manual test coverage review", "type": "quarterly"},
        {"task": "architecture/docs review", "type": "quarterly"},
        {"task": "sustainability binder refresh", "type": "quarterly"}
    ]
    df = pd.DataFrame(items)
    return df, {"total_items": len(df)}

def build_operator_periodic_review_checklist(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df_monthly, _ = build_monthly_operator_review_checklist(profile)
    df_quarterly, _ = build_quarterly_operator_review_checklist(profile)

    df = pd.concat([df_monthly, df_quarterly], ignore_index=True)
    summary = summarize_operator_periodic_review_checklist(df)
    return df, summary

def summarize_operator_periodic_review_checklist(checklist_df: pd.DataFrame) -> Dict[str, Any]:
    if checklist_df is None or checklist_df.empty:
        return {"total_tasks": 0}

    return {
        "total_tasks": len(checklist_df),
        "tasks_by_type": checklist_df["type"].value_counts().to_dict(),
        "disclaimer": "This checklist is not a scheduler. Commands are notes for manual execution. No live/broker/deploy actions included."
    }
