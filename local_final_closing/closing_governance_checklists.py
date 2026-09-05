import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def build_default_closing_checklist_items(profile: LocalFinalClosingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"item_id": "chk-1", "description": "Check non-production seal", "checked": True}
    ])

def build_closing_governance_final_handoff_checklist(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_closing_checklist_items(profile)
    return df, summarize_closing_governance_checklist(df)

def build_closing_governance_final_non_production_checklist(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_closing_checklist_items(profile)
    return df, summarize_closing_governance_checklist(df)

def build_closing_governance_final_boundary_checklist(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_closing_checklist_items(profile)
    return df, summarize_closing_governance_checklist(df)

def build_closing_governance_final_operator_checklist(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_closing_checklist_items(profile)
    return df, summarize_closing_governance_checklist(df)

def summarize_closing_governance_checklist(df: pd.DataFrame) -> dict:
    return {"total_checked": df["checked"].sum() if not df.empty else 0}
