import pytest
from advanced_factor_metadata.trend_factor_families import (
    build_trend_factor_family_registry,
    summarize_trend_factor_family,
)


def test_build_trend_factor_family_registry():
    df, summary = build_trend_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 4
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_trend_ma_slope_context" in names
    assert "factor_trend_macd_context" in names
    assert "factor_trend_donchian_context" in names
    assert "factor_trend_multi_window_context" in names

    stats = summarize_trend_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["non_signal"] is True
