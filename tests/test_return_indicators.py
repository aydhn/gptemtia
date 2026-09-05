import pytest
import pandas as pd
from advanced_technical_indicators.return_indicators import (
    add_simple_return,
    add_log_return,
    add_cumulative_return,
    add_rolling_return_sum,
    add_return_volatility_ratio,
    build_return_indicator_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_df():
    return pd.DataFrame({"close": [100.0 + i for i in range(30)]})


def test_return_indicators(sample_df):
    orig = sample_df.copy()

    df1 = add_simple_return(sample_df, window=1)
    assert "simple_return_1" in df1.columns
    assert sample_df.equals(orig)

    df2 = add_log_return(sample_df, window=1)
    assert "log_return_1" in df2.columns

    df3 = add_cumulative_return(sample_df, window=5)
    assert "cumulative_return_5" in df3.columns

    df4 = add_rolling_return_sum(sample_df, window=5)
    assert "rolling_return_sum_5" in df4.columns

    df5 = add_return_volatility_ratio(sample_df, window=5)
    assert "return_vol_ratio_5" in df5.columns


def test_return_forbidden(sample_df):
    with pytest.raises(ValueError):
        add_simple_return(sample_df, output_field="future_return")


def test_return_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_return_indicator_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
