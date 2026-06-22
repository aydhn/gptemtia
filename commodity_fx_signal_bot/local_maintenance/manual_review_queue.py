import pandas as pd
from typing import Tuple, Dict, Any, Optional

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def build_manual_review_queue(
    dependency_df: Optional[pd.DataFrame],
    stale_report_df: Optional[pd.DataFrame],
    stale_doc_df: Optional[pd.DataFrame],
    stale_test_df: Optional[pd.DataFrame],
    gap_df: Optional[pd.DataFrame],
    profile: LocalMaintenanceProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:

    queue_items = []

    if dependency_df is not None and not dependency_df.empty and "status" in dependency_df:
        for _, row in dependency_df[dependency_df["status"] != "dependency_current"].iterrows():
            queue_items.append({
                "source": "dependency_aging",
                "item_name": row.get("dependency_name", "unknown"),
                "reason": row.get("review_reason", "Needs review"),
                "base_priority": 3
            })

    if stale_report_df is not None and not stale_report_df.empty and "status" in stale_report_df:
        for _, row in stale_report_df[stale_report_df["status"] == "stale_report"].iterrows():
            queue_items.append({
                "source": "stale_reports",
                "item_name": row.get("file_path", "unknown"),
                "reason": "Report is stale based on mtime.",
                "base_priority": 1
            })

    if stale_doc_df is not None and not stale_doc_df.empty and "status" in stale_doc_df:
        for _, row in stale_doc_df[stale_doc_df["status"] == "stale_doc"].iterrows():
            queue_items.append({
                "source": "stale_docs",
                "item_name": row.get("file_path", "unknown"),
                "reason": "Documentation is stale.",
                "base_priority": 2
            })

    if stale_test_df is not None and not stale_test_df.empty and "status" in stale_test_df:
        for _, row in stale_test_df[stale_test_df["status"] == "stale_test"].iterrows():
            queue_items.append({
                "source": "stale_tests",
                "item_name": row.get("file_path", "unknown"),
                "reason": "Test file is stale.",
                "base_priority": 2
            })

    if gap_df is not None and not gap_df.empty:
        for _, row in gap_df.iterrows():
            queue_items.append({
                "source": "maintenance_gaps",
                "item_name": row.get("gap_type", "unknown_gap"),
                "reason": row.get("description", "Gap detected."),
                "base_priority": 4
            })

    df = pd.DataFrame(queue_items)
    if not df.empty:
        df = prioritize_maintenance_review_queue(df)

    summary = summarize_manual_review_queue(df)
    return df, summary

def prioritize_maintenance_review_queue(queue_df: pd.DataFrame) -> pd.DataFrame:
    # Sort by base_priority descending
    return queue_df.sort_values(by="base_priority", ascending=False).reset_index(drop=True)

def summarize_manual_review_queue(queue_df: pd.DataFrame) -> Dict[str, Any]:
    if queue_df is None or queue_df.empty:
        return {"total_items_in_queue": 0}

    return {
        "total_items_in_queue": len(queue_df),
        "items_by_source": queue_df["source"].value_counts().to_dict(),
        "disclaimer": "Queue does not perform automatic actions. Priority indicates project maintenance priority, not investment priority."
    }
