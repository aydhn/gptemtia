import pandas as pd
from typing import Tuple, Dict, Any
from pathlib import Path
import time

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def discover_report_files_for_staleness(project_root: Path) -> pd.DataFrame:
    reports_dir = project_root / "reports" / "output"
    files = []

    if reports_dir.exists():
        for filepath in reports_dir.rglob("*"):
            if filepath.is_file() and filepath.suffix in [".md", ".csv", ".json", ".txt"]:
                files.append({
                    "file_path": str(filepath.relative_to(project_root)),
                    "mtime": filepath.stat().st_mtime
                })
    return pd.DataFrame(files)

def classify_report_staleness(row: pd.Series, profile: LocalMaintenanceProfile) -> str:
    now = time.time()
    mtime = row.get("mtime", now)
    age_days = (now - mtime) / (60 * 60 * 24)

    if age_days > profile.stale_report_days_warning:
        return "stale_report"
    return "current_report"

def build_stale_report_watch_report(project_root: Path, profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if not profile.scan_reports:
        return pd.DataFrame(), {"status": "skipped"}

    df = discover_report_files_for_staleness(project_root)
    if not df.empty:
        df["status"] = df.apply(classify_report_staleness, profile=profile, axis=1)

    summary = summarize_stale_report_watch(df)
    return df, summary

def summarize_stale_report_watch(report_df: pd.DataFrame) -> Dict[str, Any]:
    if report_df is None or report_df.empty:
        return {"total_reports": 0}

    stale_count = len(report_df[report_df["status"] == "stale_report"]) if "status" in report_df else 0

    return {
        "total_reports": len(report_df),
        "stale_reports": stale_count,
        "disclaimer": "Staleness is approximated by mtime. Stale report does not imply an incorrect report. Refresh suggestions are manual or dry-run only."
    }
