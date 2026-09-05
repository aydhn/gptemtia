from pathlib import Path
import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def map_review_governance_evidence_sources(project_root: Path, profile: LocalReviewGovernanceProfile) -> pd.DataFrame:
    data = [
        {"evidence": "docs/ARCHITECTURE.md", "type": "document"},
        {"evidence": "local_review_governance/review_config.py", "type": "code"}
    ]
    return pd.DataFrame(data)

def build_review_governance_evidence_index(project_root: Path, profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = map_review_governance_evidence_sources(project_root, profile)
    return df, summarize_review_governance_evidence(df)

def summarize_review_governance_evidence(df: pd.DataFrame) -> dict:
    return {"total_evidence": len(df)}
