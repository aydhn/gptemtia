import pandas as pd
import numpy as np
import pytest
from indicators.volume_events import (
    detect_volume_spike_events,
    detect_volume_dryup_events,
    detect_money_flow_events,
    detect_cmf_accumulation_distribution_events,
    detect_obv_confirmation_events,
    detect_price_volume_divergence_events,
    detect_liquidity_events,
    build_volume_event_frame,
    VolumeEventConfig,
)


@pytest.fixture
def sample_features():
    dates = pd.date_range("2020-01-01", periods=100)
    return pd.DataFrame(
        {
            "volume_zscore_20": np.random.uniform(-3, 3, 100),
            "mfi_14": np.random.uniform(10, 90, 100),
            "cmf_20": np.random.uniform(-0.1, 0.1, 100),
            "obv_slope_10": np.random.uniform(-1, 1, 100),
            "close": np.random.uniform(90, 110, 100),
            "price_volume_diverge_10_20": np.random.uniform(-0.1, 0.1, 100),
            "liquidity_proxy_20": np.random.uniform(1, 10, 100),
            "liquidity_proxy_50": np.random.uniform(1, 10, 100),
            "volume_is_usable": [True] * 100,
        },
        index=dates,
    )


def test_detect_volume_spike_events(sample_features):
    res = detect_volume_spike_events(sample_features)
    assert "event_volume_spike" in res.columns


def test_detect_volume_dryup_events(sample_features):
    res = detect_volume_dryup_events(sample_features)
    assert "event_volume_dryup" in res.columns


def test_detect_money_flow_events(sample_features):
    res = detect_money_flow_events(sample_features)
    assert "event_mfi_14_oversold" in res.columns


def test_detect_cmf_accumulation_distribution_events(sample_features):
    res = detect_cmf_accumulation_distribution_events(sample_features)
    assert "event_cmf_accumulation" in res.columns


def test_detect_obv_confirmation_events(sample_features):
    res = detect_obv_confirmation_events(sample_features)
    assert "event_obv_rising_confirmation" in res.columns


def test_detect_price_volume_divergence_events(sample_features):
    res = detect_price_volume_divergence_events(sample_features)
    assert "event_price_volume_bullish_divergence_candidate" in res.columns


def test_detect_liquidity_events(sample_features):
    res = detect_liquidity_events(sample_features)
    assert "event_liquidity_thin" in res.columns


def test_build_volume_event_frame(sample_features):
    res, summary = build_volume_event_frame(sample_features)
    assert "event_volume_spike" in res.columns
    assert "event_volume_unusable" in res.columns
    assert summary["volume_usable"] == True
