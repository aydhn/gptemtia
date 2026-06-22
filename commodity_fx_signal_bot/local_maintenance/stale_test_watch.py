import pandas as pd
from typing import Tuple, Dict, Any
from pathlib import Path
import time

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def discover_tests_for_staleness(project_root: Path) -> pd.DataFrame:
    tests_dir = project_root / "tests"
    files = []

    if tests_dir.exists():
        for filepath in tests_dir.rglob("test_*.py"):
            files.append({
                "file_path": str(filepath.relative_to(project_root)),
                "mtime": filepath.stat().st_mtime
            })

    return pd.DataFrame(files)

def classify_test_staleness(row: pd.Series, profile: LocalMaintenanceProfile) -> str:
    now = time.time()
    mtime = row.get("mtime", now)
    age_days = (now - mtime) / (60 * 60 * 24)

    if age_days > profile.stale_test_days_warning:
        return "stale_test"
    return "current_test"

def detect_modules_without_recent_tests(project_root: Path, test_df: pd.DataFrame) -> pd.DataFrame:
    # A stub for missing test detection
    return pd.DataFrame()

def build_stale_test_watch_report(project_root: Path, profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if not profile.scan_tests:
        return pd.DataFrame(), {"status": "skipped"}

    df = discover_tests_for_staleness(project_root)
    if not df.empty:
        df["status"] = df.apply(classify_test_staleness, profile=profile, axis=1)

    summary = summarize_stale_test_watch(df)
    return df, summary

def summarize_stale_test_watch(test_df: pd.DataFrame) -> Dict[str, Any]:
    if test_df is None or test_df.empty:
        return {"total_tests": 0}

    stale_count = len(test_df[test_df["status"] == "stale_test"]) if "status" in test_df else 0

    return {
        "total_tests": len(test_df),
        "stale_tests": stale_count,
        "disclaimer": "Stale test does not mean test failure. Tests are not executed by this script. Missing recent test generates a warning for manual review."
    }
