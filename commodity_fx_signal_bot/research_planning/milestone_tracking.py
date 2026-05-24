import pandas as pd

def build_default_research_milestones() -> pd.DataFrame:
    milestones = [
        {"milestone_id": "data_quality_maturity", "title": "Data Quality Maturity", "description": "Clean and robust data pipeline."},
        {"milestone_id": "validation_maturity", "title": "Validation Maturity", "description": "Walk-forward testing and robustness."},
        {"milestone_id": "ml_research_maturity", "title": "ML Research Maturity", "description": "Machine learning models and datasets."},
        {"milestone_id": "factor_research_maturity", "title": "Factor Research Maturity", "description": "Factor stability and IC analysis."},
        {"milestone_id": "portfolio_research_maturity", "title": "Portfolio Research Maturity", "description": "Concentration and regime stress testing."},
        {"milestone_id": "meta_research_maturity", "title": "Meta Research Maturity", "description": "Consensus and conflict resolution."},
        {"milestone_id": "experiment_tracking_maturity", "title": "Experiment Tracking Maturity", "description": "Reproducibility and artifact tracking."},
        {"milestone_id": "governance_maturity", "title": "Governance Maturity", "description": "Lineage, audits, and fingerprinting."},
        {"milestone_id": "reporting_maturity", "title": "Reporting Maturity", "description": "Comprehensive and clear reports."},
        {"milestone_id": "documentation_maturity", "title": "Documentation Maturity", "description": "Up-to-date and complete docs."}
    ]
    return pd.DataFrame(milestones)

def map_tasks_to_milestones(backlog_df: pd.DataFrame, milestone_df: pd.DataFrame) -> pd.DataFrame:
    if backlog_df.empty or milestone_df.empty:
        return pd.DataFrame()

    mapping = []
    for _, task in backlog_df.iterrows():
        milestone_id = None
        task_type = task.get("task_type", "")

        if task_type == "data_quality_task":
            milestone_id = "data_quality_maturity"
        elif task_type == "validation_task":
            milestone_id = "validation_maturity"
        elif task_type == "ml_research_task":
            milestone_id = "ml_research_maturity"
        elif task_type == "factor_research_task":
            milestone_id = "factor_research_maturity"
        elif task_type == "portfolio_research_task" or task_type == "regime_research_task":
            milestone_id = "portfolio_research_maturity"
        elif task_type == "meta_research_task":
            milestone_id = "meta_research_maturity"
        elif task_type == "experiment_task":
            milestone_id = "experiment_tracking_maturity"
        elif task_type == "governance_task":
            milestone_id = "governance_maturity"
        elif task_type == "paper_research_task":
            milestone_id = "reporting_maturity"
        elif task_type == "documentation_task":
            milestone_id = "documentation_maturity"

        if milestone_id:
            mapping.append({
                "task_id": task.get("task_id"),
                "task_type": task_type,
                "milestone_id": milestone_id,
                "status": task.get("status")
            })

    return pd.DataFrame(mapping)

def calculate_milestone_progress(task_milestone_df: pd.DataFrame) -> pd.DataFrame:
    if task_milestone_df.empty:
        return pd.DataFrame()

    progress = []

    for ms_id, group in task_milestone_df.groupby("milestone_id"):
        total = len(group)
        completed = len(group[group["status"] == "task_completed"])

        progress.append({
            "milestone_id": ms_id,
            "total_tasks": total,
            "completed_tasks": completed,
            "progress_percent": (completed / total) * 100 if total > 0 else 0.0,
            "warnings": "Not a production milestone"
        })

    return pd.DataFrame(progress)

def summarize_milestone_tracking(progress_df: pd.DataFrame) -> dict:
    if progress_df.empty:
        return {"total_milestones": 0}

    return {
        "total_milestones": len(progress_df),
        "avg_progress": float(progress_df["progress_percent"].mean()) if "progress_percent" in progress_df.columns else 0.0
    }
