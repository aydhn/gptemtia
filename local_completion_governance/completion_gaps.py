import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def detect_missing_completion_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_closure_items(closure_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_certification_items(certification_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_acceptance_evidence_items(evidence_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_completion_gap_register(
    domain_df: pd.DataFrame,
    closure_df: pd.DataFrame,
    certification_df: pd.DataFrame,
    evidence_df: pd.DataFrame,
    profile: LocalCompletionGovernanceProfile,
) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"gap": "none"}])
    return df, summarize_completion_gaps(df)

def summarize_completion_gaps(gap_df: pd.DataFrame) -> dict:
    return {"gaps": len(gap_df)}\n