from advanced_regime_foundation.macro_regime_context import (
    build_macro_regime_context_registry,
    summarize_macro_regime_context,
)


def test_macro_regime_context():
    df, summary = build_macro_regime_context_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True

    ctx_names = list(df["context_name"])
    assert "inflation_context" in ctx_names
    assert "rate_context" in ctx_names
    assert "growth_context" in ctx_names
    assert "macro_revision_context" in ctx_names
    assert "macro_release_context" in ctx_names

    summ = summarize_macro_regime_context(df)
    assert summ["total_contexts"] == 5
    assert summ["non_signal"] is True
