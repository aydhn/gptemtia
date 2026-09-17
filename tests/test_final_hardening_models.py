# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Models."""

from advanced_final_hardening.final_hardening_models import (
    FinalHardeningProfileItem,
    FinalHardeningContract,
    OperatorRunbookContract,
    ReleaseCandidateContract,
    FinalFreezeContract,
    FinalInventoryItem,
    ReleaseCandidateManifest,
)


def test_models_instantiation():
    rec = FinalHardeningContract(
        contract_name="Test Contract",
        hardening_family="Hardening",
    )
    assert rec.contract_name == "Test Contract"
    assert rec.hardening_family == "Hardening"
    assert rec.non_signal is True
    assert rec.dry_run is True
    assert rec.live_trading_allowed is False


def test_operator_runbook_contract():
    rec = OperatorRunbookContract(
        runbook_name="Operator Startup",
        category="startup",
        description="Startup guide",
    )
    assert rec.runbook_name == "Operator Startup"
    assert rec.live_bot_execution_allowed is False
    assert rec.broker_execution_allowed is False


def test_release_candidate_manifest():
    rec = ReleaseCandidateManifest(
        manifest_id="MNF-159-RELEASE-CANDIDATE-001",
        current_phase=159,
        target_final_phase=160,
        next_phase=160,
    )
    assert rec.manifest_id == "MNF-159-RELEASE-CANDIDATE-001"
    assert rec.production_ready is False
    assert rec.live_trading_ready is False
    assert rec.system_executed is False
