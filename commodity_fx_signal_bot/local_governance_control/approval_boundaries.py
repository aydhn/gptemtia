import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_approval_boundaries(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [{"boundary_name": "Documentation Approval", "is_rehearsal": True}]
    return pd.DataFrame(data)

def build_default_non_approval_boundaries(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    boundaries = [
        "live trading",
        "broker execution",
        "investment advice",
        "production deployment",
        "model deployment",
        "cloud upload",
        "package publish",
        "compliance certification",
        "legal sign-off",
        "official committee approval"
    ]
    data = [{"boundary_name": b, "reason": "Explicitly forbidden in local governance"} for b in boundaries]
    return pd.DataFrame(data)

def build_approval_boundary_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_approval_boundaries(profile)
    return df, {"total": len(df)}

def build_non_approval_boundary_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_non_approval_boundaries(profile)
    return df, {"total": len(df)}

def summarize_approval_boundaries(approval_df: pd.DataFrame, non_approval_df: pd.DataFrame) -> dict:
    return {
        "approval_boundaries": len(approval_df) if approval_df is not None else 0,
        "non_approval_boundaries": len(non_approval_df) if non_approval_df is not None else 0
    }
