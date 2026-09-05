import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_review_governance_no_go_conditions(profile: LocalReviewGovernanceProfile) -> pd.DataFrame:
    data = [
        {"condition": "real approval workflow claim", "type": "no-go"},
        {"condition": "e-signature claim", "type": "no-go"},
        {"condition": "official expert sign-off claim", "type": "no-go"},
        {"condition": "legal/compliance approval claim", "type": "no-go"},
        {"condition": "production approval claim", "type": "no-go"},
        {"condition": "official acceptance claim", "type": "no-go"},
        {"condition": "broker readiness claim", "type": "no-go"},
        {"condition": "live trading approval claim", "type": "no-go"},
        {"condition": "investment advice wording", "type": "no-go"},
        {"condition": "package publish claim", "type": "no-go"},
        {"condition": "docker build/push claim", "type": "no-go"},
        {"condition": "git tag claim", "type": "no-go"},
        {"condition": "cloud upload claim", "type": "no-go"},
        {"condition": "deployment claim", "type": "no-go"},
        {"condition": "model deployment claim", "type": "no-go"},
        {"condition": "telemetry/dashboard claim", "type": "no-go"},
        {"condition": "external LLM/API claim", "type": "no-go"},
        {"condition": "vector/embedding claim", "type": "no-go"},
        {"condition": "raw secret output", "type": "no-go"},
        {"condition": "file deletion/move/overwrite claim", "type": "no-go"}
    ]
    return pd.DataFrame(data)

def build_review_governance_safe_go_conditions(profile: LocalReviewGovernanceProfile) -> pd.DataFrame:
    data = [
        {"condition": "human-review cockpit documented", "type": "safe-go"},
        {"condition": "manual approval ledger rehearsal documented", "type": "safe-go"},
        {"condition": "expert review workbook documented", "type": "safe-go"},
        {"condition": "reviewer console packet documented", "type": "safe-go"},
        {"condition": "criteria/evidence index available", "type": "safe-go"},
        {"condition": "issue/unresolved register available", "type": "safe-go"},
        {"condition": "non-goals documented", "type": "safe-go"},
        {"condition": "manual review required", "type": "safe-go"},
        {"condition": "no real approval/signoff/legal/compliance/production/live/broker/advice/deploy", "type": "safe-go"}
    ]
    return pd.DataFrame(data)

def build_review_governance_no_go_safe_go_summary(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_review_governance_no_go_conditions(profile)
    safe_go = build_review_governance_safe_go_conditions(profile)
    summary_df = pd.concat([no_go, safe_go], ignore_index=True)
    return summary_df, summarize_review_no_go_safe_go(summary_df)

def summarize_review_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"total_conditions": len(summary_df)}
