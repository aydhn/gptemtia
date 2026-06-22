import pandas as pd
from typing import Tuple, Dict, Any

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def build_periodic_review_calendar(task_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if task_df is None or task_df.empty:
        return pd.DataFrame(), {"total_items": 0}

    calendar_data = []
    for _, row in task_df.iterrows():
        calendar_data.append({
            "task_id": row["task_id"],
            "task_name": row["task_name"],
            "domain_label": row["domain_label"],
            "cadence": row["cadence"],
            "suggested_review_day": profile.default_monthly_review_day if "monthly" in row["cadence"] else "N/A"
        })

    df = pd.DataFrame(calendar_data)
    summary = summarize_review_calendar(df)
    return df, summary

def build_monthly_review_calendar(task_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> pd.DataFrame:
    if task_df is None or task_df.empty:
        return pd.DataFrame()

    monthly_tasks = task_df[task_df["cadence"].str.contains("monthly", na=False)].copy()
    if not monthly_tasks.empty:
        monthly_tasks["review_day"] = profile.default_monthly_review_day
    return monthly_tasks

def build_quarterly_review_calendar(task_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> pd.DataFrame:
    if task_df is None or task_df.empty:
        return pd.DataFrame()

    quarterly_tasks = task_df[task_df["cadence"].str.contains("quarterly", na=False)].copy()
    if not quarterly_tasks.empty:
        quarterly_tasks["review_month_interval"] = profile.default_quarterly_review_month_interval
    return quarterly_tasks

def summarize_review_calendar(calendar_df: pd.DataFrame) -> Dict[str, Any]:
    if calendar_df is None or calendar_df.empty:
        return {"total_items": 0}

    summary = {
        "total_items": len(calendar_df),
        "items_by_cadence": calendar_df["cadence"].value_counts().to_dict(),
        "disclaimer": "This calendar is not an automatic scheduler. It provides hints for manual operator review."
    }
    return summary
