# -*- coding: utf-8 -*-
"""Unit tests for Phase 160 Final Delivery Models."""

import pytest
from advanced_final_delivery.final_delivery_models import (
    FinalDeliveryProfileItem,
    FinalDeliveryPackageContract,
    FinalDeliveryComponentItem,
    FinalDeliveryInventoryItem,
    FinalDeliveryEvidenceItem,
    FinalDeliveryPhaseSummaryItem,
    FinalDeliveryBoundaryItem,
    FinalDeliveryDisabledExecutionItem,
    FinalDeliveryFinding,
    FinalDeliveryReadinessScore,
    FinalDeliveryManifest,
    Final160PhaseCompletionItem,
    FINAL_DELIVERY_PROFILE_DOMAIN,
    FINAL_PACKAGE_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def test_final_delivery_profile_item():
    item = FinalDeliveryProfileItem(
        profile_name="test_profile",
        description="test desc",
    )
    assert item.profile_name == "test_profile"
    assert item.current_phase == 160
    assert item.target_final_phase == 160
    assert item.next_phase is None
    assert item.min_readiness_score == 0.50
    assert item.non_signal is True
    assert item.local_only is True
    assert item.dry_run is True
    assert item.non_production is True
    assert item.status == FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


def test_final_delivery_manifest_defaults():
    manifest = FinalDeliveryManifest(
        manifest_id="test_manifest",
    )
    assert manifest.current_phase == 160
    assert manifest.next_phase is None
    assert manifest.phase_160_completed is True
    assert manifest.final_plan_closed is True
    assert manifest.status == FULL_ADVANCED_BOT_FINAL_DELIVERY_READY
    assert manifest.live_trading_ready is False
    assert manifest.broker_ready is False
    assert manifest.production_ready is False


def test_final_160_phase_completion_item():
    item = Final160PhaseCompletionItem(
        current_phase=160,
        target_final_phase=160,
        next_phase=None,
    )
    assert item.current_phase == 160
    assert item.target_final_phase == 160
    assert item.next_phase is None
    assert item.plan_status == "completed_contract_governance_documentation_acceptance_level"
    assert item.live_trading_ready is False
    assert item.broker_ready is False
    assert item.production_ready is False
    assert item.final_delivery_completed is True


def test_readiness_score_validation():
    score = FinalDeliveryReadinessScore(readiness_score=1.0, classification="DELIVERY_READY")
    assert score.readiness_score == 1.0

    with pytest.raises(ValueError):
        FinalDeliveryReadinessScore(readiness_score=1.5, classification="INVALID")
