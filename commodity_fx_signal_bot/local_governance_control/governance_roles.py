import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_governance_roles(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    roles = [
        "operator",
        "reviewer",
        "technical maintainer",
        "safety reviewer",
        "documentation reviewer",
        "executive observer",
        "risk committee rehearsal observer"
    ]
    data = [{"role": r, "description": f"Role for {r}", "is_rehearsal_only": True} for r in roles]
    return pd.DataFrame(data)

def build_governance_roles_matrix_rehearsal(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_governance_roles(profile)
    return df, summarize_governance_roles(df)

def summarize_governance_roles(role_df: pd.DataFrame) -> dict:
    if role_df is None or role_df.empty:
        return {"total": 0}
    return {"total": len(role_df)}
