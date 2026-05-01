import numpy as np
import pandas as pd
import pytest

from indicators.mean_reversion_feature_set import MeanReversionFeatureSetBuilder


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2023-01-01", periods=150)
    df = pd.DataFrame(
        {
            "open": np.random.uniform(100, 200, 150),
            "high": np.random.uniform(150, 250, 150),
            "low": np.random.uniform(50, 150, 150),
            "close": np.random.uniform(100, 200, 150),
            "volume": np.random.uniform(1000, 5000, 150),
        },
        index=dates,
    )
    df["high"] = df[["open", "close", "high"]].max(axis=1)
    df["low"] = df[["open", "close", "low"]].min(axis=1)
    return df


def test_build_compact_mean_reversion_features(sample_ohlcv):
    builder = MeanReversionFeatureSetBuilder()
    df, summary = builder.build_compact_mean_reversion_features(
        sample_ohlcv, include_events=True
    )
    assert not df.empty
    assert len(df) == len(sample_ohlcv)
    assert "zscore_close_20" in df.columns
    assert "rolling_mean_dist_20" in df.columns
    assert "dist_sma_20" in df.columns
    assert "dist_ema_20" in df.columns
    assert "percentile_close_120" in df.columns
    assert "minmax_pos_50" in df.columns
    assert "bb_percent_b_20_2" in df.columns
    assert "channel_dev_20" in df.columns
    assert "overextension_score_20" in df.columns
    assert "range_pos_50" in df.columns
    assert summary["feature_count"] > 0
    assert summary["event_count"] > 0
    assert not df.columns.duplicated().any()


def test_build_full_mean_reversion_features(sample_ohlcv):
    builder = MeanReversionFeatureSetBuilder()
    df, summary = builder.build_mean_reversion_features(
        sample_ohlcv, include_events=True
    )
    assert not df.empty
    assert len(df) == len(sample_ohlcv)
    assert "zscore_close_100" in df.columns
    assert "dist_sma_200" in df.columns
    assert "half_life_proxy_50" in df.columns
    assert summary["feature_count"] > 0
    assert summary["event_count"] > 0
    assert not df.columns.duplicated().any()


def test_include_events_flag(sample_ohlcv):
    builder = MeanReversionFeatureSetBuilder()
    df, summary = builder.build_compact_mean_reversion_features(
        sample_ohlcv, include_events=False
    )
    assert summary["event_count"] == 0
    event_cols = [c for c in df.columns if c.startswith("event_")]
    assert len(event_cols) == 0


def test_validate_mean_reversion_features(sample_ohlcv):
    builder = MeanReversionFeatureSetBuilder()
    df, summary = builder.build_compact_mean_reversion_features(sample_ohlcv)
    val_res = builder.validate_mean_reversion_features(df)
    assert val_res["valid"] is True
    assert val_res["has_inf"] is False


def test_summary_contains_strong_trend_warning(sample_ohlcv):
    builder = MeanReversionFeatureSetBuilder()
    df, summary = builder.build_compact_mean_reversion_features(sample_ohlcv)
    warnings = "\n".join(summary.get("warnings", []))
    assert "strong trends" in warnings.lower()
