
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def detect_duplicate_function_names(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def detect_similar_utility_module_names(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_duplicate_utility_candidates(dup_df: pd.DataFrame) -> dict: return {"total": len(dup_df)}
def build_duplicate_utility_candidate_report(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_duplicate_utility_candidates(df)
