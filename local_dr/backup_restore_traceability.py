import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile

def build_backup_restore_traceability_report(project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "ok"}

def link_backup_outputs_to_restore_checklists(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame()

def detect_backup_restore_traceability_gaps(trace_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_backup_restore_traceability(trace_df: pd.DataFrame) -> dict:
    return {"summary": "done"}
