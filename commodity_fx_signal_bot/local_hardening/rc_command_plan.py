
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def classify_rc_command_safety(command: str) -> dict: return {}
def detect_forbidden_rc_command_terms(command: str) -> list[str]: return []
def summarize_rc_command_plan(command_df: pd.DataFrame) -> dict: return {"total": len(command_df)}
def build_rc_dry_run_command_plan(profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_rc_command_plan(df)
