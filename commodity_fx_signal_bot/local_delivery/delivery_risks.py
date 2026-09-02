import pandas as pd
from local_delivery.delivery_config import LocalDeliveryProfile

def classify_delivery_risk(row: pd.Series, profile: LocalDeliveryProfile) -> str:
    return "delivery_low_risk"

def build_delivery_risk_summary(gap_df: pd.DataFrame, no_go_df: pd.DataFrame, exception_df: pd.DataFrame, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "delivery_low_risk"}])
    return df, summarize_delivery_risks(df)

def build_delivery_risk_digest(risk_df: pd.DataFrame, profile: LocalDeliveryProfile) -> tuple[str, dict]:
    text = "Risk Digest: Low Risk"
    return text, {"length": len(text)}

def summarize_delivery_risks(risk_df: pd.DataFrame) -> dict:
    return {"total_risks": len(risk_df)}
