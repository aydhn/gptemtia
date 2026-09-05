import pytest
import pandas as pd
from advanced_technical_indicators.moving_average_indicators import (
    add_sma,
    add_ema,
    add_wma,
    add_dema,
    add_tema,
    add_moving_average_distance,
    build_moving_average_indicator_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_df():
    return pd.DataFrame({"close": [100.0 + i * 0.5 for i in range(40)]})


def test_moving_average_indicators(sample_df):
    orig = sample_df.copy()

    df1 = add_sma(sample_df, window=5)
    assert "sma_5" in df1.columns
    assert sample_df.equals(orig)

    df2 = add_ema(sample_df, window=5)
    assert "ema_5" in df2.columns

    df3 = add_wma(sample_df, window=5)
    assert "wma_5" in df3.columns

    df4 = add_dema(sample_df, window=5)
    assert "dema_5" in df4.columns

    df5 = add_tema(sample_df, window=5)
    assert "tema_5" in df5.columns

    df6 = add_moving_average_distance(sample_df, window=5)
    assert "ma_distance_5" in df6.columns


def test_ma_forbidden(sample_df):
    with pytest.raises(ValueError):
        add_sma(sample_df, output_field="buy")


def test_ma_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_moving_average_indicator_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
