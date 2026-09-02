import pandas as pd
from pathlib import Path
from typing import Tuple
from local_dr.dr_config import LocalDRProfile

def simulate_secret_in_archive_incident(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    data = [
        {"incident": "secret_in_archive", "status": "resolved"}
    ]
    return pd.DataFrame(data)

def simulate_secret_in_report_incident(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    data = [
        {"incident": "secret_in_report", "status": "resolved"}
    ]
    return pd.DataFrame(data)

def build_secret_boundary_manual_response_steps(profile: LocalDRProfile) -> pd.DataFrame:
    data = [
        {"step": "revoke_secret", "status": "pending"}
    ]
    return pd.DataFrame(data)

def summarize_secret_boundary_rehearsal(df: pd.DataFrame) -> dict:
    total = len(df)
    resolved = len(df[df["status"] == "resolved"]) if not df.empty else 0
    return {
        "total_incidents": total,
        "resolved_incidents": resolved
    }

def build_secret_boundary_incident_rehearsal(project_root: Path, profile: LocalDRProfile) -> Tuple[pd.DataFrame, dict]:
    df1 = simulate_secret_in_archive_incident(project_root, profile)
    df2 = simulate_secret_in_report_incident(project_root, profile)
    df = pd.concat([df1, df2], ignore_index=True) if not df1.empty or not df2.empty else pd.DataFrame(columns=["incident", "status"])
    summary = summarize_secret_boundary_rehearsal(df)
    return df, summary
