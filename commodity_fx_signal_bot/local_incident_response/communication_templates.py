import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_communication_templates(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"template_name": "Internal Update", "body": "Mock body."}]
    return pd.DataFrame(data)

def build_communication_template_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_communication_templates(profile)
    summary = summarize_communication_templates(df)
    return df, summary

def summarize_communication_templates(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not an official communication."
    }
