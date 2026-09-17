# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Portfolio Construction Contracts."""

from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.portfolio_construction_contracts import (
    build_portfolio_construction_contract_registry,
    validate_portfolio_construction_contract,
)
from advanced_portfolio_construction.portfolio_universe_contracts import (
    build_portfolio_universe_contract_registry,
)
from advanced_portfolio_construction.portfolio_asset_eligibility_contracts import (
    build_portfolio_asset_eligibility_contract_registry,
)
from advanced_portfolio_construction.portfolio_signal_input_contracts import (
    build_portfolio_signal_input_contract_registry,
)
from advanced_portfolio_construction.portfolio_risk_input_contracts import (
    build_portfolio_risk_input_contract_registry,
)


def test_build_portfolio_construction_contract_registry():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_portfolio_construction_contract_registry(profile)
    assert len(df) >= 3
    assert summary["total_contracts"] == len(df)
    assert bool(df["contract_only"].all()) is True
    assert summary["all_construction_blocked"] is True
    assert summary["status"] == "portfolio_contract_ready"


def test_portfolio_universe_contract_registry():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_portfolio_universe_contract_registry(profile)
    assert len(df) == 10
    symbols = df["asset_symbol"].tolist()
    assert "BRENT" in symbols
    assert "GOLD" in symbols
    assert "USDTRY" in symbols
    assert bool(df["contract_only"].all()) is True


def test_portfolio_asset_eligibility_contract_registry():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_portfolio_asset_eligibility_contract_registry(profile)
    assert len(df) >= 5
    assert summary["all_contract_only"] is True


def test_portfolio_signal_input_contract_registry():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_portfolio_signal_input_contract_registry(profile)
    assert len(df) >= 3
    assert summary["all_zero_signal_generation"] is True


def test_portfolio_risk_input_contract_registry():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_portfolio_risk_input_contract_registry(profile)
    assert len(df) >= 3
    assert summary["all_contract_only"] is True


def test_validate_portfolio_construction_contract():
    valid_contract = {
        "contract_name": "valid_test_contract",
        "portfolio_construction_allowed": False,
        "capital_allocation_allowed": False,
        "position_sizing_allowed": False,
        "order_generation_allowed": False,
        "optimizer_execution_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
    }
    res = validate_portfolio_construction_contract(valid_contract)
    assert res["is_valid"] is True

    invalid_contract = {
        "contract_name": "invalid_test_contract",
        "portfolio_construction_allowed": True,
    }
    res_inv = validate_portfolio_construction_contract(invalid_contract)
    assert res_inv["is_valid"] is False
