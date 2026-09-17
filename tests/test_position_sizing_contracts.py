# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Position Sizing Contracts & Placeholders."""

from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.position_sizing_contracts import (
    build_position_sizing_contract_registry,
    validate_position_sizing_contract,
)
from advanced_portfolio_construction.fixed_fractional_sizing_placeholders import (
    build_fixed_fractional_sizing_placeholder_registry,
)
from advanced_portfolio_construction.volatility_targeting_sizing_placeholders import (
    build_volatility_targeting_sizing_placeholder_registry,
)
from advanced_portfolio_construction.risk_parity_sizing_placeholders import (
    build_risk_parity_sizing_placeholder_registry,
)
from advanced_portfolio_construction.drawdown_aware_sizing_placeholders import (
    build_drawdown_aware_sizing_placeholder_registry,
)


def test_build_position_sizing_contract_registry():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_position_sizing_contract_registry(profile)
    assert len(df) >= 5
    assert summary["total_contracts"] == len(df)
    assert summary["all_sizing_blocked"] is True
    assert summary["all_allocation_blocked"] is True
    assert summary["status"] == "portfolio_contract_ready"


def test_fixed_fractional_placeholders():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_fixed_fractional_sizing_placeholder_registry(profile)
    assert len(df) >= 3
    assert df["actual_size_calculated"].all() == False


def test_volatility_targeting_placeholders():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_volatility_targeting_sizing_placeholder_registry(profile)
    assert len(df) >= 3
    assert df["actual_size_calculated"].all() == False


def test_risk_parity_placeholders():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_risk_parity_sizing_placeholder_registry(profile)
    assert len(df) >= 3
    assert df["actual_weights_calculated"].all() == False


def test_drawdown_aware_placeholders():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_drawdown_aware_sizing_placeholder_registry(profile)
    assert len(df) >= 3
    assert df["actual_throttle_executed"].all() == False


def test_validate_position_sizing_contract():
    valid = {
        "sizing_name": "valid_test",
        "position_sizing_allowed": False,
        "capital_allocation_allowed": False,
        "order_generation_allowed": False,
        "broker_execution_allowed": False,
        "investment_advice_allowed": False,
    }
    res = validate_position_sizing_contract(valid)
    assert res["is_valid"] is True

    invalid = {
        "sizing_name": "invalid_test",
        "position_sizing_allowed": True,
    }
    res_inv = validate_position_sizing_contract(invalid)
    assert res_inv["is_valid"] is False
