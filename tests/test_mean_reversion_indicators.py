import pytest
import pandas as pd
from advanced_technical_indicators.mean_reversion_indicators import (
    add_rolling_zscore,
    add_distance_to_sma,
    add_distance_to_ema,
    add_rolling_percentile_rank_placeholder,
    add_rolling_deviation_ratio,
    build_mean_reversion_indicator_expansion_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_df():
    return pd.DataFrame({"close": [100.0 + i for i in range(30)]})


def test_mean_reversion_indicators(sample_df):
    orig = sample_df.copy()

    df1 = add_rolling_zscore(sample_df, window=10)
    assert "rolling_zscore_10" in df1.columns
    assert sample_df.equals(orig)

    df2 = add_distance_to_sma(sample_df, window=10)
    assert "dist_to_sma_10" in df2.columns

    df3 = add_distance_to_ema(sample_df, window=10)
    assert "dist_to_ema_10" in df3.columns

    df4 = add_rolling_percentile_rank_placeholder(sample_df, window=10)
    assert "rolling_percentile_rank_10" in df4.columns

    df5 = add_rolling_deviation_ratio(sample_df, window=10)
    assert "rolling_deviation_ratio_10" in df5.columns


def test_mean_reversion_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_mean_reversion_indicator_expansion_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
