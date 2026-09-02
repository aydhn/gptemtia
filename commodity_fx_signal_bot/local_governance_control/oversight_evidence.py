import pandas as pd
from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile

def map_oversight_evidence_sources(project_root: Path, profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"evidence_name": "Test Reports", "source_path": "reports/output/tests", "is_audit_proof": False}
    ]
    return pd.DataFrame(data)

def build_oversight_evidence_index(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = map_oversight_evidence_sources(project_root, profile)
    return df, summarize_oversight_evidence(df)

def summarize_oversight_evidence(evidence_df: pd.DataFrame) -> dict:
    if evidence_df is None or evidence_df.empty:
        return {"total": 0}
    return {"total": len(evidence_df)}
