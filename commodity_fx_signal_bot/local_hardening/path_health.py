
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def detect_missing_expected_paths(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def detect_path_reference_warnings(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_path_health(path_df: pd.DataFrame) -> dict: return {"total": len(path_df)}
def build_final_path_health_report(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_path_health(df)
