# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Models."""

import pytest
from advanced_realistic_backtest.realistic_backtest_models import (
    RealisticBacktestProfileItem,
    BacktestEngineContract,
    OrderSimulationContract,
    TransactionCostModelContract,
    SlippageModelContract,
    BacktestGuardItem,
    BacktestDisabledExecutionItem,
    BacktestFinding,
    BacktestReadinessScore,
    RealisticBacktestManifest,
    BacktestManualReviewItem,
)


def test_realistic_backtest_profile_item():
    item = RealisticBacktestProfileItem(
        profile_name="test_profile",
        description="Test profile",
        current_phase=146,
        target_final_phase=160,
        next_phase=147,
        dry_run=True,
        local_only=True,
        non_production=True,
        non_signal=True,
        min_readiness_score=0.50,
    )
    assert item.current_phase == 146
    assert item.non_production is True


def test_engine_contract_invariant_violation():
    with pytest.raises(ValueError):
        BacktestEngineContract(
            contract_name="test_contract",
            engine_family="event_driven",
            description="test",
            data_contract_ref="data_ref",
            feature_input_contract_ref="feat_ref",
            signal_input_contract_ref="sig_ref",
            order_simulation_ref="ord_ref",
            transaction_cost_ref="cost_ref",
            slippage_model_ref="slip_ref",
            no_lookahead_guard_ref="nl_ref",
            bias_guard_ref="bias_ref",
            backtest_execution_allowed=True,  # VIOLATION
        )


def test_order_simulation_contract():
    order = OrderSimulationContract(
        simulation_type="market_order",
        description="Standard market order",
        order_type="market",
        fill_model_ref="next_bar_open",
        latency_model_ref="net_delay",
        liquidity_constraint_ref="bar_vol_cap",
        broker_order_sent=False,
        live_order_sent=False,
    )
    assert order.broker_order_sent is False
    assert order.live_order_sent is False


def test_readiness_score_model():
    score = BacktestReadinessScore(
        score=0.85,
        classification="realistic_backtest_contract_ready_non_production",
        total_findings=2,
        critical_blockers=0,
        meets_threshold=True,
        non_signal=True,
    )
    assert score.meets_threshold is True
    assert score.score == 0.85
