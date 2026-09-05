import pandas as pd
from typing import Tuple, Dict
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile

def build_release_event_schema_contract(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field_name": "release_id", "field_type": "str", "required": True, "description": "Unique release identifier"},
        {"field_name": "canonical_event", "field_type": "str", "required": True, "description": "Canonical event name"},
        {"field_name": "scheduled_time", "field_type": "datetime", "required": True, "description": "Time of event"},
        {"field_name": "actual_release_time", "field_type": "datetime", "required": False, "description": "Actual time of release"},
        {"field_name": "period_reference", "field_type": "str", "required": True, "description": "Reference period"},
        {"field_name": "actual", "field_type": "float", "required": False, "description": "Actual value"},
        {"field_name": "forecast", "field_type": "float", "required": False, "description": "Forecast value"},
        {"field_name": "previous", "field_type": "float", "required": False, "description": "Previous value"},
        {"field_name": "revised_previous", "field_type": "float", "required": False, "description": "Revised previous value"},
        {"field_name": "surprise_value", "field_type": "float", "required": False, "description": "Surprise value"},
        {"field_name": "surprise_direction", "field_type": "str", "required": False, "description": "Surprise direction"},
        {"field_name": "revision_status", "field_type": "str", "required": True, "description": "Revision status"},
        {"field_name": "provider_name", "field_type": "str", "required": True, "description": "Provider name"},
        {"field_name": "retrieval_mode", "field_type": "str", "required": True, "description": "Retrieval mode"},
        {"field_name": "data_quality_status", "field_type": "str", "required": True, "description": "Data quality status"},
        {"field_name": "manual_review_required", "field_type": "bool", "required": True, "description": "Review flag"}
    ]
    df = pd.DataFrame(schema)
    summary = summarize_release_event_schema(df)
    return df, summary

def summarize_release_event_schema(df: pd.DataFrame) -> Dict:
    return {
        "total_fields": len(df)
    }
