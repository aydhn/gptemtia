import pandas as pd
from typing import Tuple, Dict, List, Optional
from .fx_provider_config import FXProviderProfile
from .fx_provider_interfaces import BaseFXProvider
from .fx_provider_models import FXProviderCapability

class FXProviderRegistry:
    def __init__(self):
        self.providers: Dict[str, BaseFXProvider] = {}

    def register(self, provider: BaseFXProvider) -> None:
        self.providers[provider.provider_name] = provider

    def list_providers(self) -> List[str]:
        return list(self.providers.keys())

    def get_provider(self, provider_name: str) -> Optional[BaseFXProvider]:
        return self.providers.get(provider_name)

    def list_capabilities(self) -> List[FXProviderCapability]:
        caps = []
        for p in self.providers.values():
            caps.extend(p.capabilities())
        return caps

    def to_dataframe(self) -> pd.DataFrame:
        data = []
        for name, p in self.providers.items():
            data.append({"provider_name": name, "provider_type": p.provider_type})
        return pd.DataFrame(data)

def build_default_fx_provider_registry(profile: FXProviderProfile) -> FXProviderRegistry:
    registry = FXProviderRegistry()
    # Note: actual provider implementations will be registered here or outside
    return registry

def build_fx_provider_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    registry = build_default_fx_provider_registry(profile)
    # mock data
    df = pd.DataFrame([
        {"provider_name": "fx_dry_run_fixture_provider", "provider_type": "provider_dry_run_fixture"},
        {"provider_name": "fx_manual_file_provider_placeholder", "provider_type": "provider_manual_file"},
        {"provider_name": "fx_local_cache_provider_placeholder", "provider_type": "provider_local_cache"},
        {"provider_name": "fx_official_api_provider_placeholder", "provider_type": "provider_official_api"},
        {"provider_name": "fx_licensed_provider_placeholder", "provider_type": "provider_licensed"}
    ])
    return df, summarize_fx_provider_registry(df)

def summarize_fx_provider_registry(df: pd.DataFrame) -> Dict:
    return {"total_registered": len(df)}
