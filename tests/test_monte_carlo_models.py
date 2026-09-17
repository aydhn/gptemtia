# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Models."""

import pytest
from advanced_monte_carlo_robustness.monte_carlo_models import (
    MonteCarloContractModel,
    BootstrapContractModel,
    ParameterStabilityContractModel,
    MonteCarloReadinessScore,
    MonteCarloManifest,
)


def test_monte_carlo_contract_model():
    model = MonteCarloContractModel(
        contract_name="test_contract",
        robustness_family="block_bootstrap",
        realistic_backtest_ref="PHASE_146_REF",
        walk_forward_ref="PHASE_147_REF",
        stress_testing_ref="PHASE_148_REF",
        transaction_cost_ref="COST_REF",
        slippage_model_ref="SLIPPAGE_REF",
        regime_context_ref="REGIME_REF",
        no_lookahead_guard_ref="GUARD_01",
        resampling_leakage_guard_ref="GUARD_02",
        description="Test contract description",
    )
    assert model.contract_name == "test_contract"
    assert model.monte_carlo_execution_allowed is False
    assert model.live_trading_allowed is False
    assert model.broker_execution_allowed is False


def test_monte_carlo_contract_model_rejects_live_trading():
    with pytest.raises(ValueError):
        MonteCarloContractModel(
            contract_name="bad_contract",
            robustness_family="block_bootstrap",
            realistic_backtest_ref="REF",
            walk_forward_ref="REF",
            stress_testing_ref="REF",
            transaction_cost_ref="REF",
            slippage_model_ref="REF",
            regime_context_ref="REF",
            no_lookahead_guard_ref="GUARD_01",
            resampling_leakage_guard_ref="GUARD_02",
            description="desc",
            live_trading_allowed=True,
        )


def test_parameter_stability_contract_model():
    model = ParameterStabilityContractModel(
        parameter_name="ema_span",
        strategy_ref="trend_following",
        perturbation_range="[-20%, +20%]",
        sensitivity_metric="sharpe_elasticity",
        plateau_detection_rule="flat_surface_condition",
        description="EMA span stability",
    )
    assert model.optimization_allowed is False
    assert model.sweep_allowed is False


def test_monte_carlo_readiness_score():
    score = MonteCarloReadinessScore(
        score=1.0,
        classification="monte_carlo_robustness_contract_ready_non_production",
        total_checks=10,
        passed_checks=10,
        critical_findings_count=0,
        manual_review_required=True,
        broker_ready=False,
        production_ready=False,
        live_trading_ready=False,
    )
    assert score.score == 1.0
    assert score.broker_ready is False


def test_monte_carlo_manifest():
    manifest = MonteCarloManifest(
        manifest_id="MANIFEST_149",
        current_phase=149,
        target_final_phase=160,
        next_phase=150,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        monte_carlo_executed=False,
        bootstrap_executed=False,
        resampling_executed=False,
        parameter_optimization_executed=False,
        parameter_sweep_executed=False,
        robustness_metric_calculated=False,
        parameter_stability_metric_calculated=False,
        distribution_calculated=False,
        var_calculated=False,
        expected_shortfall_calculated=False,
        optimizer_executed=False,
        model_training_executed=False,
        model_predict_executed=False,
        prediction_generated=False,
        target_label_generated=False,
        performance_claim_generated=False,
        broker_order_sent=False,
        live_order_sent=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        source_preserved=True,
        manual_review_required=True,
        phase_150_handoff_ready=True,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
    )
    assert manifest.current_phase == 149
    assert manifest.monte_carlo_executed is False
    assert manifest.phase_150_handoff_ready is True
