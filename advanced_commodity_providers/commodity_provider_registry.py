
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_interfaces import BaseCommodityProvider
from .commodity_provider_models import CommodityProviderCapability

class CommodityProviderRegistry:
    def __init__(self):
        self._providers = {}
    
    def register(self, provider: BaseCommodityProvider) -> None:
        self._providers[provider.provider_name] = provider

    def list_providers(self) -> list[str]:
        return list(self._providers.keys())

    def get_provider(self, provider_name: str) -> BaseCommodityProvider | None:
        return self._providers.get(provider_name)

    def list_capabilities(self) -> list[CommodityProviderCapability]:
        caps = []
        for p in self._providers.values():
            caps.extend(p.capabilities())
        return caps

    def to_dataframe(self) -> pd.DataFrame:
        data = []
        for k, v in self._providers.items():
            data.append({"provider_name": k, "provider_type": v.provider_type})
        return pd.DataFrame(data)

def build_default_commodity_provider_registry(profile: CommodityProviderProfile) -> CommodityProviderRegistry:
    from .commodity_dry_run_fixture import CommodityDryRunFixtureProvider
    from .commodity_manual_file_provider import CommodityManualFileProviderPlaceholder
    from .commodity_local_cache_provider import CommodityLocalCacheProviderPlaceholder
    from .commodity_official_api_provider import CommodityOfficialApiProviderPlaceholder
    from .commodity_licensed_provider import CommodityLicensedProviderPlaceholder
    registry = CommodityProviderRegistry()
    registry.register(CommodityDryRunFixtureProvider())
    registry.register(CommodityManualFileProviderPlaceholder())
    registry.register(CommodityLocalCacheProviderPlaceholder())
    registry.register(CommodityOfficialApiProviderPlaceholder())
    registry.register(CommodityLicensedProviderPlaceholder())
    return registry

def build_commodity_provider_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    registry = build_default_commodity_provider_registry(profile)
    df = registry.to_dataframe()
    return df, summarize_commodity_provider_registry(df)

def summarize_commodity_provider_registry(df: pd.DataFrame) -> dict:
    return {"total_providers": len(df)}
