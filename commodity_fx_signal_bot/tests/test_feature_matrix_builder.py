import pytest
import pandas as pd
from unittest.mock import Mock
from config.symbols import SymbolSpec
from ml.feature_matrix_builder import FeatureMatrixBuilder

def test_build_feature_matrix():
    mock_dl = Mock()
    mock_dl.load_processed_ohlcv.return_value = pd.DataFrame({"close": [10, 11]}, index=[0, 1])
    mock_dl.load_technical_indicators.return_value = pd.DataFrame({"rsi": [50, 60], "rsi_id": [1, 2]}, index=[0, 1])

    builder = FeatureMatrixBuilder(mock_dl)
    spec = SymbolSpec(symbol="TEST", name="Test", asset_class="test", sub_class="test", currency="USD")

    X, summary = builder.build_feature_matrix(spec, "1d", ("technical",))

    assert not X.empty
    assert "technical__rsi" in X.columns
    assert "technical__rsi_id" not in X.columns # Excluded
    assert summary["dropped_columns"] == ["technical__rsi_id"]

def test_clean_feature_matrix():
    builder = FeatureMatrixBuilder(Mock())
    X = pd.DataFrame({
        "good": [1, 2, 3, 4],
        "bad": [1, None, None, None]
    })

    X_clean, summary = builder.clean_feature_matrix(X, 0.35)
    assert "bad" not in X_clean.columns
    assert "good" in X_clean.columns
