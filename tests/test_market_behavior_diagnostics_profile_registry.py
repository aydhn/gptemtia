from advanced_market_behavior_diagnostics.market_behavior_diagnostics_profile_registry import (
    build_market_behavior_diagnostics_profile_registry,
    summarize_market_behavior_diagnostics_profiles,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)


def test_market_behavior_diagnostics_profile_registry():
    profile = get_default_market_behavior_diagnostics_profile()
    df, summary = build_market_behavior_diagnostics_profile_registry(profile)

    assert not df.empty
    assert len(df) >= 3
    assert "profile_name" in df.columns
    assert summary["current_phase"] == 129
    assert summary["next_phase"] == 130
    assert summary["target_final_phase"] == 160
    assert summary["non_signal"] is True
    assert summary["clustering_executed"] is False
    assert summary["model_training_executed"] is False
