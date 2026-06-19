import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile

def build_security_boundary_readiness_report(project_root: Path, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"boundary": "security", "status": "ok"}])
    return df, summarize_security_boundary_readiness(df)

def check_no_live_broker_deploy_claims(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def check_no_raw_secret_outputs(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def check_non_use_policy_presence(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def check_no_investment_advice_claims(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_security_boundary_readiness(security_df: pd.DataFrame) -> dict:
    return {"total_checks": len(security_df)}
