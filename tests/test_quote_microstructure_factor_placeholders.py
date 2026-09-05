import pytest
from advanced_factor_metadata.quote_microstructure_factor_placeholders import (
    build_quote_microstructure_factor_placeholder_registry,
    summarize_quote_microstructure_factor_placeholders,
)


def test_build_quote_microstructure_factor_placeholder_registry():
    df, summary = build_quote_microstructure_factor_placeholder_registry()
    assert not df.empty
    assert summary["total_factors"] >= 3
    assert summary["placeholder_factors"] == len(df)
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_quote_spread_context_placeholder" in names
    assert "factor_quote_mid_change_context_placeholder" in names
    assert "factor_quote_staleness_context_placeholder" in names

    stats = summarize_quote_microstructure_factor_placeholders(df)
    assert stats["total_factors"] == len(df)
    assert stats["manual_review_required"] is True
    assert stats["non_signal"] is True
