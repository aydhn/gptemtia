import pandas as pd
from research_planning.planning_models import ResearchTask, ResearchSignal
from research_planning.planning_config import ResearchPlanningProfile

def calculate_task_priority_score(task: ResearchTask, signal_map: dict[str, ResearchSignal] | None = None) -> float:
    # A simple scoring mechanism
    score = 0.0
    if signal_map and task.source_signal_ids:
        for sig_id in task.source_signal_ids:
            if sig_id in signal_map:
                sig = signal_map[sig_id]
                score += sig.severity_score * 0.4
                score += sig.opportunity_score * 0.4
                score += sig.uncertainty_score * 0.2
                if sig.quality_score is not None:
                    score += (1.0 - sig.quality_score) * 0.2

        # Source count bonus
        score += min(0.2, len(task.source_signal_ids) * 0.05)
    else:
        # Default fallback
        score = 0.5

    return min(1.0, max(0.0, score))

def infer_priority_label(priority_score: float, profile: ResearchPlanningProfile) -> str:
    if priority_score >= profile.high_priority_threshold:
        return "critical_research_priority" if priority_score > 0.85 else "high_research_priority"
    elif priority_score >= profile.min_priority_score:
        return "medium_research_priority"
    elif priority_score > 0.1:
        return "low_research_priority"
    else:
        return "deferred_research_priority"

def estimate_task_effort(task: ResearchTask) -> str:
    # Dummy logic
    if len(task.source_signal_ids) > 3:
        return "high_effort"
    elif task.task_type in ["ml_research_task", "validation_task"]:
        return "high_effort"
    return "medium_effort"

def estimate_task_expected_impact(task: ResearchTask) -> str:
    if task.task_type in ["experiment_task", "ml_research_task", "factor_research_task"]:
        return "high_expected_learning"
    return "medium_expected_learning"

def score_backlog_priorities(backlog_df: pd.DataFrame, signals: list[ResearchSignal], profile: ResearchPlanningProfile) -> tuple[pd.DataFrame, dict]:
    if backlog_df.empty:
        return backlog_df, {"scored_count": 0}

    signal_map = {s.signal_id: s for s in signals}

    scored_tasks = []

    for _, row in backlog_df.iterrows():
        # Reconstruct task object for calculation
        task = ResearchTask(
            task_id=row.get("task_id", ""),
            task_type=row.get("task_type", ""),
            title=row.get("title", ""),
            description=row.get("description", ""),
            status=row.get("status", ""),
            priority_score=0.0,
            priority_label="",
            recommendation_label="",
            source_signal_ids=row.get("source_signal_ids", []),
            related_symbols=row.get("related_symbols", []),
            related_modules=row.get("related_modules", []),
            expected_impact="",
            estimated_effort="",
            dependencies=row.get("dependencies", []),
            created_at_utc=row.get("created_at_utc", ""),
            warnings=row.get("warnings", [])
        )

        score = calculate_task_priority_score(task, signal_map)
        row["priority_score"] = score
        row["priority_label"] = infer_priority_label(score, profile)
        row["estimated_effort"] = estimate_task_effort(task)
        row["expected_impact"] = estimate_task_expected_impact(task)

        scored_tasks.append(row)

    scored_df = pd.DataFrame(scored_tasks)

    summary = summarize_priority_scores(scored_df)
    summary["is_live_priority"] = False # Explicitly state

    return scored_df, summary

def summarize_priority_scores(priority_df: pd.DataFrame) -> dict:
    if priority_df.empty:
        return {}

    counts = priority_df["priority_label"].value_counts().to_dict() if "priority_label" in priority_df.columns else {}
    avg_score = float(priority_df["priority_score"].mean()) if "priority_score" in priority_df.columns else 0.0

    return {
        "label_counts": counts,
        "average_score": avg_score
    }
