"""Test suite for Phase 135 Regime Acceptance Models."""

from advanced_regime_acceptance.regime_acceptance_models import (
    RegimeAcceptanceProfileItem,
    RegimeBlockInventoryItem,
    RegimeBlockDependencyItem,
    RegimeBlockAcceptanceGate,
    RegimeBlockAcceptanceScore,
    Phase126135AcceptanceManifest,
)


def test_models_non_signal_defaults():
    prof = RegimeAcceptanceProfileItem(
        profile_name="test_profile",
        description="test desc",
    )
    assert prof.non_signal is True
    assert prof.current_phase == 135

    inv = RegimeBlockInventoryItem(
        phase_number=126,
        module_name="advanced_regime_foundation",
        expected_scripts=7,
        expected_tests=12,
        expected_reports=6,
        expected_datalake_outputs=8,
        expected_docs=4,
        status_label="acceptance_pass",
    )
    assert inv.non_signal is True
    assert inv.source_preserved is True

    manifest = Phase126135AcceptanceManifest(
        block_name="Regime Block",
    )
    assert manifest.phase_start == 126
    assert manifest.phase_end == 135
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 136
    assert manifest.non_signal is True
    assert manifest.official_approval is False
    assert manifest.production_ready is False
    assert manifest.broker_ready is False
    assert manifest.model_training_executed is False
    assert manifest.clustering_executed is False
