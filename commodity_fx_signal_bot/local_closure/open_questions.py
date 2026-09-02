
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_open_questions(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"question": "How to scale offline?", "status": "open"}
    ])

def build_closure_open_questions_register(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_open_questions(profile)
    summary = summarize_open_questions(df)
    return df, summary

def summarize_open_questions(question_df: pd.DataFrame) -> dict:
    return {"total": len(question_df)}
