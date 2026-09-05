import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderRequest
from .provider_interfaces import BaseDataProvider
from .provider_registry import DataProviderRegistry

def resolve_provider_for_request(
    request: ProviderRequest,
    registry: DataProviderRegistry,
    profile: DataProviderAbstractionProfile,
) -> BaseDataProvider | None:
    # Basic graceful resolver that doesn't do network calls
    provider = registry.get_provider(request.provider_name)
    if provider:
        return provider
    return None

def build_provider_resolver_map(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([
        {"request_type": "ohlcv", "resolved_provider": "dry_run_fixture_provider"},
        {"request_type": "macro", "resolved_provider": "dry_run_fixture_provider"}
    ])
    return df, summarize_provider_resolver_map(df)

def summarize_provider_resolver_map(df: pd.DataFrame) -> dict:
    return {"total_mappings": len(df)}
