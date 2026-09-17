# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Disabled Execution Audit Reports."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.monte_carlo_execution_disabled import (
    build_monte_carlo_execution_disabled_report,
)
from advanced_monte_carlo_robustness.bootstrap_execution_disabled import (
    build_bootstrap_execution_disabled_report,
)
from advanced_monte_carlo_robustness.parameter_optimization_disabled import (
    build_parameter_optimization_disabled_report,
)
from advanced_monte_carlo_robustness.parameter_sweep_execution_disabled import (
    build_parameter_sweep_execution_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_metric_calculation_disabled import (
    build_monte_carlo_metric_calculation_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_model_training_disabled import (
    build_monte_carlo_model_training_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_prediction_disabled import (
    build_monte_carlo_prediction_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_live_trading_disabled import (
    build_monte_carlo_live_trading_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_broker_execution_disabled import (
    build_monte_carlo_broker_execution_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_performance_claim_disabled import (
    build_monte_carlo_performance_claim_disabled_report,
)


def test_all_disabled_execution_reports():
    profile = get_default_monte_carlo_profile()
    reports = [
        build_monte_carlo_execution_disabled_report(profile),
        build_bootstrap_execution_disabled_report(profile),
        build_parameter_optimization_disabled_report(profile),
        build_parameter_sweep_execution_disabled_report(profile),
        build_monte_carlo_metric_calculation_disabled_report(profile),
        build_monte_carlo_model_training_disabled_report(profile),
        build_monte_carlo_prediction_disabled_report(profile),
        build_monte_carlo_live_trading_disabled_report(profile),
        build_monte_carlo_broker_execution_disabled_report(profile),
        build_monte_carlo_performance_claim_disabled_report(profile),
    ]

    for df, summary in reports:
        assert not df.empty
        assert summary.get("all_executions_blocked", True) is True
        assert summary.get("live_trading_blocked", True) is True
