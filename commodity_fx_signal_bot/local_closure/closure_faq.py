
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_closure_faq(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"question": "Bu gerçek v1.0 release mi?", "answer": "Hayır."},
        {"question": "Bu resmi proje kapanışı mı?", "answer": "Hayır."}
    ])

def build_closure_faq(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_closure_faq(profile)
    summary = summarize_closure_faq(df)
    return df, summary

def summarize_closure_faq(faq_df: pd.DataFrame) -> dict:
    return {"total": len(faq_df)}
