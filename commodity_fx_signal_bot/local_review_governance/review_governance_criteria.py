import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_default_review_governance_criteria(profile: LocalReviewGovernanceProfile) -> pd.DataFrame:
    data = [
        {"criteria": "human-review cockpit available", "met": True},
        {"criteria": "manual approval ledger rehearsal available", "met": True},
        {"criteria": "approval boundaries documented", "met": True},
        {"criteria": "expert review workbook available", "met": True},
        {"criteria": "reviewer console packet available", "met": True},
        {"criteria": "issue/unresolved register available", "met": True},
        {"criteria": "no legal/compliance/production approval claim", "met": True},
        {"criteria": "no broker/live/advice claim", "met": True},
        {"criteria": "no publish/deploy claim", "met": True},
        {"criteria": "manual review required", "met": True}
    ]
    return pd.DataFrame(data)

def build_review_governance_criteria_matrix(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_review_governance_criteria(profile)
    return df, summarize_review_governance_criteria(df)

def summarize_review_governance_criteria(df: pd.DataFrame) -> dict:
    return {"total_criteria": len(df)}
