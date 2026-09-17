# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Optimization Solvers and Frontier Placeholders."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.optimization_solver_contracts import (
    build_optimization_solver_contract_registry,
)
from advanced_portfolio_optimization.convex_solver_placeholders import (
    build_convex_solver_placeholder_registry,
)
from advanced_portfolio_optimization.heuristic_solver_placeholders import (
    build_heuristic_solver_placeholder_registry,
)
from advanced_portfolio_optimization.grid_search_solver_disabled import (
    build_grid_search_solver_disabled_registry,
)
from advanced_portfolio_optimization.optimizer_execution_disabled import (
    build_optimizer_execution_disabled_report,
)
from advanced_portfolio_optimization.efficient_frontier_placeholders import (
    build_efficient_frontier_placeholder_registry,
)


def test_solver_contract_registry():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_optimization_solver_contract_registry(profile)
    assert not df.empty
    assert len(df) == 3
    assert summary["all_solvers_placeholders"] is True
    assert (df["allows_execution"] == False).all()


def test_optimizer_execution_disabled():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_optimizer_execution_disabled_report(profile)
    assert not df.empty
    assert summary["optimizer_execution_disabled"] is True
    assert (df["is_disabled"] == True).all()


def test_efficient_frontier_placeholder():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_efficient_frontier_placeholder_registry(profile)
    assert not df.empty
    assert summary["frontier_calculated"] is False
    assert (df["is_placeholder"] == True).all()
