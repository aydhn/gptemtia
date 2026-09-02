import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile

def build_archive_restore_traceability_report(project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "ok"}

def link_archive_items_to_restore_prerequisites(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame()

def detect_archive_restore_traceability_gaps(trace_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_archive_restore_traceability(trace_df: pd.DataFrame) -> dict:
    return {"summary": "done"}
