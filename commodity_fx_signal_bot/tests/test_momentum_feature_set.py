import numpy as np
import pandas as pd
import pytest

from indicators.momentum_feature_set import MomentumFeatureSetBuilder


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2023-01-01", periods=100)
    df = pd.DataFrame(
        {
            "open": np.random.uniform(100, 200, 100),
            "high": np.random.uniform(150, 250, 100),
            "low": np.random.uniform(50, 150, 100),
            "close": np.random.uniform(100, 200, 100),
            "volume": np.random.uniform(1000, 5000, 100),
        },
        index=dates,
    )
    df["high"] = df[["open", "close", "high"]].max(axis=1)
    df["low"] = df[["open", "close", "low"]].min(axis=1)
    return df


def test_build_compact_momentum_features(sample_ohlcv):
    builder = MomentumFeatureSetBuilder()
    df, summary = builder.build_compact_momentum_features(
        sample_ohlcv, include_events=True
    )
    assert not df.empty
    assert len(df) == len(sample_ohlcv)
    assert "rsi_14" in df.columns
    assert "roc_10" in df.columns
    assert "slope_rsi_14_5" in df.columns
    assert "event_rsi_14_oversold" in df.columns
    assert summary["feature_count"] > 0
    assert summary["event_count"] > 0
    assert not df.columns.duplicated().any()


def test_build_full_momentum_features(sample_ohlcv):
    builder = MomentumFeatureSetBuilder()
    df, summary = builder.build_momentum_features(sample_ohlcv, include_events=True)
    assert not df.empty
    assert len(df) == len(sample_ohlcv)
    assert "rsi_28" in df.columns
    assert "accel_rsi_14_5" in df.columns
    assert summary["feature_count"] > 0
    assert summary["event_count"] > 0
    assert not df.columns.duplicated().any()


def test_include_events_flag(sample_ohlcv):
    builder = MomentumFeatureSetBuilder()
    df, summary = builder.build_compact_momentum_features(
        sample_ohlcv, include_events=False
    )
    assert summary["event_count"] == 0
    event_cols = [c for c in df.columns if c.startswith("event_")]
    assert len(event_cols) == 0


def test_validate_momentum_features(sample_ohlcv):
    builder = MomentumFeatureSetBuilder()
    df, summary = builder.build_compact_momentum_features(sample_ohlcv)
    val_res = builder.validate_momentum_features(df)
    assert val_res["valid"] is True
    assert val_res["has_inf"] is False
