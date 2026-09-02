
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def detect_naming_convention_warnings(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_naming_convention(name_df: pd.DataFrame) -> dict: return {"total": len(name_df)}
def build_final_naming_convention_report(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_naming_convention(df)
