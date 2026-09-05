from advanced_regime_foundation.regime_foundation_profile_registry import (
    build_regime_foundation_profile_registry,
)


def test_regime_foundation_profile_registry():
    df, summary = build_regime_foundation_profile_registry()
    assert not df.empty
    assert len(df) >= 3
    assert summary["all_non_signal"] is True
    assert summary["all_local_only"] is True
    assert summary["all_model_training_disabled"] is True
    assert summary["all_clustering_disabled"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["current_phase"] == 126
    assert summary["next_phase"] == 127
    assert summary["target_final_phase"] == 160
