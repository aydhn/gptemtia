# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Portfolio Construction Labels."""

from advanced_portfolio_construction.portfolio_construction_labels import (
    PORTFOLIO_CONSTRUCTION_DOMAIN,
    POSITION_SIZING_DOMAIN,
    RISK_BUDGET_DOMAIN,
    EXPOSURE_LIMIT_DOMAIN,
    CONCENTRATION_LIMIT_DOMAIN,
    LEVERAGE_MARGIN_DOMAIN,
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
    READINESS_BLOCKED,
    READINESS_INCOMPLETE,
    READINESS_CONTRACT_READY_WITH_MANUAL_REVIEW,
    READINESS_CONTRACT_READY_NON_PRODUCTION,
    HANDOFF_READY,
    DISABLED_EXEC_PORTFOLIO_CONSTRUCTION,
    DISABLED_EXEC_LIVE_TRADING,
    DISABLED_EXEC_BROKER_EXECUTION,
)


def test_portfolio_construction_domains():
    assert PORTFOLIO_CONSTRUCTION_DOMAIN == "portfolio_construction_domain"
    assert POSITION_SIZING_DOMAIN == "position_sizing_domain"
    assert RISK_BUDGET_DOMAIN == "risk_budget_domain"
    assert EXPOSURE_LIMIT_DOMAIN == "exposure_limit_domain"
    assert CONCENTRATION_LIMIT_DOMAIN == "concentration_limit_domain"
    assert LEVERAGE_MARGIN_DOMAIN == "leverage_margin_placeholder_domain"
    assert PORTFOLIO_GUARD_DOMAIN == "claim_guard_domain"
    assert PORTFOLIO_DISABLED_EXECUTION_DOMAIN == "disabled_execution_domain"


def test_status_and_readiness_tiers():
    assert PORTFOLIO_CONTRACT_READY == "portfolio_contract_ready"
    assert READINESS_BLOCKED == "blocked"
    assert READINESS_INCOMPLETE == "incomplete"
    assert READINESS_CONTRACT_READY_WITH_MANUAL_REVIEW == "contract_ready_with_manual_review"
    assert READINESS_CONTRACT_READY_NON_PRODUCTION == "portfolio_construction_contract_ready_non_production"
    assert HANDOFF_READY == "HANDOFF_READY"


def test_execution_blockage_labels():
    assert "no_portfolio_construction" in DISABLED_EXEC_PORTFOLIO_CONSTRUCTION
    assert "no_live_trading" in DISABLED_EXEC_LIVE_TRADING
    assert "no_broker" in DISABLED_EXEC_BROKER_EXECUTION
