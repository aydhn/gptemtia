import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_redteam_no_go_conditions(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "real attack claim", "type": "no-go"}])

def build_redteam_safe_go_conditions(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "abstract misuse scenarios documented", "type": "safe-go"}])

def build_redteam_no_go_safe_go_summary(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_redteam_no_go_conditions(profile)
    safe_go = build_redteam_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], ignore_index=True)
    return df, summarize_redteam_no_go_safe_go(df)

def summarize_redteam_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"total": len(summary_df), "note": "Safe-go is not real safety approval."}
