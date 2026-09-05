import pandas as pd
def build_continuity_exception_register(memory_df, lessons_df, no_go_df, profile) -> tuple[pd.DataFrame, dict]:
    df = detect_continuity_exceptions(memory_df, lessons_df, no_go_df)
    return df, summarize_continuity_exceptions(df)
def detect_continuity_exceptions(memory_df, lessons_df, no_go_df) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "e1"}])
def summarize_continuity_exceptions(df: pd.DataFrame) -> dict:
    return {"total": len(df)}