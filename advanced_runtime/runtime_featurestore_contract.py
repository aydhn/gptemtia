import pandas as pd
from .runtime_config import AdvancedRuntimeProfile

def build_runtime_featurestore_contract(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    contracts = [
        "load advanced continuation outputs",
        "load advanced runtime outputs",
        "future normalized data access",
        "future feature matrix access",
        "future regime labels access",
        "future ML model input access",
        "future backtest result access",
        "future portfolio result access"
    ]
    data = [{"contract_name": c, "safe": True} for c in contracts]
    df = pd.DataFrame(data)
    return df, summarize_runtime_featurestore_contract(df)

def summarize_runtime_featurestore_contract(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total_contracts": len(df)}
