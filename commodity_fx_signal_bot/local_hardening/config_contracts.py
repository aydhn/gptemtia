
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_settings_fields(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_config_settings_contracts(settings_df: pd.DataFrame) -> dict: return {"total": len(settings_df)}
def build_config_settings_contract_catalog(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_config_settings_contracts(df)
