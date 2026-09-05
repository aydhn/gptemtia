import pandas as pd
from .completion_config import LocalProjectCompletionProfile

def build_default_final_risks(profile: LocalProjectCompletionProfile) -> pd.DataFrame:
    return pd.DataFrame([{"risk": "Model divergence offline", "type": "completion_info"}])

def build_project_completion_final_risk_register(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_final_risks(profile)
    return df, summarize_final_risk_register(df)

def summarize_final_risk_register(df: pd.DataFrame) -> dict:
    return {"risks": len(df), "note": "Final risk is not an investment risk."}
