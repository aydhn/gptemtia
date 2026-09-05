import pandas as pd
from typing import Tuple, Dict, List, Optional
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import CalendarProviderRequest, build_calendar_provider_request_id, to_dict

def build_calendar_provider_request_schema(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field_name": "request_id", "field_type": "str", "required": True},
        {"field_name": "provider_name", "field_type": "str", "required": True},
        {"field_name": "data_type", "field_type": "str", "required": True},
        {"field_name": "events", "field_type": "List[str]", "required": True},
        {"field_name": "region", "field_type": "Optional[str]", "required": False},
        {"field_name": "start", "field_type": "Optional[str]", "required": False},
        {"field_name": "end", "field_type": "Optional[str]", "required": False},
        {"field_name": "dry_run", "field_type": "bool", "required": True},
        {"field_name": "local_only", "field_type": "bool", "required": True},
        {"field_name": "metadata", "field_type": "dict", "required": True}
    ]
    df = pd.DataFrame(schema)
    return df, {"total_fields": len(df)}

def create_calendar_provider_request(
    provider_name: str,
    data_type: str,
    events: Optional[List[str]] = None,
    region: Optional[str] = None,
    start: Optional[str] = None,
    end: Optional[str] = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata: Optional[Dict] = None,
) -> CalendarProviderRequest:
    return CalendarProviderRequest(
        request_id=build_calendar_provider_request_id(provider_name, data_type),
        provider_name=provider_name,
        data_type=data_type,
        events=events or [],
        region=region,
        start=start,
        end=end,
        dry_run=dry_run,
        local_only=local_only,
        metadata=metadata or {}
    )

def validate_calendar_provider_request(request: CalendarProviderRequest, profile: CalendarProviderProfile) -> Dict:
    return {"valid": True, "errors": []}

def calendar_provider_request_to_dict(request: CalendarProviderRequest) -> Dict:
    return to_dict(request)
