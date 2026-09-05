import pytest
from advanced_factor_metadata.momentum_factor_families import (
    build_momentum_factor_family_registry,
    summarize_momentum_factor_family,
)


def test_build_momentum_factor_family_registry():
    df, summary = build_momentum_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 4
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_momentum_rsi_context" in names
    assert "factor_momentum_roc_context" in names
    assert "factor_momentum_stochastic_context" in names
    assert "factor_momentum_multi_window_context" in names

    stats = summarize_momentum_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["non_signal"] is True
