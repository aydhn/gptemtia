import pandas as pd
from local_simplification.simplification_config import LocalSimplificationProfile

def classify_simplification_risk(row: pd.Series, profile: LocalSimplificationProfile) -> str:
    return "simplification_low_risk"

def build_simplification_risk_summary(gap_df: pd.DataFrame, exception_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "example", "level": "simplification_low_risk"}])
    return df, summarize_simplification_risks(df)

def build_simplification_risk_digest(risk_df: pd.DataFrame, profile: LocalSimplificationProfile) -> tuple[str, dict]:
    return "Risk digest", {}

def summarize_simplification_risks(risk_df: pd.DataFrame) -> dict:
    return {"items": len(risk_df), "warnings": ["Simplification risk yatirim riski degildir."]}
