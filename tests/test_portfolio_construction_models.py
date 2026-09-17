# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Portfolio Construction Models."""

import pytest
from advanced_portfolio_construction.portfolio_construction_models import (
    PortfolioConstructionContract,
    PositionSizingContract,
    RiskBudgetContract,
    LimitContract,
    PortfolioFinding,
    PortfolioReadinessScore,
    PortfolioConstructionManifest,
    PortfolioManualReviewItem,
)


def test_portfolio_construction_contract_defaults():
    contract = PortfolioConstructionContract(
        contract_name="test_contract",
        portfolio_family="balanced",
        backtest_acceptance_ref="BKT_01",
        benchmark_evaluation_ref="BNK_01",
        model_governance_ref="GOV_01",
        regime_context_ref="REG_01",
        featurestore_ref="FS_01",
        risk_budget_ref="RB_01",
        position_sizing_ref="PS_01",
        limit_contract_ref="LIM_01",
        no_lookahead_guard_ref="GRD_01",
        investment_advice_guard_ref="GRD_02",
    )
    assert contract.contract_only is True
    assert contract.non_production is True
    assert contract.portfolio_construction_allowed is False
    assert contract.position_sizing_allowed is False
    assert contract.capital_allocation_allowed is False
    assert contract.live_trading_allowed is False
    assert contract.broker_ready is False


def test_position_sizing_contract_defaults():
    contract = PositionSizingContract(
        sizing_name="test_sizing",
        sizing_family="volatility_targeting",
        risk_budget_ref="RB_01",
        exposure_limit_ref="EXP_01",
        concentration_limit_ref="CONC_01",
        volatility_budget_ref="VOL_01",
        drawdown_budget_ref="DD_01",
        liquidity_limit_ref="LIQ_01",
        transaction_cost_ref="COST_01",
        slippage_model_ref="SLIP_01",
    )
    assert contract.contract_only is True
    assert contract.position_sizing_allowed is False
    assert contract.capital_allocation_allowed is False
    assert contract.order_generation_allowed is False


def test_portfolio_readiness_score_bounds():
    score = PortfolioReadinessScore(
        overall_score=0.85,
        classification="portfolio_construction_contract_ready_non_production",
        meets_threshold=True,
        findings_count=3,
        critical_count=0,
    )
    assert score.overall_score == 0.85
    assert score.meets_threshold is True
    assert score.production_ready is False

    with pytest.raises(ValueError):
        PortfolioReadinessScore(
            overall_score=1.5,
            classification="invalid",
            meets_threshold=True,
            findings_count=0,
            critical_count=0,
        )


def test_portfolio_manifest_prohibitions():
    manifest = PortfolioConstructionManifest(
        manifest_id="MNF-TEST-001",
    )
    assert manifest.portfolio_constructed is False
    assert manifest.position_sizing_generated is False
    assert manifest.capital_allocation_generated is False
    assert manifest.portfolio_weights_generated is False
    assert manifest.orders_generated is False
    assert manifest.broker_order_sent is False
    assert manifest.live_order_sent is False
    assert manifest.source_preserved is True
    assert manifest.phase_154_handoff_ready is True
