import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_unsafe_output_event_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [
        {
            "event_name": "mock_unsafe_output_event",
            "event_category": "event_unsafe_output_request" if not "unsafe_output".endswith("events") else "event_unsafe_output",
            "severity_label": "severity_info",
            "abstract_description": "Mock offline unsafe_output event.",
            "expected_manual_action": "No action.",
            "no_go_boundary": True,
            "evidence_refs": "none",
            "warnings": "Offline mock only."
        }
    ]
    df = pd.DataFrame(data)
    summary = summarize_unsafe_output_events(df)
    return df, summary

def summarize_unsafe_output_events(df: pd.DataFrame) -> Dict:
    return {
        "total_events": len(df) if df is not None else 0,
        "note": "Not a real event registry."
    }
