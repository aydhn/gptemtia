
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def summarize_rc_boundary_checklist(boundary_df: pd.DataFrame) -> dict: return {"total": len(boundary_df)}
def build_rc_non_use_boundary_checklist(profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_rc_boundary_checklist(df)
