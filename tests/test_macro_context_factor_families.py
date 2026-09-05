import pytest
from advanced_factor_metadata.macro_context_factor_families import (
    build_macro_context_factor_family_registry,
    summarize_macro_context_factor_family,
)


def test_build_macro_context_factor_family_registry():
    df, summary = build_macro_context_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 4
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_macro_inflation_context" in names
    assert "factor_macro_rate_context" in names
    assert "factor_macro_growth_context" in names
    assert "factor_macro_revision_context" in names
    assert "factor_macro_surprise_placeholder_context" in names

    stats = summarize_macro_context_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["non_signal"] is True
