import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile
from .training_models import TrainingLesson, build_training_lesson_id

def build_cross_layer_lesson(layer_name: str, profile: LocalTrainingProfile) -> TrainingLesson:
    return TrainingLesson(
        lesson_id=build_training_lesson_id("cross_layer_training", layer_name),
        lesson_name=f"Cross layer: {layer_name}",
        domain_label="cross_layer_training",
        role_label="operator_role",
        objective="Understand cross layer",
        steps=["Review links"],
        safe_commands=[],
        expected_outputs=[],
        status="lesson_ready",
        warnings=["Cross-layer lesson canlı sistem eğitimi değildir.", "Relationship/consistency/readiness score production guarantee değildir.", "Manual review vurgusu olmalı."]
    )

def build_cross_layer_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    layers = ["evidence_governance", "artifact_metadata", "local_knowledge_graph", "local_timeline", "local_consistency", "local_readiness", "local_maintenance", "local_archive", "local_dr", "local_training"]
    lessons = [build_cross_layer_lesson(l, profile) for l in layers]
    df = pd.DataFrame([l.__dict__ for l in lessons])
    return df, summarize_cross_layer_lessons(df)

def summarize_cross_layer_lessons(cross_df: pd.DataFrame) -> dict:
    if cross_df is None or cross_df.empty: return {"count": 0}
    return {"count": len(cross_df)}
