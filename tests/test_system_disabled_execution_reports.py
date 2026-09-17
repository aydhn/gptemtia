# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Disabled Execution Reports."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_execution_disabled import (
    build_system_execution_disabled_report,
    validate_no_system_execution_request,
)
from advanced_full_system_integration.live_trading_disabled import (
    build_live_trading_disabled_report,
)
from advanced_full_system_integration.broker_execution_disabled import (
    build_broker_execution_disabled_report,
)
from advanced_full_system_integration.production_deployment_disabled import (
    build_production_deployment_disabled_report,
)
from advanced_full_system_integration.model_training_disabled import (
    build_model_training_disabled_report,
)
from advanced_full_system_integration.model_prediction_disabled import (
    build_model_prediction_disabled_report,
)
from advanced_full_system_integration.backtest_execution_disabled import (
    build_backtest_execution_disabled_report,
)
from advanced_full_system_integration.portfolio_execution_disabled import (
    build_portfolio_execution_disabled_report,
)
from advanced_full_system_integration.risk_execution_disabled import (
    build_risk_execution_disabled_report,
)
from advanced_full_system_integration.scenario_execution_disabled import (
    build_scenario_execution_disabled_report,
)
from advanced_full_system_integration.order_generation_disabled import (
    build_order_generation_disabled_report,
)
from advanced_full_system_integration.signal_generation_disabled import (
    build_signal_generation_disabled_report,
)
from advanced_full_system_integration.investment_advice_disabled import (
    build_investment_advice_disabled_report,
)


def test_disabled_execution_builders():
    profile = get_default_full_system_integration_profile()

    builders = [
        build_system_execution_disabled_report,
        build_live_trading_disabled_report,
        build_broker_execution_disabled_report,
        build_production_deployment_disabled_report,
        build_model_training_disabled_report,
        build_model_prediction_disabled_report,
        build_backtest_execution_disabled_report,
        build_portfolio_execution_disabled_report,
        build_risk_execution_disabled_report,
        build_scenario_execution_disabled_report,
        build_order_generation_disabled_report,
        build_signal_generation_disabled_report,
        build_investment_advice_disabled_report,
    ]

    for builder in builders:
        df, summary = builder(profile)
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert summary["active_profile"] == profile.profile_name
        assert summary["all_disabled"] is True
        assert summary["non_signal"] is True


def test_validate_no_system_execution():
    safe = validate_no_system_execution_request("local inspection only")
    assert safe["is_safe"] is True
    assert safe["blocked_by_policy"] is False

    unsafe = validate_no_system_execution_request("please run_system now")
    assert unsafe["is_safe"] is False
    assert unsafe["blocked_by_policy"] is True
