
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_known_limitations(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"limitation": "No live market data", "impact": "offline only"}])

def build_closure_known_limitations_register(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_known_limitations(profile)
    summary = summarize_known_limitations(df)
    return df, summary

def summarize_known_limitations(limit_df: pd.DataFrame) -> dict:
    return {"total": len(limit_df)}
