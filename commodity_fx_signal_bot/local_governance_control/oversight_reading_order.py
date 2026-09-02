import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_oversight_reading_order(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"order": 1, "document": "FINAL_LOCAL_GOVERNANCE_CONTROL_ROOM_PACKET.md"},
        {"order": 2, "document": "EXECUTIVE_OVERSIGHT_PACKET.md"}
    ]
    return pd.DataFrame(data)

def build_oversight_report_reading_order(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_oversight_reading_order(profile)
    return df, summarize_oversight_reading_order(df)

def summarize_oversight_reading_order(order_df: pd.DataFrame) -> dict:
    if order_df is None or order_df.empty:
        return {"total": 0}
    return {"total": len(order_df)}
