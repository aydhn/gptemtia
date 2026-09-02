import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile

def build_restore_readiness_dry_run_checklist(project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "ok"}

def check_restore_prerequisite_presence(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame()

def check_restore_documentation_presence(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_restore_readiness_checklist(checklist_df: pd.DataFrame) -> dict:
    return {"summary": "done"}
