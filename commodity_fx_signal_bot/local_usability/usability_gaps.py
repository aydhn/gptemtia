import pandas as pd
from .usability_config import LocalUsabilityProfile

def detect_missing_usability_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing domain"}])

def detect_missing_friction_items(friction_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing friction"}])

def detect_missing_command_guidance(command_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing command guidance"}])

def detect_missing_operator_paths(path_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing paths"}])

def build_usability_gap_register(
    domain_df: pd.DataFrame,
    friction_df: pd.DataFrame,
    command_df: pd.DataFrame,
    path_df: pd.DataFrame,
    profile: LocalUsabilityProfile,
) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"gap": "all good"}])
    return df, {"total": len(df)}

def summarize_usability_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total": len(gap_df)}
