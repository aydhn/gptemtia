import pandas as pd
from .continuity_models import OperatorMemoryItem

def build_operator_memory_index(profile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([i.__dict__ for i in build_default_operator_memory_items(profile)])
    return df, summarize_operator_memory_map(df)
def build_operator_memory_topic_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_operator_memory_index(profile)
def build_operator_memory_reading_route(profile) -> tuple[pd.DataFrame, dict]:
    return build_operator_memory_index(profile)
def build_default_operator_memory_items(profile) -> list[OperatorMemoryItem]:
    return [OperatorMemoryItem("m1", "t1", "a1", "s1", [], "note", ["No cloud sync"])]
def summarize_operator_memory_map(df: pd.DataFrame) -> dict:
    return {"total": len(df)}