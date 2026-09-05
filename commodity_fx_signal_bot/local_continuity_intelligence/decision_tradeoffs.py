import pandas as pd
def build_decision_tradeoff_matrix(profile) -> tuple[pd.DataFrame, dict]:
    df = build_default_tradeoff_items(profile)
    return df, summarize_decision_tradeoffs(df)
def build_default_tradeoff_items(profile) -> pd.DataFrame:
    return pd.DataFrame([{"tradeoff": "t1"}])
def summarize_decision_tradeoffs(df: pd.DataFrame) -> dict:
    return {"total": len(df)}