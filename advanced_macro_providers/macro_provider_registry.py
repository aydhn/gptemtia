
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_interfaces import BaseMacroProvider
from .macro_provider_models import MacroProviderCapability

class MacroProviderRegistry:
    def __init__(self):
        self._providers = {}
        
    def register(self, provider: BaseMacroProvider) -> None:
        self._providers[provider.provider_name] = provider
        
    def list_providers(self) -> list[str]:
        return list(self._providers.keys())
        
    def get_provider(self, provider_name: str) -> BaseMacroProvider | None:
        return self._providers.get(provider_name)
        
    def list_capabilities(self) -> list[MacroProviderCapability]:
        caps = []
        for p in self._providers.values():
            caps.extend(p.capabilities())
        return caps
        
    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame([{"provider_name": k} for k in self._providers.keys()])

def build_default_macro_provider_registry(profile: MacroProviderProfile) -> MacroProviderRegistry:
    from .macro_dry_run_fixture import MacroDryRunFixtureProvider
    from .macro_manual_file_provider import MacroManualFileProviderPlaceholder
    from .macro_local_cache_provider import MacroLocalCacheProviderPlaceholder
    from .macro_official_api_provider import MacroOfficialApiProviderPlaceholder
    from .macro_licensed_provider import MacroLicensedProviderPlaceholder
    from .macro_public_dataset_provider import MacroPublicDatasetProviderPlaceholder
    
    registry = MacroProviderRegistry()
    registry.register(MacroDryRunFixtureProvider())
    registry.register(MacroManualFileProviderPlaceholder())
    registry.register(MacroLocalCacheProviderPlaceholder())
    registry.register(MacroOfficialApiProviderPlaceholder())
    registry.register(MacroLicensedProviderPlaceholder())
    registry.register(MacroPublicDatasetProviderPlaceholder())
    return registry

def build_macro_provider_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    registry = build_default_macro_provider_registry(profile)
    df = registry.to_dataframe()
    return df, summarize_macro_provider_registry(df)

def summarize_macro_provider_registry(df: pd.DataFrame) -> dict:
    return {"total_providers": len(df)}
