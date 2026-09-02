
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_featurestore_load_methods(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_featurestore_contracts(fs_df: pd.DataFrame) -> dict: return {"total": len(fs_df)}
def build_featurestore_contract_catalog(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_featurestore_contracts(df)
