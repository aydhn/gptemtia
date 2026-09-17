# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Risk Budget Contracts & Placeholders."""

from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.risk_budget_contracts import (
    build_risk_budget_contract_registry,
    validate_risk_budget_contract,
)
from advanced_portfolio_construction.per_asset_risk_budget_placeholders import (
    build_per_asset_risk_budget_placeholder_registry,
)
from advanced_portfolio_construction.per_strategy_risk_budget_placeholders import (
    build_per_strategy_risk_budget_placeholder_registry,
)
from advanced_portfolio_construction.per_regime_risk_budget_placeholders import (
    build_per_regime_risk_budget_placeholder_registry,
)
from advanced_portfolio_construction.portfolio_risk_budget_placeholders import (
    build_portfolio_risk_budget_placeholder_registry,
)


def test_build_risk_budget_contract_registry():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_risk_budget_contract_registry(profile)
    assert len(df) >= 3
    assert summary["total_contracts"] == len(df)
    assert summary["all_budget_generation_blocked"] is True
    assert summary["all_allocation_blocked"] is True
    assert summary["status"] == "portfolio_contract_ready"


def test_per_asset_risk_budget_placeholders():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_per_asset_risk_budget_placeholder_registry(profile)
    assert len(df) >= 3
    assert df["actual_budget_calculated"].all() == False


def test_per_strategy_risk_budget_placeholders():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_per_strategy_risk_budget_placeholder_registry(profile)
    assert len(df) >= 3
    assert df["actual_budget_calculated"].all() == False


def test_per_regime_risk_budget_placeholders():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_per_regime_risk_budget_placeholder_registry(profile)
    assert len(df) >= 3
    assert df["actual_budget_calculated"].all() == False


def test_portfolio_risk_budget_placeholders():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_portfolio_risk_budget_placeholder_registry(profile)
    assert len(df) >= 3
    assert df["actual_budget_calculated"].all() == False


def test_validate_risk_budget_contract():
    valid = {
        "budget_name": "valid_test",
        "risk_budget_generation_allowed": False,
        "capital_allocation_allowed": False,
        "position_sizing_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
    }
    res = validate_risk_budget_contract(valid)
    assert res["is_valid"] is True

    invalid = {
        "budget_name": "invalid_test",
        "capital_allocation_allowed": True,
    }
    res_inv = validate_risk_budget_contract(invalid)
    assert res_inv["is_valid"] is False
