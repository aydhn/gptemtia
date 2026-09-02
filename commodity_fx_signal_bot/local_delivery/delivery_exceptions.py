import pandas as pd
from local_delivery.delivery_config import LocalDeliveryProfile

def detect_delivery_exceptions(checklist_df: pd.DataFrame, index_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "none"}])

def build_delivery_exception_register(checklist_df: pd.DataFrame, index_df: pd.DataFrame, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_delivery_exceptions(checklist_df, index_df)
    return df, summarize_delivery_exceptions(df)

def summarize_delivery_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total_exceptions": len(exception_df)}
