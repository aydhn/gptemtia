"""generated_docs_review_workbook.py"""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_longterm_generated_docs_review_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"item": "sample", "status": "needs_review", "warnings": ["Generated docs review."]}
    ])

def build_longterm_generated_docs_review_workbook(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_longterm_generated_docs_review_items(profile)
    return df, summarize_longterm_generated_docs_review_workbook(df)

def summarize_longterm_generated_docs_review_workbook(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
