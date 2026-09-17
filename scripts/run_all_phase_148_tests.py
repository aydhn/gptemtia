# -*- coding: utf-8 -*-
"""Runner script to execute all Phase 148 unit tests."""

import subprocess
import sys
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent.parent / "tests"

PHASE_148_TEST_NAMES = [
    "test_stress_testing_config.py",
    "test_stress_testing_labels.py",
    "test_stress_testing_models.py",
    "test_stress_testing_profile_registry.py",
    "test_stress_testing_domain_registry.py",
    "test_stress_testing_scope_registry.py",
    "test_stress_scenario_contracts.py",
    "test_historical_stress_scenario_contracts.py",
    "test_hypothetical_stress_scenario_contracts.py",
    "test_regime_shock_scenario_contracts.py",
    "test_volatility_shock_scenario_contracts.py",
    "test_liquidity_shock_scenario_contracts.py",
    "test_spread_widening_scenario_contracts.py",
    "test_gap_risk_scenario_placeholders.py",
    "test_correlation_breakdown_scenario_placeholders.py",
    "test_macro_shock_scenario_placeholders.py",
    "test_cross_asset_contagion_scenario_placeholders.py",
    "test_execution_disruption_scenario_placeholders.py",
    "test_transaction_cost_shock_contracts.py",
    "test_slippage_shock_contracts.py",
    "test_stress_scenario_library.py",
    "test_stress_scenario_groups.py",
    "test_stress_scenario_severity_policies.py",
    "test_stress_scenario_time_horizon_policies.py",
    "test_stress_scenario_asset_scope_policies.py",
    "test_stress_scenario_regime_context.py",
    "test_stress_output_contracts.py",
    "test_scenario_output_contracts.py",
    "test_stress_metric_placeholders.py",
    "test_scenario_metric_placeholders.py",
    "test_robustness_metric_placeholders.py",
    "test_stressed_pnl_placeholders.py",
    "test_stressed_drawdown_placeholders.py",
    "test_stress_no_lookahead_guards.py",
    "test_stress_scenario_leakage_guards.py",
    "test_stress_overfitting_guards.py",
    "test_stress_data_snooping_bias_guards.py",
    "test_stress_survivorship_bias_guards.py",
    "test_stress_multiple_testing_guards.py",
    "test_stress_forbidden_column_policies.py",
    "test_stress_execution_disabled.py",
    "test_scenario_simulation_disabled.py",
    "test_stress_metric_calculation_disabled.py",
    "test_stress_optimizer_disabled.py",
    "test_stress_model_training_disabled.py",
    "test_stress_prediction_disabled.py",
    "test_stress_live_trading_disabled.py",
    "test_stress_broker_execution_disabled.py",
    "test_stress_performance_claim_disabled.py",
    "test_stress_manual_review.py",
    "test_stress_findings.py",
    "test_stress_readiness_scoring.py",
    "test_stress_testing_manifest.py",
    "test_stress_testing_report_builder.py",
    "test_stress_testing_pipeline.py",
    "test_stress_testing_health.py",
    "test_stress_testing_validation.py",
    "test_stress_testing_safety_boundary.py",
    "test_phase_149_handoff.py",
    "test_advanced_stress_testing_scripts_contract.py",
]

PHASE_148_TEST_FILES = [
    str(TESTS_DIR / f) for f in PHASE_148_TEST_NAMES if (TESTS_DIR / f).exists()
]


def main():
    print(f"Targeting {len(PHASE_148_TEST_FILES)} Phase 148 test files.")
    cmd = [sys.executable, "-m", "pytest", "-v"] + PHASE_148_TEST_FILES
    print("\nRunning pytest...")
    res = subprocess.run(cmd)
    sys.exit(res.returncode)


if __name__ == "__main__":
    main()
