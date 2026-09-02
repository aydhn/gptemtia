
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def build_contract_surface_overview(profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_contract_surface_registry(contract_df: pd.DataFrame) -> dict: return {"total": len(contract_df)}
def build_contract_surface_registry(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = build_contract_surface_overview(profile)
    return df, summarize_contract_surface_registry(df)
