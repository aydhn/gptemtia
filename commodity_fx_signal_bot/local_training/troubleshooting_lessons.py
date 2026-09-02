import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile
from .training_models import TrainingLesson, build_training_lesson_id

def build_common_troubleshooting_lessons(profile: LocalTrainingProfile) -> list[TrainingLesson]:
    commons = ["missing output file", "missing report directory", "import error", "missing optional dependency", "empty DataFrame output", "missing DataLake save/load pair", "missing status script", "broken path reference", "stale report", "secret boundary warning", "forbidden command warning"]
    return [
        TrainingLesson(
            lesson_id=build_training_lesson_id("troubleshooting_training", c),
            lesson_name=f"Fix {c}",
            domain_label="troubleshooting_training",
            role_label="developer_role",
            objective="Troubleshoot",
            steps=["Check logs"],
            safe_commands=[],
            expected_outputs=[],
            status="lesson_ready",
            warnings=["Troubleshooting auto-fix değildir.", "Dosya silme/overwrite önermez.", "Manual review ve safe status commands odaklıdır."]
        ) for c in commons
    ]

def build_troubleshooting_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    lessons = build_common_troubleshooting_lessons(profile)
    df = pd.DataFrame([l.__dict__ for l in lessons])
    return df, summarize_troubleshooting_lessons(df)

def summarize_troubleshooting_lessons(troubleshooting_df: pd.DataFrame) -> dict:
    if troubleshooting_df is None or troubleshooting_df.empty: return {"count": 0}
    return {"count": len(troubleshooting_df)}
