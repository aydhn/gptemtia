"""
Report generation timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_report_family(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    families = [
        "research_reports", "report_summarization", "master_orchestration",
        "portable_packaging", "backup_recovery", "secrets_hygiene",
        "evidence_governance", "artifact_metadata", "local_knowledge_graph",
        "local_timeline", "quality_gates", "final_review",
        "scenario_regression", "documentation"
    ]
    for fam in families:
        if fam in rel:
            return fam
    return "unknown_report_family"

def infer_report_generation_module(path: Path, project_root: Path) -> str | None:
    return classify_report_family(path, project_root)

def build_report_generation_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def summarize_report_generation_timeline(report_df: pd.DataFrame) -> dict:
    if report_df.empty:
        return {"total_report_events": 0}
    return {
        "total_report_events": len(report_df),
        "unique_reports": report_df['relative_path'].nunique() if 'relative_path' in report_df else 0
    }
