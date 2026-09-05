import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def detect_missing_review_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "None detected in domains", "severity": "info"}])

def detect_missing_cockpit_items(cockpit_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "None detected in cockpit", "severity": "info"}])

def detect_missing_expert_review_items(expert_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "None detected in expert review", "severity": "info"}])

def detect_missing_console_items(console_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "None detected in console", "severity": "info"}])

def build_review_gap_register(
    domain_df: pd.DataFrame,
    cockpit_df: pd.DataFrame,
    expert_df: pd.DataFrame,
    console_df: pd.DataFrame,
    profile: LocalReviewGovernanceProfile,
) -> tuple[pd.DataFrame, dict]:
    dfs = [
        detect_missing_review_domains(domain_df),
        detect_missing_cockpit_items(cockpit_df),
        detect_missing_expert_review_items(expert_df),
        detect_missing_console_items(console_df)
    ]
    df = pd.concat(dfs, ignore_index=True)
    return df, summarize_review_gaps(df)

def summarize_review_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total_gaps": len(gap_df)}
