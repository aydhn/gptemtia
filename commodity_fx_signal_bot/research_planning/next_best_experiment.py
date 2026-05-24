import pandas as pd
from research_planning.planning_models import ResearchTask, NextBestExperiment, build_next_best_experiment_id
from research_planning.planning_config import ResearchPlanningProfile

def build_next_best_experiment_from_task(task: ResearchTask, profile: ResearchPlanningProfile) -> NextBestExperiment:
    exp_name = "unknown_experiment"
    hypothesis = f"Resolving {task.title} will improve research quality."

    if task.task_type == "meta_research_task":
        exp_name = "meta_conflict_resolution_experiment"
    elif task.task_type == "factor_research_task":
        exp_name = "factor_stability_ablation_experiment"
    elif task.task_type == "ml_research_task":
        exp_name = "ml_dataset_quality_experiment"
    elif task.task_type == "validation_task":
        exp_name = "validation_walk_forward_extension_experiment"
    elif task.task_type == "governance_task":
        exp_name = "governance_fingerprint_completion_experiment"
    elif task.task_type == "synthetic_index_task":
        exp_name = "synthetic_index_missing_output_experiment"
    elif task.task_type == "portfolio_research_task":
        exp_name = "portfolio_concentration_research_experiment"
    elif task.task_type == "regime_research_task":
        exp_name = "regime_stress_window_extension_experiment"
    elif task.task_type == "paper_research_task":
        exp_name = "paper_rejection_reason_experiment"
    elif task.task_type == "maintenance_task" or task.task_type == "data_quality_task":
        exp_name = "observability_stale_artifact_cleanup_experiment"

    return NextBestExperiment(
        recommendation_id=build_next_best_experiment_id(task.task_id, exp_name),
        task_id=task.task_id,
        experiment_name=exp_name,
        hypothesis=hypothesis,
        module_scope=task.related_modules,
        symbols=task.related_symbols,
        timeframe=profile.research_planning_default_timeframe, # Default timeframe from profile could be used if available
        expected_learning=task.expected_impact,
        priority_score=task.priority_score,
        confidence_score=0.7,
        blocking_factors=[],
        warnings=["Not an auto-run command"]
    )

def build_next_best_experiment_table(priority_df: pd.DataFrame, profile: ResearchPlanningProfile) -> tuple[pd.DataFrame, dict]:
    if priority_df.empty:
        return pd.DataFrame(), {"count": 0}

    experiments = []

    # Sort by priority
    sorted_df = priority_df.sort_values(by="priority_score", ascending=False)

    for _, row in sorted_df.head(profile.max_next_best_experiments).iterrows():
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

        exp = build_next_best_experiment_from_task(task, profile)
        experiments.append(exp)

    from research_planning.planning_models import next_best_experiment_to_dict

    df = pd.DataFrame([next_best_experiment_to_dict(e) for e in experiments])

    summary = summarize_next_best_experiments(df)
    summary["is_auto_run"] = False # Explicitly not auto-run

    return df, summary

def filter_executable_research_candidates(next_best_df: pd.DataFrame) -> pd.DataFrame:
    if next_best_df.empty:
        return next_best_df
    # For instance, filter those with high confidence
    return next_best_df[next_best_df["confidence_score"] >= 0.5]

def summarize_next_best_experiments(next_best_df: pd.DataFrame) -> dict:
    if next_best_df.empty:
        return {"total": 0}

    return {
        "total": len(next_best_df),
        "experiment_types": next_best_df["experiment_name"].value_counts().to_dict() if "experiment_name" in next_best_df.columns else {}
    }
