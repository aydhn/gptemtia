# -*- coding: utf-8 -*-
"""Unit tests for Phase 157 Portfolio Acceptance Labels."""

from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    PORTFOLIO_ACCEPTANCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_PROFILE_DOMAIN,
    COMPONENT_REGISTRY_DOMAIN,
    COMPONENT_CHECKPOINT_DOMAIN,
    PHASE_153_PORTFOLIO_CONSTRUCTION_ACCEPTANCE_DOMAIN,
    PHASE_154_PORTFOLIO_OPTIMIZATION_ACCEPTANCE_DOMAIN,
    PHASE_155_RISK_REPORTING_ACCEPTANCE_DOMAIN,
    PHASE_156_PORTFOLIO_SCENARIO_CONTROL_ACCEPTANCE_DOMAIN,
    DEPENDENCY_ACCEPTANCE_DOMAIN,
    VALIDATION_EVIDENCE_DOMAIN,
    SAFETY_BOUNDARY_DOMAIN,
    NON_PRODUCTION_BOUNDARY_DOMAIN,
    MANUAL_REVIEW_GATE_DOMAIN,
    GO_NO_GO_BOUNDARY_DOMAIN,
    BLOCKER_DOMAIN,
    GAP_DOMAIN,
    WARNING_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_158_HANDOFF_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
    GO_CONTRACT_ONLY,
    NO_GO_LIVE_TRADING,
    NO_GO_BROKER_EXECUTION,
)


def test_labels_exist():
    assert PORTFOLIO_ACCEPTANCE_DOMAIN == "portfolio_acceptance_domain"
    assert COMPONENT_REGISTRY_DOMAIN == "component_registry_domain"
    assert PHASE_153_PORTFOLIO_CONSTRUCTION_ACCEPTANCE_DOMAIN == "phase_153_portfolio_construction_acceptance_domain"
    assert PHASE_154_PORTFOLIO_OPTIMIZATION_ACCEPTANCE_DOMAIN == "phase_154_portfolio_optimization_acceptance_domain"
    assert PHASE_155_RISK_REPORTING_ACCEPTANCE_DOMAIN == "phase_155_risk_reporting_acceptance_domain"
    assert PHASE_156_PORTFOLIO_SCENARIO_CONTROL_ACCEPTANCE_DOMAIN == "phase_156_portfolio_scenario_control_acceptance_domain"
    assert PHASE_158_HANDOFF_DOMAIN == "phase_158_handoff_domain"
    assert PORTFOLIO_ACCEPTANCE_READY == "portfolio_acceptance_ready"
    assert GO_CONTRACT_ONLY == "go_contract_only"
    assert NO_GO_LIVE_TRADING == "no_go_live_trading"
    assert NO_GO_BROKER_EXECUTION == "no_go_broker_execution"
