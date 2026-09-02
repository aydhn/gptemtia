import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def build_verification_rehearsal_steps(profile: LocalAcceptanceProfile) -> pd.DataFrame:
    steps = [
        {"step": "review scope", "action": "check README", "status": "planned"},
        {"step": "review traces", "action": "check trace matrix", "status": "planned"}
    ]
    return pd.DataFrame(steps)

def build_final_verification_rehearsal_plan(project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_verification_rehearsal_steps(profile)
    return df, summarize_verification_rehearsal_plan(df)

def summarize_verification_rehearsal_plan(plan_df: pd.DataFrame) -> dict:
    return {"total_steps": len(plan_df)}
