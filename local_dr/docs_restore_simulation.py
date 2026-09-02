import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile

def build_docs_restore_simulation_report(project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "ok"}

def simulate_required_docs_restore(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame()

def detect_docs_restore_gaps(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_docs_restore_simulation(df: pd.DataFrame) -> dict:
    return {"summary": "done"}
