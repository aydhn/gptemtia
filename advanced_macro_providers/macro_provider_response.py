
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderResponse, build_macro_provider_response_id

def build_macro_provider_response_schema(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [{"field": "response_id", "type": "str"}]
    df = pd.DataFrame(schema)
    return df, {"total_fields": 1}

def create_macro_provider_response(
    request_id: str,
    provider_name: str,
    data_type: str,
    status_label: str,
    output_ref: str = "",
    row_count: int = 0,
    schema_ref: str = "",
    warnings: list[str] | None = None,
    manual_review_required: bool = True,
) -> MacroProviderResponse:
    return MacroProviderResponse(
        response_id=build_macro_provider_response_id(request_id, provider_name),
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

def validate_macro_provider_response(response: MacroProviderResponse, profile: MacroProviderProfile) -> dict:
    return {"valid": True}

def macro_provider_response_to_dict(response: MacroProviderResponse) -> dict:
    return vars(response)
