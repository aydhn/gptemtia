
import pandas as pd
from local_dr.dr_config import LocalDRProfile

def build_failure_playbook_for_mode(row: pd.Series, profile: LocalDRProfile) -> dict:
    return {"playbook": "dummy"}

def build_failure_playbook_markdown(row: pd.Series, profile: LocalDRProfile) -> str:
    return "playbook markdown"

def build_failure_mode_playbook_index(failure_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"playbook": "dummy"}]), {"total": 1}

def summarize_failure_playbooks(playbook_df: pd.DataFrame) -> dict:
    return {"total": len(playbook_df)}
