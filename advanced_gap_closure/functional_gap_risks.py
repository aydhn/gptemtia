import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_default_functional_gap_risks(profile: FunctionalGapClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"risk": "provider abstraction too generic"}, {"risk": "credential leakage"}])

def build_functional_gap_risk_register(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_functional_gap_risks(profile)
    return df, summarize_functional_gap_risks(df)

def summarize_functional_gap_risks(df: pd.DataFrame) -> dict: return {"total": len(df)}
