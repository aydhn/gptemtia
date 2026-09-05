from advanced_regime_foundation.event_regime_context import (
    build_event_regime_context_registry,
    summarize_event_regime_context,
)


def test_event_regime_context():
    df, summary = build_event_regime_context_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True

    ctx_names = list(df["context_name"])
    assert "pre_event_context" in ctx_names
    assert "post_event_context" in ctx_names
    assert "event_importance_context" in ctx_names
    assert "release_delay_context" in ctx_names
    assert "event_window_context" in ctx_names

    summ = summarize_event_regime_context(df)
    assert summ["total_contexts"] == 5
    assert summ["non_signal"] is True
