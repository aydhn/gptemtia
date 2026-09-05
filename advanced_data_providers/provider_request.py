import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderRequest, build_provider_request_id
from dataclasses import asdict

def create_provider_request(
    provider_name: str,
    data_type: str,
    symbols: list[str] | None = None,
    timeframe: str = "1d",
    start: str | None = None,
    end: str | None = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata: dict | None = None,
) -> ProviderRequest:
    return ProviderRequest(
        request_id=build_provider_request_id(provider_name, data_type, timeframe),
        provider_name=provider_name,
        data_type=data_type,
        symbols=symbols or [],
        timeframe=timeframe,
        start=start,
        end=end,
        dry_run=dry_run,
        local_only=local_only,
        metadata=metadata or {}
    )

def build_provider_request_schema(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    schema = {
        "field": ["request_id", "provider_name", "data_type", "symbols", "timeframe", "start", "end", "dry_run", "local_only", "metadata"],
        "type": ["str", "str", "str", "list[str]", "str", "str", "str", "bool", "bool", "dict"]
    }
    df = pd.DataFrame(schema)
    return df, {"total_fields": len(df)}

def validate_provider_request(request: ProviderRequest, profile: DataProviderAbstractionProfile) -> dict:
    errors = []
    if not request.dry_run:
        errors.append("dry_run must be True")
    if not request.local_only:
        errors.append("local_only must be True")
    return {"valid": len(errors) == 0, "errors": errors}

def provider_request_to_dict(request: ProviderRequest) -> dict:
    return asdict(request)
