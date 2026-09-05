import pandas as pd
def build_continuity_glossary(profile) -> tuple[pd.DataFrame, dict]:
    df = build_default_glossary_terms(profile)
    return df, summarize_continuity_glossary(df)
def build_default_glossary_terms(profile) -> pd.DataFrame:
    return pd.DataFrame([{"term": "t1", "desc": "d1"}])
def summarize_continuity_glossary(df: pd.DataFrame) -> dict:
    return {"total": len(df)}