import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_signoff_rehearsal_forms(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [{"form_name": "Quality Signoff Rehearsal", "is_real_signoff": False}]
    return pd.DataFrame(data)

def build_manual_signoff_rehearsal_form_library(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_signoff_rehearsal_forms(profile)
    return df, summarize_signoff_rehearsal_forms(df)

def summarize_signoff_rehearsal_forms(form_df: pd.DataFrame) -> dict:
    if form_df is None or form_df.empty:
        return {"total": 0}
    return {"total": len(form_df)}
