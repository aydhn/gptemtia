from unittest.mock import MagicMock

import pandas as pd
import pytest

from config.symbols import SymbolSpec
from indicators.feature_builder import FeatureBuilder
from indicators.indicator_pipeline import IndicatorPipeline


@pytest.fixture
def mock_data_lake():
    lake = MagicMock()
    # By default, say it has data
    lake.has_processed_ohlcv.return_value = True
    lake.has_ohlcv.return_value = True

    # Dummy dataframe
    df = pd.DataFrame(
        {
            "open": [100] * 100,
            "high": [105] * 100,
            "low": [95] * 100,
            "close": [102] * 100,
            "volume": [1000] * 100,
        }
    )
    lake.load_processed_ohlcv.return_value = df
    lake.load_ohlcv.return_value = df
    return lake


@pytest.fixture
def sample_spec():
    return SymbolSpec("TEST=F", "commodity", "metals", "yahoo", "USD")


@pytest.fixture
def macro_spec():
    return SymbolSpec("USIR", "US Interest Rate", "macro", "rates", "USD", "fred")


def test_pipeline_build_success(mock_data_lake, sample_spec):
    settings = MagicMock()
    settings.skip_macro_downloads_in_ohlcv_pipeline = False
    settings.default_indicator_min_rows = 50
    settings.save_indicator_features = True

    builder = FeatureBuilder()
    pipeline = IndicatorPipeline(mock_data_lake, builder, settings)

    features, summary = pipeline.build_for_symbol_timeframe(
        sample_spec, "1d", save=True
    )

    assert summary["success"] == True
    assert features is not None
    assert mock_data_lake.save_features.called


def test_pipeline_skip_macro(mock_data_lake, macro_spec):
    settings = MagicMock()
    settings.skip_macro_downloads_in_ohlcv_pipeline = True
    settings.skip_synthetic_downloads = True
    settings.default_indicator_min_rows = 50
    settings.save_indicator_features = True

    builder = FeatureBuilder()
    pipeline = IndicatorPipeline(mock_data_lake, builder, settings)

    features, summary = pipeline.build_for_symbol_timeframe(macro_spec, "1d", save=True)

    assert summary["success"] is False
    assert summary["skipped"] is True
    assert summary["skipped"] == True
    assert features is None


def test_pipeline_no_data(mock_data_lake, sample_spec):
    mock_data_lake.has_processed_ohlcv.return_value = False
    mock_data_lake.has_ohlcv.return_value = False

    settings = MagicMock()
    settings.skip_macro_downloads_in_ohlcv_pipeline = False
    settings.default_indicator_min_rows = 50
    settings.save_indicator_features = True

    builder = FeatureBuilder()
    pipeline = IndicatorPipeline(mock_data_lake, builder, settings)

    features, summary = pipeline.build_for_symbol_timeframe(
        sample_spec, "1d", save=True
    )

    assert summary["success"] is False
    assert summary["skipped"] is True
    assert summary["skipped"] == True
    assert features is None


def test_pipeline_mean_reversion_build_success(mock_data_lake, sample_spec):
    settings = MagicMock()
    settings.skip_macro_downloads_in_ohlcv_pipeline = False
    settings.default_indicator_min_rows = 50
    settings.save_mean_reversion_features = True
    settings.save_mean_reversion_events = True
    # Mean reversion uses real rolling windows so we need a larger dummy dataframe
    df = pd.DataFrame(
        {
            "open": [100] * 150,
            "high": [105] * 150,
            "low": [95] * 150,
            "close": [102] * 150,
            "volume": [1000] * 150,
        }
    )
    mock_data_lake.load_processed_ohlcv.return_value = df
    mock_data_lake.load_ohlcv.return_value = df

    builder = FeatureBuilder()
    pipeline = IndicatorPipeline(mock_data_lake, builder, settings)

    features, summary = pipeline.build_mean_reversion_for_symbol_timeframe(
        sample_spec, "1d", save=True
    )

    assert summary["success"] == True
    assert features is not None
    assert mock_data_lake.save_features.called
