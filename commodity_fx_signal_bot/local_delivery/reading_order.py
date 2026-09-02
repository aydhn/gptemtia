import pandas as pd
from local_delivery.delivery_config import LocalDeliveryProfile

def build_default_reading_order(profile: LocalDeliveryProfile) -> pd.DataFrame:
    order = [
        "README", "SAFE_USAGE_GUIDE", "PROJECT_COMPLETION_DOSSIER",
        "FINAL_SAFETY_BOUNDARY_BINDER", "INDEPENDENT_REVIEWER_PACK",
        "FINAL_VERIFICATION_EVIDENCE_BINDER", "RC_DRY_RUN_FREEZE_MANIFEST",
        "FINAL_OPERATOR_NAVIGATION_GUIDE", "reports/output status/quality reports",
        "DataLake indexes"
    ]
    return pd.DataFrame([{"step": i+1, "item": item} for i, item in enumerate(order)])

def build_delivery_package_reading_order(profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reading_order(profile)
    return df, summarize_delivery_reading_order(df)

def summarize_delivery_reading_order(order_df: pd.DataFrame) -> dict:
    return {"total_steps": len(order_df)}
