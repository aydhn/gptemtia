
from pathlib import Path
import pandas as pd
from typing import Tuple

def build_required_gitignore_patterns() -> list[str]: return [".env", ".env.*", "!.env.example", "*.pem", "*.key", "id_rsa", "secrets/", "credentials/", "tokens/", "__pycache__/", ".pytest_cache/", ".ipynb_checkpoints/", "*.sqlite", "*.db", "local_data/", "private/", "*.log"]

def read_gitignore(project_root: Path) -> list[str]:
    path = project_root / ".gitignore"
    if not path.exists(): return []
    with open(path, "r", encoding="utf-8") as f: return [l.strip() for l in f if l.strip() and not l.startswith("#")]

def audit_gitignore_hygiene(project_root: Path) -> Tuple[pd.DataFrame, dict]:
    current = read_gitignore(project_root)
    audit = []
    for req in build_required_gitignore_patterns():
        status = "present" if req in current else "missing"
        if req == ".env" and ".env" not in current: status = "missing"
        audit.append({"pattern": req, "status": status, "recommendation": f"Add {req} to .gitignore" if status == "missing" else "No action needed"})
    df = pd.DataFrame(audit)
    return df, {"total_required": len(df), "missing_count": len(df[df["status"] == "missing"])}

def build_gitignore_recommendations(audit_df: pd.DataFrame) -> pd.DataFrame:
    if audit_df is None or audit_df.empty: return pd.DataFrame()
    return audit_df[audit_df["status"] == "missing"].copy()
