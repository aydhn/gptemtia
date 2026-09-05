import pandas as pd
from pathlib import Path
from .completion_config import LocalProjectCompletionProfile

def build_knowledge_freeze_rehearsal_registry(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"freeze_id": "kf_001", "status": "knowledge_freeze_rehearsal_available", "note": "Local documentation snapshot."}])
    return df, summarize_knowledge_freeze(df)

def build_knowledge_freeze_inventory(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "README.md", "status": "frozen_rehearsal"}])
    return df, summarize_knowledge_freeze(df)

def summarize_knowledge_freeze(df: pd.DataFrame) -> dict:
    return {"items": len(df), "note": "Knowledge freeze is not a git tag or file lock."}
