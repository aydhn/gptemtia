# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Portfolio Optimization Labels and Enums."""

from advanced_portfolio_optimization.portfolio_optimization_labels import (
    OptimizationProfileType,
    OptimizationDomainType,
    OptimizationScopeType,
    OptimizationObjectiveType,
    AllocationConstraintType,
    OptimizationSolverType,
    OptimizationExecutionStatus,
    PORTFOLIO_OPTIMIZATION_DOMAIN,
    PHASE_155_HANDOFF_DOMAIN,
    PORTFOLIO_OPTIMIZATION_CONTRACT_READY,
    HANDOFF_READY,
)


def test_labels_and_domains():
    assert PORTFOLIO_OPTIMIZATION_DOMAIN == "portfolio_optimization_domain"
    assert PHASE_155_HANDOFF_DOMAIN == "phase_155_handoff_domain"
    assert PORTFOLIO_OPTIMIZATION_CONTRACT_READY == "portfolio_optimization_contract_ready"
    assert HANDOFF_READY == "HANDOFF_READY"


def test_objective_types():
    expected = [
        "mean_variance",
        "minimum_variance",
        "maximum_sharpe",
        "risk_parity",
        "cvar",
        "drawdown_minimization",
        "turnover_minimization",
        "cost_aware",
        "slippage_aware",
        "regime_aware",
        "robust_optimization",
    ]
    actual = [e.value for e in OptimizationObjectiveType]
    for exp in expected:
        assert exp in actual


def test_allocation_constraint_types():
    assert len(AllocationConstraintType) >= 20
    assert AllocationConstraintType.LONG_ONLY.value == "long_only"
    assert AllocationConstraintType.MAX_WEIGHT.value == "max_weight"
    assert AllocationConstraintType.RISK_BUDGET.value == "risk_budget"
    assert AllocationConstraintType.TURNOVER.value == "turnover"


def test_solver_types():
    assert OptimizationSolverType.CONVEX.value == "convex"
    assert OptimizationSolverType.HEURISTIC.value == "heuristic"
    assert OptimizationSolverType.GRID_SEARCH_DISABLED.value == "grid_search_disabled"
    assert OptimizationSolverType.OPTIMIZER_DISABLED.value == "optimizer_disabled"
