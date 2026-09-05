import pandas as pd
from .completion_config import LocalProjectCompletionProfile

def build_default_knowledge_freeze_boundaries(profile: LocalProjectCompletionProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"boundary": "Not a Git tag"},
        {"boundary": "Not a file lock"},
        {"boundary": "Not an official release"}
    ])

def build_knowledge_freeze_boundary_registry(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_knowledge_freeze_boundaries(profile)
    return df, summarize_knowledge_freeze_boundaries(df)

def summarize_knowledge_freeze_boundaries(df: pd.DataFrame) -> dict:
    return {"boundaries": len(df), "note": "Boundaries defined."}
