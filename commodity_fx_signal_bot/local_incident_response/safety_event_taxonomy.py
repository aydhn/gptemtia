import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_labels import list_safety_event_category_labels

def build_default_safety_event_taxonomy(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    labels = list_safety_event_category_labels()
    data = [{"category": lbl, "description": "Offline taxonomy label"} for lbl in labels]
    return pd.DataFrame(data)

def build_safety_event_taxonomy(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_safety_event_taxonomy(profile)
    summary = summarize_safety_event_taxonomy(df)
    return df, summary

def summarize_safety_event_taxonomy(df: pd.DataFrame) -> Dict:
    return {
        "total_categories": len(df) if df is not None else 0,
        "note": "Offline safety taxonomy."
    }
