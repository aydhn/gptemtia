import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_external_llm_api_event_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [
        {
            "event_name": "mock_external_llm_api_event",
            "event_category": "event_external_llm_api_request" if not "external_llm_api".endswith("events") else "event_external_llm_api",
            "severity_label": "severity_info",
            "abstract_description": "Mock offline external_llm_api event.",
            "expected_manual_action": "No action.",
            "no_go_boundary": True,
            "evidence_refs": "none",
            "warnings": "Offline mock only."
        }
    ]
    df = pd.DataFrame(data)
    summary = summarize_external_llm_api_events(df)
    return df, summary

def summarize_external_llm_api_events(df: pd.DataFrame) -> Dict:
    return {
        "total_events": len(df) if df is not None else 0,
        "note": "Not a real event registry."
    }
