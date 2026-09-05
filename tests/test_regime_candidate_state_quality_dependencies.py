from advanced_regime_rule_free.regime_candidate_state_quality_dependencies import (
    build_regime_candidate_state_quality_dependency_registry,
    summarize_candidate_state_quality_dependencies,
    QUALITY_DEPENDENCIES,
)


def test_build_regime_candidate_state_quality_dependency_registry():
    df, summary = build_regime_candidate_state_quality_dependency_registry()
    assert len(df) == 6
    assert summary["total_quality_dependencies"] == 6
    assert summary["blocking_dependencies_count"] == 6
    assert summary["all_non_signal"] is True
    assert summary["status"] == "VALID"

    dep_ids = df["dependency_id"].tolist()
    assert "dep_phase_123_quality_score" in dep_ids
    assert "dep_phase_123_drift_score" in dep_ids
    assert "dep_feature_availability" in dep_ids
    assert "dep_staleness_diagnostics" in dep_ids
    assert "dep_namespace_quality" in dep_ids
    assert "dep_manual_review_blocker_status" in dep_ids
