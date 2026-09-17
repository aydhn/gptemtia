# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Portfolio Optimization Data Models."""

import pytest
from advanced_portfolio_optimization.portfolio_optimization_models import (
    PortfolioOptimizationProfileItem,
    PortfolioOptimizationContract,
    OptimizationObjectiveContract,
    AllocationConstraintContract,
    SolverContract,
    OptimizationMetricPlaceholder,
    OptimizationGuardItem,
    OptimizationDisabledExecutionItem,
    PortfolioOptimizationFinding,
    PortfolioOptimizationReadinessScore,
    PortfolioOptimizationManifest,
    PortfolioOptimizationManualReviewItem,
)


def test_portfolio_optimization_contract_defaults():
    contract = PortfolioOptimizationContract(
        contract_name="test_contract",
        optimization_family="mean_variance",
        portfolio_construction_ref="PC_01",
        risk_budget_ref="RB_01",
        allocation_constraint_ref="AC_01",
        objective_ref="OBJ_01",
        solver_ref="SOLV_01",
        backtest_acceptance_ref="BKT_01",
        benchmark_evaluation_ref="BNK_01",
        model_governance_ref="GOV_01",
        regime_context_ref="REG_01",
        featurestore_ref="FS_01",
        no_lookahead_guard_ref="GRD_01",
        investment_advice_guard_ref="GRD_02",
    )
    assert contract.portfolio_optimization_allowed is False
    assert contract.weight_generation_allowed is False
    assert contract.live_trading_allowed is False
    assert contract.solver_execution_allowed is False


def test_objective_contract():
    obj = OptimizationObjectiveContract(
        objective_name="mean_variance",
        objective_type="mean_variance",
        description="Markowitz mean-variance optimization objective specification",
        mathematical_formulation=r"\max (w^T \mu - \frac{\gamma}{2} w^T \Sigma w)",
        target_variable="expected_return_risk_tradeoff",
        risk_metric_ref="covariance_matrix",
    )
    assert obj.is_placeholder is True
    assert obj.is_calculated is False
    assert obj.allows_execution is False


def test_allocation_constraint_contract():
    con = AllocationConstraintContract(
        constraint_name="long_only",
        constraint_family="long_only",
        description="Long only non-negative allocation constraint",
        mathematical_formulation=r"w_i \ge 0",
        bound_type="lower_bound",
    )
    assert con.is_placeholder is True
    assert con.is_enforced_live is False
    assert con.allows_weight_generation is False


def test_solver_contract():
    solv = SolverContract(
        solver_name="convex_solver",
        solver_type="convex",
        description="Convex optimization solver placeholder",
        supported_objectives=["mean_variance", "minimum_variance"],
    )
    assert solv.is_placeholder is True
    assert solv.solver_executed is False
    assert solv.allows_execution is False


def test_findings_validator():
    finding = PortfolioOptimizationFinding(
        finding_id="FND-001",
        finding_type="safety",
        domain="portfolio_optimization",
        severity_label="INFO",
        message="Test message",
        recommendation="Review contracts manually",
    )
    assert finding.manual_review_required is True

    with pytest.raises(ValueError):
        PortfolioOptimizationFinding(
            finding_id="FND-002",
            finding_type="safety",
            domain="portfolio_optimization",
            severity_label="INFO",
            message="Test message",
            recommendation="auto-optimize portfolio immediately",
        )
