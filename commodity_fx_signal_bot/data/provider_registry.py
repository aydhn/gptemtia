"""
Registry for data providers.
"""

from typing import Dict, List
from core.exceptions import DataProviderError
from data.providers.base_provider import BaseDataProvider
from data.providers.yahoo_provider import YahooProvider
from data.providers.evds_provider import EVDSProvider
from data.providers.fred_provider import FREDProvider

_PROVIDERS: Dict[str, BaseDataProvider] = {
    "yahoo": YahooProvider(),
    "evds": EVDSProvider(),
    "fred": FREDProvider(),
}


def register_provider(name: str, provider: BaseDataProvider) -> None:
    """Register a new data provider."""
    _PROVIDERS[name] = provider


def get_provider(name: str) -> BaseDataProvider:
    """Get a data provider by name."""
    if name not in _PROVIDERS:
        raise DataProviderError(f"Data provider '{name}' not found in registry.")
    return _PROVIDERS[name]


def list_available_providers() -> List[str]:
    """List names of all registered data providers."""
    return list(_PROVIDERS.keys())
