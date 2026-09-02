
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_python_modules(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def discover_module_import_references(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_unused_module_candidates(module_df: pd.DataFrame) -> dict: return {"total": len(module_df)}
def build_unused_module_candidate_report(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_unused_module_candidates(df)
