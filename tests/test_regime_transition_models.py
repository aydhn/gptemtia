"""Tests for Regime Transition Dataclass Models."""

import pytest
from advanced_regime_transition.regime_transition_models import (
    RegimeTransitionProfileItem,
    StateSequenceContract,
    StateSequenceSchemaItem,
    TransitionMetric,
    StabilityMetric,
    TransitionQualityFinding,
    TransitionStabilityScore,
    TransitionDiagnosticsManifest,
    TransitionManualReviewItem,
)


def test_regime_transition_profile_item():
    item = RegimeTransitionProfileItem(
        profile_name="test_profile",
        description="Test Profile",
        current_phase=130,
        target_final_phase=160,
        next_phase=131,
    )
    assert item.profile_name == "test_profile"
    assert item.current_phase == 130
    assert item.non_signal is True


def test_state_sequence_contract_model():
    contract = StateSequenceContract(
        contract_name="test_contract",
        sequence_family="candidate_state_sequence",
        entity_keys=["symbol", "timeframe"],
        timestamp_field="timestamp",
        state_context_field="candidate_state",
        source_phase_refs=["Phase 128"],
        required_validation_refs=["Phase 121"],
        required_quality_refs=["Phase 129"],
    )
    assert contract.contract_name == "test_contract"
    assert contract.no_lookahead_required is True
    assert contract.non_signal_required is True
    assert contract.model_training_allowed is False


def test_transition_metric_model():
    metric = TransitionMetric(
        metric_name="state_persistence_score",
        metric_family="persistence",
        description="Descriptive persistence index",
        formula_placeholder="persistence_ratio",
        expected_range="[0.0, 1.0]",
    )
    assert metric.metric_name == "state_persistence_score"
    assert metric.non_signal is True


def test_transition_diagnostics_manifest_defaults():
    manifest = TransitionDiagnosticsManifest(
        manifest_name="test_manifest",
        current_phase=130,
        target_final_phase=160,
        next_phase=131,
    )
    assert manifest.current_phase == 130
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 131
    assert manifest.official_approval is False
    assert manifest.model_training_executed is False
