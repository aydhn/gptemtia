import pandas as pd
from typing import Tuple, Dict, Any
from pathlib import Path
import time
import re

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def discover_docs_for_staleness(project_root: Path) -> pd.DataFrame:
    docs_dir = project_root / "docs"
    files = []

    if docs_dir.exists():
        for filepath in docs_dir.rglob("*.md"):
            files.append({
                "file_path": str(filepath.relative_to(project_root)),
                "mtime": filepath.stat().st_mtime
            })

    # Include README.md at root
    readme = project_root / "README.md"
    if readme.exists():
         files.append({
                "file_path": str(readme.relative_to(project_root)),
                "mtime": readme.stat().st_mtime
            })

    return pd.DataFrame(files)

def classify_doc_staleness(row: pd.Series, profile: LocalMaintenanceProfile) -> str:
    now = time.time()
    mtime = row.get("mtime", now)
    age_days = (now - mtime) / (60 * 60 * 24)

    if age_days > profile.stale_doc_days_warning:
        return "stale_doc"
    return "current_doc"

def detect_docs_missing_recent_phase_references(project_root: Path) -> pd.DataFrame:
    # A heuristic to check if the docs mention recent phases like Phase 70
    docs_dir = project_root / "docs"
    missing = []

    if docs_dir.exists():
        for filepath in docs_dir.rglob("*.md"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    if not re.search(r'(?i)phase\s*(69|70)', content) and "ARCHITECTURE" in filepath.name:
                        missing.append({
                            "file_path": str(filepath.relative_to(project_root)),
                            "warning": "May be missing recent phase references."
                        })
            except Exception:
                pass

    return pd.DataFrame(missing)

def build_stale_documentation_watch_report(project_root: Path, profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if not profile.scan_docs:
        return pd.DataFrame(), {"status": "skipped"}

    df = discover_docs_for_staleness(project_root)
    if not df.empty:
        df["status"] = df.apply(classify_doc_staleness, profile=profile, axis=1)

    missing_phase_df = detect_docs_missing_recent_phase_references(project_root)
    if not missing_phase_df.empty:
        df = df.merge(missing_phase_df, on="file_path", how="left")

    summary = summarize_stale_documentation_watch(df)
    return df, summary

def summarize_stale_documentation_watch(doc_df: pd.DataFrame) -> Dict[str, Any]:
    if doc_df is None or doc_df.empty:
        return {"total_docs": 0}

    stale_count = len(doc_df[doc_df["status"] == "stale_doc"]) if "status" in doc_df else 0

    return {
        "total_docs": len(doc_df),
        "stale_docs": stale_count,
        "disclaimer": "Docs stale warning is for manual review only. Files are not automatically updated. Phase reference is a heuristic."
    }
