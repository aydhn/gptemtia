import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_incident_reading_order(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"order": 1, "document": "Rehearsal Packet"}]
    return pd.DataFrame(data)

def build_incident_reading_order(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_incident_reading_order(profile)
    summary = summarize_incident_reading_order(df)
    return df, summary

def summarize_incident_reading_order(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not an official procedure."
    }
