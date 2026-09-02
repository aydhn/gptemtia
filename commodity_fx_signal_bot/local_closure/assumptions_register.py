
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_assumptions(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"assumption": "Offline data is sufficient", "status": "valid"}])

def build_closure_assumptions_register(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_assumptions(profile)
    summary = summarize_assumptions(df)
    return df, summary

def summarize_assumptions(assumption_df: pd.DataFrame) -> dict:
    return {"total": len(assumption_df)}
