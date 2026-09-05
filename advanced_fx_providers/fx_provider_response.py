import pandas as pd
from typing import Tuple, Dict, List, Optional
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderResponse, build_fx_provider_response_id

def build_fx_provider_response_schema(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "response_id", "type": "str", "required": True},
        {"field": "request_id", "type": "str", "required": True},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "data_type", "type": "str", "required": True},
        {"field": "status_label", "type": "str", "required": True},
        {"field": "output_ref", "type": "str", "required": True},
        {"field": "row_count", "type": "int", "required": True},
        {"field": "schema_ref", "type": "str", "required": True},
        {"field": "warnings", "type": "list[str]", "required": True},
        {"field": "manual_review_required", "type": "bool", "required": True}
    ]
    return pd.DataFrame(schema), {"total_fields": len(schema)}

def create_fx_provider_response(
    request_id: str,
    provider_name: str,
    data_type: str,
    status_label: str,
    output_ref: str = "",
    row_count: int = 0,
    schema_ref: str = "",
    warnings: Optional[List[str]] = None,
    manual_review_required: bool = True,
) -> FXProviderResponse:
    return FXProviderResponse(
        response_id=build_fx_provider_response_id(request_id, provider_name),
        request_id=request_id, provider_name=provider_name, data_type=data_type,
        status_label=status_label, output_ref=output_ref, row_count=row_count,
        schema_ref=schema_ref, warnings=warnings or [], manual_review_required=manual_review_required
    )

def validate_fx_provider_response(response: FXProviderResponse, profile: FXProviderProfile) -> Dict:
    return {"valid": True, "errors": []}

def fx_provider_response_to_dict(response: FXProviderResponse) -> Dict:
    return response.to_dict()
