import pandas as pd
from research_planning.planning_config import ResearchPlanningProfile

def build_offline_task_orchestration_plan(backlog_df: pd.DataFrame, dependency_df: pd.DataFrame, profile: ResearchPlanningProfile) -> pd.DataFrame:
    from research_planning.task_dependencies import build_task_execution_order

    order_df = build_task_execution_order(dependency_df, backlog_df)

    if order_df.empty:
        return pd.DataFrame()

    plan = []

    for seq, (idx, row) in enumerate(order_df.iterrows(), 1):
        plan.append({
            "sequence": seq,
            "batch_id": (seq - 1) // 10 + 1,
            "task_id": row.get("task_id", ""),
            "task_type": row.get("task_type", ""),
            "title": row.get("title", ""),
            "priority_score": row.get("priority_score", 0.0),
            "priority_label": row.get("priority_label", ""),
            "dependencies": row.get("dependencies", []),
            "suggested_command": f"python -m scripts.run_{row.get('task_type', 'unknown')}_script", # Stub command
            "dry_run_required": True,
            "warnings": ["Do not use for live trading or deploy"]
        })

    plan_df = pd.DataFrame(plan)
    return plan_df

def group_tasks_into_research_batches(plan_df: pd.DataFrame, max_batch_size: int = 10) -> pd.DataFrame:
    if plan_df.empty:
        return plan_df

    # batch_id is already assigned in build_offline_task_orchestration_plan
    # But we can re-assign here if needed
    plan_df["batch_id"] = (plan_df["sequence"] - 1) // max_batch_size + 1
    return plan_df

def build_task_command_suggestions(plan_df: pd.DataFrame) -> pd.DataFrame:
    # We already added suggested_command
    return plan_df

def summarize_task_orchestration_plan(plan_df: pd.DataFrame) -> dict:
    if plan_df.empty:
        return {"total_tasks": 0}

    return {
        "total_tasks": len(plan_df),
        "total_batches": int(plan_df["batch_id"].max()) if "batch_id" in plan_df.columns else 0,
        "is_execution_plan": False # Explicitly not a live plan
    }
