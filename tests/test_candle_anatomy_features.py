import pytest
import pandas as pd
from advanced_technical_indicators.candle_anatomy_features import (
    add_candle_body_size,
    add_candle_body_pct,
    add_upper_wick_size,
    add_lower_wick_size,
    add_wick_balance,
    build_candle_anatomy_feature_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "open": [100.0, 102.0],
        "high": [105.0, 106.0],
        "low": [98.0, 99.0],
        "close": [103.0, 101.0],
    })


def test_candle_anatomy_features(sample_df):
    orig = sample_df.copy()

    df1 = add_candle_body_size(sample_df)
    assert "candle_body_size" in df1.columns
    assert sample_df.equals(orig)

    df2 = add_candle_body_pct(sample_df)
    assert "candle_body_pct" in df2.columns

    df3 = add_upper_wick_size(sample_df)
    assert "upper_wick_size" in df3.columns

    df4 = add_lower_wick_size(sample_df)
    assert "lower_wick_size" in df4.columns

    df5 = add_wick_balance(sample_df)
    assert "wick_balance" in df5.columns


def test_candle_anatomy_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_candle_anatomy_feature_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
