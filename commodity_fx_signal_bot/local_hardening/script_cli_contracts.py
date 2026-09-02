
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_script_cli_entries(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def detect_script_cli_safety_flags(script_df: pd.DataFrame) -> pd.DataFrame: return script_df
def summarize_script_cli_contracts(script_df: pd.DataFrame) -> dict: return {"total": len(script_df)}
def build_script_cli_contract_catalog(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_script_cli_contracts(df)
