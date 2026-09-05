
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderRequest, build_commodity_provider_request_id, commodity_provider_request_to_dict

def create_commodity_provider_request(
    provider_name: str,
    data_type: str,
    symbols: list[str] | None = None,
    timeframe: str = "1d",
    start: str | None = None,
    end: str | None = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata: dict | None = None,
) -> CommodityProviderRequest:
    from .commodity_symbol_normalization import normalize_commodity_symbol
    norm_symbols = [normalize_commodity_symbol(s, provider_name) for s in (symbols or [])]
    return CommodityProviderRequest(
        request_id=build_commodity_provider_request_id(provider_name, data_type, timeframe),
        provider_name=provider_name,
        data_type=data_type,
        symbols=norm_symbols,
        timeframe=timeframe,
        start=start,
        end=end,
        dry_run=dry_run,
        local_only=local_only,
        metadata=metadata or {}
    )

def validate_commodity_provider_request(request: CommodityProviderRequest, profile: CommodityProviderProfile) -> dict:
    if not request.dry_run: return {"valid": False, "error": "dry_run must be True"}
    if not request.local_only: return {"valid": False, "error": "local_only must be True"}
    return {"valid": True}

def build_commodity_provider_request_schema(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "request_id", "type": "str"},
        {"field": "provider_name", "type": "str"},
        {"field": "data_type", "type": "str"},
        {"field": "symbols", "type": "list[str]"},
        {"field": "timeframe", "type": "str"},
        {"field": "start", "type": "str"},
        {"field": "end", "type": "str"},
        {"field": "dry_run", "type": "bool"},
        {"field": "local_only", "type": "bool"},
        {"field": "metadata", "type": "dict"}
    ]
    df = pd.DataFrame(schema)
    return df, {"total_fields": len(df)}
