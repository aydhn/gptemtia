import numpy as np
import pandas as pd
import pytest

from indicators.price_action_feature_set import PriceActionFeatureSetBuilder


@pytest.fixture
def sample_ohlcv():
    data = {
        "open": [100, 105, 110, 108, 102],
        "high": [110, 115, 112, 109, 105],
        "low": [90, 100, 105, 100, 95],
        "close": [105, 110, 108, 102, 100],
        "volume": [1000, 1500, 1200, 800, 900],
    }
    for _ in range(50):
        data["open"].append(100)
        data["high"].append(110)
        data["low"].append(90)
        data["close"].append(105)
        data["volume"].append(1000)

    df = pd.DataFrame(data)
    df.index = pd.date_range(start="2023-01-01", periods=len(df), freq="D")
    return df


def test_build_compact_price_action_features(sample_ohlcv):
    builder = PriceActionFeatureSetBuilder()
    df, summary = builder.build_compact_price_action_features(
        sample_ohlcv, include_events=True
    )

    assert not df.empty
    assert "candle_body" in df.columns
    assert "candle_range" in df.columns


def test_build_price_action_features_full(sample_ohlcv):
    builder = PriceActionFeatureSetBuilder()
    full_df, full_summary = builder.build_price_action_features(
        sample_ohlcv, include_events=True
    )
    compact_df, compact_summary = builder.build_compact_price_action_features(
        sample_ohlcv, include_events=True
    )

    assert len(full_df.columns) > len(compact_df.columns)


def test_include_events_flag(sample_ohlcv):
    builder = PriceActionFeatureSetBuilder()
    df_no_events, summary_no = builder.build_price_action_features(
        sample_ohlcv, include_events=False
    )
    df_events, summary_yes = builder.build_price_action_features(
        sample_ohlcv, include_events=True
    )

    assert len(summary_no.get("event_columns", [])) == 0
    assert len(summary_yes.get("event_columns", [])) > 0


def test_summary_keys(sample_ohlcv):
    builder = PriceActionFeatureSetBuilder()
    _, summary = builder.build_price_action_features(sample_ohlcv)

    assert "input_rows" in summary
    assert "output_rows" in summary
    assert "feature_columns" in summary
    assert "event_columns" in summary
    assert "feature_count" in summary
    assert "event_count" in summary
    assert "total_nan_ratio" in summary


def test_no_duplicate_columns(sample_ohlcv):
    builder = PriceActionFeatureSetBuilder()
    df, _ = builder.build_price_action_features(sample_ohlcv)
    assert len(df.columns) == len(set(df.columns))


def test_no_infinities(sample_ohlcv):
    builder = PriceActionFeatureSetBuilder()
    # Create an artificial zero range/body
    df = sample_ohlcv.copy()
    df.loc[df.index[-1], ["open", "high", "low", "close"]] = 100

    res, _ = builder.build_price_action_features(df)

    # Check if there are any inf values
    inf_count = np.isinf(res).sum().sum()
    assert inf_count == 0


def test_gap_breakout_warning_in_summary(sample_ohlcv):
    builder = PriceActionFeatureSetBuilder()
    _, summary = builder.build_price_action_features(sample_ohlcv)

    warnings = summary.get("warnings", [])
    found = any("Gap and breakout" in w for w in warnings)
    assert found
