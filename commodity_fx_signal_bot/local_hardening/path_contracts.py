
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_path_constants_and_directories(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_path_contracts(path_df: pd.DataFrame) -> dict: return {"total": len(path_df)}
def build_path_contract_catalog(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_path_contracts(df)
