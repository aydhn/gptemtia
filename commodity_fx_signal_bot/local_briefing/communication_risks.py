import pandas as pd
from .briefing_config import LocalBriefingProfile

def classify_communication_risk(row: pd.Series, profile: LocalBriefingProfile) -> str:
    return "communication_medium_risk"

def build_communication_risk_summary(gap_df: pd.DataFrame, section_df: pd.DataFrame, template_df: pd.DataFrame, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    risks = []
    if gap_df is not None and not gap_df.empty:
        for _, row in gap_df.iterrows():
            risks.append({"risk": f"Gap found: {row['gap']}", "level": "communication_medium_risk"})
            
    df = pd.DataFrame(risks, columns=["risk", "level"])
    return df, summarize_communication_risks(df)

def build_communication_risk_digest(risk_df: pd.DataFrame, profile: LocalBriefingProfile) -> tuple[str, dict]:
    text = "Risk Digest:\n"
    if risk_df is not None and not risk_df.empty:
        for _, row in risk_df.iterrows():
            text += f"- {row['risk']} ({row['level']})\n"
    return text, {"length": len(text)}

def summarize_communication_risks(risk_df: pd.DataFrame) -> dict:
    if risk_df is None or risk_df.empty:
        return {"total_risks": 0}
    return {"total_risks": len(risk_df)}
