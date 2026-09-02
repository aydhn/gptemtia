import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_unresolved_governance_items(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item": "UI Framework Selection", "status": "unresolved"}])

def build_default_open_decisions(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    return pd.DataFrame([{"decision": "Database Engine", "status": "open", "is_official_pending": False}])

def build_governance_unresolved_item_register(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_unresolved_governance_items(profile)
    return df, {"total": len(df)}

def build_governance_open_decision_register(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_open_decisions(profile)
    return df, {"total": len(df)}

def summarize_unresolved_decisions(unresolved_df: pd.DataFrame, open_df: pd.DataFrame) -> dict:
    return {
        "unresolved_count": len(unresolved_df) if unresolved_df is not None else 0,
        "open_count": len(open_df) if open_df is not None else 0
    }
