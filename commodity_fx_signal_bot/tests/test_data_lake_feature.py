import pandas as pd
import pytest

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake


@pytest.fixture
def mock_spec():
    return SymbolSpec("TEST=F", "commodity", "metals", "yahoo", "USD")


@pytest.fixture
def temp_data_lake(tmp_path):
    dl = DataLake(root_dir=tmp_path)
    dl.format = "parquet"
    dl.root_dir = tmp_path
    return dl


def test_save_and_load_features(temp_data_lake, mock_spec):
    df = pd.DataFrame(
        {"open": [100.0, 101.0], "close": [101.0, 102.0], "rsi_14": [50.0, 51.0]}
    )

    path = temp_data_lake.save_features(mock_spec, "1d", df, "technical")
    assert path.exists()
    assert temp_data_lake.has_features(mock_spec, "1d", "technical")

    loaded_df = temp_data_lake.load_features(mock_spec, "1d", "technical")
    assert not loaded_df.empty
    assert "rsi_14" in loaded_df.columns


def test_list_feature_timeframes(temp_data_lake, mock_spec):
    df = pd.DataFrame({"close": [101.0]})
    temp_data_lake.save_features(mock_spec, "1d", df, "technical")
    temp_data_lake.save_features(mock_spec, "1h", df, "technical")

    tfs = temp_data_lake.list_feature_timeframes(mock_spec, "technical")
    assert set(tfs) == {"1d", "1h"}
