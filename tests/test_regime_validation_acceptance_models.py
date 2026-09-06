"""Tests for Phase 133 Regime Validation Acceptance Models."""

import pytest
from advanced_regime_validation_acceptance.regime_validation_acceptance_models import (
    RegimeValidationAcceptanceProfileItem,
    RegimeValidationGate,
    RegimeAcceptanceCheckItem,
    RegimeValidationFinding,
    RegimeAcceptanceScore,
    RegimeValidationAcceptanceManifest,
    RegimeAcceptanceManualReviewItem,
)


def test_models_instantiation_and_invariants():
    prof = RegimeValidationAcceptanceProfileItem(
        profile_name="test_profile", description="test profile desc"
    )
    assert prof.current_phase == 133
    assert prof.non_signal is True
    assert prof.official_approval is False

    gate = RegimeValidationGate(
        gate_id="GATE_TEST", gate_name="test_gate", domain="validation_gate_domain", description="desc"
    )
    assert gate.passed is True
    assert gate.non_signal is True

    item = RegimeAcceptanceCheckItem(
        check_id="CHECK_TEST", check_name="test_check", domain="validation_domain", target_component="component"
    )
    assert item.contains_target_or_prediction is False
    assert item.model_training_executed is False

    finding = RegimeValidationFinding(
        finding_id="F_TEST",
        finding_type="no_lookahead_acceptance_blocker",
        acceptance_domain="no_lookahead_acceptance_domain",
        severity_label="acceptance_info",
        message="test msg",
        recommendation="test rec",
    )
    assert finding.destructive_action_allowed is False
    assert finding.auto_fix_allowed is False

    score = RegimeAcceptanceScore(
        overall_score=0.95,
        score_tier="high_acceptance_integrity",
        total_checks=19,
        passed_checks=19,
        failed_checks=0,
        warning_checks=0,
        manual_review_required=False,
    )
    assert score.overall_score == 0.95

    with pytest.raises(ValueError):
        RegimeAcceptanceScore(
            overall_score=1.5,
            score_tier="invalid",
            total_checks=19,
            passed_checks=19,
            failed_checks=0,
            warning_checks=0,
            manual_review_required=False,
        )

    mani = RegimeValidationAcceptanceManifest(
        manifest_name="test_manifest", acceptance_score=0.85
    )
    assert mani.current_phase == 133
    assert mani.contains_full_article_text is False
    assert mani.clustering_executed is False

    with pytest.raises(ValueError):
        RegimeValidationAcceptanceManifest(
            manifest_name="invalid_manifest", acceptance_score=-0.1
        )
