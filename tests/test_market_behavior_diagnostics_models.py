from advanced_market_behavior_diagnostics.market_behavior_diagnostics_models import (
    CandidateStateQualityMetric,
    BehaviorQualityScore,
    BehaviorQualityFinding,
    BehaviorDiagnosticsManifest,
)


def test_market_behavior_diagnostics_models_instantiation():
    metric = CandidateStateQualityMetric(
        metric_name="candidate_state_coverage_ratio",
        domain="coverage",
        description="Metric coverage check",
        max_value=1.0,
        is_blocking=False,
    )
    assert metric.non_signal is True
    assert metric.metric_name == "candidate_state_coverage_ratio"

    score = BehaviorQualityScore(
        score_name="market_behavior_quality_score",
        overall_quality_score=0.96,
        candidate_state_quality_score=0.98,
        regime_family_quality_score=0.95,
        behavior_context_quality_score=0.94,
        transition_readiness_score=0.97,
        stability_readiness_score=0.96,
        quality_grade="HIGH_CONFIDENCE_DIAGNOSTICS",
    )
    assert score.non_signal is True
    assert score.official_approval is False
    assert score.production_ready is False

    finding = BehaviorQualityFinding(
        finding_id="BEH-QUAL-001",
        finding_type="candidate_state_ambiguity_warning",
        behavior_family="volatility",
        severity="INFO",
        message="Informational test finding",
        recommendation="Review context definition",
    )
    assert finding.non_signal is True
    assert finding.destructive_action_allowed is False


    manifest = BehaviorDiagnosticsManifest(
        manifest_name="test_manifest",
        overall_quality_score=0.95,
    )
    assert manifest.current_phase == 129
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 130
    assert manifest.clustering_executed is False
    assert manifest.model_training_executed is False
