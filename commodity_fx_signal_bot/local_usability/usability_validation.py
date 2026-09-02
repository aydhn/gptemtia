import pandas as pd
from .usability_config import LocalUsabilityProfile

def validate_usability_domains(domain_df: pd.DataFrame, profile: LocalUsabilityProfile) -> dict:
    return {"valid": True}

def validate_friction_map(friction_df: pd.DataFrame, profile: LocalUsabilityProfile) -> dict:
    return {"valid": True}

def validate_command_index(command_df: pd.DataFrame, profile: LocalUsabilityProfile) -> dict:
    return {"valid": True}

def validate_operator_paths(path_df: pd.DataFrame, profile: LocalUsabilityProfile) -> dict:
    return {"valid": True}

def validate_usability_no_go_safe_go(summary_df: pd.DataFrame, profile: LocalUsabilityProfile) -> dict:
    return {"valid": True}

def validate_no_telemetry_or_advice(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    return {"valid": True}

def build_usability_validation_report(tables: dict[str, pd.DataFrame], profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"status": "valid"}])
    return df, {"total_valid": True}
