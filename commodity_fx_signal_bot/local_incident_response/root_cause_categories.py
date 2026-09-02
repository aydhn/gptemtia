import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_root_cause_categories(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"category": "Configuration Error", "description": "Mock category."}]
    return pd.DataFrame(data)

def build_root_cause_category_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_root_cause_categories(profile)
    summary = summarize_root_cause_categories(df)
    return df, summary

def summarize_root_cause_categories(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not forensic analysis."
    }
