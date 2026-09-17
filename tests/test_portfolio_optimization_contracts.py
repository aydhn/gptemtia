# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Portfolio Optimization Contracts."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.portfolio_optimization_contracts import (
    build_portfolio_optimization_contract_registry,
    summarize_portfolio_optimization_contracts,
)


def test_portfolio_optimization_contracts():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_portfolio_optimization_contract_registry(profile)
    assert not df.empty
    assert len(df) == 11
    assert summary["contract_count"] == 11
    assert summary["all_contracts_disallow_optimization"] is True
    assert summary["all_contracts_disallow_weight_generation"] is True
    assert summary["all_contracts_disallow_live_trading"] is True
    assert (df["portfolio_optimization_allowed"] == False).all()
    assert (df["weight_generation_allowed"] == False).all()
    assert (df["live_trading_allowed"] == False).all()
