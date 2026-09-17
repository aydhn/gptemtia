import pytest
from advanced_backtest_acceptance.backtest_acceptance_models import (
    BacktestAcceptanceProfileItem,
    BacktestAcceptanceComponentItem,
    BacktestAcceptanceCheckpoint,
    BacktestPhaseAcceptanceItem,
    BacktestValidationEvidenceItem,
    BacktestAcceptanceBoundaryItem,
    BacktestAcceptanceFinding,
    BacktestAcceptanceReadinessScore,
    BacktestAcceptanceManualReviewItem,
    BacktestAcceptanceManifest,
)

def test_backtest_acceptance_models_instantiation():
    profile = BacktestAcceptanceProfileItem(
        profile_name="test_profile",
        description="Profile for testing",
    )
    assert profile.profile_name == "test_profile"
    assert profile.production_ready is False
    assert profile.broker_ready is False
    assert profile.non_signal is True

    component = BacktestAcceptanceComponentItem(
        component_id="comp_1",
        component_name="Component 1",
        phase_ref="Phase 146",
        primary_module="advanced_realistic_backtest",
        description="A verified component",
    )
    assert component.component_id == "comp_1"
    assert component.contract_only is True
    assert component.production_ready is False

    checkpoint = BacktestAcceptanceCheckpoint(
        checkpoint_id="chk_1",
        component_name="Component 1",
        expected_module="advanced_realistic_backtest",
        expected_scripts=["run_realistic_backtest_contracts.py"],
        expected_tests=["test_advanced_realistic_backtest.py"],
        expected_manifest="manifest",
        expected_validation_report="report",
        expected_safety_boundary="boundary",
        expected_handoff="handoff",
    )
    assert checkpoint.checkpoint_id == "chk_1"
    assert checkpoint.manual_review_required is True

    phase_item = BacktestPhaseAcceptanceItem(
        phase_id="pha_146",
        phase_number=146,
        title="Realistic Backtest",
        primary_module="advanced_realistic_backtest",
        checks_passed=10,
        total_checks=10,
    )
    assert phase_item.checks_passed == 10
    assert phase_item.production_ready is False

    evidence = BacktestValidationEvidenceItem(
        evidence_id="evi_1",
        phase_ref="Phase 146",
        evidence_type="manifest_presence",
        description="Manifest present",
    )
    assert evidence.status == "VERIFIED"
    assert evidence.no_live_trading is True

    boundary = BacktestAcceptanceBoundaryItem(
        boundary_id="bnd_1",
        boundary_type="safety",
        description="No live trading",
    )
    assert boundary.enforced is True
    assert boundary.status == "SECURE"

    finding = BacktestAcceptanceFinding(
        finding_id="fnd_1",
        finding_type="audit",
        phase_ref="Phase 152",
        severity_label="INFO",
        message="Audit passed cleanly",
        recommendation="Maintain offline checks",
    )
    assert finding.finding_id == "fnd_1"
    assert finding.manual_review_required is True

    score = BacktestAcceptanceReadinessScore(
        score=1.0,
        classification="backtest_acceptance_contract_ready_non_production",
        meets_threshold=True,
    )
    assert score.score == 1.0
    assert score.production_ready is False
    assert score.broker_ready is False

    with pytest.raises(ValueError):
        BacktestAcceptanceReadinessScore(score=1.5, classification="invalid", meets_threshold=False)

    review_item = BacktestAcceptanceManualReviewItem(
        gate_id="gate_1",
        phase_ref="Phase 146",
        topic="Cost models",
        review_requirement="Review cost assumptions",
        action_required="Confirm parameters",
    )
    assert review_item.gate_id == "gate_1"
    assert review_item.status == "PENDING_REVIEW"

    manifest = BacktestAcceptanceManifest(
        manifest_name="backtest_acceptance_manifest",
        manifest_id="MNF-152-001",
    )
    assert manifest.current_phase == 152
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 153
    assert manifest.production_ready is False
    assert manifest.broker_ready is False
    assert manifest.live_trading_ready is False
    assert manifest.backtest_executed is False
    assert manifest.strategy_approved is False
