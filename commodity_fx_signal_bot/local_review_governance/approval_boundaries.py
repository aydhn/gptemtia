import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_default_approval_boundaries(profile: LocalReviewGovernanceProfile) -> pd.DataFrame:
    data = [
        {"boundary": "Local manual review only", "status": "active"},
        {"boundary": "Offline rehearsal only", "status": "active"}
    ]
    return pd.DataFrame(data)

def build_default_non_approval_boundaries(profile: LocalReviewGovernanceProfile) -> pd.DataFrame:
    data = [
        {"non_approval_boundary": "no official expert sign-off"},
        {"non_approval_boundary": "no legal sign-off"},
        {"non_approval_boundary": "no compliance approval"},
        {"non_approval_boundary": "no production approval"},
        {"non_approval_boundary": "no broker readiness"},
        {"non_approval_boundary": "no live trading approval"},
        {"non_approval_boundary": "no investment advice"},
        {"non_approval_boundary": "no package publish"},
        {"non_approval_boundary": "no deployment"}
    ]
    return pd.DataFrame(data)

def build_manual_approval_boundary_registry(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_approval_boundaries(profile)
    return df, summarize_approval_boundaries(df, pd.DataFrame())

def build_non_approval_boundary_registry(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_non_approval_boundaries(profile)
    return df, summarize_approval_boundaries(pd.DataFrame(), df)

def summarize_approval_boundaries(approval_df: pd.DataFrame, non_approval_df: pd.DataFrame) -> dict:
    return {
        "approval_boundaries": len(approval_df),
        "non_approval_boundaries": len(non_approval_df)
    }
