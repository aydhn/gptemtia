import pandas as pd
from local_dr.profile import LocalDRProfile

def build_failure_mode_playbook_index(failure_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return failure_df.copy(), {"status": "ok"}

def build_failure_playbook_for_mode(row: pd.Series, profile: LocalDRProfile) -> dict:
    return {"mode": str(row.get("mode", ""))}

def build_failure_playbook_markdown(row: pd.Series, profile: LocalDRProfile) -> str:
    return f"# Playbook: {row.get('mode', '')}"

def summarize_failure_playbooks(playbook_df: pd.DataFrame) -> dict:
    return {"summary": "done"}
