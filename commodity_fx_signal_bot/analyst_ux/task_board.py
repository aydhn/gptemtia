from pathlib import Path
import pandas as pd
from .ux_config import AnalystUXProfile
from .ux_models import AnalystTask, build_analyst_task_id

def _create_task(title: str, ttype: str, desc: str, aliases: list, commands: list, status: str, priority: str) -> AnalystTask:
    return AnalystTask(
        task_id=build_analyst_task_id(title, ttype),
        title=title,
        task_type=ttype,
        description=desc,
        suggested_aliases=aliases,
        suggested_commands=commands,
        status=status,
        priority=priority,
        warnings=["Bu task board gerçek trading task board değildir. Task’lar safe/offline olmalıdır."]
    )

def build_default_analyst_tasks(profile: AnalystUXProfile) -> list[AnalystTask]:
    if not profile.generate_task_board: return []
    return [
        _create_task("Final review status kontrol et", "review", "Check status of final review", ["status:final"], ["python -m scripts.run_final_review_status"], "open", "high"),
        _create_task("Safety audit raporunu incele", "audit", "Review safety audit", ["report:safety"], ["python -m scripts.run_safety_audit"], "open", "high"),
        _create_task("Quality gate validation çalıştır", "quality", "Run quality check", ["quality:check"], ["python -m scripts.run_static_safety_scan"], "open", "medium"),
        _create_task("Scenario regression failure register incele", "regression", "Check regressions", ["status:regression"], ["python -m scripts.run_scenario_regression_status"], "open", "medium"),
        _create_task("Documentation safety scan kontrol et", "docs", "Scan docs safety", ["docs:pack"], ["python -m scripts.run_documentation_pack_report"], "open", "low"),
        _create_task("Maintenance cleanup dry-run adaylarını gözden geçir", "maintenance", "Check maintenance dry run", ["maintenance:dry_run"], ["python -m scripts.run_cleanup_dry_run_report"], "open", "low"),
        _create_task("Performance bottleneck raporunu incele", "performance", "Review performance", ["report:performance"], ["python -m scripts.run_performance_profile_report"], "open", "low"),
        _create_task("Knowledge base index durumunu kontrol et", "knowledge", "Check KB index", ["query:knowledge"], ["python -m scripts.run_research_query"], "open", "low")
    ]

def build_tasks_from_quality_reports(project_root: Path, profile: AnalystUXProfile) -> list[AnalystTask]:
    # Placeholder for reading actual reports and creating tasks
    return []

def build_tasks_from_final_gaps(project_root: Path, profile: AnalystUXProfile) -> list[AnalystTask]:
    return []

def build_tasks_from_regression_failures(project_root: Path, profile: AnalystUXProfile) -> list[AnalystTask]:
    return []

def analyst_tasks_to_dataframe(tasks: list[AnalystTask]) -> pd.DataFrame:
    if not tasks: return pd.DataFrame()
    return pd.DataFrame([t.__dict__ for t in tasks])

def summarize_analyst_task_board(task_df: pd.DataFrame) -> dict:
    if task_df.empty: return {"count": 0}
    return {"count": len(task_df)}
