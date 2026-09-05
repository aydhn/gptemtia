import pytest
import pandas as pd
from advanced_technical_indicators.oscillator_indicators import (
    add_stochastic_oscillator,
    add_williams_r,
    add_cci,
    add_ultimate_oscillator_placeholder,
    add_mfi_placeholder,
    build_oscillator_indicator_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_ohlcv():
    n = 50
    return pd.DataFrame({
        "open": [100.0 + i for i in range(n)],
        "high": [102.0 + i for i in range(n)],
        "low": [98.0 + i for i in range(n)],
        "close": [101.0 + i for i in range(n)],
        "volume": [1000] * n,
    })


def test_oscillator_indicators(sample_ohlcv):
    orig = sample_ohlcv.copy()

    df1 = add_stochastic_oscillator(sample_ohlcv, k_window=14, d_window=3)
    assert "stoch_k_14" in df1.columns
    assert "stoch_d_14_3" in df1.columns
    assert sample_ohlcv.equals(orig)

    df2 = add_williams_r(sample_ohlcv, window=14)
    assert "williams_r_14" in df2.columns

    df3 = add_cci(sample_ohlcv, window=20)
    assert "cci_20" in df3.columns

    df4 = add_ultimate_oscillator_placeholder(sample_ohlcv)
    assert "ultimate_osc" in df4.columns

    df5 = add_mfi_placeholder(sample_ohlcv, window=14)
    assert "mfi_14" in df5.columns


def test_mfi_graceful_missing_volume():
    no_vol = pd.DataFrame({
        "high": [102.0, 103.0],
        "low": [98.0, 99.0],
        "close": [101.0, 102.0],
    })
    df = add_mfi_placeholder(no_vol, window=14)
    assert "mfi_14" in df.columns
    assert df["mfi_14"].isna().all()


def test_oscillator_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_oscillator_indicator_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
