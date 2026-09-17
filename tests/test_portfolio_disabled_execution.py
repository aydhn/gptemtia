# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Disabled Execution Reports."""

from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.portfolio_construction_execution_disabled import (
    build_portfolio_construction_execution_disabled_report,
)
from advanced_portfolio_construction.position_sizing_execution_disabled import (
    build_position_sizing_execution_disabled_report,
)
from advanced_portfolio_construction.risk_budget_execution_disabled import (
    build_risk_budget_execution_disabled_report,
)
from advanced_portfolio_construction.allocation_generation_disabled import (
    build_allocation_generation_disabled_report,
)
from advanced_portfolio_construction.portfolio_optimizer_disabled import (
    build_portfolio_optimizer_disabled_report,
)
from advanced_portfolio_construction.portfolio_metric_calculation_disabled import (
    build_portfolio_metric_calculation_disabled_report,
)
from advanced_portfolio_construction.portfolio_model_training_disabled import (
    build_portfolio_model_training_disabled_report,
)
from advanced_portfolio_construction.portfolio_prediction_disabled import (
    build_portfolio_prediction_disabled_report,
)
from advanced_portfolio_construction.portfolio_live_trading_disabled import (
    build_portfolio_live_trading_disabled_report,
)
from advanced_portfolio_construction.portfolio_broker_execution_disabled import (
    build_portfolio_broker_execution_disabled_report,
)
from advanced_portfolio_construction.portfolio_deployment_disabled import (
    build_portfolio_deployment_disabled_report,
)


def test_all_11_disabled_execution_reports():
    profile = get_default_portfolio_construction_profile()

    builders = [
        build_portfolio_construction_execution_disabled_report,
        build_position_sizing_execution_disabled_report,
        build_risk_budget_execution_disabled_report,
        build_allocation_generation_disabled_report,
        build_portfolio_optimizer_disabled_report,
        build_portfolio_metric_calculation_disabled_report,
        build_portfolio_model_training_disabled_report,
        build_portfolio_prediction_disabled_report,
        build_portfolio_live_trading_disabled_report,
        build_portfolio_broker_execution_disabled_report,
        build_portfolio_deployment_disabled_report,
    ]

    for builder in builders:
        df, summary = builder(profile)
        assert len(df) == 1
        assert bool(df["is_disabled"].iloc[0]) is True
        assert summary["is_disabled"] is True
        assert summary["status"] == "portfolio_contract_ready"
