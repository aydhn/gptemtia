
import pandas as pd
from pathlib import Path
from local_dr.dr_config import LocalDRProfile

def check_restore_prerequisite_presence(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame([{"prereq": "dummy"}])

def check_restore_documentation_presence(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame([{"doc": "dummy"}])

def build_restore_readiness_dry_run_checklist(project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"checklist": "dummy"}]), {"total": 1}

def summarize_restore_readiness_checklist(checklist_df: pd.DataFrame) -> dict:
    return {"total": len(checklist_df)}
