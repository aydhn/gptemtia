import numpy as np
import pandas as pd
import pytest

from indicators.feature_builder import FeatureBuilder


@pytest.fixture
def sample_df():
    dates = pd.date_range("2023-01-01", periods=100)
    return pd.DataFrame(
        {
            "open": np.random.uniform(100, 110, 100),
            "high": np.random.uniform(110, 120, 100),
            "low": np.random.uniform(90, 100, 100),
            "close": np.random.uniform(95, 115, 100),
            "volume": np.random.randint(1000, 5000, 100),
        },
        index=dates,
    )


def test_feature_builder_default(sample_df):
    builder = FeatureBuilder()
    features, summary = builder.build_default_feature_set(sample_df)

    assert "rsi_14" in features.columns
    assert "sma_20" in features.columns
    assert summary["indicator_count"] > 0
    assert summary["input_rows"] == 100
    assert "total_nan_ratio" in summary


def test_feature_builder_validation(sample_df):
    builder = FeatureBuilder()
    features, summary = builder.build_default_feature_set(sample_df)

    val = builder.validate_feature_frame(features)
    assert val["valid"] == True
    assert val["has_inf"] == False


def test_feature_builder_empty():
    builder = FeatureBuilder()
    empty_df = pd.DataFrame()
    features, summary = builder.build_default_feature_set(empty_df)
    assert "error" in summary


def test_feature_builder_volatility(sample_df):
    builder = FeatureBuilder()
    features, summary = builder.build_volatility_feature_set(
        sample_df, compact=True, include_events=False
    )

    assert summary["feature_count"] > 0
    assert summary["input_rows"] == 100
    assert "total_nan_ratio" in summary


def test_feature_builder_mean_reversion(sample_df):
    from indicators.mean_reversion_feature_set import MeanReversionFeatureSetBuilder

    builder = FeatureBuilder()
    features, summary = builder.build_mean_reversion_feature_set(
        sample_df, compact=True, include_events=False
    )

    assert summary["feature_count"] > 0
    assert summary["input_rows"] == 100
    assert "total_nan_ratio" in summary
