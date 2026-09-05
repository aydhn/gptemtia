import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import CalendarProviderError, build_calendar_provider_error_id, to_dict

def build_calendar_provider_error_schema(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field_name": "error_id", "field_type": "str", "required": True},
        {"field_name": "provider_name", "field_type": "str", "required": True},
        {"field_name": "error_type", "field_type": "str", "required": True},
        {"field_name": "message", "field_type": "str", "required": True},
        {"field_name": "retryable", "field_type": "bool", "required": True},
        {"field_name": "blocked_by_safety", "field_type": "bool", "required": True},
        {"field_name": "recommendation", "field_type": "str", "required": True}
    ]
    df = pd.DataFrame(schema)
    return df, summarize_calendar_provider_errors(df)

def create_calendar_provider_error(
    provider_name: str, 
    error_type: str, 
    message: str, 
    retryable: bool = False, 
    blocked_by_safety: bool = False, 
    recommendation: str = ""
) -> CalendarProviderError:
    return CalendarProviderError(
        error_id=build_calendar_provider_error_id(provider_name, error_type),
        provider_name=provider_name,
        error_type=error_type,
        message=message,
        retryable=retryable,
        blocked_by_safety=blocked_by_safety,
        recommendation=recommendation
    )

def calendar_provider_error_to_dict(error: CalendarProviderError) -> Dict:
    return to_dict(error)

def summarize_calendar_provider_errors(df: pd.DataFrame) -> Dict:
    return {
        "total_fields": len(df)
    }
