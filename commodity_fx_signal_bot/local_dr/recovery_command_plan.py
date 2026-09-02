
import pandas as pd
from local_dr.dr_config import LocalDRProfile

def classify_recovery_command_safety(command: str) -> dict:
    return {"safety": "safe"}

def detect_forbidden_recovery_command_terms(command: str) -> list[str]:
    return []

def build_manual_recovery_command_plan(profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"command": "python -m scripts.run_dr_status"}]), {"total": 1}

def summarize_recovery_command_plan(command_df: pd.DataFrame) -> dict:
    return {"total": len(command_df)}
