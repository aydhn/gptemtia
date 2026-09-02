"""
Sensitive Exclusions.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile

def is_sensitive_archival_path(path: Path, project_root: Path) -> bool:
    name = path.name.lower()
    if name.startswith(".env"): return True
    if any(x in name for x in ["secret", "credential", "private_key", "id_rsa", "token", "api_key", "password", "auth"]):
        return True
    if name.endswith((".pem", ".key")):
        return True
    return False

def classify_sensitive_exclusion_reason(path: Path, project_root: Path) -> str:
    name = path.name.lower()
    if name.startswith(".env"): return "env_file"
    if "secret" in name: return "contains_secret_keyword"
    return "general_sensitive"

def build_sensitive_file_exclusion_registry(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    exclusions = []
    if project_root.exists():
        for p in project_root.rglob("*"):
            if p.is_file() and is_sensitive_archival_path(p, project_root):
                try:
                    rel_path = p.relative_to(project_root).as_posix()
                except:
                    rel_path = p.name
                exclusions.append({
                    "relative_path": rel_path,
                    "reason": classify_sensitive_exclusion_reason(p, project_root)
                })
    df = pd.DataFrame(exclusions) if exclusions else pd.DataFrame(columns=["relative_path", "reason"])
    return df, summarize_sensitive_exclusions(df)

def summarize_sensitive_exclusions(exclusion_df: pd.DataFrame) -> dict:
    return {"total_excluded": len(exclusion_df) if exclusion_df is not None else 0}
