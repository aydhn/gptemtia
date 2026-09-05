import pandas as pd
from typing import Tuple, Dict, List, Optional
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderRequest, build_fx_provider_request_id
from .fx_symbol_normalization import normalize_fx_pair_symbol

def build_fx_provider_request_schema(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "request_id", "type": "str", "required": True},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "data_type", "type": "str", "required": True},
        {"field": "pairs", "type": "list[str]", "required": True},
        {"field": "timeframe", "type": "str", "required": True},
        {"field": "start", "type": "str", "required": False},
        {"field": "end", "type": "str", "required": False},
        {"field": "dry_run", "type": "bool", "required": True},
        {"field": "local_only", "type": "bool", "required": True},
        {"field": "metadata", "type": "dict", "required": False}
    ]
    return pd.DataFrame(schema), {"total_fields": len(schema)}

def create_fx_provider_request(
    provider_name: str,
    data_type: str,
    pairs: Optional[List[str]] = None,
    timeframe: str = "1d",
    start: Optional[str] = None,
    end: Optional[str] = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata: Optional[Dict] = None,
) -> FXProviderRequest:
    normalized_pairs = [normalize_fx_pair_symbol(p, provider_name) for p in (pairs or [])]
    return FXProviderRequest(
        request_id=build_fx_provider_request_id(provider_name, data_type, timeframe),
        provider_name=provider_name, data_type=data_type, pairs=normalized_pairs,
        timeframe=timeframe, start=start, end=end, dry_run=dry_run, local_only=local_only,
        metadata=metadata or {}
    )

def validate_fx_provider_request(request: FXProviderRequest, profile: FXProviderProfile) -> Dict:
    valid = request.dry_run and request.local_only
    return {"valid": valid, "errors": [] if valid else ["Must be dry_run and local_only"]}

def fx_provider_request_to_dict(request: FXProviderRequest) -> Dict:
    return request.to_dict()
