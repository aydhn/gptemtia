import pandas as pd
from typing import Tuple, Dict, Any
from pathlib import Path
import re

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def detect_deprecated_artifact_patterns(project_root: Path) -> pd.DataFrame:
    deprecated_patterns = [
        r"(?i)old", r"(?i)deprecated", r"(?i)legacy", r"(?i)temp",
        r"(?i)backup copy", r"(?i)unused", r"(?i)draft", r"(?i)obsolete"
    ]

    findings = []
    # For a real implementation, we would recursively scan directories.
    # We will do a limited depth scan to keep performance reasonable for this demo.
    search_dirs = [project_root / "data" / "lake", project_root / "reports" / "output", project_root / "scripts"]

    for sdir in search_dirs:
        if sdir.exists():
            for filepath in sdir.rglob("*"):
                if filepath.is_file():
                    name = filepath.name
                    for pat in deprecated_patterns:
                        if re.search(pat, name):
                            findings.append({
                                "file_path": str(filepath.relative_to(project_root)),
                                "pattern_matched": pat,
                                "type": "deprecated_pattern"
                            })
                            break

    return pd.DataFrame(findings)

def detect_duplicate_or_legacy_outputs(project_root: Path) -> pd.DataFrame:
    # A stub for detecting duplication
    return pd.DataFrame()

def build_deprecated_artifact_watch_report(project_root: Path, profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if not profile.scan_cross_layer_outputs:
        return pd.DataFrame(), {"status": "skipped", "reason": "scan_cross_layer_outputs is False"}

    df1 = detect_deprecated_artifact_patterns(project_root)
    df2 = detect_duplicate_or_legacy_outputs(project_root)

    df = pd.concat([df1, df2], ignore_index=True) if not df1.empty or not df2.empty else pd.DataFrame()

    summary = summarize_deprecated_artifact_watch(df)
    return df, summary

def summarize_deprecated_artifact_watch(df: pd.DataFrame) -> Dict[str, Any]:
    if df is None or df.empty:
        return {"total_deprecated_artifacts": 0}

    return {
        "total_deprecated_artifacts": len(df),
        "disclaimer": "Artifacts are flagged for manual review. No automatic file deletion is performed."
    }
