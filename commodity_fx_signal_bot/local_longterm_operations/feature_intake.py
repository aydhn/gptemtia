"""Feature intake."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_feature_intake_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"item": "live/broker/advice/deploy enablement no-go", "warnings": ["live/broker/advice/deploy enablement no-go içerir"]}
    ])

def build_v1x_feature_intake_checklist(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_feature_intake_items(profile)
    return df, summarize_feature_intake(df)

def summarize_feature_intake(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
