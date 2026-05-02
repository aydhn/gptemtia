import pytest
import pandas as pd
import numpy as np

from regimes.trend_regime import detect_trend_regime


@pytest.fixture
def trend_df():
    # Strong bullish setup
    return pd.DataFrame(
        {
            "adx_14": [10, 20, 30, 40, 50],
            "plus_di_14": [20, 30, 40, 50, 60],
            "minus_di_14": [20, 15, 10, 5, 5],
            "ma_stack_bullish_20_50_200": [1, 1, 1, 1, 1],
            "ma_stack_bearish_20_50_200": [0, 0, 0, 0, 0],
            "macd_hist_12_26_9": [0, 1, 2, 3, 4],
        }
    )


def test_detect_trend_regime(trend_df):
    out, sum_dict = detect_trend_regime(trend_df)

    assert "regime_trend_direction" in out.columns
    assert "regime_trend_strength" in out.columns
    assert "regime_trend_label" in out.columns

    # Last row should be strong bullish
    assert out["regime_trend_label"].iloc[-1] == "strong_bullish_trend"


def test_detect_trend_regime_missing_cols():
    empty_df = pd.DataFrame({"col1": [1, 2, 3]})
    out, sum_dict = detect_trend_regime(empty_df)

    assert len(sum_dict["warnings"]) > 0
    assert out["regime_trend_label"].iloc[-1] == "unknown"
