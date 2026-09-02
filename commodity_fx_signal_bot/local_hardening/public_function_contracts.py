
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_public_functions(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def infer_function_contract(function_row: pd.Series, profile: LocalHardeningProfile) -> dict: return {}
def summarize_public_function_contracts(function_df: pd.DataFrame) -> dict: return {"total": len(function_df)}
def build_public_function_contract_catalog(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_public_function_contracts(df)
