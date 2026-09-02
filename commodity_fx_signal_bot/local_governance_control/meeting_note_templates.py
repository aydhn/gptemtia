import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_meeting_note_templates(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    types = [
        "weekly review note",
        "quality warning review note",
        "no-go/safe-go review note",
        "risk committee rehearsal note",
        "executive oversight note",
        "operator supervision note",
        "unresolved decision note",
        "exception escalation note"
    ]
    data = [{"template_type": t, "content": f"Template for {t}", "disclaimer": "Resmi meeting minute değildir."} for t in types]
    return pd.DataFrame(data)

def build_governance_meeting_note_template_library(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_meeting_note_templates(profile)
    return df, summarize_meeting_note_templates(df)

def summarize_meeting_note_templates(template_df: pd.DataFrame) -> dict:
    if template_df is None or template_df.empty:
        return {"total": 0}
    return {"total": len(template_df)}
