import pytest
from advanced_factor_metadata.cross_asset_context_factor_families import (
    build_cross_asset_context_factor_family_registry,
    summarize_cross_asset_context_factor_family,
)


def test_build_cross_asset_context_factor_family_registry():
    df, summary = build_cross_asset_context_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 5
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_fx_commodity_context" in names
    assert "factor_fx_macro_context" in names
    assert "factor_commodity_macro_context" in names
    assert "factor_macro_calendar_context" in names
    assert "factor_calendar_news_context" in names
    assert "factor_cross_domain_context_placeholder" in names

    stats = summarize_cross_asset_context_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["non_signal"] is True
