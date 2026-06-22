import pandas as pd
from typing import Tuple, Dict, Any, List
from pathlib import Path

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def detect_missing_maintenance_domains(task_df: pd.DataFrame) -> pd.DataFrame:
    gaps = []
    # If a domain has no tasks, we flag it as a gap.
    if task_df is not None and not task_df.empty:
        # A simple stub
        pass
    return pd.DataFrame(gaps)

def detect_missing_refresh_cadence(cadence_tables: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    gaps = []
    required_cadences = ["reports", "datalake", "documentation", "tests", "safety_security", "backup_packaging", "cross_layer"]

    for req in required_cadences:
        if req not in cadence_tables or cadence_tables[req] is None or cadence_tables[req].empty:
            gaps.append({
                "gap_type": "missing_cadence",
                "description": f"Missing refresh cadence for {req}.",
                "recommendation": "Review maintenance configuration to ensure this domain is scanned."
            })
    return pd.DataFrame(gaps)

def detect_missing_operator_review_items(task_df: pd.DataFrame) -> pd.DataFrame:
    gaps = []
    if task_df is not None and not task_df.empty:
        # Check if basic operator tasks are missing
        operator_tasks = task_df[task_df["domain_label"] == "operator_maintenance"]
        if operator_tasks.empty:
            gaps.append({
                "gap_type": "missing_operator_review_items",
                "description": "No tasks found for operator_maintenance.",
                "recommendation": "Add operator review tasks to the registry."
            })
    return pd.DataFrame(gaps)

def build_maintenance_gap_register(
    project_root: Path,
    task_df: pd.DataFrame,
    cadence_tables: Dict[str, pd.DataFrame],
    profile: LocalMaintenanceProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:

    df1 = detect_missing_maintenance_domains(task_df)
    df2 = detect_missing_refresh_cadence(cadence_tables)
    df3 = detect_missing_operator_review_items(task_df)

    dfs = [df for df in [df1, df2, df3] if not df.empty]
    df = pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

    summary = summarize_maintenance_gaps(df)
    return df, summary

def summarize_maintenance_gaps(gap_df: pd.DataFrame) -> Dict[str, Any]:
    if gap_df is None or gap_df.empty:
        return {"total_gaps": 0}

    return {
        "total_gaps": len(gap_df),
        "gaps_by_type": gap_df["gap_type"].value_counts().to_dict() if "gap_type" in gap_df else {},
        "disclaimer": "Maintenance gap is not a production incident. Recommendations are safe and manual."
    }
