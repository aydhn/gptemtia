import pandas as pd
from typing import Tuple, Dict, List
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_models import SafetyEvent, build_safety_event_id, safety_event_to_dict

def build_default_safety_events(profile: LocalIncidentResponseProfile) -> List[SafetyEvent]:
    categories = [
        "event_boundary_breach", "event_unsafe_output", "event_forbidden_capability_request",
        "event_secret_exposure", "event_file_action_request", "event_cloud_publish_request",
        "event_live_trading_broker_request", "event_investment_advice_request",
        "event_model_deployment_request", "event_external_llm_api_request"
    ]
    events = []
    for cat in categories:
        events.append(SafetyEvent(
            event_id=build_safety_event_id(cat, cat),
            event_name=cat,
            event_category=cat,
            severity_label="severity_medium",
            abstract_description="Mock safety event.",
            expected_manual_action="Review offline.",
            evidence_refs=[],
            manual_review_required=True,
            warnings=["Offline validation only."]
        ))
    return events

def build_safety_event_register(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    events = build_default_safety_events(profile)
    df = pd.DataFrame([safety_event_to_dict(e) for e in events])
    summary = summarize_safety_event_register(df)
    return df, summary

def summarize_safety_event_register(event_df: pd.DataFrame) -> Dict:
    return {
        "total_events": len(event_df) if event_df is not None else 0,
        "note": "This is a local safety register, not a real incident record."
    }
