import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def detect_acceptance_exceptions(checklist_df: pd.DataFrame, evidence_df: pd.DataFrame) -> pd.DataFrame:
    # return empty for now
    return pd.DataFrame(columns=["exception_id", "description", "risk"])

def build_acceptance_exception_register(checklist_df: pd.DataFrame, evidence_df: pd.DataFrame, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_acceptance_exceptions(checklist_df, evidence_df)
    return df, summarize_acceptance_exceptions(df)

def summarize_acceptance_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total_exceptions": len(exception_df)}
