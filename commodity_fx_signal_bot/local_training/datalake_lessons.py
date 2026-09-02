import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile
from .training_models import TrainingLesson, build_training_lesson_id

def build_datalake_domain_lesson(domain_name: str, profile: LocalTrainingProfile) -> TrainingLesson:
    return TrainingLesson(
        lesson_id=build_training_lesson_id("datalake_training", domain_name),
        lesson_name=f"Explore {domain_name}",
        domain_label="datalake_training",
        role_label="operator_role",
        objective="Navigate DataLake",
        steps=["Open folder"],
        safe_commands=[],
        expected_outputs=[],
        status="lesson_ready",
        warnings=["DataLake lesson raw data extraction değildir.", "Secret/private data okunmaz.", "Read-only navigation anlatılır."]
    )

def build_datalake_reading_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([build_datalake_domain_lesson("test", profile).__dict__])
    return df, summarize_datalake_lessons(df)

def summarize_datalake_lessons(datalake_lesson_df: pd.DataFrame) -> dict:
    if datalake_lesson_df is None or datalake_lesson_df.empty: return {"count": 0}
    return {"count": len(datalake_lesson_df)}
