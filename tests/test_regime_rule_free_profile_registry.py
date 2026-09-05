from advanced_regime_rule_free.regime_rule_free_profile_registry import (
    build_regime_rule_free_profile_registry,
)


def test_build_regime_rule_free_profile_registry():
    df, summary = build_regime_rule_free_profile_registry()
    assert not df.empty
    assert len(df) >= 3
    assert summary["current_phase"] == 128
    assert summary["next_phase"] == 129
    assert summary["target_final_phase"] == 160
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True
    assert summary["all_clustering_disallowed"] is True
    assert summary["all_model_training_disallowed"] is True
    assert "balanced_local_regime_rule_free_prep" in df["profile_name"].values
