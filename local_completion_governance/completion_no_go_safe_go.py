import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def build_completion_governance_no_go_conditions(profile: LocalCompletionGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "real certification claim", "status": "avoided"}])

def build_completion_governance_safe_go_conditions(profile: LocalCompletionGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "closure synthesis documented", "status": "met"}])

def build_completion_governance_no_go_safe_go_summary(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"summary": "safe-go"}])
    return df, summarize_completion_no_go_safe_go(df)

def summarize_completion_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"status": "generated"}\n