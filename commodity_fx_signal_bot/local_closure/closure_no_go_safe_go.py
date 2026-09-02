
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_closure_no_go_conditions(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "Live trading claim", "type": "no_go"},
        {"condition": "Production release claim", "type": "no_go"}
    ])

def build_closure_safe_go_conditions(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "Offline closure documented", "type": "safe_go"}
    ])

def build_closure_no_go_safe_go_summary(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df1 = build_closure_no_go_conditions(profile)
    df2 = build_closure_safe_go_conditions(profile)
    df = pd.concat([df1, df2], ignore_index=True)
    summary = summarize_closure_no_go_safe_go(df)
    return df, summary

def summarize_closure_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"total": len(summary_df)}
