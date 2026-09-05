import pandas as pd
from typing import Tuple, Dict, List, Optional
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import CalendarProviderResponse, build_calendar_provider_response_id, to_dict

def build_calendar_provider_response_schema(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field_name": "response_id", "field_type": "str", "required": True},
        {"field_name": "request_id", "field_type": "str", "required": True},
        {"field_name": "provider_name", "field_type": "str", "required": True},
        {"field_name": "data_type", "field_type": "str", "required": True},
        {"field_name": "status_label", "field_type": "str", "required": True},
        {"field_name": "output_ref", "field_type": "str", "required": True},
        {"field_name": "row_count", "field_type": "int", "required": True},
        {"field_name": "schema_ref", "field_type": "str", "required": True},
        {"field_name": "warnings", "field_type": "List[str]", "required": True},
        {"field_name": "manual_review_required", "field_type": "bool", "required": True}
    ]
    df = pd.DataFrame(schema)
    return df, {"total_fields": len(df)}

def create_calendar_provider_response(
    request_id: str,
    provider_name: str,
    data_type: str,
    status_label: str,
    output_ref: str = "",
    row_count: int = 0,
    schema_ref: str = "",
    warnings: Optional[List[str]] = None,
    manual_review_required: bool = True,
) -> CalendarProviderResponse:
    return CalendarProviderResponse(
        response_id=build_calendar_provider_response_id(request_id, provider_name),
        request_id=request_id,
        provider_name=provider_name,
        data_type=data_type,
        status_label=status_label,
        output_ref=output_ref,
        row_count=row_count,
        schema_ref=schema_ref,
        warnings=warnings or [],
        manual_review_required=manual_review_required
    )

def validate_calendar_provider_response(response: CalendarProviderResponse, profile: CalendarProviderProfile) -> Dict:
    return {"valid": True, "errors": []}

def calendar_provider_response_to_dict(response: CalendarProviderResponse) -> Dict:
    return to_dict(response)
