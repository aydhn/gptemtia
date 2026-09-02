
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_python_symbols(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def discover_symbol_references(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def classify_dead_code_candidate(symbol_row: pd.Series, reference_df: pd.DataFrame, profile: LocalHardeningProfile) -> str: return "unknown"
def summarize_dead_code_candidates(candidate_df: pd.DataFrame) -> dict: return {"total": len(candidate_df)}
def build_dead_code_candidate_report(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_dead_code_candidates(df)
