import numpy as np
import pandas as pd
import pytest

from indicators.divergence import (
    DivergenceConfig,
    detect_regular_bullish_divergence,
    detect_regular_bearish_divergence,
    detect_hidden_bullish_divergence,
    detect_hidden_bearish_divergence,
    calculate_divergence_strength,
    build_divergence_feature_frame,
)


@pytest.fixture
def synthetic_df():
    # Regular Bullish Divergence Example:
    # Price makes Lower Low, Indicator makes Higher Low

    price = [10.0, 9.0, 8.0, 9.0, 10.0, 9.0, 7.0, 8.0, 9.0]
    rsi = [50.0, 40.0, 30.0, 40.0, 50.0, 40.0, 35.0, 45.0, 55.0]

    # Pivot lows at index 2 (price=8, rsi=30) and index 6 (price=7, rsi=35)
    # P2 (7) < P1 (8)
    # I2 (35) > I1 (30) -> Regular Bullish

    return pd.DataFrame({"close": price, "rsi_14": rsi})


@pytest.fixture
def synthetic_df_bearish():
    # Regular Bearish Divergence Example:
    # Price makes Higher High, Indicator makes Lower High
    price = [10.0, 11.0, 12.0, 11.0, 10.0, 11.0, 13.0, 11.0, 10.0]
    rsi = [50.0, 60.0, 70.0, 60.0, 50.0, 60.0, 65.0, 60.0, 50.0]

    # Pivot highs at index 2 (price=12, rsi=70) and index 6 (price=13, rsi=65)
    # P2 (13) > P1 (12)
    # I2 (65) < I1 (70) -> Regular Bearish

    return pd.DataFrame({"close": price, "rsi_14": rsi})


def test_detect_regular_bullish_divergence(synthetic_df):
    config = DivergenceConfig(
        pivot_left=2, pivot_right=2, min_price_move_pct=0.0, min_indicator_move=0.0
    )
    div = detect_regular_bullish_divergence(synthetic_df, "rsi_14", config)

    assert div.sum() == 1
    assert div.iloc[6] == 1


def test_detect_regular_bearish_divergence(synthetic_df_bearish):
    config = DivergenceConfig(
        pivot_left=2, pivot_right=2, min_price_move_pct=0.0, min_indicator_move=0.0
    )
    div = detect_regular_bearish_divergence(synthetic_df_bearish, "rsi_14", config)

    assert div.sum() == 1
    assert div.iloc[6] == 1


def test_calculate_divergence_strength(synthetic_df):
    config = DivergenceConfig(
        pivot_left=2, pivot_right=2, min_price_move_pct=0.0, min_indicator_move=0.0
    )
    strength = calculate_divergence_strength(synthetic_df, "rsi_14", "bullish", config)

    # index 6 strength
    # price change pct = abs(7 - 8) / 8 = 1/8 = 0.125
    # ind change = abs(35 - 30) = 5
    # strength = 0.125 * 5 = 0.625

    assert np.isclose(strength.iloc[6], 0.625)


def test_build_divergence_feature_frame(synthetic_df):
    config = DivergenceConfig(
        pivot_left=2,
        pivot_right=2,
        min_price_move_pct=0.0,
        indicator_columns=("rsi_14", "macd_hist_12_26_9"),  # macd is missing
    )

    df_out, summary = build_divergence_feature_frame(synthetic_df, config)

    assert "macd_hist_12_26_9" in summary["missing_indicator_columns"]
    assert "div_regular_bullish_rsi_14" in df_out.columns
    assert "div_hidden_bearish_rsi_14" in df_out.columns

    # Check that it doesn't crash on missing col
    assert "div_regular_bullish_macd_hist_12_26_9" not in df_out.columns
