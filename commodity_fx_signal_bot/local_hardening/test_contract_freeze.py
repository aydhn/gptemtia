
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_test_contract_files(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_test_contract_freeze(test_df: pd.DataFrame) -> dict: return {"total": len(test_df)}
def build_test_contract_freeze_registry(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_test_contract_freeze(df)
