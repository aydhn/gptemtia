import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_containment_items(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"containment_step": "Isolate", "description": "Mock isolation."}]
    return pd.DataFrame(data)

def build_containment_rehearsal_checklist(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_containment_items(profile)
    summary = summarize_containment_rehearsal(df)
    return df, summary

def summarize_containment_rehearsal(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not a real containment action."
    }
