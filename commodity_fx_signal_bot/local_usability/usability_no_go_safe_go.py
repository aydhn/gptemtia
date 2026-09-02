import pandas as pd
from .usability_config import LocalUsabilityProfile

def build_usability_no_go_conditions(profile: LocalUsabilityProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "telemetry/analytics claim", "type": "no-go"}])

def build_usability_safe_go_conditions(profile: LocalUsabilityProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "read-only usability review available", "type": "safe-go"}])

def build_usability_no_go_safe_go_summary(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.concat([build_usability_no_go_conditions(profile), build_usability_safe_go_conditions(profile)], ignore_index=True)
    return df, {"total": len(df)}

def summarize_usability_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"total": len(summary_df)}
