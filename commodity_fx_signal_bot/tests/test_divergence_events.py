import pandas as pd
import pytest

from indicators.divergence_events import (
    DivergenceEventConfig,
    detect_bullish_divergence_events,
    detect_bearish_divergence_events,
    detect_multi_indicator_divergence_cluster,
    detect_volume_price_divergence_events,
    detect_momentum_weakening_events,
    build_divergence_event_frame,
)


@pytest.fixture
def synthetic_features():
    return pd.DataFrame(
        {
            "div_regular_bullish_rsi_14": [0, 1, 0, 0, 1],
            "div_regular_bearish_rsi_14": [1, 0, 0, 0, 0],
            "div_hidden_bullish_rsi_14": [0, 0, 0, 1, 0],
            "div_regular_bullish_macd_hist_12_26_9": [0, 0, 0, 0, 1],
            "div_regular_bullish_obv": [0, 0, 0, 0, 1],
            "div_regular_bearish_obv": [0, 0, 1, 0, 0],
        }
    )


def test_detect_bullish_divergence_events(synthetic_features):
    config = DivergenceEventConfig()
    events = detect_bullish_divergence_events(synthetic_features, config)

    assert "event_regular_bullish_divergence_candidate" in events.columns
    assert "event_hidden_bullish_divergence_candidate" in events.columns
    assert "event_bullish_divergence_candidate" in events.columns

    assert events["event_regular_bullish_divergence_candidate"].tolist() == [
        0,
        1,
        0,
        0,
        1,
    ]
    assert events["event_hidden_bullish_divergence_candidate"].tolist() == [
        0,
        0,
        0,
        1,
        0,
    ]
    assert events["event_bullish_divergence_candidate"].tolist() == [0, 1, 0, 1, 1]


def test_detect_multi_indicator_divergence_cluster(synthetic_features):
    config = DivergenceEventConfig(
        require_recent_confirmation=True, confirmation_window=2
    )
    events = detect_multi_indicator_divergence_cluster(synthetic_features, config)

    assert "event_regular_bullish_divergence_cluster" in events.columns
    # At index 4, rsi and macd and obv all fired (3 indicators)
    assert events["event_regular_bullish_divergence_cluster"].iloc[4] == 1


def test_detect_volume_price_divergence_events(synthetic_features):
    config = DivergenceEventConfig()
    events = detect_volume_price_divergence_events(synthetic_features, config)

    assert "event_volume_price_bullish_divergence_candidate" in events.columns
    assert events["event_volume_price_bullish_divergence_candidate"].iloc[4] == 1

    assert "event_volume_price_bearish_divergence_candidate" in events.columns
    assert events["event_volume_price_bearish_divergence_candidate"].iloc[2] == 1


def test_detect_momentum_weakening_events(synthetic_features):
    config = DivergenceEventConfig()
    events = detect_momentum_weakening_events(synthetic_features, config)

    assert "event_momentum_weakening_bullish_candidate" in events.columns
    # RSI and MACD should trigger it
    assert events["event_momentum_weakening_bullish_candidate"].iloc[4] == 1


def test_build_divergence_event_frame(synthetic_features):
    config = DivergenceEventConfig()
    out, summary = build_divergence_event_frame(synthetic_features, config)

    assert len(out.columns) > 0
    assert "event_bullish_divergence_candidate" in out.columns
    assert "event_volume_price_bullish_divergence_candidate" in out.columns
    assert "event_momentum_weakening_bullish_candidate" in out.columns
    assert summary["input_rows"] == 5

    # Ensure no values outside 0 and 1
    for col in out.columns:
        unique_vals = set(out[col].unique())
        assert unique_vals.issubset({0, 1})
