import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_incident_classification_items(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [
        {"class_name": "Class A", "criteria": "Mock criteria."},
        {"class_name": "Class B", "criteria": "Mock criteria 2."}
    ]
    return pd.DataFrame(data)

def build_incident_classification_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_incident_classification_items(profile)
    summary = summarize_incident_classification_registry(df)
    return df, summary

def summarize_incident_classification_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_classes": len(df) if df is not None else 0,
        "note": "Not a compliance classification."
    }
