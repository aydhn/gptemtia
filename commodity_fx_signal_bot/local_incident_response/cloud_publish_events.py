import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_cloud_publish_event_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [
        {
            "event_name": "mock_cloud_publish_event",
            "event_category": "event_cloud_publish_request" if not "cloud_publish".endswith("events") else "event_cloud_publish",
            "severity_label": "severity_info",
            "abstract_description": "Mock offline cloud_publish event.",
            "expected_manual_action": "No action.",
            "no_go_boundary": True,
            "evidence_refs": "none",
            "warnings": "Offline mock only."
        }
    ]
    df = pd.DataFrame(data)
    summary = summarize_cloud_publish_events(df)
    return df, summary

def summarize_cloud_publish_events(df: pd.DataFrame) -> Dict:
    return {
        "total_events": len(df) if df is not None else 0,
        "note": "Not a real event registry."
    }
