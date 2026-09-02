
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_generated_docs(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_generated_docs_freeze(generated_df: pd.DataFrame) -> dict: return {"total": len(generated_df)}
def build_generated_docs_freeze_catalog(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_generated_docs_freeze(df)
