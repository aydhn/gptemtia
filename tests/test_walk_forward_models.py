# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Walk-Forward Validation Models and Safety Post-Init Checks."""

import pytest
from advanced_walk_forward_validation.walk_forward_models import (
    WalkForwardProfileItem,
    WalkForwardValidationContract,
    SplitContract,
    BenchmarkContract,
    BenchmarkPlaceholder,
    ValidationMetricPlaceholder,
    WalkForwardValidationManifest,
)


def test_walk_forward_profile_item():
    p = WalkForwardProfileItem(
        profile_name="test_profile",
        description="Test Profile Description",
    )
    assert p.profile_name == "test_profile"
    assert p.non_signal is True

    with pytest.raises(ValueError):
        WalkForwardProfileItem(
            profile_name="bad_profile",
            description="Bad Profile",
            min_readiness_score=1.5,
        )


def test_walk_forward_contract_safety_check():
    c = WalkForwardValidationContract(
        contract_name="test_contract",
        validation_family="ROLLING",
        description="Rolling window test",
        data_contract_ref="dc_ref",
        feature_input_contract_ref="fc_ref",
        signal_input_contract_ref="sc_ref",
        realistic_backtest_ref="rb_ref",
        transaction_cost_ref="tc_ref",
        slippage_model_ref="sm_ref",
        split_policy_ref="sp_ref",
        embargo_policy_ref="ep_ref",
        no_lookahead_guard_ref="nlg_ref",
        bias_guard_ref="bg_ref",
    )
    assert c.walk_forward_execution_allowed is False
    assert c.non_signal is True

    with pytest.raises(ValueError):
        WalkForwardValidationContract(
            contract_name="bad_contract",
            validation_family="ROLLING",
            description="Bad",
            data_contract_ref="dc_ref",
            feature_input_contract_ref="fc_ref",
            signal_input_contract_ref="sc_ref",
            realistic_backtest_ref="rb_ref",
            transaction_cost_ref="tc_ref",
            slippage_model_ref="sm_ref",
            split_policy_ref="sp_ref",
            embargo_policy_ref="ep_ref",
            no_lookahead_guard_ref="nlg_ref",
            bias_guard_ref="bg_ref",
            walk_forward_execution_allowed=True,
        )


def test_split_contract_safety_check():
    s = SplitContract(
        split_name="test_split",
        split_type="TRAIN_VAL_TEST",
        description="Test Split",
        window_type="ROLLING",
        train_ratio=0.7,
        val_ratio=0.15,
        test_ratio=0.15,
    )
    assert s.non_signal is True
    assert s.contains_target_or_prediction is False

    with pytest.raises(ValueError):
        SplitContract(
            split_name="bad_split",
            split_type="TRAIN_VAL_TEST",
            description="Bad",
            window_type="ROLLING",
            train_ratio=0.7,
            val_ratio=0.15,
            test_ratio=0.15,
            contains_target_or_prediction=True,
        )


def test_benchmark_contract_safety_check():
    b = BenchmarkContract(
        benchmark_name="test_benchmark",
        benchmark_type="BUY_AND_HOLD",
        description="Test Benchmark",
        universe_ref="BRENT",
        baseline_strategy_ref="BUY_HOLD",
        rebalance_policy="NONE",
    )
    assert b.benchmark_executed is False
    assert b.non_signal is True

    with pytest.raises(ValueError):
        BenchmarkContract(
            benchmark_name="bad_benchmark",
            benchmark_type="BUY_AND_HOLD",
            description="Bad",
            universe_ref="BRENT",
            baseline_strategy_ref="BUY_HOLD",
            rebalance_policy="NONE",
            benchmark_executed=True,
        )


def test_metric_placeholder_safety_check():
    m = ValidationMetricPlaceholder(
        metric_name="alpha_test",
        metric_category="BENCHMARK_RELATIVE",
        description="Alpha Placeholder",
        formula_spec="R_p - beta * R_b",
    )
    assert m.metric_calculated is False
    assert m.non_signal is True

    with pytest.raises(ValueError):
        ValidationMetricPlaceholder(
            metric_name="alpha_bad",
            metric_category="BENCHMARK_RELATIVE",
            description="Bad Alpha",
            formula_spec="R_p - beta * R_b",
            metric_calculated=True,
        )


def test_manifest_safety_check():
    m = WalkForwardValidationManifest(
        manifest_id="man_test",
        current_phase=147,
        target_final_phase=160,
        next_phase=148,
    )
    assert m.walk_forward_executed is False
    assert m.oos_benchmark_executed is False
    assert m.live_trading_ready is False

    with pytest.raises(ValueError):
        WalkForwardValidationManifest(
            manifest_id="man_bad",
            current_phase=147,
            target_final_phase=160,
            next_phase=148,
            live_trading_ready=True,
        )
