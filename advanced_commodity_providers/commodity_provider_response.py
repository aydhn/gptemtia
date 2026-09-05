
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderResponse, build_commodity_provider_response_id, commodity_provider_response_to_dict

def create_commodity_provider_response(
    request_id: str,
    provider_name: str,
    data_type: str,
    status_label: str,
    output_ref: str = "",
    row_count: int = 0,
    schema_ref: str = "",
    warnings: list[str] | None = None,
    manual_review_required: bool = True,
) -> CommodityProviderResponse:
    return CommodityProviderResponse(
        response_id=build_commodity_provider_response_id(request_id, provider_name),
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

def validate_commodity_provider_response(response: CommodityProviderResponse, profile: CommodityProviderProfile) -> dict:
    return {"valid": True}

def build_commodity_provider_response_schema(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "response_id", "type": "str"},
        {"field": "request_id", "type": "str"},
        {"field": "provider_name", "type": "str"},
        {"field": "data_type", "type": "str"},
        {"field": "status_label", "type": "str"},
        {"field": "output_ref", "type": "str"},
        {"field": "row_count", "type": "int"},
        {"field": "schema_ref", "type": "str"},
        {"field": "warnings", "type": "list[str]"},
        {"field": "manual_review_required", "type": "bool"}
    ]
    df = pd.DataFrame(schema)
    return df, {"total_fields": len(df)}
