import pandas as pd
def build_operator_memory_quick_reference_cards(profile) -> tuple[pd.DataFrame, dict]:
    df = build_default_quick_reference_cards(profile)
    return df, summarize_operator_memory_cards(df)
def build_default_quick_reference_cards(profile) -> pd.DataFrame:
    return pd.DataFrame([{"what it is": "a", "what it is not": "b", "where to read": "c", "safe command family": "d", "unsafe command family": "e", "manual review note": "f"}])
def summarize_operator_memory_cards(df: pd.DataFrame) -> dict:
    return {"total": len(df)}