import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_template_for_audience(audience_label: str, profile: LocalBriefingProfile) -> dict:
    base_template = "This is an offline project update.\nNo investment advice. Requires manual review."
    return {
        "audience": audience_label,
        "template": f"{audience_label} Update:\n{base_template}"
    }

def build_stakeholder_update_templates(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    audiences = [
        "executive", "business stakeholder", "analyst",
        "operator handover", "developer handover", "compliance review", "nontechnical overview"
    ]
    templates = [build_template_for_audience(a, profile) for a in audiences]
    df = pd.DataFrame(templates)
    return df, summarize_stakeholder_templates(df)

def summarize_stakeholder_templates(template_df: pd.DataFrame) -> dict:
    if template_df is None or template_df.empty:
        return {"total_templates": 0}
    return {"total_templates": len(template_df)}
