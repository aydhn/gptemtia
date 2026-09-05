import pytest
import pandas as pd
from advanced_technical_indicators.price_action_indicators import (
    add_high_low_range,
    add_close_open_range,
    add_range_pct,
    add_gap_from_previous_close,
    add_close_location_value,
    build_price_action_indicator_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "open": [100.0, 102.0, 101.0],
        "high": [105.0, 106.0, 104.0],
        "low": [98.0, 100.0, 99.0],
        "close": [103.0, 104.0, 102.0],
    })


def test_price_action_indicators(sample_df):
    orig = sample_df.copy()

    df1 = add_high_low_range(sample_df)
    assert "high_low_range" in df1.columns
    assert sample_df.equals(orig)

    df2 = add_close_open_range(sample_df)
    assert "close_open_range" in df2.columns

    df3 = add_range_pct(sample_df)
    assert "range_pct" in df3.columns

    df4 = add_gap_from_previous_close(sample_df)
    assert "gap_from_prev_close" in df4.columns

    df5 = add_close_location_value(sample_df)
    assert "close_location_value" in df5.columns


def test_price_action_forbidden_and_errors(sample_df):
    with pytest.raises(ValueError):
        add_high_low_range(sample_df, output_field="signal")

    with pytest.raises(ValueError):
        add_high_low_range(pd.DataFrame({"close": [1]}), high_field="high")


def test_price_action_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_price_action_indicator_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
