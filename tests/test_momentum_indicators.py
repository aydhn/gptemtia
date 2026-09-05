import pytest
import pandas as pd
from advanced_technical_indicators.momentum_indicators import (
    add_momentum,
    add_roc,
    add_rsi,
    add_cmo,
    add_tsi_placeholder,
    build_momentum_indicator_expansion_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_df():
    return pd.DataFrame({"close": [100.0 + i for i in range(40)]})


def test_momentum_indicators(sample_df):
    orig = sample_df.copy()

    df1 = add_momentum(sample_df, window=10)
    assert "momentum_10" in df1.columns
    assert sample_df.equals(orig)

    df2 = add_roc(sample_df, window=10)
    assert "roc_10" in df2.columns

    df3 = add_rsi(sample_df, window=14)
    assert "rsi_14" in df3.columns

    df4 = add_cmo(sample_df, window=14)
    assert "cmo_14" in df4.columns

    df5 = add_tsi_placeholder(sample_df)
    assert "tsi_25_13" in df5.columns


def test_momentum_forbidden(sample_df):
    with pytest.raises(ValueError):
        add_rsi(sample_df, output_field="signal")


def test_momentum_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_momentum_indicator_expansion_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
