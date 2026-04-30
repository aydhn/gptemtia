import numpy as np
import pandas as pd
import pytest

from indicators.trend_feature_set import TrendFeatureSetBuilder


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2023-01-01", periods=300, freq="D")
    df = pd.DataFrame(
        {
            "open": np.random.uniform(100, 200, 300),
            "high": np.random.uniform(150, 250, 300),
            "low": np.random.uniform(50, 150, 300),
            "close": np.random.uniform(100, 200, 300),
            "volume": np.random.uniform(1000, 5000, 300),
        },
        index=dates,
    )
    df["high"] = df[["open", "close", "high"]].max(axis=1)
    df["low"] = df[["open", "close", "low"]].min(axis=1)
    return df


def test_build_compact_trend_features(sample_ohlcv):
    builder = TrendFeatureSetBuilder()

    # Without events
    features, summary = builder.build_compact_trend_features(
        sample_ohlcv, include_events=False
    )

    assert isinstance(features, pd.DataFrame)
    assert len(features) == len(sample_ohlcv)
    assert "ema_20" in features.columns
    assert "macd_12_26_9" in features.columns
    assert "adx_14" in features.columns
    assert "event_price_above_ema_20" not in features.columns

    # With events
    features_with_events, summary_events = builder.build_compact_trend_features(
        sample_ohlcv, include_events=True
    )

    assert "event_price_above_ema_20" in features_with_events.columns
    assert summary_events["event_count"] > 0

    # Check no duplicate columns
    assert not features.columns.duplicated().any()


def test_build_trend_features_full(sample_ohlcv):
    builder = TrendFeatureSetBuilder()

    features, summary = builder.build_trend_features(sample_ohlcv, include_events=True)

    assert isinstance(features, pd.DataFrame)
    assert len(features) == len(sample_ohlcv)

    # Ichimoku should be present
    assert "ichimoku_tenkan" in features.columns
    assert "ichimoku_chikou" in features.columns

    # Warnings should include Ichimoku
    assert any("Ichimoku" in w for w in summary["warnings"])
    assert any("leakage" in w.lower() for w in summary["warnings"])

    # Should produce more columns than compact
    compact_features, _ = builder.build_compact_trend_features(
        sample_ohlcv, include_events=True
    )
    assert len(features.columns) > len(compact_features.columns)


def test_validate_trend_features(sample_ohlcv):
    builder = TrendFeatureSetBuilder()
    features, _ = builder.build_compact_trend_features(
        sample_ohlcv, include_events=False
    )

    val = builder.validate_trend_features(features)
    assert val["valid"] is True
    assert val["has_inf"] is False

    # Corrupt data
    features.iloc[0, features.columns.get_loc("ema_20")] = np.inf
    val_inf = builder.validate_trend_features(features)
    assert val_inf["has_inf"] is True
    assert val_inf["valid"] is False
