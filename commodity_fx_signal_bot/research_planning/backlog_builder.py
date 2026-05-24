import pandas as pd
from datetime import datetime, timezone
from research_planning.planning_models import ResearchSignal, ResearchTask, build_research_task_id
from research_planning.planning_config import ResearchPlanningProfile

def map_signal_to_task(signal: ResearchSignal, profile: ResearchPlanningProfile) -> ResearchTask:
    task_type = "unknown_research_task"
    if signal.source_module == "governance":
        task_type = "governance_task"
    elif signal.source_module == "experiment":
        task_type = "experiment_task"
    elif signal.source_module == "meta_research":
        task_type = "meta_research_task"
    elif signal.source_module == "factor_research":
        task_type = "factor_research_task"
    elif signal.source_module == "portfolio_research":
        task_type = "portfolio_research_task"
    elif signal.source_module == "regime_research":
        task_type = "regime_research_task"
    elif signal.source_module == "validation":
        task_type = "validation_task"
    elif signal.source_module == "ml":
        task_type = "ml_research_task"
    elif signal.source_module == "paper":
        task_type = "paper_research_task"
    elif signal.source_module == "observability":
        task_type = "maintenance_task"

    return ResearchTask(
        task_id=build_research_task_id(task_type, f"Resolve {signal.title}", [signal.symbol] if signal.symbol else []),
        task_type=task_type,
        title=f"Investigate: {signal.title}",
        description=f"Derived from signal {signal.signal_id}. {signal.description}",
        status="task_planned",
        priority_score=0.0, # Handled by PriorityScoring later
        priority_label="unknown_research_priority",
        recommendation_label="unknown_recommendation",
        source_signal_ids=[signal.signal_id],
        related_symbols=[signal.symbol] if signal.symbol else [],
        related_modules=[signal.source_module],
        expected_impact="unknown_expected_learning",
        estimated_effort="unknown_effort",
        dependencies=[],
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        warnings=signal.warnings.copy()
    )

def build_backlog_from_signals(signals: list[ResearchSignal], profile: ResearchPlanningProfile) -> tuple[pd.DataFrame, dict]:
    tasks = [map_signal_to_task(s, profile) for s in signals]

    from research_planning.task_registry import deduplicate_tasks, tasks_to_dataframe
    tasks = deduplicate_tasks(tasks)

    df = tasks_to_dataframe(tasks)

    summary = {
        "total_tasks_created": len(tasks),
        "is_execution_list": False # Explicitly stating it's not an execution list
    }
    return df, summary

def merge_existing_backlog(existing_df: pd.DataFrame | None, new_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    if existing_df is None or existing_df.empty:
        return new_df, {"merged": False}

    if new_df.empty:
        return existing_df, {"merged": False}

    merged = pd.concat([existing_df, new_df]).drop_duplicates(subset=["task_id"], keep="last")
    return merged, {"merged": True, "final_count": len(merged)}

def filter_backlog_by_priority(backlog_df: pd.DataFrame, min_priority_score: float) -> pd.DataFrame:
    if backlog_df.empty or "priority_score" not in backlog_df.columns:
        return backlog_df
    return backlog_df[backlog_df["priority_score"] >= min_priority_score]

def summarize_backlog(backlog_df: pd.DataFrame) -> dict:
    if backlog_df.empty:
        return {"total_tasks": 0}

    return {
        "total_tasks": len(backlog_df),
        "task_types": backlog_df["task_type"].value_counts().to_dict() if "task_type" in backlog_df.columns else {}
    }
