import pandas as pd
import pytest

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake


@pytest.fixture
def temp_data_lake(tmp_path):
    return DataLake(tmp_path)


@pytest.fixture
def mock_spec():
    return SymbolSpec(
        symbol="GC=F",
        name="Gold",
        asset_class="metals",
        sub_class="precious",
        currency="USD",
        data_source="yahoo",
    )


@pytest.fixture
def valid_df():
    dates = pd.date_range("2023-01-01", periods=5, tz="UTC")
    return pd.DataFrame(
        {
            "open": [10.0, 11.0, 12.0, 11.5, 12.5],
            "high": [10.5, 11.5, 12.5, 12.0, 13.0],
            "low": [9.5, 10.5, 11.5, 11.0, 12.0],
            "close": [10.2, 11.2, 12.2, 11.8, 12.8],
            "adj_close": [10.2, 11.2, 12.2, 11.8, 12.8],
            "volume": [100, 200, 150, 300, 250],
        },
        index=dates,
    )


def test_safe_symbol_name():
    assert DataLake.safe_symbol_name("GC=F") == "GC_F"
    assert DataLake.safe_symbol_name("EUR/USD") == "EUR_USD"
    assert DataLake.safe_symbol_name("BTC-USD") == "BTC-USD"


def test_get_symbol_dir(temp_data_lake, mock_spec):
    dir_path = temp_data_lake.get_symbol_dir(mock_spec)
    assert dir_path.name == "GC_F"
    assert dir_path.parent.name == "precious"
    assert dir_path.parent.parent.name == "yahoo"


def test_get_ohlcv_path(temp_data_lake, mock_spec):
    path = temp_data_lake.get_ohlcv_path(mock_spec, "1d")
    assert path.name == "1d.parquet"


def test_save_and_load_ohlcv(temp_data_lake, mock_spec, valid_df):
    timeframe = "1d"

    # Save
    saved_path = temp_data_lake.save_ohlcv(mock_spec, timeframe, valid_df)
    assert saved_path.exists()
    assert temp_data_lake.has_ohlcv(mock_spec, timeframe) is True

    # Load
    loaded_df = temp_data_lake.load_ohlcv(mock_spec, timeframe)
    pd.testing.assert_frame_equal(valid_df, loaded_df, check_freq=False)


def test_metadata_operations(temp_data_lake, mock_spec):
    metadata = {"symbol": "GC=F", "available_timeframes": ["1d", "4h"]}

    saved_path = temp_data_lake.save_metadata(mock_spec, metadata)
    assert saved_path.exists()

    loaded_metadata = temp_data_lake.load_metadata(mock_spec)
    assert loaded_metadata == metadata


def test_list_available_timeframes(temp_data_lake, mock_spec, valid_df):
    temp_data_lake.save_ohlcv(mock_spec, "1d", valid_df)
    temp_data_lake.save_ohlcv(mock_spec, "4h", valid_df)

    tfs = temp_data_lake.list_available_timeframes(mock_spec)
    assert set(tfs) == {"1d", "4h"}


def test_delete_ohlcv(temp_data_lake, mock_spec, valid_df):
    timeframe = "1d"
    temp_data_lake.save_ohlcv(mock_spec, timeframe, valid_df)
    assert temp_data_lake.has_ohlcv(mock_spec, timeframe) is True

    temp_data_lake.delete_ohlcv(mock_spec, timeframe)
    assert temp_data_lake.has_ohlcv(mock_spec, timeframe) is False


def test_data_lake_save_load_volatility_features(temp_data_lake, mock_spec, valid_df):
    temp_data_lake.save_features(
        mock_spec, "1d", valid_df, feature_set_name="volatility"
    )

    assert temp_data_lake.has_features(mock_spec, "1d", feature_set_name="volatility")
    loaded = temp_data_lake.load_features(
        mock_spec, "1d", feature_set_name="volatility"
    )

    assert len(loaded) == len(valid_df)
    # pd.testing.assert_frame_equal(loaded, valid_df) # ignore check freq


def test_data_lake_save_load_mean_reversion_features(
    temp_data_lake, mock_spec, valid_df
):
    temp_data_lake.save_features(
        mock_spec, "1d", valid_df, feature_set_name="mean_reversion"
    )

    assert temp_data_lake.has_features(
        mock_spec, "1d", feature_set_name="mean_reversion"
    )
    loaded = temp_data_lake.load_features(
        mock_spec, "1d", feature_set_name="mean_reversion"
    )

    assert len(loaded) == len(valid_df)
