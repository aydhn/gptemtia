import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_incident_timeline_templates(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"template": "Basic Timeline", "description": "Mock timeline."}]
    return pd.DataFrame(data)

def build_incident_timeline_template_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_incident_timeline_templates(profile)
    summary = summarize_incident_timeline_templates(df)
    return df, summary

def summarize_incident_timeline_templates(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not a real incident timeline."
    }
