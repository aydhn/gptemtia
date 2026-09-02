import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_live_trading_broker_event_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [
        {
            "event_name": "mock_live_trading_broker_event",
            "event_category": "event_live_trading_broker_request" if not "live_trading_broker".endswith("events") else "event_live_trading_broker",
            "severity_label": "severity_info",
            "abstract_description": "Mock offline live_trading_broker event.",
            "expected_manual_action": "No action.",
            "no_go_boundary": True,
            "evidence_refs": "none",
            "warnings": "Offline mock only."
        }
    ]
    df = pd.DataFrame(data)
    summary = summarize_live_trading_broker_events(df)
    return df, summary

def summarize_live_trading_broker_events(df: pd.DataFrame) -> Dict:
    return {
        "total_events": len(df) if df is not None else 0,
        "note": "Not a real event registry."
    }
