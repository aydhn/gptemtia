import pandas as pd
from .completion_config import LocalProjectCompletionProfile

def classify_completion_risk(row: pd.Series, profile: LocalProjectCompletionProfile) -> str:
    return "completion_info"

def build_completion_risk_digest(risk_df: pd.DataFrame, profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    return "Digest", {"note": "Digest generated."}

def build_completion_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk": "mock_risk"}])
    return df, summarize_completion_risks(df)

def summarize_completion_risks(risk_df: pd.DataFrame) -> dict:
    return {"risks": len(risk_df), "note": "Completion risk yatırım riski değildir."}
