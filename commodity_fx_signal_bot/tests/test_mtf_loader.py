import pytest
import pandas as pd
from unittest.mock import Mock
from config.symbols import SymbolSpec
from mtf.mtf_loader import MTFFeatureLoader


def test_load_feature_set():
    mock_lake = Mock()
    mock_lake.has_features.return_value = True
    df = pd.DataFrame({"val": [1, 2]})
    mock_lake.load_features.return_value = df

    loader = MTFFeatureLoader(mock_lake)
    spec = SymbolSpec("TEST", "crypto", "crypto", "crypto", "USD")

    res = loader.load_feature_set(spec, "1d", "trend")
    assert not res.empty
    mock_lake.load_features.assert_called_once_with(spec, "1d", "trend")


def test_load_best_available_base_frame():
    mock_lake = Mock()
    mock_lake.has_features.return_value = False
    mock_lake.has_processed_ohlcv.return_value = True
    df = pd.DataFrame({"close": [1, 2]})
    mock_lake.load_processed_ohlcv.return_value = df

    loader = MTFFeatureLoader(mock_lake)
    spec = SymbolSpec("TEST", "crypto", "crypto", "crypto", "USD")

    res, summ = loader.load_best_available_base_frame(spec, "1d", ("trend", "momentum"))
    assert not res.empty
    assert "trend" in summ["missing"]
