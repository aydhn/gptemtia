import pytest
from advanced_factor_metadata.volatility_factor_families import (
    build_volatility_factor_family_registry,
    summarize_volatility_factor_family,
)


def test_build_volatility_factor_family_registry():
    df, summary = build_volatility_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 4
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_volatility_atr_context" in names
    assert "factor_volatility_realized_context" in names
    assert "factor_volatility_bollinger_width_context" in names
    assert "factor_volatility_range_context" in names

    stats = summarize_volatility_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["non_signal"] is True
