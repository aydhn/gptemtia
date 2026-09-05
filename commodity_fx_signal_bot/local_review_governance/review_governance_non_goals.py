import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_default_review_non_goals(profile: LocalReviewGovernanceProfile) -> pd.DataFrame:
    data = [
        {"non_goal": "no real approval workflow"},
        {"non_goal": "no e-signature"},
        {"non_goal": "no expert sign-off"},
        {"non_goal": "no legal sign-off"},
        {"non_goal": "no compliance approval"},
        {"non_goal": "no production approval"},
        {"non_goal": "no broker readiness"},
        {"non_goal": "no live trading approval"},
        {"non_goal": "no investment advice"},
        {"non_goal": "no publish/deploy"}
    ]
    return pd.DataFrame(data)

def build_review_governance_non_goals_registry(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_review_non_goals(profile)
    return df, summarize_review_governance_non_goals(df)

def summarize_review_governance_non_goals(df: pd.DataFrame) -> dict:
    return {"total_non_goals": len(df)}
