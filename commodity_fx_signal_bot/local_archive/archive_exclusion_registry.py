from pathlib import Path
import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def build_default_archive_exclusions(profile: LocalArchiveProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"pattern": ".env*", "reason": "Environment variables, contains secrets"},
        {"pattern": "*.key", "reason": "Private keys"},
        {"pattern": "*.pem", "reason": "Certificates"},
        {"pattern": "credentials*", "reason": "Credentials file"},
        {"pattern": "secrets*", "reason": "Secrets file"},
        {"pattern": "token*", "reason": "Token file"},
        {"pattern": "private*", "reason": "Private key material"},
        {"pattern": "__pycache__/*", "reason": "Python bytecode cache"},
        {"pattern": ".git/*", "reason": "Git repository history"},
        {"pattern": "data/cache/*", "reason": "Temporary cache files"}
    ])

def detect_sensitive_paths_for_exclusion(project_root: Path) -> pd.DataFrame:
    sensitive = []
    for f in project_root.glob(".env*"):
        try:
            sensitive.append({"path": str(f.relative_to(project_root)), "reason": "Environment file"})
        except ValueError: pass
    for pattern in ["*.key", "*.pem", "*credentials*", "*secret*"]:
        for f in project_root.rglob(pattern):
            if f.is_file():
                try:
                    sensitive.append({"path": str(f.relative_to(project_root)), "reason": "Matches sensitive filename pattern"})
                except ValueError: pass
    return pd.DataFrame(sensitive)

def build_archive_exclusion_registry(project_root: Path, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    defaults = build_default_archive_exclusions(profile)
    sensitive = detect_sensitive_paths_for_exclusion(project_root)
    if sensitive.empty:
        df = defaults
    else:
        df = pd.concat([defaults, sensitive.rename(columns={"path": "pattern"})], ignore_index=True)
    return df, summarize_archive_exclusions(df)

def summarize_archive_exclusions(exclusion_df: pd.DataFrame) -> Dict:
    if exclusion_df.empty: return {"total_exclusions": 0}
    return {
        "total_rules": len(exclusion_df),
        "notice": "These paths are explicitly excluded. Their values are not read."
    }
