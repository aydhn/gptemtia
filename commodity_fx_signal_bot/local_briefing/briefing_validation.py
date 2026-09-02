import pandas as pd
from .briefing_config import LocalBriefingProfile

def validate_audience_registry(audience_df: pd.DataFrame, profile: LocalBriefingProfile) -> dict:
    if audience_df is None or audience_df.empty:
        return {"valid": False, "reason": "empty"}
    if "audience_id" not in audience_df.columns:
        return {"valid": False, "reason": "missing audience_id"}
    return {"valid": True, "reason": "ok"}

def validate_briefing_sections(section_df: pd.DataFrame, profile: LocalBriefingProfile) -> dict:
    return {"valid": True, "reason": "ok"}

def validate_deck_source(slide_df: pd.DataFrame, profile: LocalBriefingProfile) -> dict:
    if slide_df is None or slide_df.empty:
        return {"valid": False, "reason": "empty"}
    if "slide_id" not in slide_df.columns:
        return {"valid": False, "reason": "missing slide_id"}
    return {"valid": True, "reason": "ok"}

def validate_decision_context(matrix_df: pd.DataFrame, profile: LocalBriefingProfile) -> dict:
    return {"valid": True, "reason": "ok"}

def validate_no_overclaim_or_advice(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    return {"valid": True, "reason": "ok"}

def build_briefing_validation_report(tables: dict[str, pd.DataFrame], profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    results = [
        {"item": "audience", "status": validate_audience_registry(tables.get("audience"), profile)["valid"]},
        {"item": "deck", "status": validate_deck_source(tables.get("deck"), profile)["valid"]}
    ]
    df = pd.DataFrame(results)
    return df, {"total_valid": df["status"].sum()}
