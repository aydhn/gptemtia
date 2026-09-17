# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Disabled Execution Reports."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.portfolio_optimization_execution_disabled import (
    build_portfolio_optimization_execution_disabled_report,
)
from advanced_portfolio_optimization.weight_generation_disabled import (
    build_weight_generation_disabled_report,
)
from advanced_portfolio_optimization.allocation_generation_disabled import (
    build_allocation_generation_disabled_report,
)
from advanced_portfolio_optimization.rebalance_generation_disabled import (
    build_rebalance_generation_disabled_report,
)
from advanced_portfolio_optimization.optimization_metric_calculation_disabled import (
    build_optimization_metric_calculation_disabled_report,
)
from advanced_portfolio_optimization.optimization_live_trading_disabled import (
    build_optimization_live_trading_disabled_report,
)
from advanced_portfolio_optimization.optimization_broker_execution_disabled import (
    build_optimization_broker_execution_disabled_report,
)


def test_disabled_execution_reports():
    profile = get_default_portfolio_optimization_profile()

    df_opt, s_opt = build_portfolio_optimization_execution_disabled_report(profile)
    assert s_opt["portfolio_optimization_disabled"] is True
    assert (df_opt["is_disabled"] == True).all()

    df_wt, s_wt = build_weight_generation_disabled_report(profile)
    assert s_wt["weight_generation_disabled"] is True
    assert (df_wt["is_disabled"] == True).all()

    df_alloc, s_alloc = build_allocation_generation_disabled_report(profile)
    assert s_alloc["allocation_generation_disabled"] is True

    df_reb, s_reb = build_rebalance_generation_disabled_report(profile)
    assert s_reb["rebalance_generation_disabled"] is True

    df_m, s_m = build_optimization_metric_calculation_disabled_report(profile)
    assert s_m["metric_calculation_disabled"] is True

    df_live, s_live = build_optimization_live_trading_disabled_report(profile)
    assert s_live["live_trading_disabled"] is True

    df_brk, s_brk = build_optimization_broker_execution_disabled_report(profile)
    assert s_brk["broker_execution_disabled"] is True
