
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_decision_log(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"decision": "Use markdown for reports", "reason": "readable"}])

def build_closure_decision_log(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_decision_log(profile)
    summary = summarize_decision_log(df)
    return df, summary

def summarize_decision_log(decision_df: pd.DataFrame) -> dict:
    return {"total": len(decision_df)}
