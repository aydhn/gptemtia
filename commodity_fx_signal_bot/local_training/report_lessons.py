import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile
from .training_models import TrainingLesson, build_training_lesson_id

def build_report_reading_lesson(report_family: str, profile: LocalTrainingProfile) -> TrainingLesson:
    return TrainingLesson(
        lesson_id=build_training_lesson_id("report_training", report_family),
        lesson_name=f"Read {report_family}",
        domain_label="report_training",
        role_label="operator_role",
        objective="Learn to read report",
        steps=["Locate", "Read"],
        safe_commands=[],
        expected_outputs=["Understanding"],
        status="lesson_ready",
        warnings=["Report lesson sonuçların doğruluğunu garanti etmez.", "Yatırım tavsiyesi üretmez."]
    )

def build_report_reading_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    families = ["research_reports", "quality_gates", "final_review", "scenario_regression", "master_orchestration", "secrets_hygiene", "backup_recovery", "portable_packaging", "evidence_governance", "artifact_metadata", "local_knowledge_graph", "local_timeline", "local_consistency", "local_readiness", "local_maintenance", "local_archive", "local_dr"]
    lessons = [build_report_reading_lesson(f, profile) for f in families]
    df = pd.DataFrame([l.__dict__ for l in lessons])
    return df, summarize_report_lessons(df)

def summarize_report_lessons(report_lesson_df: pd.DataFrame) -> dict:
    if report_lesson_df is None or report_lesson_df.empty: return {"count": 0}
    return {"count": len(report_lesson_df)}
