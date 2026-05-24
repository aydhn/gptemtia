# Research task type labels
RESEARCH_TASK_TYPE_LABELS = [
    "data_quality_task",
    "feature_quality_task",
    "validation_task",
    "ml_research_task",
    "paper_research_task",
    "factor_research_task",
    "synthetic_index_task",
    "portfolio_research_task",
    "regime_research_task",
    "meta_research_task",
    "experiment_task",
    "governance_task",
    "observability_task",
    "documentation_task",
    "maintenance_task",
    "unknown_research_task"
]

# Research priority labels
RESEARCH_PRIORITY_LABELS = [
    "critical_research_priority",
    "high_research_priority",
    "medium_research_priority",
    "low_research_priority",
    "deferred_research_priority",
    "unknown_research_priority"
]

# Task status labels
TASK_STATUS_LABELS = [
    "task_planned",
    "task_ready",
    "task_blocked",
    "task_in_progress",
    "task_completed",
    "task_rejected",
    "task_deferred",
    "task_unknown"
]

# Planning recommendation labels
PLANNING_RECOMMENDATION_LABELS = [
    "next_best_experiment",
    "next_best_cleanup",
    "next_best_validation",
    "next_best_data_quality",
    "next_best_documentation",
    "next_best_governance",
    "no_action_recommended",
    "unknown_recommendation"
]

def list_research_task_type_labels() -> list[str]:
    return RESEARCH_TASK_TYPE_LABELS.copy()

def list_research_priority_labels() -> list[str]:
    return RESEARCH_PRIORITY_LABELS.copy()

def list_task_status_labels() -> list[str]:
    return TASK_STATUS_LABELS.copy()

def list_planning_recommendation_labels() -> list[str]:
    return PLANNING_RECOMMENDATION_LABELS.copy()

def validate_research_task_type(label: str) -> None:
    if label not in RESEARCH_TASK_TYPE_LABELS:
        raise ValueError(f"Invalid research task type: {label}")

def validate_research_priority(label: str) -> None:
    if label not in RESEARCH_PRIORITY_LABELS:
        raise ValueError(f"Invalid research priority: {label}")

def validate_task_status(label: str) -> None:
    if label not in TASK_STATUS_LABELS:
        raise ValueError(f"Invalid task status: {label}")

def validate_planning_recommendation(label: str) -> None:
    if label not in PLANNING_RECOMMENDATION_LABELS:
        raise ValueError(f"Invalid planning recommendation: {label}")
