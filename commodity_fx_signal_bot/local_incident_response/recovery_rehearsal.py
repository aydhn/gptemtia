import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_recovery_items(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"recovery_step": "Restore", "description": "Mock restore."}]
    return pd.DataFrame(data)

def build_recovery_rehearsal_checklist(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_recovery_items(profile)
    summary = summarize_recovery_rehearsal(df)
    return df, summary

def summarize_recovery_rehearsal(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not a real recovery action."
    }
