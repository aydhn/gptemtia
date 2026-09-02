import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_incident_triage_items(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [
        {"triage_step": "Step 1", "description": "Offline verification."},
        {"triage_step": "Step 2", "description": "Mock triage."}
    ]
    return pd.DataFrame(data)

def build_incident_triage_checklist(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_incident_triage_items(profile)
    summary = summarize_incident_triage_checklist(df)
    return df, summary

def summarize_incident_triage_checklist(df: pd.DataFrame) -> Dict:
    return {
        "total_triage_steps": len(df) if df is not None else 0,
        "note": "Not a real incident triage."
    }
