import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile
from report_summarization.summary_models import FollowUpTask, build_follow_up_task_id

def build_follow_up_tasks_from_findings(findings_df: pd.DataFrame, warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame, profile: ReportSummaryProfile) -> list[FollowUpTask]:
    tasks = []

    if not findings_df.empty:
        for idx, row in findings_df.head(profile.max_follow_up_tasks).iterrows():
            tasks.append(map_finding_to_safe_follow_up(row))

    return tasks

def map_finding_to_safe_follow_up(finding: pd.Series) -> FollowUpTask:
    finding_type = finding.get("finding_type", "unknown_finding")
    module = finding.get("module_name", None)

    follow_up_type = "review_report_follow_up"
    if finding_type == "quality_finding":
        follow_up_type = "check_quality_gate_follow_up"
    elif finding_type == "documentation_finding":
        follow_up_type = "update_documentation_follow_up"

    cmd = suggest_safe_command_for_follow_up(follow_up_type, module)

    return FollowUpTask(
        task_id=build_follow_up_task_id("Follow-up based on finding", follow_up_type),
        follow_up_type=follow_up_type,
        title=f"Review finding in {module}",
        description=f"Action needed: {finding.get('text', 'No description')}",
        priority=finding.get("priority", "low_priority"),
        suggested_safe_command=cmd,
        related_module=module,
        related_symbol=None,
        source_paths=[finding.get("source_path", "unknown")],
        warnings=[]
    )

def suggest_safe_command_for_follow_up(follow_up_type: str, module_name: str | None = None) -> str | None:
    if follow_up_type == "check_quality_gate_follow_up":
        return "python -m scripts.run_local_ci_validation"
    if follow_up_type == "update_documentation_follow_up":
        return "python -m scripts.run_documentation_quality_report"
    if follow_up_type == "investigate_regression_follow_up":
        return "python -m scripts.run_scenario_regression_status"

    return "python -m scripts.run_final_system_review"

def follow_up_tasks_to_dataframe(tasks: list[FollowUpTask]) -> pd.DataFrame:
    if not tasks:
        return pd.DataFrame(columns=[
            "task_id", "follow_up_type", "title", "description", "priority",
            "suggested_safe_command", "related_module", "related_symbol",
            "source_paths", "warnings"
        ])
    return pd.DataFrame([t.__dict__ for t in tasks])

def summarize_follow_up_tasks(tasks_df: pd.DataFrame) -> dict:
    if tasks_df.empty:
        return {"total_tasks": 0}
    return {
        "total_tasks": len(tasks_df),
        "by_type": tasks_df["follow_up_type"].value_counts().to_dict() if "follow_up_type" in tasks_df else {}
    }
