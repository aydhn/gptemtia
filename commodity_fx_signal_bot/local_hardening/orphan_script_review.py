
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_script_files(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def discover_script_doc_references(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_orphan_script_candidates(script_df: pd.DataFrame) -> dict: return {"total": len(script_df)}
def build_orphan_script_candidate_report(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_orphan_script_candidates(df)
