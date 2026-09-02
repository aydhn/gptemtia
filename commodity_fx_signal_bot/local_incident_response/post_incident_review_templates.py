import pandas as pd
from typing import Tuple, Dict, List
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_models import PostIncidentTemplate, build_post_incident_template_id, post_incident_template_to_dict

def build_default_post_incident_review_templates(profile: LocalIncidentResponseProfile) -> List[PostIncidentTemplate]:
    templates = [
        PostIncidentTemplate(
            template_id=build_post_incident_template_id("Standard PIR"),
            template_name="Standard PIR",
            template_area="General",
            sections=["Summary", "Timeline", "Root Cause"],
            disclaimer="Not an official incident report.",
            warnings=["Offline review only."]
        )
    ]
    return templates

def build_post_incident_review_template_library(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    templates = build_default_post_incident_review_templates(profile)
    df = pd.DataFrame([post_incident_template_to_dict(t) for t in templates])
    summary = summarize_post_incident_review_templates(df)
    return df, summary

def summarize_post_incident_review_templates(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df) if df is not None else 0,
        "note": "Not an official incident report."
    }
