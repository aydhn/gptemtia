
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def check_required_docs_for_freeze(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_documentation_freeze(doc_df: pd.DataFrame) -> dict: return {"total": len(doc_df)}
def build_documentation_freeze_snapshot(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_documentation_freeze(df)
def build_readme_docs_freeze_checklist(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_documentation_freeze(df)
