import pytest
from advanced_factor_metadata.return_factor_families import (
    build_return_factor_family_registry,
    summarize_return_factor_family,
)


def test_build_return_factor_family_registry():
    df, summary = build_return_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 3
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_return_short_window_context" in names
    assert "factor_return_medium_window_context" in names
    assert "factor_return_multi_horizon_context" in names

    stats = summarize_return_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["non_signal"] is True
