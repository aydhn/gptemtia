import pytest
import pandas as pd
from unittest.mock import MagicMock, patch
from macro.macro_provider import MacroProvider
from macro.macro_series import MacroSeriesSpec
from config.settings import Settings

@patch('macro.macro_provider.MacroProvider.fetch_macro_series')
def test_fetch_many_concurrent(mock_fetch_series):
    settings = Settings()
    # Need mock values so settings doesn't fail if variables aren't set
    settings.evds_api_key = "test_key"
    settings.fred_api_key = "test_key"
    provider = MacroProvider(settings)

    # Setup mock to return a simple dataframe
    mock_df = pd.DataFrame({"value": [1, 2, 3]})
    mock_fetch_series.return_value = mock_df

    # Create specs
    specs = [
        MacroSeriesSpec(code="TEST_1", source="yahoo", frequency="D", name="Test 1"),
        MacroSeriesSpec(code="TEST_2", source="yahoo", frequency="D", name="Test 2", enabled=False),
        MacroSeriesSpec(code="TEST_3", source="yahoo", frequency="D", name="Test 3"),
    ]

    results = provider.fetch_many(specs)

    # Assertions
    assert len(results) == 2
    assert "TEST_1" in results
    assert "TEST_3" in results
    assert "TEST_2" not in results
    assert mock_fetch_series.call_count == 2

@patch('macro.macro_provider.MacroProvider.fetch_macro_series')
def test_fetch_many_handles_exceptions(mock_fetch_series):
    settings = Settings()
    settings.evds_api_key = "test_key"
    settings.fred_api_key = "test_key"
    provider = MacroProvider(settings)

    # Setup mock to throw an exception for the first call, succeed for second
    def side_effect(spec, *args, **kwargs):
        if spec.code == "TEST_FAIL":
            raise ValueError("Test error")
        return pd.DataFrame({"value": [1, 2, 3]})

    mock_fetch_series.side_effect = side_effect

    specs = [
        MacroSeriesSpec(code="TEST_FAIL", source="yahoo", frequency="D", name="Test Fail"),
        MacroSeriesSpec(code="TEST_SUCCEED", source="yahoo", frequency="D", name="Test Succeed"),
    ]

    results = provider.fetch_many(specs)

    # Assertions - it shouldn't crash and should return the successful one
    assert len(results) == 1
    assert "TEST_SUCCEED" in results
