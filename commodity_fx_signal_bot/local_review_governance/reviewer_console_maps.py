import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_reviewer_console_command_map(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"command": "python -m scripts.run_review_status", "type": "offline"}])
    return df, summarize_reviewer_console_map(df)

def build_reviewer_console_output_map(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"output": "reports/output/local_review_governance", "type": "offline"}])
    return df, summarize_reviewer_console_map(df)

def summarize_reviewer_console_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
