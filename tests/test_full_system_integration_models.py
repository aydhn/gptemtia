# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Full System Integration Models."""

import pytest
from advanced_full_system_integration.full_system_integration_models import (
    FullSystemIntegrationProfileItem,
    SystemComponentItem,
    SystemComponentCheckpoint,
    SystemIntegrationContract,
    AdvancedAcceptanceRehearsalItem,
    SystemBoundaryItem,
    SystemDisabledExecutionItem,
    SystemIntegrationFinding,
    SystemIntegrationReadinessScore,
    FullSystemIntegrationManifest,
    SystemManualReviewItem,
)


def test_full_system_integration_profile_item():
    item = FullSystemIntegrationProfileItem(
        profile_name="test_profile",
        description="test desc",
        current_phase=158,
        target_final_phase=160,
        next_phase=159,
        min_readiness_score=0.50,
        non_signal=True,
        dry_run=True,
        local_only=True,
        non_production=True,
        broker_ready=False,
        production_ready=False,
        live_trading_ready=False,
    )
    assert item.profile_name == "test_profile"
    assert item.current_phase == 158
    assert item.non_production is True
    assert item.dry_run is True
    assert item.broker_ready is False


def test_system_component_item():
    comp = SystemComponentItem(
        component_id="CMP-01",
        component_name="Test Component",
        layer_name="data",
        module_name="test_mod",
        status="active",
        contract_only=True,
        non_production=True,
        dry_run=True,
        local_only=True,
        production_ready=False,
        broker_ready=False,
        live_ready=False,
        signal_ready=False,
        system_executed=False,
    )
    assert comp.component_id == "CMP-01"
    assert comp.contract_only is True
    assert comp.system_executed is False


def test_system_component_checkpoint():
    ckp = SystemComponentCheckpoint(
        checkpoint_id="CKP-01",
        component_name="Test Component",
        expected_module="test_mod",
        contract_only=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        manual_review_required=True,
        production_ready=False,
        broker_ready=False,
        live_ready=False,
        signal_ready=False,
    )
    assert ckp.checkpoint_id == "CKP-01"
    assert ckp.manual_review_required is True


def test_system_integration_contract():
    cnt = SystemIntegrationContract(
        contract_id="CNT-01",
        subsystem_name="data_pipeline",
        contract_type="data_to_feature",
        version="1.0.0",
        status="active",
        contract_only=True,
        non_production=True,
        manual_review_required=True,
        zero_execution_guaranteed=True,
        notes="None",
    )
    assert cnt.contract_id == "CNT-01"
    assert cnt.zero_execution_guaranteed is True


def test_advanced_acceptance_rehearsal_item():
    reh = AdvancedAcceptanceRehearsalItem(
        rehearsal_id="REH-01",
        rehearsal_name="Preflight Check",
        target_layer="preflight",
        verification_type="dry_run",
        status="passed",
        is_satisfied=True,
        notes="Verified",
        contract_only=True,
        non_production=True,
        zero_execution_verified=True,
    )
    assert reh.rehearsal_id == "REH-01"
    assert reh.is_satisfied is True
    assert reh.zero_execution_verified is True


def test_system_boundary_item():
    bnd = SystemBoundaryItem(
        boundary_id="BND-01",
        boundary_type="safety",
        rule_name="no_live_trading",
        action_type="block",
        is_allowed=False,
        reason="Non-production research environment",
    )
    assert bnd.boundary_id == "BND-01"
    assert bnd.is_allowed is False


def test_system_disabled_execution_item():
    dis = SystemDisabledExecutionItem(
        item_id="DIS-01",
        execution_type="live_trading",
        is_disabled=True,
        blocking_reason="Prohibited in Phase 158",
        enforcement_layer="contract",
        status="DISABLED",
    )
    assert dis.item_id == "DIS-01"
    assert dis.is_disabled is True


def test_system_integration_finding():
    fnd = SystemIntegrationFinding(
        finding_id="FND-01",
        finding_type="warning",
        domain="core",
        severity_label="low",
        message="Notice only",
        recommendation="Proceed with caution",
        manual_review_required=True,
        is_blocking=False,
    )
    assert fnd.finding_id == "FND-01"
    assert fnd.is_blocking is False


def test_system_integration_readiness_score():
    score = SystemIntegrationReadinessScore(
        overall_score=0.95,
        classification="ready",
        meets_threshold=True,
        total_checks=20,
        passed_checks=19,
        warning_count=1,
        blocker_count=0,
        non_signal=True,
        dry_run=True,
        local_only=True,
        non_production=True,
        broker_ready=False,
        production_ready=False,
        live_trading_ready=False,
        official_approval=False,
    )
    assert score.overall_score == 0.95
    assert score.meets_threshold is True

    with pytest.raises(ValueError):
        SystemIntegrationReadinessScore(
            overall_score=1.5,
            classification="invalid",
            meets_threshold=False,
            total_checks=1,
            passed_checks=1,
            warning_count=0,
            blocker_count=0,
        )


def test_full_system_integration_manifest():
    mnf = FullSystemIntegrationManifest(
        manifest_id="FSI-MANIFEST-PHASE-158",
        current_phase=158,
        target_final_phase=160,
        next_phase=159,
        full_system_integration_completed=True,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
    )
    assert mnf.manifest_id == "FSI-MANIFEST-PHASE-158"
    assert mnf.production_ready is False


def test_system_manual_review_item():
    rev = SystemManualReviewItem(
        item_id="REV-01",
        gate_name="Gate 1",
        title="Manual Audit",
        description="Audit checklist",
        action_required="Signoff",
        status="PENDING_REVIEW",
    )
    assert rev.item_id == "REV-01"
    assert rev.status == "PENDING_REVIEW"
