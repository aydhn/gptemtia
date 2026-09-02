
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def detect_release_overclaim_terms(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def detect_live_broker_deploy_terms(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def detect_destructive_command_terms(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def summarize_safety_hardening(safety_df: pd.DataFrame) -> dict: return {"total": len(safety_df)}
def build_final_safety_hardening_report(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_safety_hardening(df)
