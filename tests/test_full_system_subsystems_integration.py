# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Subsystems Integration Modules."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.data_pipeline_integration import (
    build_data_pipeline_integration_registry,
)
from advanced_full_system_integration.feature_factor_integration import (
    build_feature_factor_integration_registry,
)
from advanced_full_system_integration.regime_integration import (
    build_regime_integration_registry,
)
from advanced_full_system_integration.ml_governance_integration import (
    build_ml_governance_integration_registry,
)
from advanced_full_system_integration.backtest_acceptance_integration import (
    build_backtest_acceptance_integration_registry,
)
from advanced_full_system_integration.portfolio_acceptance_integration import (
    build_portfolio_acceptance_integration_registry,
)
from advanced_full_system_integration.risk_reporting_integration import (
    build_risk_reporting_integration_registry,
)
from advanced_full_system_integration.scenario_control_integration import (
    build_scenario_control_integration_registry,
)
from advanced_full_system_integration.reporting_integration import (
    build_reporting_integration_registry,
)
from advanced_full_system_integration.telegram_interface_integration_placeholders import (
    build_telegram_interface_integration_placeholder_registry,
)
from advanced_full_system_integration.local_paper_trading_integration_placeholders import (
    build_local_paper_trading_integration_placeholder_registry,
)


def test_subsystems_integration_builders():
    profile = get_default_full_system_integration_profile()

    builders = [
        build_data_pipeline_integration_registry,
        build_feature_factor_integration_registry,
        build_regime_integration_registry,
        build_ml_governance_integration_registry,
        build_backtest_acceptance_integration_registry,
        build_portfolio_acceptance_integration_registry,
        build_risk_reporting_integration_registry,
        build_scenario_control_integration_registry,
        build_reporting_integration_registry,
        build_telegram_interface_integration_placeholder_registry,
        build_local_paper_trading_integration_placeholder_registry,
    ]

    for builder in builders:
        df, summary = builder(profile)
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert summary["active_profile"] == profile.profile_name
        assert summary["status"] == "full_system_integration_ready"
        assert summary["non_signal"] is True
