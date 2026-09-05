import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def classify_final_closeout_risk(row: pd.Series, profile: LocalFinalClosingProfile) -> str:
    if row.get("type") == "no_go_triggered":
        return "final_closeout_critical_risk"
    return "final_closeout_low_risk"

def build_final_closeout_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    risks = []
    if exception_df is not None and not exception_df.empty:
        for _, row in exception_df.iterrows():
            risks.append({"risk_source": "exception", "detail": row.get("detail", ""), "level": classify_final_closeout_risk(row, profile)})
    if gap_df is not None and not gap_df.empty:
        for _, row in gap_df.iterrows():
            risks.append({"risk_source": "gap", "detail": row.get("gap", ""), "level": "final_closeout_medium_risk"})
            
    df = pd.DataFrame(risks)
    return df, summarize_final_closeout_risks(df)

def build_final_closeout_risk_digest(risk_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> tuple[str, dict]:
    return "Risk digest", {"digest_length": 11}

def summarize_final_closeout_risks(risk_df: pd.DataFrame) -> dict:
    if risk_df is None or risk_df.empty:
        return {"total_risks": 0, "critical": 0}
    return {
        "total_risks": len(risk_df),
        "critical": len(risk_df[risk_df["level"] == "final_closeout_critical_risk"])
    }
