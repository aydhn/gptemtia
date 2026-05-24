import pandas as pd
from research_planning.planning_models import ResearchTask

def calculate_research_debt_score(backlog_df: pd.DataFrame) -> float:
    if backlog_df.empty:
        return 0.0

    # Simple debt calculation based on high priority tasks of certain types
    debt_score = 0.0
    for _, row in backlog_df.iterrows():
        if row.get("task_type") in ["governance_task", "data_quality_task", "maintenance_task", "validation_task"]:
            if row.get("priority_label") == "critical_research_priority":
                debt_score += 0.1
            elif row.get("priority_label") == "high_research_priority":
                debt_score += 0.05
            else:
                debt_score += 0.01

    return min(1.0, debt_score)

def classify_research_debt_level(score: float) -> str:
    if score >= 0.75:
        return "critical_research_debt"
    elif score >= 0.5:
        return "high_research_debt"
    elif score >= 0.25:
        return "moderate_research_debt"
    return "low_research_debt"

def build_research_debt_table(backlog_df: pd.DataFrame) -> pd.DataFrame:
    if backlog_df.empty:
        return pd.DataFrame()

    debt_rows = []

    # Filter only debt-related tasks
    debt_types = ["governance_task", "data_quality_task", "maintenance_task", "validation_task", "experiment_task"]

    if "task_type" in backlog_df.columns:
        debt_df = backlog_df[backlog_df["task_type"].isin(debt_types)].copy()

        for _, row in debt_df.iterrows():
            debt_rows.append({
                "task_id": row.get("task_id"),
                "debt_source": row.get("task_type"),
                "title": row.get("title"),
                "priority_score": row.get("priority_score"),
                "priority_label": row.get("priority_label"),
                "warnings": "Critical debt item" if row.get("priority_label") == "critical_research_priority" else ""
            })

    return pd.DataFrame(debt_rows)

def summarize_research_debt(debt_df: pd.DataFrame) -> dict:
    if debt_df.empty:
        return {"total_debt_items": 0}

    return {
        "total_debt_items": len(debt_df),
        "debt_sources": debt_df["debt_source"].value_counts().to_dict() if "debt_source" in debt_df.columns else {}
    }
