import pytest
from advanced_factor_metadata.composite_factor_placeholders import (
    build_composite_factor_placeholder_registry,
    summarize_composite_factor_placeholders,
)


def test_build_composite_factor_placeholder_registry():
    df, summary = build_composite_factor_placeholder_registry()
    assert not df.empty
    assert summary["total_factors"] >= 3
    assert summary["placeholder_factors"] == len(df)
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_composite_technical_context_placeholder" in names
    assert "factor_composite_macro_event_context_placeholder" in names
    assert "factor_composite_cross_asset_context_placeholder" in names

    stats = summarize_composite_factor_placeholders(df)
    assert stats["total_factors"] == len(df)
    assert stats["manual_review_required"] is True
    assert stats["non_signal"] is True
