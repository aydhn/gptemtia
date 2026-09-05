import pytest
import pandas as pd
from advanced_technical_indicators.quote_microstructure_features import (
    add_quote_mid,
    add_quote_spread,
    add_quote_spread_pct,
    add_bid_ask_ratio_placeholder,
    add_quote_staleness_placeholder,
    build_quote_microstructure_feature_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_quotes():
    return pd.DataFrame({
        "timestamp": pd.date_range("2026-01-01 09:00:00", periods=5, freq="s"),
        "bid": [1.0850, 1.0851, 1.0849, 1.0850, 1.0852],
        "ask": [1.0852, 1.0853, 1.0851, 1.0852, 1.0854],
    })


def test_quote_microstructure_features(sample_quotes):
    orig = sample_quotes.copy()

    df1 = add_quote_mid(sample_quotes)
    assert "quote_mid" in df1.columns
    assert sample_quotes.equals(orig)

    df2 = add_quote_spread(sample_quotes)
    assert "quote_spread" in df2.columns

    df3 = add_quote_spread_pct(sample_quotes)
    assert "quote_spread_pct" in df3.columns

    df4 = add_bid_ask_ratio_placeholder(sample_quotes)
    assert "bid_ask_ratio_placeholder" in df4.columns

    df5 = add_quote_staleness_placeholder(sample_quotes)
    assert "quote_staleness_placeholder" in df5.columns


def test_quote_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_quote_microstructure_feature_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
