from advanced_regime_rule_free.regime_candidate_state_context import (
    build_regime_candidate_state_context_registry,
    summarize_regime_candidate_state_context,
)


def test_build_regime_candidate_state_context_registry():
    df, summary = build_regime_candidate_state_context_registry()
    assert len(df) == 8
    assert summary["all_non_signal"] is True
    assert summary["all_not_signal"] is True
    assert summary["status"] == "VALID"

    ctx_ids = df["context_id"].tolist()
    assert "volatility_candidate_context" in ctx_ids
    assert "trend_candidate_context" in ctx_ids
    assert "range_candidate_context" in ctx_ids
    assert "macro_event_candidate_context" in ctx_ids
    assert "news_attention_candidate_context" in ctx_ids
    assert "cross_asset_candidate_context" in ctx_ids
    assert "transition_candidate_context" in ctx_ids
    assert "uncertainty_candidate_context" in ctx_ids
