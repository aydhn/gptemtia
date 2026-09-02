import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_approval_checklists(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"checklist_name": "Safety Checks", "item": "No live trading claim", "required": True},
        {"checklist_name": "Safety Checks", "item": "No production approval claim", "required": True},
        {"checklist_name": "Quality Checks", "item": "Documentation up to date", "required": True}
    ]
    return pd.DataFrame(data)

def build_manual_approval_checklist_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_approval_checklists(profile)
    return df, summarize_approval_checklists(df)

def summarize_approval_checklists(checklist_df: pd.DataFrame) -> dict:
    if checklist_df is None or checklist_df.empty:
        return {"total": 0}
    return {"total": len(checklist_df), "checklists": checklist_df["checklist_name"].nunique()}
