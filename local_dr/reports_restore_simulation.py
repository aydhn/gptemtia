import pandas as pd
from pathlib import Path
from typing import Tuple
from local_dr.dr_config import LocalDRProfile

def simulate_report_domain_restore_requirements(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    data = [
        {"domain": "reports", "requirement": "templates_exist", "status": "pass"},
        {"domain": "reports", "requirement": "data_sources_available", "status": "pass"}
    ]
    return pd.DataFrame(data)

def detect_reports_restore_gaps(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    return df[df["status"] != "pass"]

def summarize_reports_restore_simulation(df: pd.DataFrame) -> dict:
    total = len(df)
    passed = len(df[df["status"] == "pass"]) if not df.empty else 0
    return {
        "total_requirements": total,
        "passed_requirements": passed,
        "gaps": total - passed
    }

def build_reports_restore_simulation_report(project_root: Path, profile: LocalDRProfile) -> Tuple[pd.DataFrame, dict]:
    df = simulate_report_domain_restore_requirements(project_root, profile)
    gaps = detect_reports_restore_gaps(df)
    summary = summarize_reports_restore_simulation(df)
    return df, summary
