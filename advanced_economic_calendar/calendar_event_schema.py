import pandas as pd
from typing import Tuple, Dict
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile

def build_calendar_event_schema_contract(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field_name": "event_id", "field_type": "str", "required": True, "description": "Unique event identifier"},
        {"field_name": "canonical_event", "field_type": "str", "required": True, "description": "Canonical event name"},
        {"field_name": "scheduled_time", "field_type": "datetime", "required": True, "description": "Time of event"},
        {"field_name": "region", "field_type": "str", "required": True, "description": "Region code"},
        {"field_name": "currency", "field_type": "str", "required": True, "description": "Currency code"},
        {"field_name": "category", "field_type": "str", "required": True, "description": "Event category"},
        {"field_name": "importance", "field_type": "str", "required": True, "description": "Event importance"},
        {"field_name": "mapped_indicator", "field_type": "str", "required": True, "description": "Mapped macro indicator"},
        {"field_name": "provider_name", "field_type": "str", "required": True, "description": "Provider name"},
        {"field_name": "retrieval_mode", "field_type": "str", "required": True, "description": "Retrieval mode"},
        {"field_name": "event_status", "field_type": "str", "required": True, "description": "Status"},
        {"field_name": "manual_review_required", "field_type": "bool", "required": True, "description": "Review flag"}
    ]
    df = pd.DataFrame(schema)
    summary = summarize_calendar_event_schema(df)
    return df, summary

def summarize_calendar_event_schema(df: pd.DataFrame) -> Dict:
    return {
        "total_fields": len(df)
    }
