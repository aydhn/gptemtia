import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_labels import list_severity_labels

def build_default_incident_severity_taxonomy(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    labels = list_severity_labels()
    data = [{"severity_label": lbl, "description": "Offline severity."} for lbl in labels]
    return pd.DataFrame(data)

def classify_incident_severity(event_category: str, profile: LocalIncidentResponseProfile) -> str:
    return "severity_medium"

def build_incident_severity_taxonomy(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_incident_severity_taxonomy(profile)
    summary = summarize_incident_severity_taxonomy(df)
    return df, summary

def summarize_incident_severity_taxonomy(df: pd.DataFrame) -> Dict:
    return {
        "total_severities": len(df) if df is not None else 0,
        "note": "Offline severity taxonomy, not real production severity."
    }
