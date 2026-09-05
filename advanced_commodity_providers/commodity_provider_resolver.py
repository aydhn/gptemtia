
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_interfaces import BaseCommodityProvider
from .commodity_provider_models import CommodityProviderRequest
from .commodity_provider_registry import CommodityProviderRegistry

def resolve_commodity_provider_for_request(
    request: CommodityProviderRequest,
    registry: CommodityProviderRegistry,
    profile: CommodityProviderProfile,
) -> BaseCommodityProvider | None:
    return registry.get_provider(request.provider_name)

def build_commodity_provider_resolver_map(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"request_type": "all", "resolved_provider": "dry_run"}])
    return df, summarize_commodity_provider_resolver_map(df)

def summarize_commodity_provider_resolver_map(df: pd.DataFrame) -> dict:
    return {"total_mappings": len(df)}
