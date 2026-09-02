import pandas as pd
from local_simplification.simplification_config import LocalSimplificationProfile

def build_simplification_no_go_conditions(profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "auto-refactor claim", "type": "no-go"}])

def build_simplification_safe_go_conditions(profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "read-only complexity map available", "type": "safe-go"}])

def build_complexity_no_go_safe_go_summary(profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.concat([build_simplification_no_go_conditions(profile), build_simplification_safe_go_conditions(profile)])
    return df, summarize_complexity_no_go_safe_go(df)

def summarize_complexity_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"items": len(summary_df), "warnings": ["Safe-go gercek refactor izni degildir."]}
