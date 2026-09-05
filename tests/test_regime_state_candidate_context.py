from advanced_regime_matrix.regime_state_candidate_context import (
    build_regime_state_candidate_contexts,
    is_valid_regime_state_candidate_context,
)


def test_build_regime_state_candidate_contexts():
    df, s = build_regime_state_candidate_contexts()
    assert len(df) == 10
    assert s["total_candidate_contexts"] == 10
    assert s["candidate_contexts_as_targets"] is False
    assert s["all_research_only"] is True

    contexts = set(df["context_name"].values)
    assert "volatility_expansion_context" in contexts
    assert "trend_strong_bull_context" in contexts
    assert "range_tight_compression_context" in contexts
    assert "liquidity_stress_context" in contexts

    assert is_valid_regime_state_candidate_context("volatility_expansion_context") is True
    assert is_valid_regime_state_candidate_context("target_buy_label") is False
