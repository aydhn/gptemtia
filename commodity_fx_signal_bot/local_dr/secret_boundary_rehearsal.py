
import pandas as pd
from pathlib import Path
from local_dr.dr_config import LocalDRProfile

def simulate_secret_in_archive_incident(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame([{"incident": "dummy"}])

def simulate_secret_in_report_incident(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame([{"incident": "dummy"}])

def build_secret_boundary_manual_response_steps(profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame([{"steps": "dummy"}])

def build_secret_boundary_incident_rehearsal(project_root: Path, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"rehearsal": "dummy"}]), {"total": 1}

def summarize_secret_boundary_rehearsal(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
