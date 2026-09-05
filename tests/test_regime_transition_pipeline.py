"""Tests for Regime Transition Pipeline."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_pipeline import (
    RegimeTransitionPipeline,
)


def test_regime_transition_pipeline_steps():
    profile = get_default_regime_transition_profile()
    pipeline = RegimeTransitionPipeline(profile=profile)

    # Step 1
    dfs_1, s_1 = pipeline.build_profiles_domains_contracts(save=False)
    assert len(dfs_1) == 5
    assert "profiles" in dfs_1

    # Step 2
    dfs_2, s_2 = pipeline.build_metrics_thresholds_guards(save=False)
    assert len(dfs_2) == 6
    assert "transition_metrics" in dfs_2

    # Step 3
    dfs_3, s_3 = pipeline.build_state_transition_diagnostics(save=False)
    assert len(dfs_3) == 6
    assert "persistence" in dfs_3

    # Step 4
    dfs_4, s_4 = pipeline.build_regime_family_transition_reports(save=False)
    assert len(dfs_4) == 3
    assert "volatility_transition" in dfs_4

    # Step 5
    dfs_5, s_5 = pipeline.build_macro_news_cross_asset_context(save=False)
    assert len(dfs_5) == 3
    assert "macro_event_context" in dfs_5

    # Step 6
    dfs_6, s_6 = pipeline.build_dependencies_findings_scoring_manifest(save=False)
    assert len(dfs_6) == 6
    assert "manifest" in dfs_6

    # Step 7
    dfs_7, s_7 = pipeline.build_health_validation_safety_handoff(save=False)
    assert len(dfs_7) == 4
    assert "validation" in dfs_7

    # Master Status
    df_status, s_all = pipeline.build_regime_transition_status(save=False)
    assert not df_status.empty
    assert s_all["overall_status"] == "READY"
    assert s_all["non_signal"] is True
    assert s_all["current_phase"] == 130
    assert s_all["next_phase"] == 131
    assert s_all["target_final_phase"] == 160
