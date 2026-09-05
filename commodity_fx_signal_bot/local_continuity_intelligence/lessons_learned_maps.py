import pandas as pd
from .continuity_models import LessonLearnedItem
def build_lessons_learned_category_registry(profile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([i.__dict__ for i in build_default_lessons(profile)])
    return df, summarize_lessons_learned_map(df)
def build_lessons_learned_phase_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_lessons_learned_category_registry(profile)
def build_lessons_learned_risk_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_lessons_learned_category_registry(profile)
def build_lessons_learned_quality_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_lessons_learned_category_registry(profile)
def build_lessons_learned_safety_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_lessons_learned_category_registry(profile)
def build_default_lessons(profile) -> list[LessonLearnedItem]:
    return [LessonLearnedItem("l1", "c1", "p1", "t1", "s1", "f1", ["Safety certification değildir."])]
def summarize_lessons_learned_map(df: pd.DataFrame) -> dict:
    return {"total": len(df)}