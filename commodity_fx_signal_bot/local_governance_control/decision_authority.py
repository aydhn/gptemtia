import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_decision_authority_map(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"decision_type": "Accept Rehearsal", "authorized_role": "reviewer", "notes": "Not a real decision"}
    ]
    return pd.DataFrame(data)

def build_decision_authority_map_rehearsal(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_decision_authority_map(profile)
    return df, summarize_decision_authority_map(df)

def summarize_decision_authority_map(authority_df: pd.DataFrame) -> dict:
    if authority_df is None or authority_df.empty:
        return {"total": 0}
    return {"total": len(authority_df)}
