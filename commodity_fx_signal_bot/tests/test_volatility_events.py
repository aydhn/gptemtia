import numpy as np
import pandas as pd
import pytest

from indicators.volatility_events import (
    VolatilityEventConfig,
    build_volatility_event_frame,
    detect_atr_regime_events,
    detect_channel_breakout_setup_events,
    detect_channel_compression_events,
    detect_gap_volatility_events,
    detect_range_shock_events,
    detect_volatility_expansion_events,
    detect_volatility_squeeze_events,
)


@pytest.fixture
def sample_features():
    dates = pd.date_range("2023-01-01", periods=10)
    df = pd.DataFrame(
        {
            "percentile_bb_width_20_2_120": [0.5, 0.05, 0.05, 0.5, 0.95, 0.95, 0.5, 0.5, 0.5, 0.5],
            "atr_pct_14": [0.01, 0.02, 0.04, 0.04, 0.02, 0.005, 0.005, 0.01, 0.01, 0.01],
            "slope_atr_pct_14_5": [0.0, 0.0, 0.1, 0.1, -0.1, -0.1, 0.0, 0.0, 0.0, 0.0],
            "percentile_hist_vol_20_120": [0.5, 0.05, 0.05, 0.5, 0.95, 0.95, 0.5, 0.5, 0.5, 0.5],
            "range_pct": [0.01, 0.01, 0.05, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01],
            "abs_gap_pct": [0.001, 0.001, 0.001, 0.02, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001],
            "percentile_donchian_width_20_120": [0.5, 0.05, 0.05, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            "channel_pos_donchian20": [0.5, 0.5, 0.5, 0.5, 0.98, 0.02, 0.5, 0.5, 0.5, 0.5],
        },
        index=dates,
    )
    return df


def test_detect_volatility_squeeze_events(sample_features):
    res = detect_volatility_squeeze_events(sample_features)
    assert "event_volatility_squeeze_bb20" in res.columns
    assert res["event_volatility_squeeze_bb20"].iloc[1] == 1  # 0.05 < 0.10
    assert res["event_volatility_squeeze_bb20"].iloc[0] == 0


def test_detect_volatility_expansion_events(sample_features):
    res = detect_volatility_expansion_events(sample_features)
    assert "event_volatility_expansion_bb20" in res.columns
    assert res["event_volatility_expansion_bb20"].iloc[4] == 1  # 0.95 > 0.90
    assert res["event_volatility_expansion_bb20"].iloc[0] == 0


def test_detect_atr_regime_events(sample_features):
    res = detect_atr_regime_events(sample_features)
    assert "event_atr_pct_high" in res.columns
    assert "event_atr_pct_low" in res.columns
    assert "event_atr_pct_rising" in res.columns
    assert "event_atr_pct_falling" in res.columns
    assert res["event_atr_pct_high"].iloc[2] == 1  # 0.04 > 0.03
    assert res["event_atr_pct_low"].iloc[5] == 1  # 0.005 < 0.01
    assert res["event_atr_pct_rising"].iloc[2] == 1
    assert res["event_atr_pct_falling"].iloc[4] == 1


def test_detect_range_shock_events(sample_features):
    res = detect_range_shock_events(sample_features)
    assert "event_range_shock_high" in res.columns
    assert res["event_range_shock_high"].iloc[2] == 1


def test_detect_gap_volatility_events(sample_features):
    res = detect_gap_volatility_events(sample_features)
    assert "event_gap_volatility_high" in res.columns
    assert res["event_gap_volatility_high"].iloc[3] == 1


def test_detect_channel_compression_events(sample_features):
    res = detect_channel_compression_events(sample_features)
    assert "event_channel_compression_donchian20" in res.columns
    assert res["event_channel_compression_donchian20"].iloc[1] == 1


def test_detect_channel_breakout_setup_events(sample_features):
    res = detect_channel_breakout_setup_events(sample_features)
    assert "event_channel_breakout_setup_upper" in res.columns
    assert "event_channel_breakout_setup_lower" in res.columns
    assert res["event_channel_breakout_setup_upper"].iloc[4] == 1
    assert res["event_channel_breakout_setup_lower"].iloc[5] == 1


def test_build_volatility_event_frame(sample_features):
    df, summary = build_volatility_event_frame(sample_features)
    assert not df.empty
    assert "event_volatility_squeeze_bb20" in df.columns
    assert summary["total_event_count"] > 0

    # Ensure no buy/sell naming
    for col in df.columns:
        assert "buy" not in col.lower()
        assert "sell" not in col.lower()
        assert "signal" not in col.lower()
