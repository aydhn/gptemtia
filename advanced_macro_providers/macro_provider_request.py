
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderRequest, build_macro_provider_request_id
from .macro_symbol_normalization import normalize_macro_indicator_symbol

def build_macro_provider_request_schema(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [{"field": "request_id", "type": "str"}]
    df = pd.DataFrame(schema)
    return df, {"total_fields": 1}

def create_macro_provider_request(
    provider_name: str,
    data_type: str,
    indicators: list[str] | None = None,
    region: str | None = None,
    frequency: str = "monthly",
    start: str | None = None,
    end: str | None = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata: dict | None = None,
) -> MacroProviderRequest:
    norm_inds = [normalize_macro_indicator_symbol(ind, provider_name) for ind in (indicators or [])]
    return MacroProviderRequest(
        request_id=build_macro_provider_request_id(provider_name, data_type, frequency),
        provider_name=provider_name,
        data_type=data_type,
        indicators=norm_inds,
        region=region,
        frequency=frequency,
        start=start,
        end=end,
        dry_run=dry_run,
        local_only=local_only,
        metadata=metadata or {}
    )

def validate_macro_provider_request(request: MacroProviderRequest, profile: MacroProviderProfile) -> dict:
    return {"valid": True}

def macro_provider_request_to_dict(request: MacroProviderRequest) -> dict:
    return vars(request)
