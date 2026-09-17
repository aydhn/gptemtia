# -*- coding: utf-8 -*-
"""Unit tests for Phase 160 Final Delivery Labels."""

from advanced_final_delivery.final_delivery_labels import (
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    PHASE_160_COMPLETED,
    SAFE_LOCAL_ONLY,
    SAFE_DRY_RUN,
    SAFE_NON_PRODUCTION,
    SAFE_NON_SIGNAL,
    SAFE_RESEARCH_ONLY,
    FINAL_PACKAGE_DOMAIN,
    FINAL_DELIVERY_PROFILE_DOMAIN,
    FINAL_BOUNDARY_DOMAIN,
    FINAL_DISABLED_EXECUTION_DOMAIN,
    FINAL_MANIFEST_DOMAIN,
    FINAL_COMPLETION_DOMAIN,
    EXECUTION_BLOCKED_NO_LIVE_TRADING,
    EXECUTION_BLOCKED_NO_BROKER,
    EXECUTION_BLOCKED_NO_SIGNAL_GENERATION,
    EXECUTION_BLOCKED_NO_ORDER_GENERATION,
    EXECUTION_BLOCKED_NO_PRODUCTION_DEPLOYMENT,
    EXECUTION_BLOCKED_NO_MODEL_TRAINING,
    EXECUTION_BLOCKED_NO_PREDICTION,
    SEVERITY_CRITICAL,
    SEVERITY_HIGH,
    SEVERITY_MEDIUM,
    SEVERITY_LOW,
    SEVERITY_INFO,
)


def test_delivery_labels():
    assert FULL_ADVANCED_BOT_FINAL_DELIVERY_READY == "full_advanced_bot_final_delivery_ready"
    assert PHASE_160_COMPLETED == "phase_160_completed"
    assert SAFE_LOCAL_ONLY == "LOCAL_ONLY"
    assert SAFE_DRY_RUN == "DRY_RUN"
    assert SAFE_NON_PRODUCTION == "NON_PRODUCTION"
    assert SAFE_NON_SIGNAL == "NON_SIGNAL"
    assert SAFE_RESEARCH_ONLY == "RESEARCH_ONLY"

    assert FINAL_PACKAGE_DOMAIN == "final_package_domain"
    assert FINAL_DELIVERY_PROFILE_DOMAIN == "final_delivery_profile_domain"
    assert FINAL_BOUNDARY_DOMAIN == "final_boundary_domain"
    assert FINAL_DISABLED_EXECUTION_DOMAIN == "final_disabled_execution_domain"
    assert FINAL_MANIFEST_DOMAIN == "final_manifest_domain"
    assert FINAL_COMPLETION_DOMAIN == "final_completion_domain"

    assert EXECUTION_BLOCKED_NO_LIVE_TRADING == "execution_blocked_no_live_trading"
    assert EXECUTION_BLOCKED_NO_BROKER == "execution_blocked_no_broker"
    assert EXECUTION_BLOCKED_NO_SIGNAL_GENERATION == "execution_blocked_no_signal_generation"
    assert EXECUTION_BLOCKED_NO_ORDER_GENERATION == "execution_blocked_no_order_generation"
    assert EXECUTION_BLOCKED_NO_PRODUCTION_DEPLOYMENT == "execution_blocked_no_production_deployment"
    assert EXECUTION_BLOCKED_NO_MODEL_TRAINING == "execution_blocked_no_model_training"
    assert EXECUTION_BLOCKED_NO_PREDICTION == "execution_blocked_no_prediction"

    assert SEVERITY_INFO == "INFO"
    assert SEVERITY_CRITICAL == "CRITICAL"
