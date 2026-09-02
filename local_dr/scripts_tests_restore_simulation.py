import pandas as pd
from pathlib import Path
from typing import Tuple
from local_dr.dr_config import LocalDRProfile

def simulate_scripts_restore_requirements(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    data = [
        {"item_type": "script", "name": "run.sh", "status": "pass"}
    ]
    return pd.DataFrame(data)

def simulate_tests_restore_requirements(project_root: Path, profile: LocalDRProfile) -> pd.DataFrame:
    data = [
        {"item_type": "test", "name": "test_main.py", "status": "pass"}
    ]
    return pd.DataFrame(data)

def detect_scripts_tests_restore_gaps(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    return df[df["status"] != "pass"]

def summarize_scripts_tests_restore_simulation(df: pd.DataFrame) -> dict:
    total = len(df)
    passed = len(df[df["status"] == "pass"]) if not df.empty else 0
    return {
        "total": total,
        "passed": passed,
        "gaps": total - passed
    }

def build_scripts_tests_restore_simulation_report(project_root: Path, profile: LocalDRProfile) -> Tuple[pd.DataFrame, dict]:
    df_scripts = simulate_scripts_restore_requirements(project_root, profile)
    df_tests = simulate_tests_restore_requirements(project_root, profile)
    df_combined = pd.concat([df_scripts, df_tests], ignore_index=True) if not df_scripts.empty or not df_tests.empty else pd.DataFrame(columns=["item_type", "name", "status"])
    gaps = detect_scripts_tests_restore_gaps(df_combined)
    summary = summarize_scripts_tests_restore_simulation(df_combined)
    return df_combined, summary
