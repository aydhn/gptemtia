import pandas as pd
def build_continuity_concept_index(profile) -> tuple[pd.DataFrame, dict]:
    df = build_default_continuity_concepts(profile)
    return df, summarize_continuity_concepts(df)
def build_default_continuity_concepts(profile) -> pd.DataFrame:
    return pd.DataFrame([{"concept": "c1", "def": "d1"}])
def summarize_continuity_concepts(df: pd.DataFrame) -> dict:
    return {"total": len(df)}