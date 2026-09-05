import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def build_default_completion_governance_criteria(profile: LocalCompletionGovernanceProfile) -> pd.DataFrame:
    data = [
        {"criteria": "closure synthesis available", "status": "met"},
        {"criteria": "certification rehearsal available", "status": "met"},
        {"criteria": "project freeze summary available", "status": "met"},
        {"criteria": "acceptance evidence pack available", "status": "met"},
        {"criteria": "completion binder available", "status": "met"},
        {"criteria": "no official certification", "status": "met"},
        {"criteria": "no official acceptance", "status": "met"},
        {"criteria": "no legal/compliance approval", "status": "met"},
        {"criteria": "no production approval", "status": "met"},
        {"criteria": "no live/broker/advice", "status": "met"},
        {"criteria": "manual review required", "status": "met"}
    ]
    return pd.DataFrame(data)

def build_completion_governance_criteria_matrix(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_completion_governance_criteria(profile)
    return df, summarize_completion_governance_criteria(df)

def build_completion_governance_final_readiness_matrix(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_completion_governance_criteria(profile)
    return df, summarize_completion_governance_criteria(df)

def summarize_completion_governance_criteria(df: pd.DataFrame) -> dict:
    return {"total_criteria": len(df)}\n