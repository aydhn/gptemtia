import pandas as pd
from research_planning.planning_models import ResearchTask

def infer_task_dependencies(task: ResearchTask, backlog_df: pd.DataFrame) -> list[str]:
    deps = []
    if backlog_df.empty:
        return deps

    # Logic to infer dependencies. For example, ML tasks depend on Data Quality tasks.
    if task.task_type == "ml_research_task":
        # Find any data quality tasks for the same symbol/module
        if "task_type" in backlog_df.columns:
            dq_tasks = backlog_df[backlog_df["task_type"] == "data_quality_task"]
            for _, row in dq_tasks.iterrows():
                # Oversimplified overlap check
                deps.append(row.get("task_id"))

    elif task.task_type == "factor_research_task":
        if "task_type" in backlog_df.columns:
            dq_tasks = backlog_df[backlog_df["task_type"] == "feature_quality_task"]
            for _, row in dq_tasks.iterrows():
                deps.append(row.get("task_id"))

    return list(set(deps))

def build_task_dependency_table(backlog_df: pd.DataFrame) -> pd.DataFrame:
    if backlog_df.empty:
        return pd.DataFrame()

    dep_rows = []

    for _, row in backlog_df.iterrows():
        task = ResearchTask(
            task_id=row.get("task_id", ""),
            task_type=row.get("task_type", ""),
            title=row.get("title", ""),
            description=row.get("description", ""),
            status=row.get("status", ""),
            priority_score=row.get("priority_score", 0.0),
            priority_label=row.get("priority_label", ""),
            recommendation_label=row.get("recommendation_label", ""),
            source_signal_ids=row.get("source_signal_ids", []),
            related_symbols=row.get("related_symbols", []),
            related_modules=row.get("related_modules", []),
            expected_impact=row.get("expected_impact", ""),
            estimated_effort=row.get("estimated_effort", ""),
            dependencies=row.get("dependencies", []),
            created_at_utc=row.get("created_at_utc", ""),
            warnings=row.get("warnings", [])
        )

        deps = infer_task_dependencies(task, backlog_df)

        dep_rows.append({
            "task_id": task.task_id,
            "task_type": task.task_type,
            "dependencies": deps,
            "dependency_count": len(deps)
        })

    return pd.DataFrame(dep_rows)

def detect_task_dependency_cycles(dependency_df: pd.DataFrame) -> dict:
    if dependency_df.empty:
        return {"has_cycles": False, "cycles": []}

    # A simple cycle detection could go here. For now, assuming no cycles.
    return {"has_cycles": False, "cycles": []}

def build_task_execution_order(dependency_df: pd.DataFrame, backlog_df: pd.DataFrame) -> pd.DataFrame:
    if dependency_df.empty or backlog_df.empty:
        return pd.DataFrame()

    # A simple topological sort could go here.
    # For now, just sort by priority, then dependency count.

    merged = pd.merge(backlog_df, dependency_df[["task_id", "dependency_count", "dependencies"]], on="task_id", how="left")

    if "priority_score" in merged.columns and "dependency_count" in merged.columns:
        # Sort so that items with fewer dependencies and higher priority come first
        merged = merged.sort_values(by=["dependency_count", "priority_score"], ascending=[True, False])

    return merged

def summarize_task_dependencies(dependency_df: pd.DataFrame) -> dict:
    if dependency_df.empty:
        return {"total_tasks": 0, "tasks_with_dependencies": 0}

    with_deps = len(dependency_df[dependency_df["dependency_count"] > 0]) if "dependency_count" in dependency_df.columns else 0

    return {
        "total_tasks": len(dependency_df),
        "tasks_with_dependencies": with_deps
    }
