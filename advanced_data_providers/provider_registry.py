import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_interfaces import BaseDataProvider
from .provider_models import ProviderCapability
from dataclasses import asdict

class DataProviderRegistry:
    def __init__(self):
        self._providers: dict[str, BaseDataProvider] = {}

    def register(self, provider: BaseDataProvider) -> None:
        self._providers[provider.provider_name] = provider

    def list_providers(self) -> list[str]:
        return list(self._providers.keys())

    def get_provider(self, provider_name: str) -> BaseDataProvider | None:
        return self._providers.get(provider_name)

    def list_capabilities(self) -> list[ProviderCapability]:
        caps = []
        for p in self._providers.values():
            caps.extend(p.capabilities())
        return caps

    def to_dataframe(self) -> pd.DataFrame:
        data = []
        for name, p in self._providers.items():
            meta = p.metadata()
            data.append(asdict(meta))
        return pd.DataFrame(data) if data else pd.DataFrame()

def build_default_provider_registry(profile: DataProviderAbstractionProfile) -> DataProviderRegistry:
    registry = DataProviderRegistry()
    # In a real setup, we would import the placeholders and register them here.
    return registry

def build_provider_registry(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    registry = build_default_provider_registry(profile)
    df = registry.to_dataframe()
    return df, summarize_provider_registry(df)

def summarize_provider_registry(df: pd.DataFrame) -> dict:
    return {"total_registered_providers": len(df)}
