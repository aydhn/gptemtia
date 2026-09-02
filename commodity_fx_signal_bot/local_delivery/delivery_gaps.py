import pandas as pd
from local_delivery.delivery_config import LocalDeliveryProfile

def detect_missing_delivery_manifest_items(manifest_items_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_handoff_items(index_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_transfer_checklist_items(checklist_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_delivery_evidence(evidence_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_delivery_gap_register(
    manifest_items_df: pd.DataFrame,
    index_df: pd.DataFrame,
    checklist_df: pd.DataFrame,
    evidence_df: pd.DataFrame,
    profile: LocalDeliveryProfile,
) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"gap": "none"}])
    return df, summarize_delivery_gaps(df)

def summarize_delivery_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total_gaps": len(gap_df)}
