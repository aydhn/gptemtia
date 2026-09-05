import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_expert_review_checklist_registry(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"checklist": "Expert Checklist 1", "status": "rehearsal"}])
    return df, summarize_expert_review_map(df)

def build_expert_review_evidence_map(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"evidence": "docs/ARCHITECTURE.md", "mapped": True}])
    return df, summarize_expert_review_map(df)

def build_expert_review_role_matrix(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"role": "reviewer_external_expert_rehearsal", "access": "read-only"}])
    return df, summarize_expert_review_map(df)

def build_expert_review_reading_order(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"order": 1, "doc": "Cockpit Index"}])
    return df, summarize_expert_review_map(df)

def summarize_expert_review_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
