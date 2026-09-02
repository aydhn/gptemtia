import pandas as pd
from .training_config import LocalTrainingProfile

def classify_training_risk(row: pd.Series, profile: LocalTrainingProfile) -> str:
    return "training_medium_risk"

def build_training_risk_summary(gap_df, command_df, policy_df, profile):
    risks = []
    if gap_df is not None and not gap_df.empty:
        risks.append({"risk": "Gaps found", "label": "training_medium_risk"})
    df = pd.DataFrame(risks)
    if df.empty:
        df = pd.DataFrame(columns=["risk", "label"])
    return df, summarize_training_risks(df)

def build_training_risk_digest(risk_df: pd.DataFrame, profile: LocalTrainingProfile) -> tuple[str, dict]:
    return "Risk Digest", {"count": len(risk_df)}

def summarize_training_risks(risk_df: pd.DataFrame) -> dict:
    if risk_df is None or risk_df.empty: return {"count": 0}
    return {"count": len(risk_df)}
