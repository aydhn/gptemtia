from advanced_regime_rule_free.regime_candidate_state_metadata import (
    build_regime_candidate_state_metadata_registry,
    summarize_regime_candidate_state_metadata,
    CANDIDATE_STATE_METADATA_ITEMS,
)


def test_build_regime_candidate_state_metadata_registry():
    df, summary = build_regime_candidate_state_metadata_registry()
    assert len(df) == 8
    assert summary["total_candidate_metadata_records"] == 8
    assert summary["all_non_signal"] is True
    assert summary["all_phase_129_ready"] is True
    assert summary["status"] == "VALID"

    families = df["candidate_state_family"].tolist()
    assert "volatility" in families
    assert "trend" in families
    assert "range" in families
    assert "macro_event" in families
    assert "news_attention" in families
    assert "cross_asset" in families
    assert "transition" in families
    assert "uncertain" in families
