import numpy as np
import pandas as pd
import pytest

from indicators.volume_feature_set import VolumeFeatureSetBuilder


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2020-01-01", periods=100)
    np.random.seed(42)
    return pd.DataFrame(
        {
            "open": np.random.uniform(100, 110, 100),
            "high": np.random.uniform(110, 120, 100),
            "low": np.random.uniform(90, 100, 100),
            "close": np.random.uniform(95, 115, 100),
            "volume": np.random.uniform(1000, 5000, 100),
        },
        index=dates,
    )


def test_build_compact_volume_features(sample_ohlcv):
    builder = VolumeFeatureSetBuilder()
    df, summary = builder.build_compact_volume_features(
        sample_ohlcv, include_events=True
    )
    assert "volume_sma_20" in df.columns
    assert "event_volume_spike" in df.columns
    assert summary["volume_usable"] == True


def test_build_volume_features_no_events(sample_ohlcv):
    builder = VolumeFeatureSetBuilder()
    df, summary = builder.build_volume_features(sample_ohlcv, include_events=False)
    assert "volume_sma_20" in df.columns
    assert "event_volume_spike" not in df.columns
