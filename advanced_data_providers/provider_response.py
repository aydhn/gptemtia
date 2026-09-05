import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderResponse, build_provider_response_id
from dataclasses import asdict

def create_provider_response(
    request_id: str,
    provider_name: str,
    data_type: str,
    status_label: str,
    output_ref: str = "",
    row_count: int = 0,
    schema_ref: str = "",
    warnings: list[str] | None = None,
    manual_review_required: bool = True,
) -> ProviderResponse:
    return ProviderResponse(
        response_id=build_provider_response_id(request_id, provider_name),
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

def build_provider_response_schema(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    schema = {
        "field": ["response_id", "request_id", "provider_name", "data_type", "status_label", "output_ref", "row_count", "schema_ref", "warnings", "manual_review_required"],
        "type": ["str", "str", "str", "str", "str", "str", "int", "str", "list[str]", "bool"]
    }
    df = pd.DataFrame(schema)
    return df, {"total_fields": len(df)}

def validate_provider_response(response: ProviderResponse, profile: DataProviderAbstractionProfile) -> dict:
    errors = []
    return {"valid": len(errors) == 0, "errors": errors}

def provider_response_to_dict(response: ProviderResponse) -> dict:
    return asdict(response)
