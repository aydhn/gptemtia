import pytest
from data.provider_registry import get_provider, list_available_providers, register_provider
from data.providers.yahoo_provider import YahooProvider
from data.providers.base_provider import BaseDataProvider
from core.exceptions import DataProviderError
import pandas as pd
from typing import Optional

class MockProvider(BaseDataProvider):
    def fetch_ohlcv(self, symbol: str, interval: str, start: Optional[str] = None, end: Optional[str] = None, period: Optional[str] = None) -> pd.DataFrame:
        return pd.DataFrame()

def test_get_yahoo_provider():
    provider = get_provider("yahoo")
    assert isinstance(provider, YahooProvider)
    assert provider.name == "YahooProvider"

def test_get_unknown_provider():
    with pytest.raises(DataProviderError, match="not found in registry"):
        get_provider("unknown_provider_name")

def test_list_available_providers():
    providers = list_available_providers()
    assert len(providers) >= 3
    assert "yahoo" in providers
    assert "evds" in providers
    assert "fred" in providers

def test_register_provider():
    mock = MockProvider()
    register_provider("mock", mock)

    assert "mock" in list_available_providers()
    provider = get_provider("mock")
    assert isinstance(provider, MockProvider)
