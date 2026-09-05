from advanced_regime_foundation.cross_asset_regime_context import (
    build_cross_asset_regime_context_registry,
    summarize_cross_asset_regime_context,
)


def test_cross_asset_regime_context():
    df, summary = build_cross_asset_regime_context_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True

    ctx_names = list(df["context_name"])
    assert "fx_commodity_context" in ctx_names
    assert "fx_macro_context" in ctx_names
    assert "commodity_macro_context" in ctx_names
    assert "macro_calendar_context" in ctx_names
    assert "calendar_news_context" in ctx_names
    assert "cross_domain_context_placeholder" in ctx_names

    summ = summarize_cross_asset_regime_context(df)
    assert summ["total_contexts"] == 6
    assert summ["non_signal"] is True
